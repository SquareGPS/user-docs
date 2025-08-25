# Locking/Unlocking Padlock

## Locking/Unlocking PadlockOverview

The “Locking/Unlocking Padlock” rule is essential for organizations using GPS-enabled smart locks to secure valuable assets and critical areas. This rule monitors the status of these locks, ensuring that users are instantly notified whenever a lock is engaged or disengaged.

Specifically designed for GPS locks, this rule provides real-time alerts for all lock interactions, whether securing an area or locking cargo in a container.

## Rule settings

This rule is entirely dependent on the device's capabilities and hardware configuration. There are no specific settings to configure within the rule itself.

For common settings, please refer to [Rules and notifications](../).

## System operation details

* **Reset timer:** The “Locking/Unlocking Padlock” alert has a 1-minute reset timer, meaning it will not trigger more frequently than once every minute. Events occurring during this reset period will be omitted from notifications and reports.
* **Multiple trackers:** This rule supports multiple trackers, provided they can detect Locking/Unlocking (Padlock) events and have the feature integrated into the platform. Users can monitor these events across various devices efficiently.
* **GPS-independent processing:** The platform processes and displays Locking/Unlocking events even if the data packet lacks valid GPS coordinates. These events are recorded regardless of whether they occur inside or outside a geofence, ensuring no critical event is missed.
