# Fuel level change

## Overview

Monitoring fuel levels is crucial for managing fuel consumption and detecting unauthorized usage. The Fuel Level Change rule is designed to provide real-time notifications whenever significant changes in fuel levels occur, such as sudden increases or decreases.

These notifications can be delivered through the web user interface, SMS, or email, and can be consolidated into reports. This proactive monitoring helps users quickly respond to fuel level changes, potentially lowering fuel costs and resolving disputes among employees.

> \[!INFO] Before setting up this rule, ensure that the fuel level sensor you intend to monitor is properly configured. For detailed instructions on setting up and configuring fuel level sensors, please refer to the [Fuel level sensor section](../../devices-and-settings/vehicle-sensors/measurement-sensors/fuel-level-sensor.md).

## Rule settings

#### Sensor

Specify the fuel level sensor that will be used as the source for notifications and analysis. The number of fuel changes indicated is regulated by the Accuracy parameter of the fuel level sensor, which is explained in the [Fuel level sensor section](../../devices-and-settings/vehicle-sensors/measurement-sensors/fuel-level-sensor.md).

For common settings, please refer to [Rules and Notifications](../).

## System operation details

* The platform smooths sensor data and compares the total change within a 10-minute window against the fuel sensor's Accuracy setting to determine if a notification should be triggered. For example, with an Accuracy setting of 5%, a fuel level change of 5 liters or more for a 100-liter tank within 10 minutes will trigger an alert. If the cumulative change meets or exceeds this threshold, the platform will send a notification.
* Fuel change volume estimation is not currently included in notifications but will be available soon.
* The "Fuel Level Change" alert has a 15-minute reset timer, meaning the alert will not trigger more often than once every 15 minutes. If a fuel level change occurs while the rule is in its reset period, the platform will omit the event, including in the reports.
* This rule supports only one device per rule. This limitation is due to the complexities involved in cross-referencing multiple measurement sensors with different trackers, calibration tables, and other measurement and filtering aspects.
