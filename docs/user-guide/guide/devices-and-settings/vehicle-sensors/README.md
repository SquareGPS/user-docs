---
description: "Add and configure sensors in Navixy: discrete, measurement, virtual, and manufacturer-specific. Monitor fuel, temperature, engine diagnostics, and more."
---

# Vehicle sensors

The **Sensors and buttons** block in Navixy allows you to manage and configure various sensors connected to your GPS devices from the platform standpoint. This feature is essential for monitoring various vehicle parameters, such as fuel levels, temperature, and engine diagnostics, directly through the platform.

## Overview

The **Sensors and buttons** block is located in the **Devices and settings** module, which you can access by clicking the corresponding item in the main menu.

The block provides an overview of the number of sensors already connected to the selected device. Expanding the panel lets you add new sensors or edit existing ones.

![](../../../.gitbook/assets/image-20240815-205217.png)

The number and type of sensors you can connect depend on the GPS device model. For example, certain devices allow you to configure data parameters transmitted via the CAN bus or OBDII diagnostic connector.

## Appears when

The **Sensors and buttons** block appears when the device model has inputs (digital, analog, or RS232).

## Adding and editing sensors

To manage your sensors, you can use the following buttons:

* **Add**: Allows you to add a new sensor
* **Edit**: Lets you modify the parameters of an existing sensor
* **Delete**: Removes the selected sensor from the system

### Sensor types

<table data-view="cards"><thead><tr><th>Type</th><th data-card-target data-type="content-ref">Link</th></tr></thead><tbody><tr><td><strong>Discrete sensors</strong></td><td><a href="discrete-sensors/">discrete-sensors</a></td></tr><tr><td><strong>Measurement sensors</strong></td><td><a href="measurement-sensors/">measurement-sensors</a></td></tr><tr><td><strong>Aggregation sensors</strong></td><td><a href="aggregation-sensors.md">aggregation-sensors.md</a></td></tr><tr><td><strong>Virtual sensors</strong></td><td><a href="virtual-sensors/">virtual-sensors</a></td></tr><tr><td><strong>Specialized sensors by manufacturer</strong></td><td><a href="specialized-sensors-by-manufacturer/">specialized-sensors-by-manufacturer</a></td></tr></tbody></table>

### Copying sensor settings

To streamline configuration, you can copy sensor settings from one device to another, provided the devices are of the same model. This is particularly useful when managing large fleets with similar vehicle types.

**Steps to copy sensor settings:**

1. Click the copy button (📋).
2. Select the devices to which you want to apply the copied settings.
3. Click **Apply**.

{% hint style="danger" %}
Copying sensor settings will overwrite the current settings on the selected devices. Ensure that you only select the devices you intend to update.
{% endhint %}
