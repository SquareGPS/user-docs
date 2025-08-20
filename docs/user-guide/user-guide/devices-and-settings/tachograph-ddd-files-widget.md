# Tachograph DDD files widget

The **DDD files widget** in Navixy is designed to manage the download and storage of DDD files, which are critical for monitoring driver compliance and rest through tachographs. These files are essential for ensuring that drivers adhere to regulations and help identify any irregularities in tachograph data.

#### What are DDD files?

DDD files store detailed information from tachographs about driver activities, including driving hours, rest periods, and potential compliance violations. The frequency of downloading and the retention period for these files are regulated by law. For instance, in European countries, DDD files are typically downloaded about every month from driver's cards and about every three months from the tachograph, with a mandatory storage period of one year.

## Initial setup

Before you can begin downloading DDD files, a few initial setup steps are required:

{% stepper %}
{% step %}
**Unload data from the company or driver card**

Connect a card reader to your computer and use it to unload data from the company or driver card.
{% endstep %}

{% step %}
**Enter the company number**

Enter the company number within the TachoAuthClient application. This application is necessary for downloading DDD files and can be obtained by contacting Navixy technical support.
{% endstep %}
{% endstepper %}

## Setting up DDD files download

{% stepper %}
{% step %}
**Enter the company card number**

In the DDD files widget, input the company card number (an internal document of the organization) and click **Save**. This step is crucial to ensure that all DDD files are correctly associated with your company.
{% endstep %}

{% step %}
**Specify Email addresses**

You can set up email notifications to receive DDD files by specifying up to five email addresses. Click the **+** button to add each email address, ensuring that key stakeholders are notified when files are available.
{% endstep %}
{% endstepper %}

## Downloading DDD files

{% stepper %}
{% step %}
**Manual download**

To manually download a DDD file, click the **Download** button next to the specific file you need. Please note that the download process can take between 5 to 10 minutes.
{% endstep %}

{% step %}
**Important considerations**

Ensure that the vehicle’s ignition is on during the download process. If the ignition is off, the download will fail, and you will need to restart the process.

The DDD files will be sent to the specified email addresses once the download is complete.
{% endstep %}
{% endstepper %}

The **DDD files widget** streamlines the process of managing tachograph data, ensuring compliance with regulations and providing valuable insights into driver behavior and vehicle usage.

{% hint style="warning" %}
Navixy only supports the download functionality of DDD files. We do not process them in any way and do not read any data from them.
{% endhint %}
