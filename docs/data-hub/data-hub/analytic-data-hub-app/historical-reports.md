# Historical reports

Historical reports transform your operational data into strategic insights by analyzing patterns, trends, and performance metrics across time periods you define, enabling data-driven decisions for fleet optimization and resource planning.

## Measurement sensor report

![](../../.gitbook/assets/image-20250813-124709.png)

**When to use**: Fuel management planning, predictive maintenance scheduling, and identifying equipment performance patterns across multiple vehicles and time periods.

**What data you see**: Time-series sensor measurements aggregated into statistical summaries, showing average, minimum, and maximum values for each sensor across your selected timeframe.

<details>

<summary>Data processing logic</summary>

The system processes sensor data through sophisticated time-series analysis:

* **Time bucketing aggregation**: Raw sensor readings undergo grouping into 15-second intervals using PostgreSQL's `time_bucket` function, creating manageable data points from continuous sensor streams. This approach balances analytical precision with processing efficiency.
* **Multi-sensor correlation**: The query joins `business_data.sensors_data_by_hours` with `raw_business_data.objects` to combine sensor measurements with vehicle context. Each sensor reading includes calibration data when available, converting raw values into meaningful units (liters for fuel, degrees for temperature).
* **Statistical calculation**: For each time bucket, the system calculates average, minimum, and maximum values across all readings. When sensor calibration data is missing or invalid, raw values display without modification to maintain data transparency.
* **Quality filtering**: GPS quality validation ensures only reliable location data (satellites > 3, non-zero coordinates) contributes to sensor context, while invalid readings are excluded from statistical calculations.

All timestamps convert to UTC for consistent analysis regardless of vehicle geographic location, enabling accurate trend identification across different operational zones.

</details>

## Object activity report

![](../../.gitbook/assets/image-20250813-124725.png)

**When to use**: Route optimization analysis, vehicle utilization assessment, and operational efficiency measurement across defined time periods and fleet segments.

**What data you see**: Comprehensive activity metrics including total distance traveled, trip duration, average speeds, and route patterns for each vehicle in your selected fleet subset.

<details>

<summary>Data processing logic</summary>

This report combines historical and real-time data through complex track generation:

* **Hybrid data sourcing**: The system intelligently selects between `business_data.tracks` for historical analysis and `raw_telematics_data.tracking_data_core` for fresh data, depending on your time range. Periods longer than 12 hours use pre-processed tracks for optimal performance, while recent periods generate tracks from raw telematics data.
* **Track reconstruction**: For real-time analysis, the system applies movement detection algorithms using speed thresholds (≥3 km/h) and time gaps (>300 seconds) to identify distinct trips. Raw coordinate data (stored as integers) converts to decimal degrees through division by 10,000,000 for geographic calculations.
* **Distance calculation**: Geographic distance uses PostGIS functions for precise measurements between consecutive GPS points, while duration calculations derive from timestamp differences between track start and end points.
* **Zone integration**: Geographic analysis cross-references vehicle positions with defined zones using `ST_DWithin` calculations, providing operational context for trip start and end locations.

The underlying query structure adapts based on your selected parameters, optimizing between historical data retrieval and real-time track generation to deliver comprehensive activity analysis.

</details>

## Eco-driving report

![](../../.gitbook/assets/image-20250813-124745.png)

**When to use**: Driver safety analysis, insurance compliance reporting, and fleet risk management assessment for developing targeted training programs and reducing operational costs.

**What data you see**: Comprehensive driving behavior analysis including speeding violations, harsh driving events, and calculated safety scores for each vehicle, with precise GPS coordinates and timestamps for each incident.

<details>

<summary>Data processing logic</summary>

The eco-driving analysis processes telematics data through sophisticated behavioral pattern detection:

