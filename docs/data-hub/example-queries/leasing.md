---
description: Leasing Case Study and SQL Recipe Book
---

# Leasing

_**Narrative summary of common business requirements/workflows from the Leasing industry mapped to concrete SQL implementations based on the data at Navixy Data Hub.**_

## **Lifecycle Coverage with Navixy Data Hub SQL Recipes** <a href="#lifecycle-coverage-with-navixy-data-hub-sql-recipes" id="lifecycle-coverage-with-navixy-data-hub-sql-recipes"></a>

Leasing companies (particularly banks and fleet‑leasing providers) retain ownership of the vehicle or equipment while the client merely rents its use, so they absorb the asset‑related risk throughout the contract. 

To protect residual value, enforce contractual limits (mileage, geography, maintenance), and streamline full‑service obligations, they rely on Navixy.  Real‑time GPS data, sensors based diagnostics, and behavioural analytics let them verify usage conditions, automate service scheduling, detect mechanical issues early, calculate penalties or excess‑kilometre fees, and, when necessary, immobilise or recover the asset—all of which secures their investment, reduces operational cost, and enhances customer transparency across the entire lease lifecycle.

Navixy Data Hub will help to organize any kind of analytics at every stage of the leasing contract. A leasing contract passes through several predictable phases: Onboarding & Asset Setup → Operational Phase → Risk & Compliance Oversight

The following SQL recipes in your book collectively monitor every critical milestone across that lifecycle:

| Lifecycle Phase                       | Goals & Milestones                                                                                                             | Covered Use Cases / Recipes                                                                                                                                                                |
| ------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| 1. Onboarding  & Asset Setup          | • Register vehicle, activate insurance and driver credentials. • Import assets into the client portal with correct visibility. | Registration/Insurance Expiry Alerts – baseline dates captured. Driver License Expiry – validates drivers before release.                                                                  |
| 2. Preventive Maintenance Planning    | • Establish recurring, mileage‑based and time‑based service schedules. • Guarantee seasonal tyre changes.                      | Routine Inspections by Interval – calendar‑driven tasks.  Service by Mileage Threshold – km‑driven minor/major service rules. Engine Hours Monitoring – hour‑driven service for machinery. |
| 3. Contract‑Bound Usage Limits        | • Enforce mileage allowances and financial caps. • Detect over‑usage early to avoid end‑term surprises.                        | Mileage Cap & Penalties – yearly / contract‑total kilometre policing.                                                                                                                      |
| 4. Real‑time Driver & Asset Behaviour | • Protect asset value; coach drivers. • Spot misuse that voids “full‑service” coverage.                                        | Harsh Braking. Harsh Acceleration. Sudden Turns/Cornering.                                                                                                                                 |
| 5. Risk & Compliance Oversight        | • Keep assets inside geographic and contractual boundaries. • Retain right to disable or recover.                              | Geofence Exit (Country Border) – instant alert on territory breach. Ignition & Idle Detection – fuel wastage / misuse tracking.                                                            |

## **Registration / Insurance Expiry Alerts**

Banks must track upcoming registration and insurance expirations because they’re responsible for technical inspections, registration, and insurance. Timely alerts prevent fines and vehicle downtime.

```sql
SELECT v.vehicle_id,       v.vehicle_label,       v.registration_number,       v.free_insurance_valid_till_date,       v.liability_insurance_valid_tillFROM raw_business_data.vehicles vWHERE v.free_insurance_valid_till_date BETWEEN CURRENT_DATE AND CURRENT_DATE + (30 * INTERVAL '1 day')   OR v.liability_insurance_valid_till   BETWEEN CURRENT_DATE1 AND CURRENT_DATE + (30 * INTERVAL '1 day');
```

## **Driver License Expiry**

Although not always mandatory, offering proactive license-expiry alerts is a value-add service. Early warnings let clients renew licenses before they lapse. Please note you

```sql
SELECT e.employee_id,
       e.first_name || ' ' || e.last_name AS driver_name,
       e.driver_license_number,
       e.driver_license_valid_till
FROM raw_business_data.employees e
WHERE e.driver_license_valid_till BETWEEN CURRENT_DATE AND CURRENT_DATE + (30 * INTERVAL '1 day');
```

## Geofence Exit (Country Border) <a href="#geofence-exit-country-border" id="geofence-exit-country-border"></a>

Contracts may restrict vehicle movement to a specific territory (e.g., Serbia). Exiting that zone should instantly alert the bank so it can act (e.g., contact client, immobilize asset).

