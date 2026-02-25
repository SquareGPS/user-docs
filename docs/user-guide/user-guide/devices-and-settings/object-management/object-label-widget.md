# Object label widget

The **Object label** widget allows you to manage key identification details of your device. This widget contains the following fields:

* **Object label:** This is where you assign a name to the device. The name can be anything that helps you identify the device easily, such as the vehicle's make and model, the owner's name, or any other descriptor that suits your needs.
* **Group:** This field lets you assign the device to a specific group. Grouping devices can be useful for organizing your fleet by department, function, or location.
* **Tags:** Tags provide an additional way to categorize and search for devices within the platform, making it easier to manage large fleets with specific tagging criteria.
* **Model:** The model of the device currently in use, shown at the top right corner along with the device’s IMEI or ID number.

After making any changes, click **Save** to apply them.

## Device replacement functionality

You can easily replace a GPS tracker connected to the platform. Whether it’s time for an upgrade or the device is malfunctioning, the replacement mechanism ensures a smooth transition by preserving the original device’s configuration, settings, and historical data. Accessible through the **Devices and settings** interface section, this intuitive and responsive process minimizes downtime and maximizes convenience, keeping your operations running continuously.

{% hint style="warning" %}
Some devices, such as smartphones used as trackers through the **X-GPS Tracker** application, are not supported by the replacement mechanism and do not have the **Replace Device** button available for them.

In addition, historical data becomes available only after the new device has been successfully activated.
{% endhint %}

### How to replace a device

{% stepper %}
{% step %}
**Select the device**

Navigate to the **Devices and settings** section and select the required device from the object list by clicking on it.
{% endstep %}

{% step %}
**Initiate the replacement**

Click **Replace device** on the device information pane.

<figure><img src="attachments/image-20241213-115932.png" alt=""><figcaption></figcaption></figure>
{% endstep %}

{% step %}
**Review sensor instructions**

1. Confirm that the new hardware supports the original device's settings.
2. If additional sensors were connected to the original device, ensure they are reconnected to identical inputs on the new device to preserve historical data.
3. Carefully read and follow any further on-screen instructions regarding the device’s sensors before proceeding. Follow any specific guidelines provided, then click **Next step**.
{% endstep %}

{% step %}
**Connect a replacement device**

Follow the same steps as for connecting a new device to the platform, except for the object name. It inherits the name of the original device and cannot be changed.

1. **Select the new device model:** Choose the new device model from the list provided and click **Next step**.
2. **Enter device details:** Specify the phone number, APN settings, and device ID (IMEI) for the new device.
3. **Complete the replacement:** Click **Replace** to finalize the process. The platform will send activation commands to the new device and monitor its activation status.
{% endstep %}
{% endstepper %}

{% hint style="warning" %}
Note that once the **Replace** button is pressed, the replacement process cannot be canceled.
{% endhint %}

These steps ensure that the replacement device is properly configured and ready to take over from the previous one, minimizing downtime and maintaining fleet operations smoothly.

### **Handling activation issues**

If the device fails to activate, you can repeat the replacement process with the same device or try a different one. If the issue persists, you may manually configure the device according to its instructions.
