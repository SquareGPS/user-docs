# Fuel level sensor

Fuel sensors are essential for monitoring fuel levels in vehicles and tanks, providing key data for tracking consumption, detecting refueling and draining, and optimizing fuel management. Using this data effectively helps prevent fuel losses, identify vehicles with high consumption, and improve overall efficiency, leading to significant cost savings.

### Understanding fuel sensor readings

The accuracy of fuel data depends on several key factors:

1. **Fuel level sensor type**: The precision of the sensor and its compatibility with the GPS device.
2. **Sensor installation**: Proper installation is crucial, especially for non-standard tanks. Manufacturer guidelines should be followed for optimal performance.
3. **Device-side settings**: Ensure the sensor is configured correctly and transmitting data to the platform. It's preferable to handle calibrations directly on the platform rather than the device.
4. **Platform settings**: Accurate settings on the platform are essential not only for data displayed in widgets but also for the functionality of draining/refueling alerts and fuel level reports.

### Setting up a fuel sensor

Fuel sensors are categorized as "[Measurement sensors](./)" on the Navixy platform. To add a fuel sensor:

1. **Navigate to Devices and settings -> Sensors and buttons**.
2. Click the **+** icon and select **Measurement sensor**.
3. Configure the sensor:

* **Sensor name**: Assign a clear name for easy identification.
* **Input**: Select the input channel from which fuel data will be transmitted.
* **Units**: Choose the appropriate unit of measure (e.g., liters).
* **Accuracy**: Define the accuracy percentage, which will be used to calculate the absolute error in fuel volume.
* **Thresholds for drain detection**: Set thresholds to detect fuel drains based on the rate of change over time or mileage.

#### Advanced fuel sensor settings

* **Ignore in movement**: Automatically exclude any drains or refills that occur while the vehicle is moving. This is determined by the "Parking Detection" setting.
* **Filter timeout**: Adjust the timeout period to filter out unstable readings during vehicle movement or immediately after refueling. This setting is especially useful for vehicles with large tanks.
* **Calibration table**: Convert sensor readings into usable units, such as liters. Accurate calibration is essential for reliable data.
* **Advanced filters**: Set filters to ignore readings below or above certain thresholds, and apply multipliers to adjust the sensor data as needed.

#### Fuel data processing on the platform

The Navixy platform reads and stores fuel sensor data as it is received. Sensor settings, including filters and calibration, are applied when the data is output. This means you can adjust settings at any time and regenerate reports to reflect the updated configurations.

#### Detecting and reporting fuel events

* **Drains and refills**: The platform uses a combination of calibration tables and accuracy levels to identify and log fuel drain and refill events.
* **Reporting**: Fuel reports analyze the rate of fuel level changes and apply set thresholds to identify significant events. Consecutive similar events are grouped into a single report entry.

#### Ignoring fuel events during movement

When the option to ignore refuels or drains during movement is enabled, the platform uses a specialized algorithm to filter out these events. If refueling begins or ends within the specified filter timeout before or after a trip, the event is logged. Otherwise, it is filtered out.

#### Analyzing fuel sensor data quality

Navixy employs advanced statistical methods to assess the quality of fuel sensor data. A quality score is assigned on a 10-point scale, with 1 being the lowest quality and 10 the highest. This rating is available in fuel volume reports, both within the interface and in downloaded documents (PDF/XLS). The score can also be retrieved via API requests.

## Fuel level sensor

Fuel sensors are a vital component for tracking the fuel levels of various vehicles and static tanks. With the help of platform algorithms, fuel consumption levels, refueling and discharges can be monitored through the data collected by these sensors. Efficient utilization of this data can lead to significant cost savings by preventing fuel losses and identifying vehicles with excessive fuel consumption, whose profits fail to meet expectations. By leveraging the insights provided by fuel sensors, you can stay ahead of any potential issues and optimize your fuel consumption, thereby boosting overall profitability.