This SQL query is designed to monitor and identify when a device exits a predefined geographic zone labeled "Tallaght Depot Geofences." The process begins by collecting and ordering geographic points that define the boundary of the zone. To ensure the boundary forms a valid polygon, the first point is appended to the end of the list, effectively closing the shape. This closed set of points is then used to create a polygon representing the geographic zone, which is converted into a geography object for spatial analysis.

The query then retrieves device tracking data within a specified time range, converting raw latitude and longitude values into geographic points. It calculates whether each device point is inside or outside the predefined zone using the ST\_Contains function, which checks for spatial containment. The calculated parameter pos indicates 'inside' if the point is within the zone and 'outside' otherwise. Finally, the query filters these results to detect transitions where a device moves from inside the zone to outside, using a window function to compare the current position with the previous one. This logic helps in monitoring device movements and detecting exit events from specific geographic areas. Make sure you add the correct value for the parameter: `z.zone_label = 'your_zone_label'.`

```sql
WITH zone AS (
  SELECT z.zone_id,
         ST_MakePolygon(ST_MakeLine(ARRAY_AGG(ST_MakePoint(g.longitude, g.latitude) ORDER BY g.number)))::geography AS geog
  FROM raw_business_data.zones z
  JOIN raw_business_data.geofence_points g ON g.zone_id = z.zone_id
  WHERE z.zone_label = 'your_zone_label'
  GROUP BY z.zone_id
),
pts AS (
  SELECT device_id,
         device_time,
         ST_SetSRID(ST_MakePoint(longitude/1e7::numeric, latitude/1e7::numeric), 4326)::geography AS geog
  FROM raw_telematics_data.tracking_data_core
  WHERE device_time BETWEEN '2025-07-27 00:00:00' AND '2025-07-28 23:59:59'
),
states AS (
  SELECT p.*,
         CASE WHEN ST_Contains(z.geog::geometry, p.geog::geometry) THEN 'inside' ELSE 'outside' END AS pos
  FROM pts p CROSS JOIN zone z
),
filtered_states AS (
  SELECT
    device_id,
    device_time,
    pos,
    LAG(pos) OVER (PARTITION BY device_id ORDER BY device_time) AS prev_pos
  FROM states
)
SELECT device_id, device_time, pos
FROM filtered_states
WHERE prev_pos = 'inside' AND pos = 'outside';

```

## **Routine Inspections by Time Interval**

Some maintenance tasks recur on fixed time schedules. The system should flag vehicles whose next inspection/check is due within a defined interval.

```sql
SELECT vehicle_id,       description,       start_date,       date_repeat_interval,       start_date + date_repeat_interval * floor(EXTRACT(EPOCH FROM (CURRENT_DATE - start_date)) /                                                 EXTRACT(EPOCH FROM date_repeat_interval)) AS last_due,       start_date + date_repeat_interval * (floor(EXTRACT(EPOCH FROM (CURRENT_DATE - start_date)) /                                                  EXTRACT(EPOCH FROM date_repeat_interval)) + 1) AS next_dueFROM raw_business_data.vehicle_service_tasksWHERE date_repeat_interval IS NOT NULL  AND start_date + date_repeat_interval * (floor(EXTRACT(EPOCH FROM (CURRENT_DATE - start_date)) /                                                 EXTRACT(EPOCH FROM date_repeat_interval)) + 1)      BETWEEN CURRENT_DATE AND CURRENT_DATE + (30 * INTERVAL '1 day');
```

## **Service by Mileage Threshold (Minor/Major)**

Minor and major services are triggered by mileage since the last service event. When accumulated kilometers exceed the threshold, the appropriate service must be scheduled.

Please note the `vst.description field should have relevant comments / description to use it for the filters in the SQL code below.`

```sql
SELECT
  v.vehicle_id,
  v.vehicle_label,
  km.km_since_service,
  vst.mileage_limit
FROM
  raw_business_data.vehicles v
  JOIN LATERAL (
    SELECT MAX(vst.completion_date) AS last_service_date
    FROM raw_business_data.vehicle_service_tasks vst
    WHERE vst.vehicle_id = v.vehicle_id
      AND (vst.description ILIKE '%minor%' OR vst.description ILIKE '%major%')
      AND vst.completion_date IS NOT NULL
  ) ls ON TRUE
  JOIN raw_business_data.objects o ON o.object_id = v.vehicle_id
  JOIN LATERAL (
    SELECT SUM(t.track_distance_meters) / 1000.0 AS km_since_service
    FROM business_data.tracks t
    WHERE t.device_id = o.device_id
      AND t.track_start_time > ls.last_service_date
  ) km ON TRUE
  JOIN raw_business_data.vehicle_service_tasks vst
    ON vst.vehicle_id = v.vehicle_id
    AND vst.completion_date = ls.last_service_date
    AND (vst.description ILIKE '%minor%' OR vst.description ILIKE '%major%')

```

