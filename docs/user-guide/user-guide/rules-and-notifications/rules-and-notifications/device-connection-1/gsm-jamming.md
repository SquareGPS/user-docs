# GSM jamming

## Overview

GSM jamming refers to the disruption of GSM signals (mobile or cellular signals) due to interference from nearby sources. This interference, often called masking or frequency masking, can prevent mobile devices from connecting to mobile networks, affecting services such as mobile data (2G, 3G, 4G, LTE), text messaging, and voice calls. In the context of GPS tracking, GSM jamming can lead to the loss of real-time data communication, making it crucial to have detection rules in place.

For example, a logistics company using GPS-equipped vehicles to transport valuable cargo relies on GSM signals for real-time location tracking. If GSM jamming occurs, these signals are disrupted, potentially compromising the security of the shipments. By implementing rules to detect GSM jamming, the company can receive immediate alerts, allowing for swift action to protect their assets.

## Rule settings

This rule is entirely dependent on the device's capabilities and hardware configuration. There are no specific settings to configure within the rule itself.

For common settings, please refer to [Rules and Notifications](../../).

## System operation details

* **Reset timer:** The "GSM jamming" alert has a 5-minute reset timer, meaning the alert will not trigger more frequently than once every 5 minutes. If an event occurs during the reset period, it will be omitted by the platform and will not be included in reports.
* **Multiple devices:** Users can select multiple trackers to monitor under this rule. The only requirement is that the selected trackers must support GSM jamming events and be integrated with the platform. This flexibility allows users to monitor this event type across various vehicles or devices conveniently.
* **GPS-independent event alert:** The platform will register and display the event even if it is received in a message without valid GPS coordinates. This ensures that users are informed of the event, regardless of location data. The Inside/Outside radio button settings for geofences are ignored in these cases, as the platform prioritizes displaying potentially critical events.

## See also

* [GPS jamming](../device-positioning-1/gps-jamming.md)
