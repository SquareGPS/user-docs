# Auto-geofencing

## Overview

The "Auto geofencing" feature, available in select GPS tracking devices, is a robust solution designed to enhance vehicle security by preventing unauthorized towing or theft.

This feature automatically establishes a geofence around the vehicle's current location when the ignition is turned off. If the vehicle moves outside this predefined boundary without the ignition being engaged, the system immediately triggers an alert, providing an additional layer of protection. Utilization of the Auto geofencing feature requires a GPS tracker that supports this functionality.

## Rule settings

This rule is entirely dependent on the device's capabilities and hardware configuration. There are no specific settings to configure within the rule itself.

For common settings, please refer to [Rules and Notifications](../).

## System operation details

* **Reset timer**: The "Auto Geofencing" alert has a 1-minute reset timer, meaning it won’t trigger more often than once every minute. If an event occurs during the reset period, it will be omitted from reports.
* **Multiple devices**: You can select multiple trackers for this rule, provided they support Auto Geofencing events and the feature is integrated into the platform. This flexibility allows you to monitor several vehicles or assets simultaneously.
* **GPS-independent event alert**: If the platform receives an Auto Geofencing event from a tracker without valid GPS coordinates, the event will still be counted as valid and displayed. This ensures that critical events are not missed, regardless of their occurrence within or outside the defined geofences.
