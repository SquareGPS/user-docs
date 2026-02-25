# Quick start guide

This guide will help you quickly set up your first data flow in IoT Logic and begin processing your telematics data.

## Prerequisites

Before proceeding with creating your first flow, ensure you have:

* An **Owner** role in your Navixy account
* Activated devices in your account
* Understanding of what data sources you want to process

{% hint style="info" %}
IoT Logic workspace is available only to account **Owners** and is not displayed for regular **Users**. For details on user roles, see [Users and Roles](../users-and-roles/).
{% endhint %}

## Flow configuration

Take a look at a short video that showcases the process of creating a new flow with data attribute calculations and adding custom attributes to devices on the platform:

{% embed url="https://files.gitbook.com/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F446mKak1zDrGv70ahuYZ%2Fuploads%2FGAVD9gNxaRYpHDSAlOmf%2FIot%20Logic%20Demo%20Screencast.mp4?alt=media&token=94fd4cf6-bd45-4953-9263-52863288d9b9" %}
Process of creating a new flow with data attribute calculations and adding custom attributes to devices on the platform
{% endembed %}

Now, let’s break down the flow configuration process step by step.

{% stepper %}
{% step %}
#### Step 1: Access IoT Logic workspace

1. Log into your Navixy account
2. Click your profile icon in the top-left corner of the screen to access **Account settings**
3. Select **IoT Logic** in the settings sidebar

The IoT Logic workspace appears with three main sections:

* **Flow settings bar** - Contains controls for managing flows
* **Nodes pane** - Lists available nodes for building your flow
* **Canvas** - The main workspace where you design your flow

For details on the workspace, see [Workspace and default flow](workspace-and-default-flow.md).
{% endstep %}

{% step %}
#### Step 2: Create a new flow

1. Click the **New flow** button in the flow settings bar
2. In the **New flow** dialog:

* Enter a descriptive name for your flow (e.g., "Fleet Telemetry Processing")
* Add a brief description explaining the flow's purpose
* Ensure the **Flow enabled** toggle is switched ON

3. Click **Save** to create the flow

