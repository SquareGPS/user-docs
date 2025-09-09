# Engine hours report

The **Engine Hours** report in Navixy provides detailed insights into the duration your vehicle's engine was running, both while in motion and during idling periods. This report is essential for fleet managers who need to monitor engine usage, optimize operational efficiency, and plan maintenance schedules. Below is a comprehensive guide on how this report works, the parameters involved, and how to interpret the data.

## Overview

The Engine Hours report is designed to show you the total time your vehicle's engine was on, segmented into periods of motion and idling. This report includes several key visual aids, such as a period activity chart and a daily activity bar graph, to help you quickly understand and analyze the data.

## How it works

The report calculates engine hours based on data points received by the Navixy platform. For accurate calculations, the following configurations and conditions must be met:

1. **Ignition sensor configuration:**\
   The ignition sensor must be correctly connected to the device and accurately register the ignition status. This can be a discrete ignition sensor or an ignition-based virtual sensor on the platform.
2. **Ignition duration:**\
   The ignition must be on for at least 60 seconds for the time to be recorded in the report.
3. **Parking detection:**\
   The platform uses parking detection settings to differentiate between engine hours spent in motion and idling. For example, if the parking detection speed is set below 3 km/h and the vehicle remains at or below this speed for more than 5 minutes, this time will be recorded as idling, not motion.
4. **Data point frequency:**\
   The frequency with which your device sends data points affects the accuracy of the report. Delays in data transmission can lead to inaccuracies, particularly if the ignition state changes but isn't immediately reported.

### Example calculation

| Point | Time     | Ignition State | Engine Hours                               |
| ----- | -------- | -------------- | ------------------------------------------ |
| 1     | 16:00:00 | Off            | 0 minutes                                  |
| 2     | 16:01:00 | On             | 0 minutes (ignition was off at last point) |
| 3     | 16:01:32 | On             | 0 minutes (less than 60 seconds)           |
| 4     | 16:05:32 | Off            | 4 minutes and 32 seconds                   |

## Report parameters

The Engine Hours report includes several configurable parameters that allow you to customize the output to meet your specific needs:

* **Show details:** Provides detailed information about the specific location and time when the engine was on.
* **Display summary:** Shows an overview of all devices. You can enable or disable this feature depending on whether you need a summary page.
* **Display only summary:** Aggregates data for multiple trackers into a single summary. This option requires at least two devices.
* **Use smart filter:** Excludes short trips from the report. A trip is considered short if it covers less than 300 meters and the device transmits fewer than four data points.

## Visualizations

![Overall engine activity diagram](../../../user-guide/reports/specific-report-details/attachments/image-20240815-010415.png)

### Overall activity diagram

This diagram provides a comprehensive view of the total time the engine was on during the selected period. It distinguishes between the time the engine was off, time spent in motion, and time spent idling.

### Daily activity histogram

The histogram breaks down engine hours into daily segments, showing both motion and idle times. Hovering over each day provides a more detailed view of that day's engine activity.

### Engine hours table

The table presents detailed daily data, including:

* **Date:** The specific day for which the data is calculated.
* **Engine Hours:** Total engine hours for the day.
* **In Motion:** Time spent in motion and its percentage of total engine hours.
* **Idling:** Time spent idling and its percentage of total engine hours.
* **Average Interval:** The average duration the engine was running after each ignition on event.
* **Mileage:** The distance traveled while the engine was running.
* **Average Speed:** The average speed for the day.
* **Intervals:** The number of intervals during which the engine was on throughout the day.

{% hint style="info" %}
If you notice a discrepancy between the mileage in the Trip report and the Engine hours report, check two things:

* Ensure the smart filter setting is consistently applied across all reports. Inconsistencies in its use can cause discrepancies.
* Verify that the ignition was detected during all vehicle movements by comparing trip start and end times with the engine hours data.
{% endhint %}

## Interpreting the report

To effectively use the Engine hours report, consider the following:

* **Discrepancies:** If you notice a discrepancy between the mileage in the trip report and the engine hours, check whether the smart filter is applied consistently across all reports and whether the ignition was correctly detected during motion.
* **Analyzing data:** The report allows you to analyze engine usage by employees, assess vehicle efficiency, estimate replacement timelines, calculate depreciation costs, and reconfigure fuel and lubricant costs based on idle time.