* **Speed violation detection**: The system continuously monitors vehicle speeds against configurable limits, applying grace periods and severity-based penalty structures. Speeding events require sustained violations (>60 seconds) to avoid penalizing brief speed spikes, while penalty points scale from light infractions (0-20 km/h over) to severe violations (>60 km/h over).
* **Harsh driving analysis**: Real-time acceleration calculations analyze speed changes over time intervals to detect harsh braking (>3.5 m/s² deceleration), harsh acceleration (>3.0 m/s²), and sharp turns using heading change thresholds (>30° at speeds >30 km/h). Each event includes GPS coordinates for location-specific pattern analysis.
* **Dynamic scoring system**: Safety scores derive from penalty point accumulation normalized per distance traveled, enabling fair comparison across different route lengths and operational patterns. The system uses configurable maximum scores with distance-based normalization to ensure consistent evaluation.
* **Violation documentation**: Each detected event captures precise GPS coordinates, timestamps, and severity measurements, creating comprehensive incident logs for driver coaching and compliance reporting.

The underlying algorithm processes 15-second aggregated GPS data from `raw_telematics_data.tracking_data_core`, applying haversine distance calculations for accurate geographic analysis and timestamp-based acceleration computations for behavioral assessment.

</details>

## Shifts report

![](../../.gitbook/assets/image-20250813-124757.png)

**When to use**: Workforce productivity analysis, operational pattern identification, and shift efficiency measurement for fleet scheduling optimization.

**What data you see**: Daily activity summaries showing total operational time, average speeds, maximum speeds, and activity periods for each vehicle, grouped by date and operational shifts.

<details>

<summary>Data processing logic</summary>

The shifts analysis processes raw tracking data through operational pattern detection:

* **Movement classification**: The system analyzes speed readings and time intervals to distinguish between active movement (≥3 km/h), temporary stops, and parked periods. Time gaps exceeding 300 seconds trigger new activity period detection.
* **Shift boundary detection**: Track segmentation uses configurable speed thresholds and time gap analysis to identify distinct operational periods. Each shift period includes precise start and end timestamps with duration calculations.
* **Activity aggregation**: Daily summaries combine all operational periods for each vehicle, calculating total activity duration, average operational speeds, and maximum speeds achieved during active periods.
* **Performance metrics**: The system generates utilization statistics by comparing active operational time against total elapsed time, providing efficiency insights for fleet management decisions.

GPS coordinate validation ensures only quality positioning data contributes to distance and speed calculations, while timestamp standardization to UTC enables consistent shift analysis across different geographic locations.

</details>

### Mileage report

<figure><img src="../../.gitbook/assets/image.png" alt=""><figcaption></figcaption></figure>

**When to use**: Fleet utilization analysis, operational efficiency assessment, and work time versus non-work time usage pattern identification for optimizing vehicle deployment and identifying unauthorized usage.

**What data you see**: Distance traveled categorized by work hours, non-work hours, and weekends, with weekly distribution trends, department comparisons, and detailed breakdowns showing active days and maximum trip distances.

<details>

<summary>Data processing logic</summary>

The vehicle mileage analysis processes GPS track data through time-based classification and distance aggregation:

* **Time category classification**: The system evaluates each GPS track segment against configurable work hours and calendar days to classify mileage into three distinct categories. Work time mileage captures distance traveled during configured business hours on weekdays, non-work time represents after-hours weekday travel, and weekend mileage encompasses all Saturday and Sunday movement regardless of time. This classification occurs at the track segment level, with each portion of a journey assigned based on its timestamp.
* **Distance calculation**: Geographic distance measurements use coordinate geometry algorithms to calculate distance the traveled between consecutive GPS points. The system processes raw position data from `raw_telematics_data.tracking_data_core`, converting integer-stored coordinates (divided by 10,000,000) to decimal degrees for accurate haversine distance calculations.
* **Temporal aggregation**: Weekly pattern analysis groups track segments by ISO week number, summing distances within each time category. The system generates both absolute mileage totals (in kilometers) and percentage distributions to reveal how operational patterns shift across weeks.
* **Grouping analysis**: Department, object, and driver comparisons aggregate individual vehicle data into organizational units. The system calculates average monthly mileage per vehicle by dividing total distance by the number of active days and normalizing to 30-day months, enabling fair comparison across different analysis periods.
* **Activity detection**: Active day calculations identify calendar dates with recorded mileage by analyzing track timestamps. Maximum track distance determination processes individual trip segments to identify the longest continuous journey for each grouping, using movement detection thresholds (≥3 km/h) and time gap analysis (>300 seconds) to separate distinct trips.

