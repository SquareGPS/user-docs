# Parking detection widget

Parking detection identifies when an object has been stationary for a specified time period and within a set speed threshold, using GPS data.

![image-20240815-183001.png](attachments/image-20240815-183001.png)

**Parameters for parking detection:**

- **Minimum idle detection time** (`min_parking`): This is the minimum amount of time that an object must remain stationary before it is considered parked.
- **Maximum idle speed** (`min_speed`): This is the speed threshold under which the object must stay to be detected as parked.

By default, these parameters are set to 5 minutes and 3 km/h, respectively.

**Parking detection conditions:**

- **By speed and time**:  
Parking status is detected when the object's speed drops below the defined `min_speed` and stays there for longer than `min_parking`. Stops shorter than `min_parking` are not considered as parking and will not interrupt the trip.
- **Considering ignition**:
  - The trip starts if the speed is greater than or equal to `min_speed` and the ignition is on.
  - The trip ends if the speed drops below `min_speed` and either the elapsed time exceeds `min_parking` or the ignition is off.
- **Considering motion sensor**:
  - The trip starts if the speed is greater than or equal to `min_speed` and the motion sensor detects movement.
  - The trip ends if the speed drops below `min_speed` or the motion sensor detects no movement, and the elapsed time exceeds `min_parking`.
- **Considering both motion and ignition**:
  - The ignition status takes precedence over the motion sensor.
  - The trip starts if the speed is greater than or equal to `min_speed`, and both the motion sensor detects movement and the ignition is on.
  - The trip ends if the speed drops below `min_speed` or the motion sensor detects no movement, and the elapsed time exceeds `min_parking` with the ignition off.

These settings allow for fine-tuning parking detection to accurately reflect the vehicle's real-world behavior, minimizing false detections and improving trip tracking accuracy.