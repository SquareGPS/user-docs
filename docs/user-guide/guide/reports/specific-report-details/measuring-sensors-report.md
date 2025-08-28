# Measuring sensors report

The **Measuring sensors report** in Navixy is designed to provide detailed data from configured measurement sensors or virtual sensors with a source value calculation method over a selected period.

This report allows users to view both graphical and statistical information from their devices' sensors, aiding in effective monitoring and decision-making.

## Requirements for generating the report

To successfully generate the **Measuring sensors report**, the following conditions must be met:

* **Device compatibility:** Ensure that the device supports the required sensor reading on the platform. You can verify this by checking the list of supported inputs for the specific model.
* **Active data transmission:** The device and its sensors must be configured correctly and actively transmitting data.
* **Virtual sensors:** [Virtual sensors](../../devices-and-settings/vehicle-sensors/virtual-sensors/) should have a source value calculation method and provide numeric values to the platform.
* **Sensor configuration:** The measurement sensors must be properly configured on the platform.

## Report parameters

The report uses several parameters to tailor the output to your needs:

* **Details time range:** Displays the received readings in increments of 5, 30 minutes, 1, 3, or 6 hours in the data detail table.
* **X-axis on the graph:** Choose whether to display the information by time or mileage.
* **Smooth data:** Apply smoothing to the graph to filter out peak values and average the data when there is significant variance.
* **Show address:** Displays the address received by the platform along with the data from the sensor. The address shown corresponds to the first reading in the detail segment.
* **Use smart filter:** Exclude data from short trips, defined as trips shorter than 300 meters with fewer than 4 data points sent by the device.

For each device, you must select the sensor for which to generate the report. Only devices with configured [measurement](../../devices-and-settings/vehicle-sensors/measurement-sensors/) or [virtual](../../devices-and-settings/vehicle-sensors/virtual-sensors/) sensors will be available in the list. If you select a virtual sensor of a wrong type, the report will indicate "This is not a measurement sensor."

## Visualizations

### Graph with sensor readings

The graph in the report displays measurement or virtual sensor readings in graphical form, helping you visualize data trends over time or distance.

* **Hovering over points:** When you hover over a point on the graph, you can view the exact time it was recorded and the sensor value. If the X-axis is set to mileage, you will also see the distance at which the reading was taken.

### Table with statistical data

The report includes a statistical data table that provides daily summaries of the sensor readings.

**Columns in the statistical data table:**

* **Date:** The specific date for the recorded data.
* **Minimum (units of measure):** The lowest value recorded by the sensor on that date.
* **Maximum (units of measure):** The highest value recorded by the sensor on that date.
* **Average value (units of measure):** The average of all sensor readings for that date.

Note: The units of measure will vary depending on the sensor settings.

### Data breakdown table

The **data breakdown table** presents sensor readings over specified time intervals, such as every 30 minutes, starting from a set time. It provides a detailed view of sensor data, helping to identify trends or issues during specific periods.

* **Interpreting the table:** If "No data" appears, it means no readings were received during that time. This could be due to the device not transmitting data, being turned off, or the sensor being disconnected.
