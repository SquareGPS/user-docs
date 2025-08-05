# Object widget

In Navixy, **Object widget** serves as a comprehensive collection of telematics data blocks for monitoring and managing your fleet. It provides an in-depth look at your business assets, GPS devices, and the sensors connected to them.

> \[!NOTE] **Navigation**
>
> * By default, to access the detailed view of a specific object, either click the object’s icon on the map or hover your mouse over it and click the appearing ![Info\_Icon.png](../../objects-list/attachments/30a5254e-69b1-4b7a-ae95-fe62476c8574) button.
> * If the **Show info by click** option is enabled in the [Additional settings](https://squaregps.atlassian.net/wiki/spaces/USERDOCSOLD/pages/edit-v2/2909015397#Additional-settings), clicking on an object also opens the **Object widget**.

Once opened, the panel displays extensive information about the selected object, including current status, GPS location, and further telematics data. All operational management tools are conveniently located in one place, allowing for efficient fleet management and quick response to any arising issues.

![Object\_widget\_big.png](../../objects-list/attachments/Object_widget_big.png)

## Structure

The top section of the widget panel contains essential details about the object, including its name, movement status, and connection status. It also includes the following options:

* **Customization options**\
  The widget layout provides robust customization capabilities to help you organize information according to your needs:
  * **Data blocks**: Click ![Cogwheel](../../objects-list/attachments/image-20250331-110457.png) to open widget settings and select which data blocks you want to display. By default, all blocks available to the objects are selected. This menu also enables the display of the update time below each sensor.
  * **Layout management**: Click ![Lock](../../objects-list/attachments/image-20250402-082022.png) to switch into layout management mode. When it’s enabled, you can drag data blocks to your preferred positions. In this mode, you can also change the order of information inside the blocks manually in the same drag-and-drop manner.
* **Street view access**\
  Clicking the widget enables **Street view**, displaying the real-world imagery of the object’s position on the map for improved context and navigation.
* **Video monitoring**\
  The ![Video](../../objects-list/attachments/video-camera-20250522-083504.png) button, available only for GPS devices with this functionality, opens the **Video monitoring** window. Here, you can watch a live stream from your camera or review past recordings stored in the device’s memory or the cloud. To learn more about this feature, see [Video monitoring](object-widget.md#video-monitoring).
* **Apply pins to all vehicles**\
  The ![Apply pins to all vehicles](../../objects-list/attachments/image-20250402-082231.png) button allows you to instantly mark all data blocks as **Favorites**, ensuring their information is shown under the object’s name in the **Objects list**. For details on this feature, see [Favorites](object-widget.md#favorites).

## Data blocks

The **Object widget** organizes crucial information through specialized data blocks. Each component serves a specific purpose in providing comprehensive monitoring and management capabilities.

> \[!INFO] The blocks' availability and content depend on the GPS device assigned to the selected object. They display only the information transmitted by the device or sensors connected to it. You can also customize their appearance. For details, see [Customization options](object-widget.md#customization) above.

Here's a detailed overview of the available blocks:

| **Block**              | **Description**                                                                                                                                                                                                                                                                         |
| ---------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Location**           | Delivers precise positioning data, including the latest known location with either a street address or GPS coordinates, accompanied by timestamps. The widget also tracks current speed and altitude measurements.                                                                      |
| **GPS device**         | Provides basic information about the GPS device, including its connection status, GPS/GSM signal level, and subscription plan.                                                                                                                                                          |
| **Status**             | Provides movement status, speed, and direction.                                                                                                                                                                                                                                         |
| **OBD2 & CAN**         | Connects to the vehicle's onboard systems to provide real-time diagnostic data, such as fuel level, engine speed, coolant temperature, and any diagnostic trouble codes when the GPS device is properly connected to the vehicle's CAN bus or OBD2 port.                                |
| **Sensor readings**    | Monitors and displays data from all configured device sensors, providing recent readings with timestamps. Separate sensors can be marked as **Favorites** for quick access to critical measurements.                                                                                    |
| **Odometer**           | <p>Tracks the device's total mileage. This data can be adjusted manually via the <img src="../../objects-list/attachments/image-20250414-102340.png" alt="Edit"><br><br>button, ensuring accurate distance records.</p>                                                                 |
| **Engine hours**       | <p>Monitors the total running time of the engine. This data can be adjusted manually via the <img src="../../objects-list/attachments/image-20250414-102340.png" alt="Edit"><br><br>button for accurate usage tracking.</p>                                                             |
| **Inputs**             | Monitors the current state of various connected sensors, including the ignition status and other vehicle sensors such as door sensors, providing real-time feedback on vehicle status.                                                                                                  |
| **Outputs**            | Enables active control over devices connected to the GPS device, including features such as remote vehicle immobilization, allowing for direct intervention when necessary.                                                                                                             |
| **Driver**             | Displays the vehicle’s driver and allows you to assign them directly through the widget. Also displays their phone number, key, and the time the driver was assigned.                                                                                                                   |
| **Working statuses**   | Manages operational states by displaying and enabling changes to the object's current status, helping track its working history.                                                                                                                                                        |
| **Recent events**      | <p>Tracks and displays alerts related to the object. By default, you can see three recent events with an option to view all of them. Click <img src="../../objects-list/attachments/470bd6c2-70c4-4cef-b124-494171f98f34" alt="View"><br><br>next to the event to open its details.</p> |
| **Electronic padlock** | Provides security management for devices equipped with smart lock features, enabling remote control over the lock state, including both locking and unlocking capabilities.                                                                                                             |

## Favorites

The **Object list** can display not only the objects' names and connection status but also specific telematics data from GPS devices and connected sensors. To achieve that, you need to mark the data blocks as **Favorites** by following these steps:

1. Hover the cursor over the desired data block inside the **Object widget**.
2. Click the appearing ![image-20250129-163848.png](../../objects-list/attachments/image-20250129-163848.png) button to mark it as **Favorite**.

Once marked as **Favorite**, the selected data entry will appear under the corresponding object in the **Object list**, ensuring quick and easy access. To remove a block from the list display, click ![image-20250129-163848.png](../../objects-list/attachments/image-20250129-163848.png)

again.

## Video monitoring

The **Video monitoring** window provides real-time and historical video access for GPS devices with camera support. This feature enables visual monitoring capabilities through a dedicated interface accessible from the **Object widget**. The system supports both live streaming and recorded video playback from multiple camera sources.

### Live stream monitoring

The live stream functionality delivers real-time video feeds from installed dash cams or MDVR devices directly to your monitoring interface.

To use the live stream feature, follow these steps:

1. Click ![image-20250522-120053.png](../../objects-list/attachments/image-20250522-120053.png) to initiate the live stream.
2. Use the player controls to navigate through the recent footage.
3. Select the **Live** button to return to real-time viewing.

> \[!WARNING] Video streaming consumes significant data traffic. To conserve bandwidth, the platform automatically stops the stream when you close the video window or navigate to another module. For most browsers, closing the tab will also stop the stream, though some browser extensions may interfere with this function.

### Video playback

The playback functionality enables review of historical video footage stored either on the device or in the cloud platform. This capability supports event analysis, driver behavior monitoring, and incident investigation.

To use the playback feature, follow these steps:

1. Open the date selection menu to choose the date for the video you want to watch.
2. Depending on your history, the following icons will be displayed under the date:

* **Gray dot**: Information is stored in the device's memory. Viewing it requires uploading it from the device to the cloud. This is done while you’re playing the video.
* **Blue dot**: Content already available in cloud storage.
* **No dot**: No video content available for selected date

3. Select your desired date to access the hourly timeline.
4. Choose specific time segments from the fragment line for playback

> \[!WARNING] Consider data usage implications when downloading multiple fragments
