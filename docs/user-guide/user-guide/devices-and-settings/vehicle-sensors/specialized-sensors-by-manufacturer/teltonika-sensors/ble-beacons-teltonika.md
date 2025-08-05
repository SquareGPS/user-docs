# BLE Beacons (Teltonika)

Teltonika BLE beacons are versatile devices that can collect data on temperature, magnetic state, and transmit their identifiers over long distances, reaching up to 200 meters in open areas.

[![Teltonika bluetooth beacons](https://www.navixy.com/wp-content/uploads/2020/10/bluetelt.png)

](https://www.navixy.com/wp-content/uploads/2020/10/bluetelt.png)

These beacons utilize **Bluetooth Low Energy** technology (BLE 4.0+) , known for its energy efficiency, allowing them to operate for extended periods on their internal batteries—up to 2 years for SLIM models, up to 5 years for COIN models, and up to 19 years for PUCK models.

The beacons are housed in cases with an IP68 rating, providing robust protection against dust and water.

## Supported beacon models

- **Blue COIN MAG**: Small magnetic beacon
- **Blue PUCK MAG**: Large magnetic beacon
- **Blue COIN ID**: Small ID beacon
- **Blue PUCK ID**: Large ID beacon
- **Blue SLIM ID**: Card-sized beacon for employee identification
- **Blue COIN T**: Small temperature beacon
- **Blue PUCK T**: Large temperature beacon

### Temperature sensors

To add a temperature sensor:

1. Navigate to the measuring sensors section in the input tab.
2. Select **"BLE: Temperature"** as the input type.
3. Choose **"Temperature"** as the sensor type.

[![Teltonika bluetooth beacons](https://www.navixy.com/wp-content/uploads/2020/10/chrome_zqbp0ajule.png)

](https://www.navixy.com/wp-content/uploads/2020/10/chrome_zqbp0ajule.png)

### Magnetic sensors

Magnetic sensors display their status in the “Sensor readings” [information widget](/wiki/pages/createpage.action?spaceKey=USERDOCSOLD&title=Device%20information%20widgets&linkCreation=true&fromPageId=2909013722). This widget allows you to monitor whether the sensor is currently active or not.

### Driver identification sensors

Identification sensors function similarly to iButton and RFID but without the need for a physical reader. When the sensor is within the tracker's range, its identifier will automatically be displayed.

**See also:**

- [Assigning driver ID keys in the Driver’s profile](../../../../fleet-management/drivers.md)
- [Driver identification (Rules and notifications)](../../../../rules-and-notifications/scheduling-and-dispatching/driver-identification.md)