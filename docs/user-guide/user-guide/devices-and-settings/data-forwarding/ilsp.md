# ILSP

## ILSP — Protocol for private security vehicle data between servers

ILSP offers private security services in Mexico. The ILSP data forwarding protocol enables their software to share vehicle data across networks.

_Protocol Category: Enterprise compliance_

#### Table of contents

1. [What is ILSP?](ilsp.md#what-is-ilsp)
2. [Technical information about ILSP](ilsp.md#tech-info-ilsp)
3. [ILSP Configuration](ilsp.md#ilsp-config)
4. [Setting up](ilsp.md#setting-up)
5. [Managing](ilsp.md#managing)
6. [Troubleshooting](ilsp.md#troubleshooting)

### What is ILSP?

The ILSP data forwarding protocol is for companies that have common monitoring centers dedicated to security issues and need to monitor vehicle positioning and need to share this data with a third party.

Using ILSP, partners can update their information with Navixy data such as vehicle data, positioning, etc. Users can connect with multiple companies and send information to the ILSP. streamlining fleet and security data.

### ILSP general technical information

The ILSP protocol utilizes the POST method to send JSON data over HTTP to the ILSP servers for further data processing.

Data sent to ILSP:

* Customer ID
* Transport Line ID
* License Plate
* Tracker Event and time
  * SOS, power lost, and GSM damp alarm
* Latitude
* Longitude
* Speed
* Heading
* Odometer
* Battery

### ILSP Configuration

#### Setting up

Required Parameters

* Login and Password
  * ILSP Login and Password
* Destination server address and port
  * Address:https://www.ilspservices.com.mx/
  * Port: 443

To set up data forwarding in ILSP protocol, open the device settings from the main menu by pressing the “Gear” icon on the bottom left of the screen.

Then, click the “Data forwarding” widget.

Click “Retranslators management”.

This will open a popup where you will input the required parameters by pressing the + button

For the ILSP protocol, input the following information:

\| Parameter | Explanation | | --- | --- | | Name | Enter a name to make this retranslator easily identifiable | | Protocol | Select the ILSP protocol from the dropdown | | Destination server address and port | \* Address: https://www.ilspservices.com.mx/\
\* Port: 443 |

A Retranslation management screen should look similar to the following, with ILSP login and password. Make sure the "Enabled" button is checked and click the "Save" button to complete the process.

![ILSP](https://www.navixy.com/wp-content/uploads/2022/10/image-8-600x111.png)

Next, the retranslator will need to be linked to the device on the ILSP side. To do so, select the “Link” ![link image](https://www.navixy.com/wp-content/uploads/2022/08/image-3.png)

button in the data forwarding widget. Select the retranslator to be connected, and click “Link” below.

Next, add information needed to identify the device on ILSP in the External ID field, either by clicking the pencil icon or the external ID field itself. This value should include the following from the ILSP side:

UserId|VehicleLicensePlate|RouteID

#### Managing

To edit or stop data being forwarded, please refer to the following steps:

To stop the data forwarding, click the “Trash” button.

Next, acknowledge the change on the popup.

To change retranslator settings such as name, login information, or enabled, click “Retranslators management.”

This will open the retranslator management window. Select the row to edit and either click the pencil in the top left, or double-click the row in question to allow editing. Save any changes.

![ILSP](https://www.navixy.com/wp-content/uploads/2022/10/image-9-600x100.png)

#### Troubleshooting

If data does not display on the 3rd party ILSP system, please verify:

* Username and password for ILSP are correctly entered
* URL was entered correctly
* Retranslator is enabled
* External ID information is correct
