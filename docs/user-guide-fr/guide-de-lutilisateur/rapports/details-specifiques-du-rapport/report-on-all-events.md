# Report on all events

The **Report on all events** in Navixy is a comprehensive tool that provides a detailed overview of every event logged by the platform. It covers a wide range of event types, categorized into general events, location-based events, hardware events, and service notifications.

This report is particularly valuable when there is a need to monitor device activity over a specified period, analyze event patterns, and document specific incidents.

## Overview of the report

The report on all events includes the following features:

- **Event logging:** Displays when and where each event occurred, along with associated driver information if a driver was assigned to the device at the time.
- **Event distribution graph:** Visual representation of how events were distributed over the selected time period.
- **Aggregate summary:** Summarizes the total number of events logged for each type during the reporting period.

To ensure that events are logged correctly, you must create the appropriate rules for your devices. This report also includes a driver column, indicating which driver was assigned to the device when each event was logged.

## Report parameters

In addition to standard report parameters, the report on all events includes:

- **Group by event type:** Organizes events into tables based on their type. If not selected, events are displayed in the order they were logged by the device.
- **Event type selection:** Allows you to filter the report by specific event types, divided into four groups. A quick search feature helps you find the events you need.

## Understanding event types

Events in this report fall into three main categories:

1. **Hardware events:** These are processed by the device using its internal algorithms and settings before being sent to the platform.
2. **Software events:** Logged based on data processed by the platform.
3. **Always running events:** Continuously triggered events that do not correspond to specific rules.

Here’s a breakdown of common event types and their associated rules:

- **General events:**
  - **Inside/outside auto-created geofence:** Triggered by the 'unauthorized movement (by coordinates)' rule.
  - **Cruise control on/off:** Associated with the 'cruise control on/off' rule.
  - **Tracker attach:** Related to the 'tracker detach from object' rule.
  - **Forward collision warning:** Linked to the 'advanced driver assistance systems (ADAS)' rule.
  - **GPS signal lost/recovered:** Tied to the 'GPS signal lost/recovered' rule.
  - **Harsh driving:** Triggered by the 'harsh driving' rule.
  - **Parking start/end:** Related to the 'parking state detection' rule.
- **Location-based events:**
  - **Geofence entry/exit:** Logs when a vehicle enters or exits a predefined geofence.
  - **POI visits:** Tracks visits to points of interest (POIs).
- **Hardware events:**
  - **Ignition activation:** Logs when the ignition is turned on or off.
  - **GSM/GPS jamming:** Indicates attempts to jam the GSM or GPS signals.
- **Service notifications:**
  - **Low battery:** Alerts when the device's battery level drops below a certain threshold.
  - **Check engine light (MIL) on:** Logs when the vehicle’s check engine light is activated.

## Data visualization

### Events table

The **events table** provides a detailed list of all events, including:

- **Time:** The exact time the event occurred.
- **Event name:** The name of the event that was triggered.
- **Address:** The location where the event took place.
- **Employee:** The employee assigned to the device when the event was received.

### Event distribution graph

The **event distribution graph** visually represents the frequency and distribution of events over the selected time period. This can help identify patterns or unusual spikes in activity.

### Number of events by type

This section of the report tallies the total occurrences of each event type during the reporting period. If a specific event type did not occur, it will be marked with a dash.