# Displaying new calculated attributes on the Navixy platform

New attributes calculated within **Initiate Attribute** node can be monitored just like the actual data attributes coming from devices in **Data Stream Analyzer (DSA)** and the **Tracking** module. While DSA shows them natively, to display the new attributes in the **Tracking** module, you need to add them as custom attributes to the devices first.

After creating calculated attributes in the **Initiate Attribute** node, you can make further use of them on the Navixy platform in two main ways:

* Through the **Data Stream Analyzer (DSA)** for troubleshooting
* By adding them as **custom attributes** to your devices for ongoing tracking

{% hint style="info" %}
To produce actual values, calculated attributes should meet the following prerequisites:

* The flow containing them should be saved with an up-to-date configuration of the **Initiate Attribute** node.
* The **Initiate Attribute** node must be connected to at least 1 **Output Endpoint** node.
* The device must be actively sending data through the flow.
{% endhint %}

### Monitoring calculated attributes in Data Stream Analyzer

All new data attributes calculated within a flow appear automatically in Data Stream Analyzer (DSA) as soon as actual data is received and processed through the flow. This allows you to verify calculations and troubleshoot issues in real time.

To monitor calculated attributes in DSA:

1. Create an attribute in an **Initiate Attribute** node.\
   For this example, let’s take a simple formula to convert temperature from C° to F° and save it to an attribute with the name _temperatureF_.
2. Make sure to connect this **Initiate Attribute** to an **Output Endpoint** node.
3. Click ![DATA\_ANALYZER.png](https://2096203889-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F446mKak1zDrGv70ahuYZ%2Fuploads%2Fgit-blob-8575cac51055c96e5503881b5bd8a7c5ebdfeff6%2FDATA_ANALYZER.png?alt=media) to open DSA.
4. Select a device that sends data to the **Initiate Attribute** node containing the attribute of interest from the **Devices** list.
5. Find the attribute in the table and monitor its values. For our example, it should look like this:

<figure><img src="https://2096203889-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F446mKak1zDrGv70ahuYZ%2Fuploads%2Fgit-blob-86841f05f2a29801a821ee015f965168f8ed7e23%2Fcalculated-attribute-in-DSA.webp?alt=media" alt="Newly created attribute temperatureF in the Data Stream Analyzer table"><figcaption></figcaption></figure>

{% hint style="info" %}
If your calculated attribute doesn't appear in DSA, verify that:

* The flow is enabled and properly saved
* The device is sending data (check for other attributes updating)
* The **Initiate Attribute** node's connections are correct
* The attribute name is spelled correctly in the node configuration
{% endhint %}

For more details on troubleshooting with real-time data, see Data Stream Analyzer.

### Adding custom attributes to objects on the Navixy platform

New calculated data attributes from IoT Logic flows can be used as virtual sensors for actual devices in your account and displayed on Object widget and Object list. This enables you to monitor aggregated metrics along with actual device readings in one place, which significantly expands your Tracking possibilities.

To make calculated attributes visible in the Tracking module alongside regular device data, you need to add them as virtual sensors to your devices. This allows you to:

* Monitor calculated metrics in the Object widget
* Add important calculations to the Object list for quick access
* Include calculated values in reports
* Create rules and notifications based on calculated values

#### Creating a custom attribute for a device

{% hint style="info" %}
A custom sensor must be added individually to each device. To add the same attribute to multiple devices, repeat these steps for each of them.
{% endhint %}

![](https://2096203889-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F446mKak1zDrGv70ahuYZ%2Fuploads%2Fgit-blob-d12111313bd783c68217f4e9c6fbffc8f934d3c8%2FInitiate-attribute-config.png?alt=media)

1. Go to **Devices and Settings** menu in the left sidebar.
2. Select the device you want to add a new sensor to.
3. Click <img src="https://2096203889-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F446mKak1zDrGv70ahuYZ%2Fuploads%2Fgit-blob-8162eb61f85ccbbb68c97e0a17a48eef5e8b574b%2Fimage-20250422-143344.png?alt=media" alt="image-20250422-143344.png" data-size="line"> In **Sensors and buttons** section, then select one of the options:
   1. **Measurement/IoT Logic sensor** - for numeric attributes only, like speed, temperature, etc.
   2. **Virtual/IoT Logic sensor** - for any other non-numeric attribute values.
4. Fill in the following fields in the **Main** tab:
   1. **Label**\
      Enter a name for your sensor. It will be displayed in **Object widget**. The label can be the same as the attribute name in IoT Logic.
   2. **Parameter**\
      Find and select the needed custom attribute from the list of available parameters. IoT Logic attributes are visually separated from the standard Navixy list of parameters by adding “IoT: {attribute}“ prefix (Like “CAN:” or “OBD:”)
   3. **Sensor type**\
      Find and select the appropriate type according to the nature of the attribute: **Fuel**, **Temperature**, etc. You can use **Custom** if there’s no fitting type for your attribute.
   4. **Units**\
      Select the appropriate measurement units according to the nature of your attribute. The options in this list vary depending on your selected **Sensor type**. You can use **Custom** if there’s no fitting unit for your attribute.
5. (Optional) Go to the **Calibration** tab and set up calibration if needed.\
   For instruction on this tab’s setting, see Calibration.
6. Click **Save** to complete the configuration process.

{% hint style="success" %}
After saving, the new custom parameter appears automatically in the **Sensor readings** data block of **Object widget**. For example, we added a custom **TempDelta** parameter:\
![image-20250702-132535.png](https://2096203889-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F446mKak1zDrGv70ahuYZ%2Fuploads%2Fgit-blob-5ec1c55178fb7b01a02117f473fd9a3e8a847efe%2Fimage-20250702-132535.png?alt=media)
{% endhint %}

#### Adding a custom attribute to Object list

**Object widget** offers a **Favorites** mechanism that allows displaying a selection of data block entries in the **Object list**, right under an object’s label. It also applies to custom parameters from the **Sensor readings** data block.

To directly display your calculated attributes in the **Object list**:

1. Open the **Object widget** containing your custom attribute.
2. Find your custom attribute in the **Sensor readings** data block.
3. Click the star icon next to the attribute to add it to **Favorites**.
4. The attribute will now appear in the **Object list** under the object name.

For instructions on how to display a parameter in **Object list**, see Object widget - Favorites.