## **Mileage Cap & Penalties**

Leasing contracts often cap mileage (e.g., 25,000 km/year). If the limit is exceeded, penalty clauses apply. The system must compare actual mileage over the contract period with the agreed limit and calculate fees.

```sql
WITH driven AS (
  SELECT
    o.object_id,
    DATE_TRUNC('year', t.track_start_time) AS year,
    SUM(t.track_distance_meters) / 1000.0 AS km_year
  FROM
    business_data.tracks t
    JOIN raw_business_data.objects o ON o.device_id = t.device_id
  WHERE
    t.track_start_time >= '2023-01-01'::date
    AND t.track_start_time < '2024-01-01'::date
  GROUP BY
    o.object_id, DATE_TRUNC('year', t.track_start_time)
),
limits AS (
  SELECT
    object_id,
    10000 AS km_limit,
    0.5 AS penalty_rate
  FROM
    raw_business_data.objects
)
SELECT
  d.object_id,
  d.year,
  d.km_year,
  l.km_limit,
  GREATEST(d.km_year - l.km_limit, 0) AS km_over,
  GREATEST(d.km_year - l.km_limit, 0) * l.penalty_rate AS penalty_amount
FROM
  driven d
  JOIN limits l ON d.object_id = l.object_id;
```

## **Engine Hours Monitoring**

For machinery and agricultural equipment, operating hours—not mileage—drive maintenance and billing. Engine-hour data (e.g., from CAN-Bus) must be monitored and summarized.

```sql
WITH last_service AS (
  SELECT
    vst.vehicle_id,
    MAX(vst.completion_date) AS last_service_date,
    MAX(vst.completion_engine_hours) AS last_service_engine_hours
  FROM
    raw_business_data.vehicle_service_tasks vst
  GROUP BY
    vst.vehicle_id
),
engine_hours_since_service AS (
  SELECT
    v.vehicle_id,
    SUM(t.track_duration_seconds) / 3600.0 AS engine_hours_since_service
  FROM
    raw_business_data.vehicles v
    JOIN raw_business_data.objects o ON o.object_id = v.object_id
    JOIN business_data.tracks t ON t.device_id = o.device_id
    JOIN last_service ls ON ls.vehicle_id = v.vehicle_id
  WHERE
    t.track_start_time > ls.last_service_date
  GROUP BY
    v.vehicle_id
)
SELECT
  v.vehicle_id,
  v.vehicle_label,
  ls.last_service_engine_hours,
  ehs.engine_hours_since_service,
  (COALESCE(ehs.engine_hours_since_service,0) + COALESCE(ls.last_service_engine_hours,0)) AS current_engine_hours,
  vst.engine_hours_limit
FROM
  raw_business_data.vehicles v
  JOIN last_service ls ON ls.vehicle_id = v.vehicle_id
  LEFT JOIN engine_hours_since_service ehs ON ehs.vehicle_id = v.vehicle_id
  JOIN raw_business_data.vehicle_service_tasks vst
    ON vst.vehicle_id = v.vehicle_id
    AND vst.completion_date = ls.last_service_date
```

## **Harsh Braking Events**

Driving behavior affects wear and contract compliance. Detecting harsh braking helps the bank attribute premature brake/tire wear to driver misuse and, if needed, shift costs.

SQL query below first calculates the speed in kilometers per hour and the time difference between consecutive data points for each device. Using this information, it then computes the deceleration rate in kilometers per hour per second. Finally, it filters and returns records where the deceleration rate is 20 km/h per second or higher, indicating significant deceleration events.

```sql
WITH spd AS (
  SELECT
    device_id,
    device_time,
    speed/100.0 AS kmh,
    LAG(speed/100.0) OVER (PARTITION BY device_id ORDER BY device_time) AS prev_kmh,
    EXTRACT(EPOCH FROM (device_time - LAG(device_time) OVER (PARTITION BY device_id ORDER BY device_time))) AS dt_sec
  FROM
    raw_telematics_data.tracking_data_core
  WHERE
    device_time BETWEEN '2025-07-24 00:00:00' AND '2025-07-24 23:59:59'
),
decels AS (
  SELECT
    device_id,
    device_time,
    (prev_kmh - kmh) / NULLIF(dt_sec, 0) AS decel_kmh_per_sec
  FROM
    spd
  WHERE
    prev_kmh IS NOT NULL
)
SELECT *
FROM decels
WHERE decel_kmh_per_sec >= 20;
```

