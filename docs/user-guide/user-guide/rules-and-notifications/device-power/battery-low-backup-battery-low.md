# Battery low (Backup battery low)

## Overview

A GPS device reports a battery low alert when the charge level of its internal battery drops below a predetermined threshold. This alert is triggered to notify users that the device's power is running low, indicating that the battery needs to be recharged or replaced soon.

In the case of portable trackers, this alert signals that the primary power source is depleting, while for vehicle-mounted trackers, it may indicate that the backup battery is running low, potentially compromising the device's ability to continue tracking if the main power supply is lost.

![](https://squaregps.atlassian.net/wiki/images/icons/grey_arrow_down.png)

Role of internal batteries in GPS devices

An internal battery in a GPS device is a built-in power source that plays a crucial role in the device's functionality. Depending on the purpose of the GPS tracker, this internal battery can serve different roles.

* **In portable GPS trackers,** the internal battery is typically the primary power source. These batteries are essential for tracking assets, people, or vehicles in scenarios where external power may not be available.
* **For vehicle-mounted GPS trackers,** the internal battery usually acts as a backup power source. This backup battery kicks in when the main power supply from the vehicle is interrupted, whether due to disconnection, tampering, or vehicle battery failure. The backup battery ensures continuous tracking and data transmission, providing an extra layer of security and reliability, especially in critical fleet management or anti-theft applications.

## Two battery monitoring rules

In Navixy, there are two distinct rules designed to monitor the battery status of your GPS devices: the "Low Battery" rule and the "Backup Battery Low" rule.

* **The "Low Battery" rule** applies to the primary power source of the device, typically used in portable trackers or devices solely reliant on internal batteries.
* **The "Backup Battery Low" rule** specifically monitors the charge level of secondary or backup batteries, which are commonly found in vehicle-mounted trackers.

These are hardware-based rules, meaning the device itself or its configuration determines the trigger threshold for the low battery alert. When the battery charge drops below this threshold, the device reports it, and the system sends a notification, allowing users to take proactive steps to recharge the device and prevent downtime.

## Rule settings

This rule is entirely dependent on the device's capabilities and hardware configuration. There are no specific settings to configure within the rule itself.

For common settings, please refer to [Rules and Notifications](../).

## Platform specifics

The "Low battery" and "Backup battery low" alerts share several operational similarities, but there is a difference in their reset timers.

* **Reset timers**: The "Backup battery low" alert has a 1-minute reset timer, meaning the alert will not trigger more frequently than once per minute. In contrast, the "Low battery" alert has a longer 30-minute reset timer, so it will not trigger more frequently than once every 30 minutes. If an event occurs during the reset period for either rule, it will be omitted from the platform, including reports.
* **Tracker selection**: Both rules allow users to monitor multiple trackers, provided the trackers support the respective events and the feature is integrated on the platform. This capability enables efficient monitoring of battery levels across various vehicles or devices.
* **Event registration**: For both rules, the platform will register and display the event even if it is received in a packet without valid coordinates. This ensures that users are informed of the event regardless of its location, maintaining consistent oversight of their assets.
