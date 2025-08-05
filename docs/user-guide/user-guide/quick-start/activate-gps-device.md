# Activate GPS device

Activating a device simply means adding a new device to your user account. You can activate any [supported GPS tracking device](https://navixy.com/devices/). If your model is not yet supported, please contact your [service provider](service-provider.md) to either get this device integrated with Navixy or finding an alternative device with similar functionality. We also suggest reaching out to your [service provider](service-provider.md) before proceeding, as they may have their own recommendations.

There are two methods of activating a GPS tracking device:

1. [Activate GPS device automatically (recommended)](#Activate-GPS-device-automatically) — simplifies device setup by automatically configuring your device without any manual intervention. This method is recommended for most cases except when [manual activation is required or preferred](#Activate-GPS-device-manually).
2. [Activate GPS device manually](#Activate-GPS-device-manually) — requires you to physically enter configuration settings into the device using its configurator, or more direct with SMS. This option is useful if the automatic configuration is not feasible due to specific technical or regional constraints.

## Activate GPS device automatically

Navixy offers the unique advantage of fully automatic device activation, which in most cases frees users from the need to manually configure their devices. The process includes sending initial configuration commands to a device you are connecting via text message (SMS). However, if the automatic activation is not suitable in your case, you can always [configure the device manually](#Activate-GPS-device-manually).

### Automatic activation steps

Once you log in to your user account, navigate to Device activation in the left menu. This will launch the activation wizard.

1. **Object name:** Choose any name you prefer (e.g., “Vehicle ABC”).
2. **Device model and manufacturer:** Search and select from a list sorted alphabetically and grouped by manufacturers.
3. **Enter SIM card phone number:** Enter the phone number of the SIM card installed in the device.
  1. The Navixy platform will attempt to determine the appropriate APN settings based on the phone number you provided. If the APN settings are not found, you will need to enter them manually.
4. **Enter device factory ID/IMEI:**
  1. The length of this value can change depending on model. If you have questions, please work with your [service provider](service-provider.md).
5. **Activation Code (optional):**
  1. If enforced by your service provider, they may have to provide you with an activation code before you are able to register a device.
6. **Activate:** After entering the necessary information, click “Next Step”. Then, SMS messages containing configuration commands will be sent to the device. Please ensure the device is powered on and able to receive these messages.

Within about 15 minutes, the device should come online and be ready for use, depending on default device reporting settings.

![](https://squaregps.atlassian.net/wiki/images/icons/grey_arrow_down.png)

Details about automatic configuration

With automatic activation, setting up your device is simple and user-friendly, with no need for USB cables, drivers, or configuration utilities. The process is quick, allowing the device to be operational within minutes. Configuration parameters, such as APN settings and server details, are sent automatically via SMS from the server to the device. Once connected, the device receives automatic updates, such as tracking mode settings, primarily over the IP channel.

## Activate GPS device manually

While Navixy offers [automatic GPS device activation](#Activate-GPS-device-automatically) that simplifies the setup process, there are instances where manual configuration may be required or preferred. This section covers steps for manual device configuration and particular use cases when this method is preferred.

### Manual activation steps

To manually activate your device, you must either send the SMS activation commands manually, or physically connect to your devices' configurator with your PC. The information required for either option is as follows:

1. **APN credentials** — You may find this information from your SIM provider. Devices typically require: APN name and/or APN user, APN password if required.
2. **Server address** — Choose the server address based on your data residency preferences and/or your Service Provider recommendations:
  - EU platform: `tracker.navixy.com` (recommended) or `52.57.1.136`
  - US platform: `tracker.us.navixy.com` (recommended) or `13.52.37.2`
3. **Server port** — This parameter depends on your device make and model and can be found in the [Devices section](https://navixy.com/devices/) of our website. For example, for [Queclink GV65](https://www.navixy.com/devices/queclink/queclink-gv65/) device the server port would be 47764.

Please update those fields within your device configurator to begin connecting to our platform.

For SMS activation, please either consult the device manual or the support team for the SMS commands used to activate your specific device.

> [!INFO]
> Note: SMS activation highly depends on your SIM provider’s capability. In our experience, SMS commands from a typical phone are unable to reach a device. In such an event, you must utilize your SIM provider’s portal to send the messages.

### When manual activation is required or preferred

![](https://squaregps.atlassian.net/wiki/images/icons/grey_arrow_down.png)

Cellular devices with SMS deliverability issues

Although Navixy and its partners utilize SMS gateways with high deliverability and worldwide coverage, some countries have local regulations and technical issues that can hinder the delivery of M2M commands sent via SMS text messages. These issues include:

- **Anti-spam regulations**: Local restrictions on message sender names, text length, and binary texts.
- **Technical issues**: Special symbols like $, #, and % that are used in the configuration commands may not pass through all network nodes in the SMS delivery chain successfully.

If automatic setup fails due to these issues, you can manually configure the basic parameters, such as APN credentials, server address, and port. The server port and IP address for a specific device model can be found in the Devices section of our website. For detailed configuration instructions, please refer to the device's manual or consult the technical support of your [service provider](service-provider.md).

![](https://squaregps.atlassian.net/wiki/images/icons/grey_arrow_down.png)

Devices connected via MQTT protocol

MQTT devices, which use the Publisher/Subscriber model for communication, require a unique setup process. These devices must be configured manually because they do not follow the traditional client-server model. You need to:

1. Configure the device with the appropriate MQTT broker settings.
2. Manually set up the device’s connection parameters, such as the MQTT broker address and port.
3. Ensure the correct topics and security credentials are configured.

Please refer to the[Activate Your MQTT Device on Navixy](https://squaregps.atlassian.net/wiki/spaces/SC/pages/2732589133/Activate+Your+MQTT+Device+on+Navixy) section of our [Expert Center](https://squaregps.atlassian.net/wiki/spaces/SC) for more details.

![](https://squaregps.atlassian.net/wiki/images/icons/grey_arrow_down.png)

Devices connected via LoRa network

LoRa (Long Range) networks, which are commonly used for IoT applications due to their low power and long-range capabilities, also require manual configuration. This is because LoRa networks operate differently from standard cellular networks using LoRaWAN gateways and have specific requirements:

- Manually enter the device’s LoRaWAN credentials
- Set up the server address and network parameters to match the LoRa network specifications

This setup is somewhat unique for each integration. Therefore please consult with the technical support of your [service provider](service-provider.md) on how to integrate your LoRa devices and LoRaWAN gateway with Navixy.

![](https://squaregps.atlassian.net/wiki/images/icons/grey_arrow_down.png)

Devices connected via Satellite network

Devices using satellite networks such as Iridium, Globalstar or Starlink need manual configuration due to the distinct nature of satellite communication, which differs significantly from terrestrial networks.

Devices that use a satellite link and the Navixy platform communicate through a gateway provided by the satellite operator. This gateway acts as a bridge between the satellite network and the Internet, ensuring seamless data transmission.

To configure a satellite device to be monitoring on Navixy, you need to:

1. Point your device to the satellite network
2. On the satellite network side, have their system point their data to the Navixy platform
3. Verify that the device is properly registered and able to communicate with the satellite network.

Because each integration can be unique, please consult the technical support of your [service provider](service-provider.md) for guidance on integrating your devices and gateway with Navixy.

![](https://squaregps.atlassian.net/wiki/images/icons/grey_arrow_down.png)

Devices connected via other Telematics systems or Gateways

There are scenarios where devices are already connected to other telematics systems, such as OEM telematics platforms or other GPS servers, and you need them to be monitored on both that platform and Navixy.

To monitor devices that are part of other telematics systems with Navixy, you need to:

- Configure data transmission:  
Set up the other platform to send data to Navixy using one of the protocols supported by Navixy.
- Add a virtual device:  
Create a virtual device on the Navixy platform that maps to the data source using a unique device identifier.

For more details, please read how to [Integrate IoT Data from Servers and Gateways](https://squaregps.atlassian.net/wiki/spaces/SC/pages/2732621933/Integrate+IoT+Data+from+Servers+and+Gateways).

## FAQ and Troubleshooting

If you encounter any issues while activating your devices, please consult our [F.A.Q. and Troubleshooting Guide](../faq/gps-device-activation-troubleshooting.md) or contact your [Service provider](service-provider.md) for assistance.