Fuel level sensors come in various types and each serves a particular purpose. You can find detailed information about them in our [Expert Center](https://app.gitbook.com/s/IgDb43gtyXcm1Av4h1np/vehicle-telematics-technology/fuel-management). For the purpose of this article, we will be focusing on the fuel operation of the platform. Additionally, we will be discussing the fuel sensor settings and the impact that they have on the overall fuel management process.

### What the fuel sensor readings depend on

The accuracy of fuel data displayed is dependent on several factors including:

* The fuel level sensor - what kind and how well it is able to read from the tank, and how well it interacts with the GPS tracker.
* Tank sensor installation - if you have a non-standard tank or require a non-standard installation, it is best to consult with the manufacturer on how to install such a sensor.
* Device-side settings - make sure that the sensor is configured and the device sends its data to the platform. It is desirable not to do additional calibrations on the device side, but to do it directly on the platform.
* Settings on the platform side - not only the readings in the widgets depend on them, but also the operation of draining and refueling alerts and fuel level reports. By optimizing these settings, it becomes easier to identify anomalies and irregularities in fuel data readings that may require further attention.

### Sensor creation

Fuel sensors are a type of [Measurement sensor](./) that can be created on a GPS tracking platform. To create a fuel sensor, navigate to the Device Management section and click on the Sensors and Buttons panel. Next, click on the + icon and select "measurement sensor" from the dropdown menu.

### Fuel sensor settings

Once you choose Fuel Level as the sensor type, additional settings will appear. The complete list of options for the fuel sensor includes:

* Sensor name - assign a clear and convenient name for the sensor. This name will be visible on widgets, reports, and rules to help you easily identify the sensor.
* Input - select the input from which the device transmits fuel data.
* Units – select a unit of measure.
* Accuracy - this refers to the specified percentage used to calculate the absolute error in tank volume. This error value will be used to compute the amount for refills and drains.
* Thresholds for drain detection - are used to determine drains in fuel reports. This parameter can be represented as the rate of change in the fuel level. Both thresholds are always checked, and if the fuel level changes faster than at least one of the set thresholds for more than accuracy level, the report will mark the fuel drain.
  * By time - maximum allowable flow rate is measured in units per hour and can be set in the sensor settings. When calculating the speed change over time, the platform compares the fuel level change between points. If it is not set, the default value is 120 units per hour. It doesn’t mean the fuel must change more than 120 per hour. It means the fuel level should change faster than 120 per hour (equal to 20 L per 10 minutes or 2 L per minute) to determine the drain in a report. This value should be set a few percentage points higher than the likely consumption rate during heavy loads or when the vehicle is ascending uphill.
  * By mileage - the maximum allowable fuel level change speed is measured in units per 100 km. It doesn’t mean the fuel must change more than set per 100 km. For example, we set 100 L per 100 km. It means the fuel level should change faster than 100 L per 100 km (equal to 10 L per 10 km or 1 L per km) to determine the drain in a report. This value must be manually entered and should not be based solely on the manufacturer's specified fuel consumption rate. We recommend conducting tests and verifying the actual fuel consumption rate recorded in the reports, then set the necessary values accordingly for maximum accuracy.
* Ignore in movement - the platform will automatically exclude any drains and refills that occur during movement from rules and reports. Movement is determined by the [Parking Detection setting](../../localisation-et-mouvement/widget-de-detection-de-stationnement.md).
  * Drains – drains in movement will be excluded.
  * Refills – refills in movement will be filtered.
  * Filter timeout - This setting appears when the Ignore feature is enabled. It determines the timeout period in minutes that will be used to shorten the driving intervals for fuel filtering. This option can be helpful if the fuel level stabilizes only after some time has passed since refueling, and the vehicle has already started moving. This is more commonly seen in vehicles with large fuel tanks. The default setting for this feature is 5 minutes.
* Calibration table - this parameter is used to convert the sensor readings into desired units such as liters. Some sensor manufacturers may provide the conversion values for the table. However, in most situations, calibration will be necessary in order to achieve accurate readings.
  * Tank volume - is the maximum volume of the tank, which is specified in units in the calibration table. If calibration values are not specified, the default value of 100 is assumed, which indicates that the data is being transmitted in percentage.
  * Even if your sensor already sends data to the platform in liters, it is better to specify the calibration as 0 = 0 liters and maximum fuel tank capacity = X liters.
  * If it is a sensor that transmits fuel level information in percentages, specify calibration 0 = 0 liters and 100 = maximum fuel tank capacity in liters.
* Advanced settings - are below the calibration table.
  * Ignore values - values should be specified the same way they come to the platform from the device.
    * Less - the filter can be used to ignore any readings that fall below a certain threshold, X. This is helpful in situations where a sensor's readings may fall below a certain value. For example, a loose wire or a sensor that sends a reading of 0 when the ignition is switched off.
    * More - the filter can be used to ignore any readings that exceed a certain threshold, X. This is valuable when dealing with sensors whose readings may occasionally increase dramatically. For example, if an error is detected or if there is a higher voltage than expected.
  * Multiplier - multiply the resulting values by a certain coefficient. If you want to divide values, use decimals.

### How fuel works on the platform

#### Receiving and processing fuel data

The platform reads and saves fuel sensor readings as they are received from the devices. Data from fuel sensors is only saved once a fuel sensor has been created in the system.

Filters for minima and maxima, calibration tables, and other sensor settings are only applied when the data is being output. As a result, you can change the settings at any time and rebuild the reports to see how the changes have affected the saved data. This provides flexibility in terms of configuration and ensures that the data is always up-to-date with the latest settings.

#### Drains and refills in rules

Rules for draining and refueling are based on the calibration table and absolute error, which is calculated as `tank volume * accuracy`.

The platform will record the last current reading of the sensor for a ten-minute span. Based on this reading, the following events will be triggered:

* If the fuel level has increased by more than the absolute error, a "filling" event will be recorded.
* If the fuel level has decreased by more than the absolute error, a "draining" event will be recorded.

For instance, if the tank capacity is 100 liters and the accuracy is 5%, a 5-liter change in fuel level within a 10-minute timeframe will trigger the rule.

#### Refills and drains in reports

The reporting system provides a more advanced method of analysis as it relies on a larger pool of saved data. All parameters are taken into account in the report analysis.

The platform uses the rate of fuel level decrease and absolute error to identify and register fuel drains. A "drain" occurs when the fuel level decreases by more than the absolute error within the specified thresholds for drains by time or mileage (if set).

In the report, a "filling" event is recorded when the fuel level increases by more than the absolute error. The platform will group consecutive filling or draining events, meaning that if the same condition is triggered repeatedly, the platform will group them into a single large filling or draining event.

#### Ignoring refills and drains in motion

Once you have enabled one or both options for ignoring - the next algorithm will be used for reports and alerts in addition to standard:

* If refueling begins during the [parking time](../../localisation-et-mouvement/widget-de-detection-de-stationnement.md), it will be displayed in the report and logged by the rule. Additionally, if refueling starts within X minutes of the filter timeout before parking or within X minutes of the filter timeout after the trip starts, it will also be logged by the rule and shown in the report.
* However, if refueling starts earlier than X minutes from the filter timeout before parking or later than X minutes from the filter timeout since the beginning of the trip, it will be filtered out.
* In cases where no filter timeout is specified, all refills that start during trips will be filtered.

#### Fuel sensor readings analysis and classification

The application of various statistical methods has resulted in a model for analyzing the quality of sensor data. Navixy team has developed an adaptive algorithm that can classify the quality of raw sensor data readings and provide a score on a 10-point scale: from 1 - the lowest quality, to 10 - high-quality data.\
To try this innovation, you need to generate a [fuel volume report](https://docs.navixy.com/eco-fleet/fuel-volume-report) for the object(s) under investigation. The quality rating will be available at the bottom of the report both in the interface of the cabinet and in documents (PDF/XLS) downloaded based on the generated report. The rating can also be obtained using API requests.

### See also

* [Enhancing fuel management accuracy with Fuel Sensor Quality Index](https://www.navixy.com/blog/enhancing-fuel-management-accuracy-with-fuel-sensor-quality-index/)
* [Mastering calibration tables for accurate fuel management](https://www.navixy.com/blog/calibration-tables/)
