# navixy-ws

## Navixy WS

## Navixy Web Service— Protocol to send XML data

Navixy Web Service data forwarding protocol transmits fleet data from the Navixy system to any third-party system.

_Protocol Category: Data consolidation protocol_&#x20;

#### Table of contents

1. [What is Navixy Web Service?](navixy-ws.md#what-is-ws)
2. [Technical information about Navixy Web Service](navixy-ws.md#tech-info-ws)
3. [Navixy Web Service Configuration](navixy-ws.md#ws-config)
4. [Setting up](navixy-ws.md#setting-up)
5. [Managing](navixy-ws.md#managing)
6. [Troubleshooting](navixy-ws.md#troubleshooting)

### What is Navixy Web Service?

Navixy Web Service data forwarding protocol is flexible, allowing third parties to store fleet data in their databases to use for any purposes or to display data on the web resources.

Since this data forwarding protocol is platform agnostic, it would be the ideal option for any partner that works with XML files.

### Navixy Web Service general technical information

The Navixy Web Service protocol utilizes SOAP to allow the pulling of XML data from tracking devices as part of the OSI application layer. Data is pulled on demand.

Data fields that are sent:

* DateGPS
  * Date and time in UTC
* Ignition
  * Boolean ignition status
* Latitude
* Longitude
* SpeedGPS
  * km/h
* UnitPlate
  * License plate
* Altitude
  * Meters
* Course
  * Direction vehicle is heading, for example: N,S,E,O,NO,NE,SO,SE
* DeviceID
  * IMEI
* NumSat
  * Number of GNSS satellites the device is utilizing
* Odometer
  * Traveled distance in km

### Navixy Web Service Configuration

#### Setting up

**Navixy settings:**

Required Parameters

* Login and Password
  * This could be anything as long as it’s not taken

To set up data forwarding in Navixy Web Service protocol, open the device settings from the main menu by pressing the “Gear” icon on the bottom left of the screen.

Then, click the “Data forwarding” widget.

Click “Protocols”.

This will open a popup where you will input the required parameters by pressing the + button.

For the Navixy Web Service protocol, input the following information:

\| Parameter | Explanation | | --- | --- | | Name | Enter a name to make this retranslator easily identifiable | | Protocol and Login | Select the Navixy Web Service protocol from the dropdown;\
\
Use any login and passcode as long as it's not already in use. | | Destination server address and port | These aren’t needed for the Navixy Web Service protocol, however, you must still fill these in |

A Retranslation management screen should look similar to the following, with the Navixy Web Service login and password. Make sure the "Enabled" button is checked and click the "Save" button to complete the process.

![Recurso Confiable](https://www.navixy.com/wp-content/uploads/2022/10/pasted-image-0-4-600x112.png)

Next, the retranslator will need to be linked to the device. To do so, select the “Link”

![link image](https://www.navixy.com/wp-content/uploads/2022/08/image-3.png)

button in the data forwarding widget. Select the retranslator to be connected, and click “Link” below.

Select the retranslator to be connected, and click “Link”.

External ID is not needed for the Navixy Web Service protocol.

Select “Save” once completed.

#### External access:

Required Parameters

* Login and Password
  * This should match what was input above
* deviceIDs
  * Max of 100
* startDate and endDate
  * The following is an example for September 9, 2022 12am UTC to 11:59:59
  * UTC: 2022-09-01T00:00:00Z to 2022-09-01T11:59:59Z

The description of the protocol in WSDL can be found below, relating to where the server is located:

EU [https://soap.navixy.com/LocationDataService?wsdl](https://soap.navixy.com/LocationDataService?wsdl)

US [https://soap.us.navixy.com/LocationDataService?wsdl](https://soap.us.navixy.com/LocationDataService?wsdl)

A SOAP request must be made utilizing one of the above WSDL pages. The XML request itself is as follows, replaced with the associated information:

\<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:tem="http://tempuri.org">

&#x20;  [soapenv:Header](navixy-ws.md)

&#x20;  [tem:authentication](navixy-ws.md)

&#x20;   username

&#x20;   password

&#x20;  \</tem:authentication>

&#x20;  \</soapenv:Header>

&#x20;  [soapenv:Body](navixy-ws.md)

&#x20;  [tem:dataRequest](navixy-ws.md)

&#x20;   &#x20;

&#x20;     IMEI of device

&#x20;     2022-08-30T00:00:00Z

&#x20;     2022-08-31T00:00:00Z

&#x20;  \</tem:dataRequest>

&#x20;  \</soapenv:Body>

\</soapenv:Envelope>

An example response may look something like this:

&#x20;   &#x20;

&#x20;        2022-08-30T00:02:55.000Z

&#x20;        false

&#x20;        75.9270866

&#x20;        -85.5207616

&#x20;        0.0

&#x20;        ss3ssj

&#x20;        284.0

&#x20;        E

&#x20;        866258048802349

&#x20;        15

&#x20;        59845

&#x20;   &#x20;

#### Managing

To edit or stop data being forwarded, please refer to the following steps:

To stop the data forwarding, click the “Trash” button.

Next, acknowledge the change on the popup.

To change retranslator settings such as name, login information, or enabled, click “Protocols.”

This will open the retranslator management window. Select the row to edit and either click the pencil in the top left, or double-click the row in question to allow editing. Save any changes.

![Recurso Confiable](https://www.navixy.com/wp-content/uploads/2022/10/pasted-image-0-1-2-600x106.png)

#### Troubleshooting

In order to verify and test your SOAP request to the platform, it is suggested to use SoapUI which can be found here: [https://www.soapui.org/downloads/soapui/](https://www.soapui.org/downloads/soapui/)

1. Install Soap UI
2. From the file menu, select “New SOAP Project”
3. Paste the correct path into the WSDL field according to the server and select “Create sample requests for all operations?”
4. US: https://soap.us.navixy.com/LocationDataService?wsdl
5. EU: https://soap.navixy.com/LocationDataService?wsdl
