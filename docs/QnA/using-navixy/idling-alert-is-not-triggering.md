# Idling alert is not triggering

### Question

What could be the reason why the alert is not popping up and there is no track in the reports?

### Answer

To activate the alert, you must set the duration after which idling will be considered excessive. The rule monitors when a vehicle is parked (as determined by the Parking Detection settings) while the ignition is **ON**. If the vehicle remains in this state longer than the specified duration, a notification will be triggered.

Customers often assume that the ignition input will be created on the platform by default, but this is not the case. The platform does not know where the ignition is connected unless the manufacturer has clearly documented that input.

![](<../.gitbook/assets/Unknown image (117)>)
