# Bluetooth sensors widget

Some devices have a special **Bluetooth sensors widget** in Navixy, which allows you to configure external Bluetooth sensors that are connected to certain tracker models. These sensors typically transmit raw data, including only the MAC address and sensor value.

To ensure the platform correctly interprets this data, you must manually configure each sensor within this widget.

#### How to configure Bluetooth sensors

{% stepper %}
{% step %}
**Access the Bluetooth sensors widget**

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

Once you’ve entered the MAC address and selected the sensor type, save the settings. The system will automatically create the corresponding sensors in the Sensors and Buttons widget, linking them to the appropriate functionalities within the platform.
{% endstep %}
{% endstepper %}

\
This process ensures that your Bluetooth sensors are correctly configured and their data is accurately interpreted by the Navixy platform, enhancing the functionality and reliability of your fleet management and asset tracking operations.
