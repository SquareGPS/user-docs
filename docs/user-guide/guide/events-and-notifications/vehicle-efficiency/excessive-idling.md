# Excessive idling

## Overview

Excessive idling is an important event to monitor in fleet management, as it directly impacts fuel consumption, vehicle wear, and overall operational efficiency. Navixy offers two methods for detecting excessive idling: hardware related and platform related. Each method has its own advantages and is suited to different types of fleet needs.

**The platform related rule** is managed by the platform and uses parameters set by the user, such as idling duration and parking detection. This rule is ideal for those who need a flexible and customizable solution that works with any tracker that reports basic data like ignition state and GPS location.

**The hardware related rule,** on the other hand, relies on the GPS tracker’s built-in capability to detect idling events. The hardware generates and transmits the idling event directly to the platform. This method is advantageous for trackers that have advanced idling detection features, offering potentially greater accuracy and additional functionality.

## Rule settings

### Platform related

* **Idling duration:** Set the duration after which idling will be considered excessive. The rule will monitor when a vehicle is parked (as determined by the Parking Detection settings) and the ignition is ON. If the vehicle remains in this state beyond the specified duration, a notification will be triggered.

For common settings, please refer to [Rules and Notifications](../).

### Hardware related

* **Device-specific settings:** This rule relies on the hardware’s configuration for detecting idling. You should refer to your device documentation to set up idling detection on the tracker. The platform will then receive and display idling events based on the device’s output.

For common settings, please refer to [Rules and Notifications](../).

## System operation details

* **Platform related idling detection:** The platform continuously monitors the vehicle’s ignition state and parking status. When the vehicle is parked with the ignition ON, the platform starts counting the idling duration. If the idling exceeds the user-defined threshold, the system sends an alert. This method works with a wide range of trackers and offers flexibility in setting custom idling thresholds.
* **Hardware related idling detection:** The tracker itself monitors idling and sends an event to the platform when idling exceeds the predefined threshold set in the device. The platform simply forwards this event to the user. This method can offer higher accuracy and advanced features depending on the tracker’s capabilities.
* **Notifications:** Regardless of the detection method, you will receive notifications through the user interface, email, or SMS. These notifications help fleet managers take immediate action to reduce unnecessary idling, thus saving fuel and reducing wear on the vehicles.
* **Reports:** You can generate reports on excessive idling to analyze patterns and make data-driven decisions to improve fleet efficiency. These reports can be particularly useful for identifying habitual idling or assessing the impact of idling on fuel costs and vehicle maintenance.
