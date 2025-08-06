# Recurso Confiable

## Recurso Confiable—GPS tracking/data forwarding for enterprises

Recurso Confiable is a security and logistics software that monitors, gives visibility, and generates predictability on transport operations. Navixy created the Recurso Confiable data forwarding protocol to be used by other companies that also work with Recurso Confiable across multiple industries in Mexico, Colombia, the United States, and Central America.

_Protocol Category: Enterprise protocol_

#### Table of contents

1. [What is Recurso Confiable?](recurso-confiable.md#what-is-rc)
2. [Technical information about Recurso Confiable](recurso-confiable.md#tech-info-rc)
3. [Recurso Confiable Configuration](recurso-confiable.md#rc-config)
4. [Setting up](recurso-confiable.md#setting-up)
5. [Managing](recurso-confiable.md#managing)
6. [Troubleshooting](recurso-confiable.md#troubleshooting)

### What is Recurso Confiable?

With the Recurso Confiable protocol, enterprise partners can transfer GPS tracking data safely and reliably into a single location to optimize fleet management processes. This allows the client a way to work and communicate with other Recurso Confiable partners.

When developing this protocol, Navixy took into account the needs of large logistics and retail companies. Companies can streamline important fleet management and GPS tracking platform data and capabilities such as control systems, trip planning, tracking in real-time, predictive modeling reporting, geofence implementation and editing, route optimization, and more. Companies previously disconnected from one another on the Recurso Confiable network are now able to communicate efficiently and quickly.

### Recurso Confiable general technical information

The Recurso Confiable protocol utilizes SOAP to push XML data every 5 minutes over HTTP to Recurso Confiable.

Data that’s sent to Recurso Confiable:

* AVL Event Code
* License Plate
* Shipment ID
* Date
* Direction
* Latitude
* Longitude
* Altitude
* Speed
* Course
* Ignition
* Odometer
* CustomerID
* CustomerName
* Device ID

### Recurso Confiable Configuration

#### Setting up

Required Parameters

* Recurso Confiable Login and Password
* External ID
* Destination server address
  * [http://gps.rcontrol.com.mx/Tracking/wcf/RCService.svc](http://gps.rcontrol.com.mx/Tracking/wcf/RCService.svc)
* Destination server port
  * 80

To set up data forwarding in the Recurso Confiable protocol, open the device settings from the main menu by pressing the “Gear” icon on the bottom left of the screen

Then, click the “Data forwarding” widget.

Click “Protocols”.

This will open a popup where you will input the required parameters by pressing the + button.

For the Recurso Confiable protocol, input the following information:

\| Parameter | Explanation | | --- | --- | | Name | Enter a name to make this retranslator easily identifiable | | Protocol and Login | Select the Recurso Confiable protocol from the dropdown;\
\
Use Recurso Confiable Login and Password | | Destination server address and port | Address: [http://gps.rcontrol.com.mx/Tracking/wcf/RCService.svc](http://gps.rcontrol.com.mx/Tracking/wcf/RCService.svc) | Port: 80 |

A Retranslation management screen should look similar to the following, with Recurso Confiable login and password. Make sure the "Enabled" button is checked and click the "Save" button to complete the process.

![Recurso Confiable](https://www.navixy.com/wp-content/uploads/2022/10/pasted-image-0-1-1-600x120.png)

Next, the retranslator will need to be linked to the device on the Recurso Confiable side. To do so, select the “Link” ![link image](https://www.navixy.com/wp-content/uploads/2022/08/image-3.png)

button in the data forwarding widget. Select the retranslator to be connected, and click “Link” below.

Next, add information needed to identify the device on Recurso Confiable in the External ID field, either by clicking the pencil icon or the external ID field itself. This value should include the following from the Recurso Confiable side, where only the License Plate is mandatory:

License Plate

Route ID

Company ID

Company Name

The format for the External ID field will be separated by a pipe. For example:

ABC123|1|123|John

If only the License Plate is available, the External ID can be entered by itself:

ABC123

Or if any other information is missing, be sure to include the pipes, for example:

ABC123||123|

Select “Save” once completed.

#### Managing

To edit or stop data being forwarded, please refer to the following steps:

Select the “Pencil” icon or click in the associated box to edit the external ID used to point to the device on the 3rd party system.

To stop the data forwarding, click the “Trash” button.

Next, acknowledge the change on the popup.

To change retranslator settings such as name, login information, or enabled, click “Retranslators management.”

This will open the retranslator management window. Select the row to edit and either click the pencil in the top left, or double-click the row in question to allow editing. Save any changes.

![Recurso Confiable](https://www.navixy.com/wp-content/uploads/2022/10/pasted-image-0-3-600x107.png)

#### Troubleshooting

If data does not display on the 3rd party Recurso Confiable system, please verify:

* Username and password for Recurso Confiable are correctly entered
* URL was entered correctly
* Retranslator is enabled
* External ID matches the related Recurso Confiable information
