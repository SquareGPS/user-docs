# Types of fuel level sensors

* [Types of fuel sensors](types-of-fuel-level-sensors.md#types-of-fuel-sensors)
  * [Float fuel sensor](types-of-fuel-level-sensors.md#float-fuel-sensor)
  * [Capacitive fuel sensor](types-of-fuel-level-sensors.md#capacitive-fuel-sensor)
  * [Ultrasonic fuel sensor](types-of-fuel-level-sensors.md#ultrasonic-fuel-sensor)
* [How to choose the right fuel sensor](types-of-fuel-level-sensors.md#how-to-choose-the-right-fuel-sensor)
  * [Tank dimensions](types-of-fuel-level-sensors.md#tank-dimensions)
  * [Multiple sensors on one vehicle](types-of-fuel-level-sensors.md#multiple-sensors-on-one-vehicle)
  * [Fuel sensor outputs](types-of-fuel-level-sensors.md#fuel-sensor-outputs)
* [Leading fuel sensor manufacturers](types-of-fuel-level-sensors.md#leading-fuel-sensor-manufacturers)
  * [Omnicomm (Russia)](types-of-fuel-level-sensors.md#omnicomm-russia)
  * [Technoton (Belarus)](types-of-fuel-level-sensors.md#technoton-belarus)
  * [Siensor (China)](types-of-fuel-level-sensors.md#siensor-china)
  * [Escort (Russia)](types-of-fuel-level-sensors.md#escort-russia)

Fuel sensors are devices designed to make accurate measurements of the fuel level in a vehicle’s tank. According to these measurements a GPS tracking and telematics platform features the following data:

* fuel level in the tank of a vehicle
* fuel consumption per time period
* average fuel consumption. e.g. miles per gallon (mpg)
* fuel refills or drains

Fuel sensors are used on stationary units, such as fuel tanks at gas stations, and on vehicles: cars, locomotives, ships, etc.

## Types of fuel sensors

The most common types of fuel sensors are:

* Factory-installed sensors
  * **Float fuel sensor**
* Additionally Installed sensors
  * **Capacitive fuel sensor**
  * **Ultrasonic sensor**

The floating fuel sensor, which comes pre-installed in vehicles, provides a gauge of the fuel level on the dashboard. However, it's important to note that these sensors only offer an approximate reading and are not highly accurate, with a relative error ranging from 10-20%.

On the other hand, in fleet management systems, integrators of GPS tracking and telematics opt for capacitive or ultrasonic fuel sensors. These sensors are known for their precision, boasting a significantly lower relative error of only 1-2%.

### Float fuel sensor

A float fuel sensor is installed into the tank of a vehicle at the factory.

![Float fuel sensor](https://www.navixy.com/wp-content/uploads/2019/05/float-type-fuel-sensor.png)

**Operation concept:** A potentiometer is connected to a float, which is used to measure the fuel level. As the fuel level changes, the position of the float also changes, resulting in a corresponding change in resistance. This change in resistance ultimately leads to a change in the output voltage of the sensor. The data collected by the float sensor is then transmitted to the dashboard of a vehicle via:

* a separate wire, analog signal (in the older vehicles)
* CAN bus, digital signal (in the modern vehicles)

### Capacitive fuel sensor

Some fleet owners install a Capacitive Sensor in order to monitor fuel consumption and fuel drains.

![Capacitive fuel sensor by Omnicomm](https://www.navixy.com/wp-content/uploads/2019/05/LLS-fuel-sensor-by-omnicomm-600x600.png)

![Capacitive fuel sensor design concept](https://www.navixy.com/wp-content/uploads/2019/05/capacitive-fuel-sensor-design-concept.png)

**Operation concept:** Capacitive Fuel Sensor is an actual electric capacitor.

The measuring system consists of two tubes that do not make physical contact. One tube is inserted into the other, serving as capacitor plates. The tubes are connected to the sensor on one end, and left open on the other, while also being electrified.

When the tubes are placed into a vehicle tank, they are filled with fuel, including the space in between. The fuel acts as a dielectric for the electric capacitor. As the fuel fills the space between the tubes, the electrical capacitance changes accordingly.

Gasoline has lower electrical resistance compared to air, resulting in faster recharge times. Therefore, the more fuel present in the tubes, the more rapidly the capacitor will be charged.

The sensor measures the height of the fuel column in both the tank and the fuel sensor itself. This is determined by the time it takes to charge the capacitor. These parameters, along with geolocation data, are then transmitted to the GPS tracking platform through the GPS tracker.

### Ultrasonic fuel sensor

![Ultrasonic Fuel Sensor](https://www.navixy.com/wp-content/uploads/2019/05/ultrasonic-fuel-sensor.png)

![Ultrasonic Fuel Sensor](https://www.navixy.com/wp-content/uploads/2019/05/ultrasonic-fuel-sensor2.png)

Some fleet operators choose to install ultrasonic fuel sensors to monitor fuel consumption and fuel drains.

**Operation concept:** Ultrasonic sensor has a wire connection with a GPS tracker and works as an ultrasonic transmitter.

This transmitter, which is fixed on the outside wall of a fuel tank, at the bottom, sends ultrasonic impulses. The signal travels from the bottom up to the fuel surface and back. The reflected signal will be received by the same transmitter. Based on the time of flight it measures the height of the fuel column in the tank.

These parameters are sent to the GPS tracker and further to the GPS tracking platform alongside geolocation and other valuable data.

_However, this technology has a few pitfalls._ First of all, the installation process is typically difficult and requires a few items:

* A special epoxy glue or a metal band is used to connect the sensor to the bottom of the tank. Make sure the sensor adheres perfectly to the tank surface, otherwise ultrasonic signals will be distorted and the measurements will be inaccurate.
* Should the tank have any baffles (to control the rapid flow of fuel and prevent its sloshing), it may affect the signal and the measurements. This makes choosing the right spot for the sensor even more difficult and is often done in a hit-and-miss fashion.
* The echo signal can be distorted or lost if the tank shape is too complex. Besides, blisters and pits on the internal surface of the tank can also affect the quality of the measurements. As the result - a greater error.
* Dirt and water accumulate at the bottom of the tank. Again, it distorts the ultrasonic beam and causes false fluctuations in the fuel level readings.

In real-world terms, Ultrasonic fuel sensors are only used for vehicles running on gas, as there are no other options available.

## How to choose the right fuel sensor

To select between capacitive and ultrasonic fuel sensor one needs to know:

* tank dimensions (primarily the height)
* outputs to connect with the tracker

### Tank dimensions

Tank height and shape play a crucial role for capacitive fuel sensors. Make sure the client provides this data (at least approximately) before the installation.

The measuring part of the sensor must be slightly bigger than the tank height (to make sure the sensor reaches fuel at the bottom of the tank). During installation the measuring tubes will be cut to fit the tank. However, it is important to leave a gap of 1-1.5 inches (3-4 cm) between the sensor and the bottom to prevent a short circuit due to possible dirt or water accumulation at the tank bottom.

![Tank dimensions](https://www.navixy.com/wp-content/uploads/2019/05/tank-dimensions.png)

Different manufacturers of fuel sensors can offer different size ranges, however in most cars a sensor of 0.7 m (∼27.6 inch) will be enough.

### Multiple sensors on one vehicle

One might need to consider a few fuel sensors for one vehicle, if it falls into one of the following cases:

* **The vehicle has two or more fuel tanks.** Generally, a heavy-duty vehicle (a truck or an off-road vehicle) will have two or more fuel tanks. Installing a fuel sensor on each tank will provide a full picture of the fuel level. In a GPS tracking system it can be displayed separately for each sensor and as an aggregate value of all the fuel sensors.
* **The fuel tank of the vehicle has a complex shape.** As it is often the case with agricultural equipment, a fuel tank might have a customized shape or consist of two different sections. In this case, it requires two or more fuel sensors to provide for precise measurements. The GPS tracking and telematics system will show an average value of all the fuel sensors.
* **The fuel tank of the vehicle is extra long.** Such tanks can be usually found on campers or trains. In this case, as you can imagine, even minor fluctuations in the tank will affect the sensor readings. Using two sensors and installing them diagonally at the opposite sides will help to eliminate the problem. The GPS tracking system will show an average value of the both fuel sensors. Extra long tanks (long and only 4-6”/ 10-15 cm high) are often used in cars. In this case it might be most efficient to consider fuel level monitoring via CAN-data.

> \[!INFO] Fuel tankers have 2 or 3 tanks, each of them having at least 3 sections. For maximum accuracy each tank and each section should be equipped with a fuel level sensor. Make sure, that the sensor has an RS-485 output. An RS-232 won’t provide data for multiple sensors to be connected to the same tracker.

![Multiple sensors on one vehicle](https://www.navixy.com/wp-content/uploads/2019/05/wiring-diagram-rs485.png)

### Fuel sensor outputs

If your client’s vehicle is already equipped with a tracker, the first task will be to ask for the tracker’s make and model. Once you’ve cleared that up, go to Navixy [Devices](https://www.navixy.com/devices/) to check available outputs for the tracker and to select the fuel sensor that fits. If the tracker supports both analog and digital signals (just like [Teltonika FMB 125](https://www.navixy.com/devices/teltonika/teltonika-fmb125/)), a fuel sensor with a digital interface (e.g. RS-485) should be favored.

If a client needs both a fuel sensor and a tracker, we would definitely recommend a digital interface (e.g. RS-485) in both cases.

## Leading fuel sensor manufacturers

Fuel sensor manufacturing (as any other telematics sensors manufacturing) is a very painstaking but profitable process. Fuel sensors are produced by:

* **Sensors and meters manufacturers**, e.g. Siensor, Escort, etc.
* **GPS tracker manufacturers** – in this case a fuel sensor is a secondary product. Some GPS tracker manufacturers purchase sensors by other companies and brand them as their own.

Currently the most popular fuel sensor developers and manufacturers are:

### Omnicomm (Russia)

* **Marketed in:** Eastern Europe, Latin America, Russia and CIS
* **Exhibited in:** trade shows in Russia, UAE, Mexico
* **Available languages:** English, Spanish, Russian, Portuguese  [https://www.omnicomm-world.com/](https://www.omnicomm-world.com/)
* [Facebook](https://www.facebook.com/OmnicommWorld), [LinkedIn](https://www.linkedin.com/company/omnicomm/)

|                                                                                                                                                                |           |                                                                                                                                                                                    |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ![Omnicomm LLS 4 Digital fuel sensor](https://www.navixy.com/wp-content/uploads/2019/05/LLS4-fuel-sensor-600x250.png)                                          | LLS 4     | <p>Digital fuel sensor<br>Specification: <a href="https://www.navixy.com/wp-content/uploads/2019/05/omnicomm-sensors.pdf">Omnicomm-sensors</a></p>                                 |
| ![Omnicomm LLS-AF 4 Frequency-analogue fuel sensor](https://www.navixy.com/wp-content/uploads/2019/05/LLS-AF4-fuel-sensor-600x250.png)                         | LLS-AF 4  | <p>Frequency-analogue fuel sensor<br>Specification: <a href="https://www.navixy.com/wp-content/uploads/2019/05/omnicomm-sensors.pdf">Omnicomm-sensors</a></p>                      |
| ![Omnicomm LLS 20230 Digital fuel sensor in an explosion-proof variation](https://www.navixy.com/wp-content/uploads/2019/05/LLS-20230-fuel-sensor-600x250.png) | LLS 20230 | <p>Digital fuel sensor in an explosion-proof variation<br>Specification: <a href="https://www.navixy.com/wp-content/uploads/2019/05/omnicomm-sensors.pdf">Omnicomm-sensors</a></p> |

### Technoton (Belarus)

* **Marketed in:** Russia and CIS, Eastern Europe, Latin America, Middle East.
* **Exhibited in:** trade shows in Russia
* **Available languages:** English, Spanish, Russian [https://www.jv-technoton.com](https://www.jv-technoton.com/)
* [LinkedIn](https://www.linkedin.com/company/technoton/)

|                                                                                                                                                                         |            |                                                                                                                                                                                                                                                 |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ![](https://www.navixy.com/wp-content/uploads/2019/05/DUT-E-fuel-sensor-150x150.png)                                                                                    | DUT-E      | <p>Digital / Frequency-analogue/CAN-like fuel sensors. Any fuel sensor can come with one of the mentioned outputs<br>Specification: <a href="https://www.navixy.com/wp-content/uploads/2019/05/technoton-sensors.pdf">Technoton-sensors</a></p> |
| ![Technoton DUT-E 2Bio Fuel sensor with automatic detection of fuel brand change](https://www.navixy.com/wp-content/uploads/2019/05/DUT-E-2Bio-fuel-sensor-150x150.png) | DUT-E 2Bio | <p>Fuel sensor with automatic detection of fuel brand change (e.g. summer/ winter diesel fuel)<br>Specification: <a href="https://www.navixy.com/wp-content/uploads/2019/05/technoton-sensors.pdf">Technoton-sensors</a></p>                    |

### Siensor (China)

* **Marketed:** all over the globe
* **Exhibited in:** trade shows in Russia
* **Available languages:** English, Portuguese, Russian, Chinese\
  [http://siensor.com](http://siensor.com/)
* [Facebook](https://www.facebook.com/siensor/)

|                                                                                                                        |       |                                                                                                                                                   |
| ---------------------------------------------------------------------------------------------------------------------- | ----- | ------------------------------------------------------------------------------------------------------------------------------------------------- |
| ![Siensor D10X Digital fuel sensor](https://www.navixy.com/wp-content/uploads/2019/05/D10X-fuel-sensor-150x150.png)    | D10X  | <p>Digital fuel sensor<br>Specification: <a href="https://www.navixy.com/wp-content/uploads/2019/05/siensor-sensors.pdf">Siensor-sensors</a></p>  |
| ![Siensor AF10X Analogue fuel sensor](https://www.navixy.com/wp-content/uploads/2019/05/AF10X-fuel-sensor-150x150.png) | AF10X | <p>Analogue fuel sensor<br>Specification: <a href="https://www.navixy.com/wp-content/uploads/2019/05/siensor-sensors.pdf">Siensor-sensors</a></p> |

### Escort (Russia)

* **Marketed:** all over the globe
* **Exhibited in:** trade shows in Russia
* **Available languages:** English, Spanish, Russian\
  [https://www.fmeter.ru/en/](https://www.fmeter.ru/en/)
* [Facebook](https://www.facebook.com/gkeskort/)

|                                                                                                                                                    |               |                                                                                                                                                                                                              |
| -------------------------------------------------------------------------------------------------------------------------------------------------- | ------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| ![Escort TD-BLE Wireless fuel level sensor](https://www.navixy.com/wp-content/uploads/2019/05/TD-BLE-fuel-sensor-600x498.png)                      | TD-BLE        | <p>Wireless fuel level sensor<br>Specification: <a href="https://www.navixy.com/wp-content/uploads/2019/05/escort-sensor.pdf">Escort-sensor</a></p>                                                          |
| ![Escort TD-150 Fuel sensor with multiple output signals](https://www.navixy.com/wp-content/uploads/2019/05/Escort-TD-150-fuel-sensor-600x498.png) | Escort TD-150 | <p>Fuel sensor with multiple output signals: RS-485, analogue output, frequency output<br>Specification: <a href="https://www.navixy.com/wp-content/uploads/2019/05/escort-sensor.pdf">Escort-sensor</a></p> |