For additional information on flow configuration, see [Flow management -> Creating a new flow](flow-management/#creating-a-new-flow).

{% hint style="info" %}
Disabled flows don't process any data. When a flow is disabled, devices in that flow will not transmit data to any destination, including the Navixy platform.
{% endhint %}
{% endstep %}

{% step %}
#### Step 3: Configure a Data Source node

1. From the **Nodes** pane, drag a **Data Source** node onto the canvas
2. Hover your mouse over the node to display quick actions, or double-click the node to open its configuration panel
3. Configure the following settings:

* **Node name** - Enter a descriptive name, specifying the sent data origin (e.g., _Staff vehicles_)
* **Sources** - Select devices whose readings you want to send to this flow.

4. Click **Apply changes** to apply the configuration

For details on the node configuration, see [Data Source node](flow-management/data-source-node.md).
{% endstep %}

{% step %}
#### Step 4: Add data enrichment (Optional)

1. Drag an **Initiate Attribute** node onto the canvas
2. Hover your mouse over the node to display quick actions, or double-click the node to open its configuration panel
3. Add a descriptive **Node name** to specify its purpose and calculations it makes (e.g. _Temperature °F to °C_)
4. Define your attribute:
   1. **Attribute name** - A clear, descriptive name (e.g., "speed\_mph")
   2. **Formula** - The calculation expression (e.g., `speed/1.609` to convert km/h to mph)\
      :bulb:**Note**: Short syntax is the primary option. Use full syntax when you need historical/indexed values or explicit validity checks (e.g., `value('speed', 1, 'valid')`).\
      Attribute names [can be autofilled](flow-management/initiate-attribute-node/managing-attributes.md#autofill-attribute-names) to avoid typos.
5. Add additional attributes if needed by clicking **Add Attribute**. To remove an attribute, click the delete icon next to it.
6. Click **Apply changes** to apply the configuration
7. Create a connection:
   1. Click the output connector of the **Data Source** node
   2. Drag the transition to the input connector of the **Initiate Attribute** node

For details on node configuration, see [Initiate Attribute node](flow-management/initiate-attribute-node/).

For details on actions with attributes, see [Managing attributes](flow-management/initiate-attribute-node/managing-attributes.md).

For sample calculation formulas, see [Calculation examples](flow-management/initiate-attribute-node/calculation-examples.md).
{% endstep %}

{% step %}
#### Step 5: Configure data output

1. Drag an **Output Endpoint** node onto the canvas
2. Hover your mouse over the node to display quick actions, or double-click the node to open its configuration panel
3. Select endpoint **Mode**:

* **Default endpoint** - a standard output for sending flow data to the Navixy platform. It is pre-configured and cannot be edited.
* **MQTT endpoint** - a custom output for sending flow data to 3rd-party destinations over MQTT.

4. Configure the following settings:
   1. **Endpoint name** - enter a descriptive name for this output
   2. **MQTT Version** - select **3.1.1** or **5.0**
   3. **IP** - enter the destination IP address
   4. **Port** - specify the port number (commonly _1883_ for MQTT, _8883_ for MQTT over TLS)
   5. **Topic** - specify the topic used for data transmission
   6. **QoS** - select **0**, **1**, or **2**
   7. **MQTT Client ID** - enter the client ID expected by the receiving side
   8. (optional) **Use Authentication** - toggle on, then enter **MQTT username** and **MQTT password**
   9. (optional) **Use SSL** - toggle on for TLS
5. Click **Apply changes** to apply the configuration
6. Connect your other nodes to this output node in needed order to finalize the flow structure

{% hint style="info" %}
Each flow should include a **Default endpoint** node to ensure data is sent to the platform. Without this connection, device data won't be visible in the Navixy interface.
{% endhint %}

For details on node configuration, see [Output Endpoint node](flow-management/output-endpoint-node.md).
{% endstep %}

{% step %}
#### Step 6: Save and activate your flow

1. Verify all nodes are properly connected in your flow
2. Click the **Save flow** button in the **Nodes** pane

{% hint style="success" %}
Your flow is now active and processing data in real-time!
{% endhint %}
{% endstep %}
{% endstepper %}

## Flow validation

To confirm your flow is working correctly, use the **Data Stream Analyzer** tool:

1. Click the **Data analyzer** button in the flow settings bar
2. Select the devices you want to monitor from the dropdown list
3. Observe the incoming data attributes and their values
4. Use filtering options to focus on specific parameters
5. Verify that any calculated attributes show the correct values

For details on using the tool, see [Data Stream Analyzer](data-stream-analyzer.md).

{% hint style="success" %}
Congratulations! Your first IoT Logic data flow is up and running.
{% endhint %}

## Next steps

Now that you've created your first IoT Logic flow, you can:

* [Adapt this quick start example](quick-start-guide.md#adapting-this-example) to your business needs
* Create more complex data transformations with multiple [Initiate Attribute nodes](flow-management/initiate-attribute-node/)
* Set up additional [output destinations](flow-management/output-endpoint-node.md) for your data that can become reusable profiles for consistent configurations
* [Manage already created flows](flow-management/) to adjust data processing to any changes you face
* [Design advanced flows](flow-management/flow-configuration-example.md) for specific business scenarios using different node combinations and configurations

### Adapting this example

This example can be adapted to various industry use cases by modifying:

* **Device selection**: Choose devices relevant to your specific assets
* **Unit conversions**: Adjust formulas based on your standard measurement units
* **Calculated metrics**: Create industry-specific indicators based on your business needs
* **Output configuration**: Connect to your specific analysis platform or database

The foundational pattern of collecting, transforming, and forwarding remains consistent across industries, making this a versatile template for IoT data processing.

## API access

IoT Logic functionality can also be accessed programmatically through the Navixy API. This allows developers to automate flow creation, management, and monitoring.

{% hint style="info" %}
For security reasons, API access requires appropriate permissions. Contact your account administrator to ensure you have the necessary access rights.
{% endhint %}

For complete API documentation, parameters, request/response formats, and code examples, refer to the [Navixy IoT Logic API documentation](https://app.gitbook.com/o/YVLWhgAwCZPoU5vlRsCs/s/tx3J5BxnWyPV0nP2xr0z/).

## Frequently asked questions

#### What happens to devices not assigned to a custom flow?

Devices not explicitly assigned to any custom flow are automatically handled by the default flow, which sends their data directly to the Navixy platform.

#### Can I use the same device in multiple flows?

No, each device can only be assigned to one flow at a time. When added to a custom flow, a device is automatically removed from the default flow to prevent duplicate data processing.

#### Will my flow continue working if I log out?

Yes, once activated, flows operate independently of your user session. As long as the flow is enabled, it will process data even when you're not logged in.

#### How do I know if my flow is working correctly?

Use the Data Stream Analyzer to monitor real-time data transmission. This tool shows both raw device data and calculated attributes, allowing you to verify that your transformations are working as expected.

#### What happens if I disable a flow?

When you disable a flow, devices assigned to that flow will not transmit data to any destination, including the Navixy platform. The devices will appear offline in the Navixy interface until you re-enable the flow.
