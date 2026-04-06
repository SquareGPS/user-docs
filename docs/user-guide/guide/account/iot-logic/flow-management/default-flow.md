---
description: Learn how the default flow works in IoT Logic, what devices it covers, and how it relates to your custom flows.
---

# Default flow

<figure><img src="https://2096203889-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F446mKak1zDrGv70ahuYZ%2Fuploads%2FCb4Z86p71sMSUFYlrnGx%2Fimage.png?alt=media&#x26;token=bf13b66d-8eb3-4b6b-b10d-75a3c6b940eb" alt=""><figcaption></figcaption></figure>

Navixy offers a pre-configured data flow that includes all devices connected to the account and sends their data directly to the platform. This flow is available in every account and cannot be edited. It consists of two basic nodes: **Default Input** and **Default Output Endpoint**.

The default flow serves as a foundational data transmission path in the Navixy system. Its primary purpose is to ensure that data from devices not included in any custom flow is not lost and is transmitted to the default destination - the Navixy platform.

## Key characteristics of the default flow

* Present in every Navixy account regardless of whether IoT Logic is actively used
* Cannot be deleted, edited, or modified in any way
* Automatically includes all devices not assigned to custom flows
* Provides direct data transmission without transformations
* Maintains system stability by protecting the default data transmission path

When you create custom flows and assign specific data sources to them, those devices are automatically removed from the default flow to prevent data duplication. This ensures each device's data is processed through exactly one flow at any given time.

## Default input

The **Default Input** node serves as the universal data collector for your account. It automatically receives data from all active devices that are not explicitly assigned to custom flows.

This node functions as a dynamic container that adjusts its scope based on your custom flow configurations. As you create new custom flows and assign devices to them, those devices are removed from the default input's scope. Similarly, if you delete a custom flow, any devices previously managed by that flow return to the default input's scope.

{% hint style="info" %}
**Note for editors:** The statement above about devices being removed from the default input's scope may be inaccurate with multi-flow support. Confirm the behavior and rewrite in Stage 2.
{% endhint %}

This dynamic behavior ensures complete data coverage across your account while preventing duplicate data processing.

## Default Output Endpoint

{% columns %}
{% column %}
The **Default Output Endpoint** node provides a pre-configured destination for sending device data to the Navixy platform. This node is pre-configured with optimal settings for direct transmission to Navixy's servers.
{% endcolumn %}

{% column %}

<div align="right"><figure><img src="https://2096203889-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F446mKak1zDrGv70ahuYZ%2Fuploads%2Fgit-blob-e565ed3421fbe577455090d76ccc1e184c548b09%2Fimage-20250403-151042%20(3).png?alt=media" alt="Navixy Default output endpoint node"><figcaption></figcaption></figure></div>
{% endcolumn %}
{% endcolumns %}

The endpoint ensures that all data collected through the default flow is properly formatted and transmitted to the Navixy platform, enabling full visibility of your devices in the main Navixy interface.

{% hint style="info" %}
The **Default Output Endpoint** node is also available for use in custom flows. Each custom flow should maintain connections to this output node to ensure device data is sent to the platform, enabling monitoring capabilities using Navixy tools. If the Navixy output is removed from a custom flow, data from the devices involved in that flow will no longer reach the platform.
{% endhint %}

## Using Data Stream Analyzer with the default flow

**Data Stream Analyzer** is flow-responsive, which means that it monitors only the data within the flow where it was opened. Using the tool within the default flow allows you to troubleshoot and monitor data transmission for all the devices in this account that are not assigned to any custom flows. In case there are no custom flows in the account at all, you can monitor every device in the account through the default flow. This functionality is particularly useful for diagnosing connectivity or data issues with devices that are not assigned to any custom flows.

To access this feature, select the default flow and click <img src="https://2096203889-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F446mKak1zDrGv70ahuYZ%2Fuploads%2Fgit-blob-ede03d06378ad314235498a6559967083ffcd035%2Fimage-20250403-151357%20(3).png?alt=media" alt="image-20250403-151357.png" data-size="line"> button in the top menu.

For detailed instructions on using the tool, refer to [Data Stream Analyzer](../data-stream-analyzer.md).

{% hint style="info" %}
**Note for editors:** Point 2 in the "Understanding flow relationships" section below states each device can only belong to one flow at a time. Rewrite the entire section in Stage 2 once multi-flow device behavior is confirmed.
{% endhint %}

## Understanding flow relationships

The relationship between the default flow and custom flows follows these principles:

1. **Every device in your account must have a path to transmit data** - The IoT Logic system ensures that all devices connected to your account always have a defined route for their data. This guarantees no device data is ever lost due to routing configuration issues, maintaining complete visibility of your device fleet.
2. **Each device can only be assigned to one flow at a time** - To prevent duplicate data processing and ensure consistent handling, devices are exclusively assigned to a single flow. This creates clear data pathways and eliminates potential conflicts between different processing configurations.
3. **The default flow automatically handles any device not explicitly assigned elsewhere** - The default flow serves as a "catch-all" mechanism that automatically manages all devices not specifically configured in custom flows. This ensures that newly added devices or devices removed from custom flows always have an immediate path for data transmission.
4. **Custom flows take precedence over the default flow for device assignment** - When you create a custom flow and include specific devices, those devices are automatically removed from the default flow. This prioritization system allows you to implement specialized processing for selected devices while maintaining the default handling for others.

This systematic approach ensures complete data coverage while allowing for customized data processing where needed.
