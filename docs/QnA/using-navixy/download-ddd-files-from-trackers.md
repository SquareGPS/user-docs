# Download DDD files from trackers

### Question

How to download DDD files from trackers using Navixy?

### Answer

DDD files are tachograph data files used in commercial transport, mainly in the EU.

DDD is a standard binary format for downloading data from a digital tachograph.

Using Navixy, files can be requested for sending to a list of emails specified in the DDD file recipients portlet.

![](<../.gitbook/assets/Unknown image (122)>)

It’s important to understand that the platform doesn't process DDD files in any way (no reading or changing the data). The platform just sends DDD files via email to the list of recipients specified in the user account.

This is the only available functionality related to DDD files on the platform.

To download a DDD file, the following conditions must be met:

* Vehicle ignition must be ON.
* The company card is inserted into the card reader.
* An EU, MENA, or US server is set in the Tacho Auth Client app configs.
* The Tacho Auth Client application must be running on the same computer where the card reader is connected. The app status should be Connected.

The procedure can take up to 15 minutes.

If you don’t have the Tacho Auth Client application, please feel free to reach out to our support team.

Once you receive the Tacho Auth Client application, you need to unpack the ZIP archive on the same PC where the card reader with the company card is connected. Also, you need to install Java (17+) before running the app. Once you start the application, a log file is created. The log file may be helpful if any issue occurs with the app. In case you face an issue related to the application, please feel free to reach out to our support team.

Here are the supported device models for DDD file downloading:

* Galileosky v5.0
* BCE FM Tacho
* BCE FMS500 Tacho
* Teltonika FMB630
* Teltonika FMB640
* Teltonika FMC640
* Teltonika FM6300
* Teltonika FM6320

In case you use Teltonika, make sure that WEB Tacho Settings Status is disabled as on the following screenshot:

![](<../.gitbook/assets/Unknown image (123)>)

If the customer has scheduled DDD file downloads, they need to insert the card each time a DDD file request is made to the tachograph.

Before starting the application, open the `config.properties` file in a text editor. Once opened, make sure that the `server.hostname` parameter points to the platform tracking address.

![](<../.gitbook/assets/Unknown image (124)>)

A tracking server address can be clarified on the device list page. Select a device, and you will find a server address corresponding to your instance (EU, US, MENA).

Once the server address is set (it can be a domain or an IP), you can start the application.

In case you use Windows, right click on the `start.bat` file and select “Run as administrator”:

![](<../.gitbook/assets/Unknown image (125)>)

Once you have successfully run the application and all conditions above are met, you can proceed to the user interface and request DDD files to be sent via email to the recipient list.

### Links

* [Tachograph DDD files widget](https://www.navixy.com/docs/user/guide/devices-and-settings/tachograph-ddd-files-widget)
* [Device list](https://www.navixy.com/devices/)