## **Harsh Acceleration Events**

Aggressive acceleration increases wear on tires, transmissions, drivetrains, and engine mounts. Identifying these events supports coaching and potential cost recovery.

The SQL query below is designed to identify significant acceleration events from a dataset of tracking data. It first calculates the speed in kilometers per hour and the time difference between consecutive data points for each device. Using this information, it then computes the acceleration rate in kilometers per hour per second. Finally, it filters and returns records where the acceleration rate meets or exceeds a specified threshold, indicating significant acceleration events.

```sql
WITH spd AS (
  SELECT
    device_id,
    device_time,
    speed/100.0 AS kmh,
    LAG(speed/100.0) OVER (PARTITION BY device_id ORDER BY device_time) AS prev_kmh,
    EXTRACT(EPOCH FROM (device_time - LAG(device_time) OVER (PARTITION BY device_id ORDER BY device_time))) AS dt_sec
  FROM
    raw_telematics_data.tracking_data_core
  WHERE
    device_time BETWEEN '2025-07-28 00:00:00' AND '2025-07-28 23:59:59'
)
SELECT
  device_id,
  device_time,
  (kmh - prev_kmh) / NULLIF(dt_sec, 0) AS accel_kmh_per_sec
FROM
  spd
WHERE
  prev_kmh IS NOT NULL
  AND (kmh - prev_kmh) / NULLIF(dt_sec, 0) >= 20;
```

## **Sudden Turns / Cornering**

Sharp turns combined with abrupt speed changes indicate risky driving. Tracking such behavior helps detect improper use of the vehicle.

This SQL query is designed to identify significant changes in direction and speed from tracking data over a specified time period. It first converts raw latitude and longitude values into decimal degrees and calculates the speed in kilometers per hour. Using the LAG function, it retrieves previous location and speed data for each device, allowing for the computation of changes over time. The query then calculates the heading change in degrees using trigonometric functions to determine the bearing between consecutive points. It also computes the change in speed between these points. Finally, the query filters the results to include only those records where the absolute change in heading is 10 degrees or more and the absolute change in speed is 5 km/h or more, identifying significant maneuvers or events in the tracking data.

```sql
WITH pts AS (
  SELECT
    device_id,
    device_time,
    latitude/1e7::numeric AS lat,
    longitude/1e7::numeric AS lon,
    LAG(latitude/1e7::numeric) OVER (PARTITION BY device_id ORDER BY device_time) AS prev_lat,
    LAG(longitude/1e7::numeric) OVER (PARTITION BY device_id ORDER BY device_time) AS prev_lon,
    speed/100.0 AS kmh,
    LAG(speed/100.0) OVER (PARTITION BY device_id ORDER BY device_time) AS prev_kmh
  FROM
    raw_telematics_data.tracking_data_core
  WHERE
    device_time BETWEEN '2025-07-28 00:00:00' AND '2025-07-28 23:59:59'
),
bearing AS (
  SELECT *,
         atan2(
           sin(radians(lon-prev_lon))*cos(radians(lat)),
           cos(radians(prev_lat))*sin(radians(lat)) -
           sin(radians(prev_lat))*cos(radians(lat))*cos(radians(lon-prev_lon))
         ) * 180/pi() AS heading_change,
         (kmh - prev_kmh) AS delta_speed
  FROM pts
)
SELECT *
FROM bearing
WHERE abs(heading_change) >= 10
  AND abs(delta_speed) >= 5;

```

## **Ignition & Idle Detection**

Measuring idle time (ignition on, low/no speed) helps reduce fuel waste and identify misuse. Long idling periods should be reported and managed.

```sql
WITH ign AS (  SELECT device_id,         device_time,         value::int AS ign_on  FROM raw_telematics_data.states  WHERE state_name = 'ignition'    AND device_time BETWEEN :from_ts AND :to_ts),spd AS (  SELECT device_id, device_time, speed/100.0 AS kmh  FROM raw_telematics_data.tracking_data_core  WHERE device_time BETWEEN :from_ts AND :to_ts),merged AS (  SELECT i.device_id,         i.device_time,         i.ign_on,         s.kmh,         LEAD(i.device_time) OVER (PARTITION BY i.device_id ORDER BY i.device_time) AS next_time  FROM ign i  LEFT JOIN spd s USING (device_id, device_time))SELECT device_id,       device_time AS idle_start,       next_time   AS idle_end,       EXTRACT(EPOCH FROM (next_time - device_time))/60 AS idle_minutesFROM mergedWHERE ign_on = 1 AND kmh < :idle_speed AND next_time - device_time >= INTERVAL ':idle_min minutes';
```
