# Trips dashboard

The **Trips Dashboard** is the second tab of the Dashboard app. Where the **Fleet Live Status Dashboard** answers "what is the fleet doing right now?", the Trips Dashboard answers "what did the fleet do over the past week?". It pulls completed trips together into a single view of utilisation, distance, duration, and per-object performance, so you can spot under-used vehicles, over-worked ones, and unusual driving behaviour without building a report.

{% hint style="info" %}
The Trips Dashboard is currently in beta (v1.0.0). It's an early version released so we can shape it based on real feedback. If something is missing, confusing, or could be more useful, please tell us through the **Send Feedback** button at the top of the tab. The two dashboards version independently, so the Fleet Live Status and Trips tabs may show different version numbers.
{% endhint %}

The Fleet Live Status tab opens by default when you open the Dashboard app; switch to the **Trips Dashboard** tab from the tab bar at the top of the page.

## What counts as a trip

Every number on this dashboard is built from trips, so it helps to know what the platform treats as a trip before reading the panels. The same trip-building logic is used elsewhere in the platform; this section is a short summary so the dashboard makes sense in context.

The platform processes incoming GPS data every minute and stitches points into trips. Only well-formed points are eligible: a point needs an event ID, valid coordinates, and satellite information. Points that look like GPS jumps (more than 5 km from the previous point) and points that arrive out of order are discarded.

A point counts as moving when the recorded speed is at least 3 km/h, and additionally either the distance from the previous point exceeds 50 m or the device's hardware "is moving" flag is set. A new trip starts after a gap of at least 20 minutes with no data from the device, or when a device starts moving again after being parked for at least 5 minutes. The trip's `Start Time` is the timestamp of the first moving point, and the `End Time` is when the final parking segment of the trip began.

For a trip to be recorded at all, four conditions need to hold: the total distance is at least 100 m, the maximum speed reaches at least 3 km/h, there are at least 2 GPS points, and movement was actually detected. Trips that fail any of these checks are discarded. This is why some very short journeys never show up in the dashboard, and why a vehicle that drifted slightly while parked won't generate a trip.

## Data window and refresh

The Trips Dashboard always shows the **last 7 days** of trip data. There is no date picker, and the window cannot be changed. For trip data over a different period, use the [Trips and parkings report](/docs/user/guide/reports).

The dashboard refreshes itself every **90 seconds** while the browser tab is in focus, and the **Update** button in the top-right corner forces an immediate refresh. The 90-second cadence is slower than the Fleet Live Status tab's 60 seconds, because the trip-level aggregations span a week of data and are more expensive to compute.

Because trip processing runs every minute with a small overlap, a trip that ended in the last one or two minutes may not yet be visible, or may appear with an incomplete end time. It will be reflected on the next refresh.

## Headline metrics

The top of the dashboard is a row of nine KPI tiles, arranged in two rows, that summarise the week at fleet level.

The first two tiles frame the week in terms of activity. **Total Objects** counts every device registered in your account, and **Objects with Trips** counts those that recorded at least one trip in the last 7 days. The gap between them is your share of inactive or stored devices for the week, and it's the first thing to glance at: if Objects with Trips is much smaller than Total Objects, the per-object averages elsewhere on the page will look low for reasons that aren't about driver behaviour.

The next three tiles describe how many trips happened. **Amount of Trips** is the total count of trips across the fleet. **Trips per Object, AVG** is the average number of trips per device, and **Distance per Trip, AVG** is the average trip length in kilometres, rounded to two decimal places.

Two distance tiles cover ground covered: **Total Distance** is the sum of all trip distances over the period, and **Distance per Object, AVG** is the average kilometres per device.

Two duration tiles cover time on the move: **Total Duration** sums all trip durations, and **Duration per Trip, AVG** gives the average trip duration. Both are formatted as `X h Y min`, with seconds truncated rather than rounded.

One important detail about the "per Object, AVG" tiles. **Trips per Object, AVG** and **Distance per Object, AVG** both divide by the total number of registered devices, not by the number of devices that actually had trips. If your account carries many inactive or stored devices, these averages will look lower than the picture for your active fleet alone. The **Objects with Trips** tile (and the **Objects with/without Trips** donut described next) is the right view for the active-only counterpart.

## Per-object charts

Below the KPI tiles, six charts break the same week of data down by object.

The **Objects with/without Trips** donut sits on the left and shows the fleet split between devices that recorded at least one trip during the week and those that didn't. It's the visual companion to the **Total Objects** and **Objects with Trips** tiles, and the quickest way to spot whether the fleet's activity rate matches expectations.

The remaining five charts are top-10 bar charts that rank individual vehicles by different measures. **Top 10 Objects by Distance** and **Top 10 Objects by Trips** are the clearest views of workload. A vehicle that leads on distance is the one carrying the heaviest workload by kilometres; a vehicle that leads on trips makes the most journeys. These don't always line up: a delivery van running short loops can sit at the top of the trips chart without appearing on the distance chart, and that pattern itself is worth spotting.

**Top 10 Objects by Speed** ranks devices by the highest maximum speed recorded during the week, which is the chart to check when reviewing driving behaviour or investigating speed alerts. This chart may also include speeds from trips that are still in progress when the dashboard loads, so its time coverage can differ very slightly from the other panels.

**Top 10 Objects by Idling Time** and **Top 10 Objects by Engine Hours** are usually read together. Idling is a common source of hidden fuel and maintenance cost, so surfacing it here lets you act on it during the week rather than discovering it in a monthly report. Engine Hours adds context: a vehicle that leads in engine hours but not in distance is typically running while stationary, which often loops back to the same idling pattern.

## Objects trips details

The **Objects Trips Details** table at the bottom of the dashboard lists individual trip records, one row per trip. Columns include the object's label, start and end times, distance, duration, start and end coordinates, start and end addresses, and the number of GPS points in the trip. Every column is sortable by clicking its header, and the table scrolls horizontally on narrower screens.

One thing to note when comparing this table to the KPI tiles above. The table is scoped to trips longer than 10 km, while the KPI tiles count every recorded trip. Shorter trips that still meet the trip-building rules above (at least 100 m, 3 km/h, 2 points, movement detected) are counted in the **Amount of Trips** tile and shown in the charts, but they don't appear as individual rows in this table. As a result, the row count is typically lower than the **Amount of Trips** tile, sometimes substantially. Use the KPI tile as your answer to "how many trips happened" and the table as your answer to "where the longer journeys went".

The address columns are best-effort. Start and end addresses are resolved by reverse geocoding the coordinates against the Navixy geocoder. When the geocoder is unavailable, address cells appear blank without an error message. Address resolution also covers the first 500 rows of the table by default, so rows beyond that limit appear with coordinates but without addresses.

## Exporting panel data

Every panel on the Trips Dashboard, both charts and tables, has a download icon in its top-right corner. Click it to export the panel's current data as a CSV file. The export reflects the state of the panel at the moment you click, which is useful for capturing a snapshot for a handover, a weekly report, or further analysis in a spreadsheet.

Like the Fleet Live Status tab, the Trips Dashboard does not currently support global filters, custom time ranges, or shared links.

## Sending feedback

The **Send Feedback** button in the top-right corner of the Trips Dashboard opens a short form scoped to this tab. You can select the specific widget your feedback relates to (or the Trips Dashboard as a whole), write a message up to 399 characters, and send it directly to the product team. During the beta, this is the most direct channel for influencing how the Trips Dashboard evolves.
