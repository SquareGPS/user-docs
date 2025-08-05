# Deviation from the route

## Overview

The route deviation rule enables monitoring of deviations from a predefined route. This rule ensures that vehicles or objects adhere to planned routes, improving efficiency and enhancing security by promptly identifying and addressing any deviations. Users will receive notifications whenever a vehicle or object deviates from the specified route, helping to maintain compliance and optimize operations.

## Rule settings

#### Route Geofences around paths

To utilize the route deviation rule, you must first create one or more route geofences in the platform. Follow these steps to set up the rule:

1. **Create route Geofences**: Before setting up the rule, ensure you have created route geofences categorized as "route."
2. **Select Geofences**: Choose the route geofences you want to monitor for deviations. Only geofences categorized as "route" can be used for this purpose.

For common settings, please refer to [Rules and Notifications](../../rules-and-notifications.md).

## System operation details

- The "Deviation from the route" alert has a 10-second reset timer, meaning the alert event will not occur more often than once every 10 seconds. If an event occurs while the rule is waiting for the reset, the platform will omit the event, including in reports.
- This rule is processed in the cloud and not tied to any specific hardware, allowing it to be applied to multiple trackers simultaneously. This flexibility enables you to select several trackers within a single rule.