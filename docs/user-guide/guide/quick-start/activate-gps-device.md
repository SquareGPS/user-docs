# Activate GPS device

{% hint style="info" %}
You can activate any [supported GPS tracking device](https://navixy.com/devices/). If your model is not yet supported, please contact your [service provider](about-service-providers.md) to either get this device integrated with Navixy or finding an alternative device with similar functionality. We also suggest reaching out to your [service provider](about-service-providers.md) before proceeding, as they may have their own recommendations.
{% endhint %}

In Navixy, activating a device simply means adding a new device to your user account. To do it, the platform offers two methods:

1. [Activate GPS device automatically (recommended)](activate-gps-device.md#activate-gps-device-automatically) — simplifies device setup by automatically configuring your device without any manual intervention. This method is recommended for most cases except when [manual activation is required or preferred](activate-gps-device.md#when-manual-activation-is-required-or-preferred).
2. [Activate GPS device manually](activate-gps-device.md#activate-gps-device-manually) — requires you to physically enter configuration settings into the device using its configurator, or more directly through SMS. This option is useful if the automatic configuration is not feasible due to specific technical or regional constraints.

{% include "../../.gitbook/includes/device-limit-hint.md" %}

## Activate GPS device automatically

Navixy offers the unique advantage of fully automatic device activation, which in most cases Navixy provides fully automatic device activation, eliminating the need for manual interaction with the device in most cases. No USB cables, drivers, or configuration utilities are required, allowing devices to become operational shortly after activation.

To initiate activation, you need to provide basic device data, such as the device IMEI and the SIM card ICCID. The platform sends initial configuration commands to the device via SMS, including APN and server connection details. Once connected, the device receives further configuration updates, such as tracking mode settings, primarily over the IP channel.

However, if the automatic activation [is not suitable in your case](activate-gps-device.md#when-manual-activation-is-required-or-preferred), you can always [configure the device manually](activate-gps-device.md#activate-gps-device-manually).

### Automatic activation steps

Once you log in to your user account, navigate to **Device activation** in the left sidebar. This will launch the activation wizard.

{% stepper %}
{% step %}
#### **Device manufacturer and model**&#x20;

Search and select from a list sorted alphabetically and grouped by manufacturers.

{% hint style="success" %}
When ready, click **Next** to proceed.
{% endhint %}
{% endstep %}

{% step %}
#### **Object name and group**

1. Choose a descriptive **Label**, (e.g., “Vehicle ABC”). It will become the main identifier in the Navixy platform.
2. Assign the object to a **Group** for clear categorization. **Main group** is selected by default.

{% hint style="success" %}
When ready, click **Next** to proceed.
{% endhint %}
{% endstep %}

{% step %}
#### Device connection parameters

Required connection parameters differ depending on the device involved. Those requirements are stored in Navixy and the platform adjusts field availability and value requirement dynamically for each device. You may not see some of the options described below for your particular device, follow the instructions inside the activation dialog for the exact guidance applicable to your case.

{% hint style="info" %}
If you have an activation code from your service provider, you can skip manual parameter entry by using that code instead.
{% endhint %}

1. Enter **Device ID**. The required format depends on your device type:
   1. Most GPS trackers and dashcams use IMEI, a 15-digit factory number printed on the device label or packaging.
   2.  Some devices require an ID from third-party applications or a manufacturer-specific identifier.<br>

       Contact your [service provider](about-service-providers.md) if you're unsure which ID format to use.&#x20;
2. Insert **Phone number**. Provide the SIM card number including the country code (e.g., +1234567890). This number is typically printed on the SIM card packaging.\
   The platform automatically detects appropriate APN settings based on the phone number. If automatic detection fails, you'll need to enter APN settings manually.
3. Configure **GPRS settings** (if required):
   1. **APN** - the network address the GPS device uses to connect to the mobile operator’s data network. It is provided by the SIM card operator and is usually listed in the SIM documentation, on the operator’s website, or by their support team.
   2. **Username** and **Password** - Access credentials required by some mobile operators. Leave these fields blank if your operator doesn't require them. Contact your SIM provider if you're unsure whether credentials are needed.
4. Use **Activation Code** (if provided by your service provider). Some service providers pre-configure devices and issue activation codes that replace manual parameter entry. If your provider gave you an activation code, enter it here.

The platform will attempt to determine the appropriate APN settings based on the phone number you provided. If the APN settings are not found, you will need to enter them manually.

{% hint style="success" %}
When ready, click **Next** to proceed.
{% endhint %}
{% endstep %}

{% step %}
#### Activation

After you entered all the necessary information you are ready for the activation.&#x20;

1. Review the instructions of the final step: they remind you that for the Automatic activation requires the device to be powered on and able to receive messages.
2. When ready, click **Activate**. SMS messages containing configuration commands will be sent to the device.

{% hint style="info" %}
If the SMS commands are not received by the device for any reason, you can again in a few minutes. If it doesn't help, you can [configure your device manually](activate-gps-device.md#activate-gps-device-manually): the connection parameters (**Server address** and **Port**) will be shown in this step's dialog. You can also find connection parameters for a specific device in our [catalog of supported devices](https://www.navixy.com/devices/).\
In case of further issues, contact your [Service provider](about-service-providers.md) for assistance.
{% endhint %}
{% endstep %}
{% endstepper %}

{% hint style="success" %}
Within about 15 minutes, the device should come online and be ready for use, depending on default device reporting settings.
{% endhint %}

## Activate GPS device manually

While Navixy offers [automatic GPS device activation](activate-gps-device.md#activate-gps-device-automatically) that simplifies the setup process, there are instances where manual configuration may be required or preferred. This section covers steps for manual device configuration and particular use cases when this method is preferred.

### Manual activation steps

To manually activate your device, you must either send the SMS activation commands manually, or physically connect to your devices' configurator with your PC. The information required for either option is as follows:

1. **APN credentials**: You may find this information from your SIM provider. Devices typically require: APN name and/or APN user, APN password if required.
2. **Server address**: Choose the server address based on your data residency preferences and/or your Service Provider recommendations:
   1. EU platform: `tracker.navixy.com` (recommended) or `52.57.1.136`
   2. US platform: `tracker.us.navixy.com` (recommended) or `13.52.37.2`
3. **Server port**: This parameter depends on your device make and model and can be found in the [Devices section](https://navixy.com/devices/) of our website. For example, for [Queclink GV65](https://www.navixy.com/devices/queclink/queclink-gv65/) device the server port would be `47764`.

Please update those fields within your device configurator to begin connecting to our platform.

For SMS activation, please either consult the device manual or the support team for the SMS commands used to activate your specific device.

{% hint style="info" %}
SMS activation highly depends on your SIM provider’s capability. In our experience, SMS commands from a typical phone are unable to reach a device. In such an event, you must utilize your SIM provider’s portal to send the messages.
{% endhint %}

### When manual activation is required or preferred

<details>

<summary>Cellular devices with SMS deliverability issues</summary>

Although Navixy and its partners utilize SMS gateways with high deliverability and worldwide coverage, some countries have local regulations and technical issues that can hinder the delivery of M2M commands sent via SMS text messages. These issues include:

* **Anti-spam regulations**: Local restrictions on message sender names, text length, and binary texts.
* **Technical issues**: Special symbols like $, #, and % that are used in the configuration commands may not pass through all network nodes in the SMS delivery chain successfully.

If automatic setup fails due to these issues, you can manually configure the basic parameters, such as APN credentials, server address, and port. The server port and IP address for a specific device model can be found in the Devices section of our website. For detailed configuration instructions, please refer to the device's manual or consult the technical support of your [service provider](about-service-providers.md).

</details>

<details>

<summary>Devices connected via MQTT protocol</summary>

MQTT devices, which use the Publisher/Subscriber model for communication, require a unique setup process. These devices must be configured manually because they do not follow the traditional client-server model. You need to:

1. Configure the device with the appropriate MQTT broker settings.
2. Manually set up the device’s connection parameters, such as the MQTT broker address and port.
3. Ensure the correct topics and security credentials are configured.

Please refer to the [Activate Your MQTT Device on Navixy](https://app.gitbook.com/s/IgDb43gtyXcm1Av4h1np/faq-and-troubleshooting/gps-devices/add-and-manage-devices/activate-your-mqtt-device-on-navixy) section of our [Expert Center](https://app.gitbook.com/o/YVLWhgAwCZPoU5vlRsCs/s/IgDb43gtyXcm1Av4h1np/) for more details.

</details>

<details>

<summary>Devices connected via LoRa network</summary>

LoRa (Long Range) networks, which are commonly used for IoT applications due to their low power and long-range capabilities, also require manual configuration. This is because LoRa networks operate differently from standard cellular networks using LoRaWAN gateways and have specific requirements:

* Manually enter the device’s LoRaWAN credentials
* Set up the server address and network parameters to match the LoRa network specifications

This setup is somewhat unique for each integration. Therefore please consult with the technical support of your [service provider](about-service-providers.md) on how to integrate your LoRa devices and LoRaWAN gateway with Navixy.

</details>

<details>

<summary>Devices connected via Satellite network</summary>

Devices using satellite networks such as Iridium, Globalstar or Starlink need manual configuration due to the distinct nature of satellite communication, which differs significantly from terrestrial networks.

Devices that use a satellite link and the Navixy platform communicate through a gateway provided by the satellite operator. This gateway acts as a bridge between the satellite network and the Internet, ensuring seamless data transmission.

To configure a satellite device to be monitoring on Navixy, you need to:

1. Point your device to the satellite network
2. On the satellite network side, have their system point their data to the Navixy platform
3. Verify that the device is properly registered and able to communicate with the satellite network.

Because each integration can be unique, please consult the technical support of your [service provider](about-service-providers.md) for guidance on integrating your devices and gateway with Navixy.

</details>

<details>

<summary>Devices connected via other Telematics systems or Gateways</summary>



</details>

There are scenarios where devices are already connected to other telematics systems, such as OEM telematics platforms or other GPS servers, and you need them to be monitored on both that platform and Navixy.

To monitor devices that are part of other telematics systems with Navixy, you need to:

* Configure data transmission:\
  Set up the other platform to send data to Navixy using one of the protocols supported by Navixy.
* Add a virtual device:\
  Create a virtual device on the Navixy platform that maps to the data source using a unique device identifier.

For more details, please read how to [Integrate IoT Data from Servers and Gateways](https://app.gitbook.com/s/IgDb43gtyXcm1Av4h1np/faq-and-troubleshooting/gps-devices/add-and-manage-devices/integrate-iot-data-from-servers-and-gateways).

## FAQ and Troubleshooting

If you encounter any issues while activating your devices, please consult our [F.A.Q. and Troubleshooting Guide](../faq/gps-device-activation-troubleshooting.md) or contact your [Service provider](about-service-providers.md) for assistance.
