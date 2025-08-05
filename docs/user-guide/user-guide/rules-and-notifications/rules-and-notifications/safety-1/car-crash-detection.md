# Car Crash Detection

## Overview

The "Car Crash Detection" rule monitors and alerts you to significant driving events by specifically detecting vehicle collisions. This rule helps maintain awareness of driver behavior and enables your dispatch team to respond swiftly to any accidents.

This rule is hardware-dependent, triggered by accelerometer data from the GPS device. The event is generated on the GPS device side, and the platform displays the alert based on the data received.

Accurate collision detection requires proper installation of the tracker, including correct wiring and alignment along the x, y, and z axes. Detailed installation instructions are typically provided in the tracker’s user manual.

## Rule settings

As this rule is processed on the GPS device side rather than in the cloud, no additional settings are required.

For common settings, please refer to [Rules and Notifications](../../).

## System operation details

* **Reset timer:** The "Car Crash Detection" alert has a 1-minute reset timer, meaning the alert will not trigger more frequently than once per minute. If another collision event is detected within this reset period, it will be omitted from the platform and reports.
* **Multiple devices:** This rule allows you to select multiple trackers for notifications. The only requirement is that the trackers must support Car Crash Detection events and have this feature integrated into the platform. This enables monitoring of collision events across various vehicles.
* **GPS-independent event alert:** The platform will register and display a Car Crash Detection event even if the data packet lacks valid GPS coordinates. The system prioritizes displaying critical events, regardless of whether they occurred inside or outside designated geofences. The Inside/Outside geofence settings are ignored for this rule to ensure that no crucial event is missed..
