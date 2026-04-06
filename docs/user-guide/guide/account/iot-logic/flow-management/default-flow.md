---
description: Learn how the default flow works in IoT Logic, what devices it covers, and how it relates to your custom flows.
---

# Default flow

<figure><img src="https://2096203889-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F446mKak1zDrGv70ahuYZ%2Fuploads%2FCb4Z86p71sMSUFYlrnGx%2Fimage.png?alt=media&#x26;token=bf13b66d-8eb3-4b6b-b10d-75a3c6b940eb" alt=""><figcaption></figcaption></figure>

Navixy offers a pre-configured data flow that includes all devices connected to the account and sends their data directly to the platform. This flow is available in every account and cannot be edited. It consists of two basic nodes: **Default Input** and **Default Output Endpoint**.

The default flow serves as a foundational data transmission path in the Navixy system. Its primary purpose is to ensure that all device data reaches the Navixy platform, regardless of whether devices are also assigned to custom flows.

## Key characteristics of the default flow

* Present in every Navixy account regardless of whether IoT Logic is actively used
* Cannot be deleted, edited, or modified in any way
* Processes all devices in the account, including those assigned to custom flows
* Provides direct data transmission without transformations
* Maintains system stability by protecting the default data transmission path

## Default input

The **Default Input** node serves as the universal data collector for your account. It automatically receives data from all active devices that are not explicitly assigned to custom flows.

The default flow receives data from all devices, including those assigned to custom flows. Assigning a device to a custom flow does not affect its membership in the default flow.

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

**Data Stream Analyzer** is flow-responsive, which means that it monitors only the data within the flow where it was opened. Using the tool within the default flow allows you to troubleshoot and monitor data transmission for all devices in the account, since the default flow processes every device. This functionality is particularly useful for diagnosing connectivity or data issues across your fleet.

To access this feature, go to the IoT Logic start page, click the default flow name in the **Created flows** table to open it on the canvas, then click the **Data Analyzer** tab at the top of the canvas.

For detailed instructions on using the tool, refer to [Data Stream Analyzer](../data-stream-analyzer.md).

## Understanding flow relationships

The relationship between the default flow and custom flows follows these principles:

1. **Every device in your account must have a path to transmit data** - The IoT Logic system ensures that all devices connected to your account always have a defined route for their data. This guarantees no device data is ever lost due to routing configuration issues, maintaining complete visibility of your device fleet.
2. **A device can belong to multiple flows at the same time** - All flows that include the device process its data simultaneously, and results are merged to avoid data loss. There are no constraints on how many flows a device can belong to.
3. **The default flow processes all devices** - The default flow receives data from every device in your account, including those assigned to custom flows. Assigning a device to a custom flow does not remove it from the default flow.

This approach ensures complete data coverage while allowing for customized data processing where needed.
