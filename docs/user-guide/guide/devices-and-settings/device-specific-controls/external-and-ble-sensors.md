---
description: Bind Bluetooth and specialized device-side sensor channels so Navixy reads their data correctly. Pairs with the Sensors and buttons block.
---

# External and BLE sensors

## Purpose

Some devices expose a block for **binding external Bluetooth/BLE or specialized sensor channels** on the device side. These sensors typically transmit raw data — often just a MAC address and a value — so you map each channel here, and the platform then interprets it correctly. This block **pairs with** the platform-side [Sensors and buttons](../vehicle-sensors/) block: here you bind the device-side channel; there the resulting sensor feeds reports, widgets, and rules.

{% hint style="info" %}
This block and its fields are model-specific. Examples include generic Bluetooth sensor mapping (by MAC address), and vendor channel mapping such as **CalAmp accumulators**, **Mayak BT**, and **Topfly BLE** sensors. Your device shows only what its firmware supports.
{% endhint %}

<!-- SCREENSHOT: Bluetooth sensors block — MAC address field and sensor-type selector. Annotate: MAC address entry, sensor-type dropdown. -->

## How to configure Bluetooth sensors

{% stepper %}
{% step %}
**Access the Bluetooth sensors block**

Navigate to the Devices and Settings section. Select the specific device for which you want to configure Bluetooth sensors.
{% endstep %}

{% step %}
**Specify the MAC address**

Enter the unique MAC address of the Bluetooth sensor you wish to configure. This ensures the platform recognizes and associates the sensor with the correct device.
{% endstep %}

{% step %}
**Select the sensor type**

Choose the appropriate sensor type from the following options:

* **Temperature and humidity sensor**: For monitoring environmental conditions.
* **Tire pressure and temperature Sensor**: For tracking tire status in real-time.
* **Panic button**: For emergency alerts.
* **Identification key**: For access control and security.
* **Door sensor**: For monitoring door status (open/closed).
* **Relay**: For controlling electrical circuits.
{% endstep %}

{% step %}
**Save the configuration**

Once you’ve entered the MAC address and selected the sensor type, save the settings. The system will automatically create the corresponding sensors in the **Sensors and buttons** block, linking them to the appropriate functionalities within the platform.
{% endstep %}
{% endstepper %}

This process ensures that your Bluetooth sensors are correctly configured and their data is accurately interpreted by the Navixy platform.

## Appears when

Appears only on device models that support external Bluetooth/BLE or vendor-specific sensor channels.

## Gotchas

* Manufacturer/Bluetooth sensors often need configuration **on the device side** too; channel numbering can differ between the device's configurator and Navixy.
* Saving here automatically creates the corresponding sensors in the **Sensors and buttons** block.

## See also

* [Vehicle sensors](../vehicle-sensors/) — the platform-side sensors this block feeds.
* [Specialized sensors by manufacturer](../vehicle-sensors/specialized-sensors-by-manufacturer/) — manufacturer-specific sensor setup.
