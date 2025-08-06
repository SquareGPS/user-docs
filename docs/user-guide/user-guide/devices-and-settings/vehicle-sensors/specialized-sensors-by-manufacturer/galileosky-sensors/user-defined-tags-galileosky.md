# User-defined tags (Galileosky)

Galileosky devices, known for their versatility and advanced capabilities, particularly stand out due to their support for user-defined tags. Most GPS devices transmit a predefined set of data, including essential information such as coordinates, altitude, acceleration, mileage, and vehicle-specific details like ignition status and coolant temperature. However, this data is often limited to what the manufacturer supports, restricting the monitoring of additional parameters.

With [Galileosky devices](https://www.navixy.com/devices/galileosky/), particularly those supporting Easy Logic, users can overcome these limitations by defining custom tags, allowing for the transmission of a broader range of data. This flexibility enables users to monitor additional parameters that are not typically supported by standard GPS devices.

[![Data transfer in Galileosky user tags](https://www.navixy.com/wp-content/uploads/2019/09/configurator_2019-09-28_13-28-39-600x370.png)

](https://www.navixy.com/wp-content/uploads/2019/09/configurator_2019-09-28_13-28-39.png)[![Data transfer in Galileosky user tags](https://www.navixy.com/wp-content/uploads/2019/09/chrome_2019-09-28_13-40-07-600x296.png)

](https://www.navixy.com/wp-content/uploads/2019/09/chrome_2019-09-28_13-40-07.png)

## Benefits of user-defined tags with Galileosky devices

1. **Custom data transmission**: Users can define specific parameters to be monitored and transmitted, expanding the scope beyond the predefined data set.
2. **Enhanced data analysis**: By using Easy Logic, users can perform arithmetic operations on the data before it's sent to the server. This includes summing, averaging, or converting sensor data into more meaningful insights.
3. **Conditional data reporting**: Logical operations can be applied to ensure that data is only transmitted when specific conditions are met, optimizing data usage and relevance.
4. **Event counting and reporting**: Galileosky devices can count specific events and report them in real-time, providing critical insights for fleet management or telematics applications.
5. **Automated actions**: The devices can be programmed to perform specific actions, such as switching outputs or triggering alerts, based on the predefined conditions, which are then reported to the server.

### Practical applications

With Galileosky devices and Easy Logic, you can:

- **Arithmetic operations**: You can manipulate sensor data before it’s transmitted to the server. This includes summing, averaging, or converting sensor readings into formats that better suit your analysis needs.
- **Logical operations**: Transmit data only when specific conditions are met, ensuring that the data collected is relevant and efficiently used. This can help in optimizing data transmission and reducing unnecessary data load.
- **Event counting**: Easily track and count specific events based on predefined criteria. This feature is particularly useful for monitoring repetitive or cyclical processes.
- **Automated actions**: Set up actions, such as switching outputs, based on certain conditions and have these actions reported to the server. This functionality is ideal for automating responses to real-time data inputs.

## How to configure Galileo’s user-defined tags with Navixy

### Configure Galileosky devices

1. **Install the Galileosky configurator**: Begin by downloading and installing the Galileosky Configurator software.
2. **Setup in Easy Logic**: Use Easy Logic to define the necessary conditions and operations for your custom tags. This process involves scripting within the Easy Logic environment to set up the data you wish to monitor and transmit.

### Configure sensors in Navixy

1. Navigate to the *Devices and Settings* section in the Navixy platform.
2. Go to *Sensors and Buttons* and create a new measurement sensor.
3. Select the appropriate input (User Tag), sensor type, and units.
4. Note that in the Galileosky Configurator, user tags are numbered from 0 to 7, while in Navixy, they are numbered from 1 to 8. Therefore, tag 0 in the Configurator corresponds to input 1 in Navixy, and so on.

As with any other sensor, you can apply additional settings, such as calibration, multipliers, or thresholds, to refine the data output.

Once configured, these user-defined tags allow for enhanced monitoring and reporting capabilities, providing users with the ability to capture and analyze data that goes beyond standard GPS device limitations.

4. **Configure the Sensor in Navixy**

- **Action**:
- Create a new measurement sensor.
- Select the appropriate input (User tag), sensor type, and measurement units.
- Be mindful of the numbering difference: user tags in the Galileosky Configurator are numbered from 0 to 7, while in Navixy, they are numbered from 1 to 8. Thus, tag 0 in Galileosky corresponds to input 1 in Navixy, and so forth.
- **Purpose**: Correct configuration ensures that the data processed by Galileosky’s Easy Logic is correctly interpreted and displayed on the Navixy platform.

5. **Apply Additional Sensor Settings**

- **Action**: Enhance your sensor’s functionality by setting up a calibration table, applying multipliers to adjust values, or establishing thresholds to filter out outliers.
- **Purpose**: These additional settings help in refining the data to ensure it is as accurate and useful as possible.

6. **Monitoring and Reporting in Navixy**

- **Action**: Use the Sensor Readings widget in Navixy to monitor the data in real-time. Additionally, you can generate detailed reports based on the sensor data, providing comprehensive insights into your operations.
- **Purpose**: This integration enables continuous monitoring and in-depth analysis of the customized data collected by your Galileosky devices.