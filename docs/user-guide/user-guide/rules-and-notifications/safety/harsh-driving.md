# Harsh driving

## Overview

The "Harsh driving" rule is designed to help businesses monitor and improve driving behavior, ensuring safer vehicle operation and reducing the risk of accidents. This rule is particularly valuable for fleets, rental car companies, and logistics operations, where driving quality directly impacts vehicle maintenance costs, safety, and customer satisfaction. By detecting and responding to harsh driving incidents, businesses can better manage their vehicles, reduce wear and tear, and maintain a high standard of service.

This rule works by utilizing the devices’s built-in accelerometer to monitor sudden acceleration, harsh braking, and sharp turns. When the GPS device detects any of these events, it sends the data to the platform, which then generates alerts and logs the incidents for review. To use this rule, ensure that the harsh driving detection feature is configured correctly in the Device settings or tracker configurator.

## Rule settings

Ensure that the harsh driving feature is configured in the Devices and settings menu, specifically in the Harsh Driving widget, or through the device’s configuration tool. Once set up, users can create and manage the rule from the platform.

No other specific settings are required for this rule. For common settings, please refer to [Rules and Notifications](../../rules-and-notifications.md).

## System operation details

- **Reset timer:** The "Harsh Driving" alert has a 10-second reset timer, meaning the alert will not trigger more frequently than once every 10 seconds. If an event occurs during the reset period, the platform will suppress the alert to keep notifications and reports accurate and manageable.
- **Multiple devices:** Users can apply this rule to multiple trackers, provided they support harsh driving detection and have this feature integrated into the platform. This allows users to monitor harsh driving incidents across various vehicles or devices efficiently.
- **GPS-independent event processing:** The platform processes and displays harsh driving events even if the data packet lacks valid GPS coordinates. These events are recorded regardless of whether they occur inside or outside a designated geofence. The Inside/Outside geofence settings are bypassed in this case to ensure no critical event is missed.