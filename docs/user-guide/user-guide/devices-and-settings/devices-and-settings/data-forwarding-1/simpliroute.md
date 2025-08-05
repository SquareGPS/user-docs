# simpliroute

## Simpliroute

## SimpliRoute

SimpliRoute is a data retransmission protocol that delivers vehicle tracking data for users to send information from their system to SimpliRoute.

_Protocol Category: Enterprise compliance_

#### Table of contents

1. [What is SimpliRoute?](simpliroute.md#what-is-simpliroute)
2. [Technical information about SimpliRoute](simpliroute.md#tech-info-simpliroute)
3. [Simpliroute Configuration](simpliroute.md#simpliroute-config)
4. [Setting up](simpliroute.md#setting-up)
5. [Managing](simpliroute.md#managing)
6. [Troubleshooting](simpliroute.md#troubleshooting)

### What is SimpliRoute?

SimpliRoute is a data retransmission protocol that delivers vehicle location data and links it to the SimpliRoute order system. This allows users the ability to track orders that are managed within this software and that are synchronized with the vehicle positions obtained.

This data retransmission protocol is ideal for users looking to comply with Simpliroute data forwarding to track vehicle positioning.

### SimpliRoute general technical information

The SimpliRoute protocol utilizes the POST method to send JSON data over HTTP to the SimpliRoute servers for further data processing.

Data sent to SimpliRoute:

* Vehicle VIN
* License Plate
* Latitude
* Longitude
* Date/Time
* Speed
* Ignition
* GPS Provider - tax number specified in user information

### SimpliRoute Configuration

#### Setting up

Required Parameters

* Vehicle built with associated license plate and VIN according to the standards [here](https://www.navixy.com/docs/user/web-interface-docs/fleet/).

To set up data forwarding for the SimpliRoute protocol, open the device settings from the main menu by pressing the “Gear” icon on the bottom left of the screen.

Then, click the “Data forwarding” widget.

Click “Protocols”.

This will open a popup where you will input the required parameters by pressing the + button.

For the SimpliRoute protocol, input the following information:

\| Parameter | Explanation | | --- | --- | | Name | \* Address: http://unigis2.unisolutions.com.ar/HUB/UNIGIS/MAPI/SOAP/GPS/Service.asmx\
\* Port: 80 | | Protocol | Select the Simple Route protocol from the dropdown | | Destination server address and port | \* Address: https://k8k5azm77j.execute-api.sa-east-1.amazonaws.com/prod/gps\
\* Port: 443 |

A Retranslation management screen should look similar to the following, with SimpliRoute login and password. Make sure the "Enabled" button is checked and click the "Save" button to complete the process.

![SimpliRoute](https://www.navixy.com/wp-content/uploads/2022/10/pasted-image-0-2-600x115.png)

Next, the retranslator will need to be linked to the device on the Unigis side. To do so, select the ![image-20250310-140837.png](../../data-forwarding/attachments/image-20250310-140837.png)

button in the data forwarding widget. Select the retranslator to be connected, and click “Link” below.

External ID is not needed for the SimpliRoute protocol.

Select “Save” once completed.

#### Managing

To edit or stop data being forwarded, please refer to the following steps:

To stop the data forwarding, click the “Trash” button.

Next, acknowledge the change on the popup.

To change retranslator settings such as name, login information, or enabled, click “Protocols.”

This will open the retranslator management window. Select the row to edit and either click the pencil in the top left, or double-click the row in question to allow editing. Save any changes.

![SimpliRoute](https://www.navixy.com/wp-content/uploads/2022/10/pasted-image-0-1-600x116.png)

#### Troubleshooting

If data does not display on the 3rd party SimpliRoute system, please verify:

* URL was entered correctly
* Retranslator is enabled
* Tracker on Navixy is associated with a vehicle on the platform with a valid license plate and VIN
