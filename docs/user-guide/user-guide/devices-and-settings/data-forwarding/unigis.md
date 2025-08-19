# Unigis

The **Unigis** protocol is a vehicle location data forwarding protocol between Navixy and TMS platform developed by Unigis company. The most frequent use cases relate to real-time collection of GPS tracking and vehicle Telematics data by logistics departments of large manufacturing and retail chain companies. Most of these companies are located in the US, Mexico, Colombia, Chile, Argentina, Brazil and Spain.

_Protocol Category: Enterprise Compliance_

#### Table of contents

1. [What is Unigis?](unigis.md#what-is-unigis)
2. [Technical information about Unigis](unigis.md#tech-info-unigis)
3. [Unigis Configuration](unigis.md#unigis-config)
4. [Setting up](unigis.md#setting-up)
5. [Managing](unigis.md#managing)
6. [Troubleshooting](unigis.md#troubleshooting)

### What is Unigis?

Through the Unigis data forwarding protocol, fleet GPS tracking data is streamlined across multiple servers allowing data retransmission between Navixy and Unigis partners.

Using the Unigis protocol, users can integrate with self-service chains and/or suppliers of products and services within the Unigis network, such as Walmart, Home Depot, and Kimberly Clark. Fleet data can be transmitted between all parties without requiring access to Navixy's platform.

### Unigis general technical information

The Unigis protocol utilizes SOAP to send XML data from tracking devices to Unigis over HTTP as part of the OSI application layer. Data is pushed from the Navixy platform to Unigis every 5 minutes.

Data that’s sent to Unigis:

* Date and time
* Longitude
* Latitude
* Altitude
* Speed
* Inputs events
* Door Open
* Panic Button
* Engine Off
* Theft
* External ID (License Plate)

Nature: ASCII

### Unigis Configuration

#### Setting up

To initiate data forwarding using the Unigis protocol from Navixy, you will need the following parameters:

<table><thead><tr><th width="281.6363525390625">Parameter</th><th>Explanation</th></tr></thead><tbody><tr><td>Destination server address and port</td><td>URL of endpoint and port that is used by Ungis TMS.<br><br>Most commonly:<br><br>* Address: http://unigis2.unisolutions.com.ar/HUB/UNIGIS/MAPI/SOAP/GPS/Service.asmx<br>* Port: 80</td></tr><tr><td>Login and password</td><td>Your Unigis login and password</td></tr><tr><td>External ID</td><td>License plate number of an individual vehicle</td></tr></tbody></table>

To set up data forwarding in Unigis protocol, open the device settings from the main menu by pressing the “Gear” icon on the bottom left of the screen

1. Then, click the “Data forwarding” widget
2. Click “Protocols”
3. This will open a popup where you will input the required parameters by pressing the + button

For the Unigis protocol, input the following information:

1. Name: Enter a name to make this retranslator easily identifiable
2. Protocol: Select the Unigis protocol from the dropdown
3. Unigis Login and Password
4. Destination server address, e.g. http://unigis2.unisolutions.com.ar/HUB/UNIGIS/MAPI/SOAP/GPS/Service.asmx
5. Destination port, e.g. 80

A Retranslation management screen should look like the following, with Unigis login and password. Make sure the **Enabled** button is checked and click the **Save** button to complete the process.

![](https://www.navixy.com/wp-content/uploads/2022/08/pasted-image-0-600x112.png)

Next, the retranslator will need to be linked to the device on the Unigis side. To do so, select the **Link** <img src="https://www.navixy.com/wp-content/uploads/2022/08/image-3.png" alt="link image" data-size="line"> button in the data forwarding widget. Select the retranslator to be connected, and click **Link** below.

Next, add the ID of the device in the 3rd-party system either by clicking the pencil icon or the external ID field. This value should be the license plate number on the Unigis side. Select **Save** once completed.

#### Managing

To edit or stop data from being forwarded, please refer to the following steps:

1. Select the **Pencil** icon or click in the associated box to edit the external ID used to point to the device on the 3rd party system.
2. Click the **Trash** button to stop the data forwarding.
3. Acknowledge the change in the pop-up.
4. Click **Protocols** to change retranslator settings such as name, login information, or enabled status
5. This will open the retranslator management window. Select the row to edit and either click the pencil in the top left or double-click the row in question to allow editing. Save any changes.

![](https://www.navixy.com/wp-content/uploads/2022/08/pasted-image-0-1-600x96.png)

#### Troubleshooting

If data does not display on the 3rd-party Unigis system, please make sure that:

* Username and password for Unigis are correctly entered
* URL was entered correctly
* Retranslator is enabled
* External ID matches the license plate on Unigis