GPS quality validation ensures only reliable positioning data (satellites > 3, non-zero coordinates) contributes to distance calculations, while timestamp standardization to UTC enables consistent time classification regardless of vehicle geographic location.

</details>

### Trips report

<figure><img src="../../.gitbook/assets/image (1).png" alt=""><figcaption></figcaption></figure>

**When to use**: Journey pattern analysis, route optimization assessment, and operational behavior evaluation for understanding trip frequency, distance distribution, and identifying unusual travel patterns.

**What data you see**: Individual trip metrics including distance, duration, and average speed, with weekly volume trends, group-level comparisons, and complete trip-by-trip details showing start/end times and driver assignments.

<details>

<summary>Data processing logic</summary>

The vehicle trips analysis identifies and processes individual journeys through intelligent movement detection:

* **Trip detection algorithm**: The system analyzes GPS track data and vehicle state information to identify distinct trips using speed and time thresholds. A trip begins when vehicle speed exceeds the minimum idle speed threshold (default 3 km/h) and ends when speed drops below this threshold for the minimum idle time duration (default 5 minutes). Brief stops shorter than the idle time threshold are treated as pauses within the same trip rather than trip boundaries, filtering out momentary traffic stops or loading delays.
* **Enhanced detection parameters**: When available, the system incorporates ignition status and motion sensor data to refine trip detection accuracy. This multi-factor approach prevents false trip endings during brief stationary periods where the engine remains running, ensuring only meaningful parking events trigger trip completion.
* **Distance and duration calculation**: For each detected trip, the system calculates total distance using PostGIS geographic functions between consecutive GPS points from `raw_telematics_data.tracking_data_core`. Trip duration derives from the time difference between the first and last track point of the journey. Average speed calculations divide total distance by duration, providing realistic operational velocity that includes any brief in-trip stops.
* **Temporal aggregation**: Weekly analysis groups trips by ISO week number, calculating both trip counts and cumulative distances. This dual metric approach reveals whether operational volume changes correlate with average trip length variations—high trip counts with low total distance indicate many short journeys, while the inverse suggests fewer but longer trips.
* **Group comparison analytics**: Department, object, driver, and garage groupings aggregate trip data to enable comparative analysis. The system sums total distances, counts individual trips, and calculates mean trip durations for each unit. These metrics enable identification of operational role differences—delivery fleets show many short trips while field service vehicles may exhibit fewer but longer journeys.
* **Speed data availability**: When GPS signal quality is insufficient or speed data capture fails, the system cannot reliably calculate average speeds. This condition typically occurs during GPS signal loss in areas with poor satellite visibility (tunnels, dense urban areas, underground parking) or during data processing anomalies. The report displays "No speed data available" for affected periods, indicating these trips require investigation or have incomplete telematics records.

All trip timestamps convert to UTC for consistent analysis across different operational zones, while GPS quality validation (satellites > 3, non-zero coordinates) ensures only reliable positioning data contributes to trip detection and distance calculations.

</details>

## Next steps

When historical analysis reveals optimization opportunities or raises specific operational questions, progress to [Custom Analysis & SQL Configurator](../../explorer-for-datahub/custom-analysis-sql-configurator/) to create tailored investigations that address your unique fleet management requirements and develop custom analytical solutions.
