# Unigis

The Unigis protocol is a vehicle location data forwarding protocol between Navixy and TMS platform developed by Unigis company. The most frequent use cases relate to real-time collection of GPS tracking and vehicle Telematics data by logistics departments of large manufacturing and retail chain companies. Most of these companies are located in the US, Mexico, Columbia, Chile, Argentina, Brazil and Spain.

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

\| Parameter | Explanation | | --- | --- | | Destination server address and port | URL of endpoint and port that is used by Ungis TMS.\
\
Most commonly:\
\
\* Address: http://unigis2.unisolutions.com.ar/HUB/UNIGIS/MAPI/SOAP/GPS/Service.asmx\
\* Port: 80 | | Login and password | Your Unigis login and password | | External ID | License plate number of an individual vehicle |

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

A Retranslation management screen should look similar to the following, with Unigis login and password. Make sure the "Enabled" button is checked and click the "Save" button to complete the process.

![Types and parameters](https://www.navixy.com/wp-content/uploads/2022/08/pasted-image-0-600x112.png)

Next, the retranslator will need to be linked to the device on the Unigis side. To do so, select the “Link” ![link image](https://www.navixy.com/wp-content/uploads/2022/08/image-3.png)

button in the data forwarding widget. Select the retranslator to be connected, and click “Link” below.

Next, add the ID of the device on the 3rd party system, either by clicking the pencil icon or the external ID field. This value should be the license plate number on the Unigis side. Select “Save” once completed.

#### Managing

To edit or stop data being forwarded, please refer to the following steps:

1. Select the “Pencil” icon or click in the associated box to edit the external ID used to point to the device on the 3rd party system
2. To stop the data forwarding, click the “Trash” button
3. Next, acknowledge the change on the popup

To change retranslator settings such as name, login information, or enabled, click “Protocols.”

This will open the retranslator management window. Select the row to edit and either click the pencil in the top left, or double-click the row in question to allow editing. Save any changes.

![data forwarding management](https://www.navixy.com/wp-content/uploads/2022/08/pasted-image-0-1-600x96.png)

#### Troubleshooting

If data does not display on the 3rd party Unigis system, please verify:

* Username and password for Unigis are correctly entered
* URL was entered correctly
* Retranslator is enabled
* External ID matches the license plate on Unigis
