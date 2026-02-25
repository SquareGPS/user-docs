# Short trips in history and long parking states

### Question

Why does trip history show very short trips along with long parking durations?

![](<../.gitbook/assets/Unknown image (109)>)

### Answer

Most likely, the device has **Consider ignition state** enabled in the Parking Detection portlet.

![](<../.gitbook/assets/Unknown image (110)>)

Most likely, the tracker sends inconsistent and intermittent ignition state data. Once the platform detects ignition OFF state, the trip state is changed to Parked, bypassing the Min idle detection logic:

* The trip starts if the speed is greater than or equal to min\_speed and the ignition is on.
* The trip ends if the speed drops below min\_speed and either the elapsed time exceeds min\_parking or the ignition is off.

Since it is enough for the device to send OFF ignition state for a trip to be ended, many trips in the trip history will be short and last no longer than a couple of seconds. The duration of such trips is determined by the duration of the ignition ON state.

To make sure that the ignition is the root cause, you can prepare a Raw Data spreadsheet with the discrete\_inputs columns selected:

![](<../.gitbook/assets/Unknown image (111)>)

To resolve the situation, you can either fix ignition detection from the device side so it detects ignition consistently without unexpected drops, or switch off the Consider ignition state option in the Parking detection portlet. The old track durations will not change after the fix.

### Links

* [Parking detection widget](https://www.navixy.com/docs/user/guide/devices-and-settings/location-and-movement/parking-detection-widget)
* [Raw Data](https://www.navixy.com/docs/expert-center/faq-and-troubleshooting/access-iot-data/save-iot-data-to-csv-file)
