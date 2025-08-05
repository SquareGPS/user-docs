# GPS jamming

## Overview

GPS jamming occurs when GPS or GNSS frequencies are disrupted by interference from nearby sources, a process known as masking or frequency masking. This interference can cause the device to lose its connection with satellites, leading to distorted or completely lost GPS data. GPS jamming differs from [GSM jamming](../device-connection/gsm-jamming.md), as they operate on separate frequency bands. When GPS jamming occurs, the device may lose its satellite connection, resulting in either zero visible satellites or invalid coordinates that the tracking platform cannot recover.

The GPS jamming rule enhances vehicle and asset security by preventing theft in scenarios where GPS signal interference is used to disable tracking systems. For instance, if a vehicle is targeted for theft or hijacking, this rule provides a timely alert, allowing for quick action to prevent loss or harm. It's an essential tool for businesses to protect their fleets and valuable assets.

## Rule settings

This rule is entirely dependent on the device's capabilities and hardware configuration. There are no specific settings to configure within the rule itself.

For common settings, please refer to [Rules and notifications](../../rules-and-notifications.md).

## System operation details

- **Reset timer:** The "GPS jamming" alert has a 5-minute reset timer, meaning that the alert will not trigger more than once every 5 minutes. If an event occurs during the reset period, it will be omitted from the platform, including reports.
- **Multiple devices:** This rule allows you to select multiple trackers to receive notifications from, provided that the selected trackers support GPS jamming events and the feature is integrated into the platform. This flexibility enables monitoring of GPS jamming events across various vehicles or devices.
- **GPS-independent event alert:** The platform will register and display the event even if it is received in a packet without valid coordinates. The event will be displayed regardless of whether it occurred within or outside the bound geofences, as the platform prioritizes showing potentially critical events over omitting them.

## See also

- [GSM jamming](../device-connection/gsm-jamming.md)