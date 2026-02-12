# Troubleshooting trip history issues

### Question

How can I troubleshoot trip history issues? What should I do if a device’s trip history is intermittent?

### Answer

If you find that part of a device’s trip history (or the entire trip) is missing on the platform, try displaying the trip without any processing or filters. To do this, uncheck the “Smart Filter” and “Split by Stops” options in the trip history settings:

![](<../.gitbook/assets/Unknown image (126)>)

If the issue still persists, most likely the device didn’t send necessary GPS points to the platform. To confirm this fact, the user can export data using the Raw Data feature. Once exported, find the time interval when the trip has gaps.

![image-20251224-110231.png](<../.gitbook/assets/Unknown image (127)>)

In the example above, points are missing for **one hour on December 10, 2025**, from **04:11:57 to 05:13:20**. This confirms that the tracker did not transmit any data to the platform during the reviewed time interval.

Additionally, there are cases where trip history is repeatedly interrupted, resulting in small gaps between detected trips. In such cases, most likely the user needs to adjust tracker data acquisition settings within the tracker configuration.

Try starting from adjusting the Tracking Mode settings in the user cabinet (if such a portlet is available for the given tracker in the Devices and Settings menu):

<figure><img src="../.gitbook/assets/image (6).png" alt="" width="287"><figcaption></figcaption></figure>

Set up the On Moving and On Idle parameters to make the tracker record and send data more frequently. In case you use Teltonika, you can adjust more parameters directly in the device configuration:

![](<../.gitbook/assets/Unknown image (129)>)

Here is an example above of how such settings may look. You can try to apply the same configuration as specified in the screenshot above.

Most likely, the issue with trip history gaps will not repeat after adjusting the tracker configuration.

Please note that configuring a tracker to record and send points more frequently introduces higher SIM-card traffic consumption.

### Links

* [Raw Data](https://www.navixy.com/docs/expert-center/faq-and-troubleshooting/access-iot-data/save-iot-data-to-csv-file)
