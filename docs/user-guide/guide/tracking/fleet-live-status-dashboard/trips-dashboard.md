---
description: Review the last 7 days of fleet trips in one view: utilization KPIs, top-performer charts by distance and speed, and a sortable trip details table.
---

# Trips dashboard

The **Trips Dashboard** is the second tab of the Dashboard app. Where the **Fleet Live Status Dashboard** answers "what is the fleet doing right now?", the Trips Dashboard answers "what did the fleet do over the past week?". It pulls completed trips together into a single view of utilization, distance, duration, and per-object performance, so you can spot under-used vehicles, over-worked ones, and unusual driving behavior without building a report.

{% hint style="info" %}
The Trips Dashboard is currently in beta (v1.0.0). It's an early version released so we can shape it based on real feedback. If something is missing, confusing, or could be more useful, please tell us through the **Send Feedback** button at the top of the tab. The two dashboards version independently, so the Fleet Live Status and Trips tabs may show different version numbers.
{% endhint %}

The Fleet Live Status tab opens by default when you open the Dashboard app; switch to the **Trips Dashboard** tab from the tab bar at the top of the page.

## What counts as a trip

Every number on this dashboard is built from trips, so it helps to know what the platform treats as a trip before reading the panels. The same trip-building logic is used elsewhere in the platform; this section is a short summary so the dashboard makes sense in context.

The platform processes incoming GPS data every minute and stitches points into trips. Only well-formed points are eligible: a point needs an event ID, valid coordinates, and satellite information. Points that look like GPS jumps (more than 5 km from the previous point) and points that arrive out of order are discarded.

A point counts as moving when the recorded speed is at least 3 km/h, and additionally either the distance from the previous point exceeds 50 m or the device's hardware "is moving" flag is set. A new trip starts after a gap of at least 20 minutes with no data from the device, or when a device starts moving again after being parked for at least 5 minutes. The trip's `Start Time` is the timestamp of the first moving point, and the `End Time` is when the final parking segment of the trip began.

For a trip to be recorded at all, four conditions need to hold. Trips that fail any of these checks are discarded, which is why some very short journeys never show up in the dashboard, and why a vehicle that drifted slightly while parked won't generate a trip.

* Total distance is at least 100 m
* Maximum speed reaches at least 3 km/h
* At least 2 GPS points
* Movement was detected

## Data window and refresh

The Trips Dashboard always shows the **last 7 days** of trip data. There is no date picker, and the window cannot be changed. For trip data over a different period, use the [Trips and parkings report](../../reports/specific-report-details/trip-report.md).

The dashboard refreshes itself every **90 seconds** while the browser tab is in focus, and the **Update** button in the top-right corner forces an immediate refresh. The 90-second cadence is slower than the Fleet Live Status tab's 60 seconds, because the trip-level aggregations span a week of data and are more expensive to compute.

Because trip processing runs every minute with a small overlap, a trip that ended in the last one or two minutes may not yet be visible, or may appear with an incomplete end time. It will be reflected on the next refresh.

## Headline metrics

The top of the dashboard is a row of nine KPI tiles, arranged in two rows, that summarize the week at fleet level.

The first two tiles frame the week in terms of activity:

* **Total Objects**: every device registered in your account.
* **Objects with Trips**: devices that recorded at least one trip in the last 7 days. The gap between these two is your share of inactive or stored devices for the week; if it's large, the per-object averages elsewhere on the page will look low for reasons that aren't about driver behavior.

The next three describe trip volume:

* **Amount of Trips**: total count of trips across the fleet.
* **Trips per Object, AVG**: average number of trips per device.
* **Distance per Trip, AVG**: average trip length in kilometers, rounded to two decimal places.

Two tiles cover distance:

* **Total Distance**: sum of all trip distances over the period.
* **Distance per Object, AVG**: average kilometers per device.

Two tiles cover time on the move:

* **Total Duration**: sum of all trip durations.
* **Duration per Trip, AVG**: average trip duration, formatted as `X h Y min` (seconds truncated, not rounded).

{% hint style="info" %}
**Trips per Object, AVG** and **Distance per Object, AVG** both divide by the total number of registered devices, not by the number that actually had trips. If your account carries many inactive or stored devices, these averages will look lower than your active fleet's picture alone. Use **Objects with Trips** and the **Objects with/without Trips** donut for the active-only view.
{% endhint %}

## Per-object charts

Below the KPI tiles, six charts break the same week of data down by object.

* **Objects with/without Trips**: a donut chart showing the fleet split between devices that recorded at least one trip during the week and those that didn't. The visual companion to the **Total Objects** and **Objects with Trips** tiles, and the quickest way to spot whether the fleet's activity rate matches expectations.
* **Top 10 Objects by Distance**: ranks vehicles by total kilometers. A vehicle at the top here carries the heaviest workload; compare with the Trips chart to distinguish long-haul from short-loop patterns.
* **Top 10 Objects by Trips**: ranks vehicles by number of trips. A delivery van running short loops can top this chart without appearing on the Distance chart, and that contrast is often worth investigating.
* **Top 10 Objects by Speed**: ranks devices by highest maximum speed during the week. The chart to check when reviewing driving behavior or investigating speed alerts. Note: it may include speeds from trips still in progress when the dashboard loads, so its time coverage can differ slightly from the other panels.
* **Top 10 Objects by Idling Time**: surfaces idling, a common source of hidden fuel and maintenance cost, so you can act during the week rather than discovering it in a monthly report.
* **Top 10 Objects by Engine Hours**: best read alongside Idling Time. A vehicle that leads in engine hours but not in distance is typically running while stationary, which often traces back to the same idling pattern.

## Objects trips details

The **Objects Trips Details** table at the bottom of the dashboard lists individual trip records, one row per trip. Every column is sortable by clicking its header, and the table scrolls horizontally on narrower screens. Columns include:

* Object label
* Start and end times
* Distance and duration
* Start and end coordinates
* Start and end addresses
* Number of GPS points in the trip

{% hint style="info" %}
The table is scoped to trips longer than 10 km, while the KPI tiles count every recorded trip. Shorter trips that still meet the trip-building rules (at least 100 m, 3 km/h, 2 points, movement detected) are counted in **Amount of Trips** and shown in the charts, but don't appear as rows here. Use the KPI tile as your answer to "how many trips happened" and the table as your answer to "where the longer journeys went".
{% endhint %}

The address columns are best-effort. Start and end addresses are resolved by reverse geocoding the coordinates against the Navixy geocoder. When the geocoder is unavailable, address cells appear blank without an error message. Address resolution also covers the first 500 rows of the table by default, so rows beyond that limit appear with coordinates but without addresses.

## Exporting panel data

Every panel on the Trips Dashboard, both charts and tables, has a download icon in its top-right corner. Click it to export the panel's current data as a CSV file. The export reflects the state of the panel at the moment you click, which is useful for capturing a snapshot for a handover, a weekly report, or further analysis in a spreadsheet.

Like the Fleet Live Status tab, the Trips Dashboard does not currently support global filters, custom time ranges, or shared links.

## Sending feedback

The **Send Feedback** button in the top-right corner of the Trips Dashboard opens a short form scoped to this tab. You can select the specific widget your feedback relates to (or the Dashboard as a whole), write a message up to 399 characters, and send it directly to the product team. During the beta, this is the most direct channel for influencing how the Trips Dashboard evolves.
