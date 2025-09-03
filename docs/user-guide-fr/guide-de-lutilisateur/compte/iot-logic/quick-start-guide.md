# Quick start guide

This guide will help you quickly set up your first data flow in IoT Logic and begin processing your telematics data.

### Prerequisites

Before proceeding with creating your first flow, ensure you have:

* An **Owner** role in your Navixy account
* Activated devices in your account
* Understanding of what data sources you want to process

{% hint style="info" %}
IoT Logic workspace is available only to account **Owners** and is not displayed for regular **Users**. For details on user roles, see Users and Roles.
{% endhint %}

### Flow configuration

Take a look at a short video that showcases the process of creating a new flow with data attribute calculations and adding custom attributes to devices on the platform:

{% embed url="https://files.gitbook.com/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F446mKak1zDrGv70ahuYZ%2Fuploads%2FGAVD9gNxaRYpHDSAlOmf%2FIot%20Logic%20Demo%20Screencast.mp4?alt=media&token=94fd4cf6-bd45-4953-9263-52863288d9b9" %}
Process of creating a new flow with data attribute calculations and adding custom attributes to devices on the platform
{% endembed %}

Now, let’s break down the flow configuration process step by step.

#### Step 1: Access IoT Logic workspace

1. Log into your Navixy account
2. Click your profile icon in the top-left corner of the screen to access **Account settings**
3. Select **IoT Logic** in the settings sidebar

The IoT Logic workspace appears with three main sections:

* **Flow settings bar** - Contains controls for managing flows
* **Nodes pane** - Lists available nodes for building your flow
* **Canvas** - The main workspace where you design your flow

For details on the workspace, see Workspace and default flow.

#### Step 2: Create a new flow

1. Click the **New flow** button in the flow settings bar
2. In the **New flow** dialog:

* Enter a descriptive name for your flow (e.g., "Fleet Telemetry Processing")
* Add a brief description explaining the flow's purpose
* Ensure the **Flow enabled** toggle is switched ON

3. Click **Save** to create the flow

For additional information on flow configuration, see Flow management -> Creating a new flow.

{% hint style="info" %}
Disabled flows don't process any data. When a flow is disabled, devices in that flow will not transmit data to any destination, including the Navixy platform.
{% endhint %}

#### Step 3: Configure a Data Source node

1. From the **Nodes** pane, drag a **Data Source** node onto the canvas
2. Hover your mouse over the node to display quick actions, or double-click the node to open its configuration panel
3. Configure the following settings:

* **Node name** - Enter a descriptive name, specifying the sent data origin (e.g., _Staff vehicles_)
* **Sources** - Select devices whose readings you want to send to this flow. You can filter your available devices by data **Manufacturer** and device **Model**.

4. Click **Save** to apply the configuration

For details on the node configuration, see Data Source node.

#### Step 4: Add data enrichment (Optional)

1. Drag an **Initiate Attribute** node onto the canvas
2. Hover your mouse over the node to display quick actions, or double-click the node to open its configuration panel
3. Add a descriptive **Node name** to specify its purpose and calculations it makes (e.g. _Temperature °F to °C_)
4. Define your attribute:

* **Attribute name** - A clear, descriptive name (e.g., "speed\_mph")
* **Formula** - The calculation expression (e.g., `value('speed')/1.609` to convert km/h to mph)\
  **Note**. Attribute names can be autofilled to ensure correct naming
* **Generation time** - When the data entry was created on the device (defaults to `now()`)
* **Server time** - When the data was received by the server (defaults to `now()`)

5. Add additional attributes if needed by clicking **Add attribute**

{% hint style="danger" %}
The **Reset form** button discards all created attributes within a node. If you want to remove a certain attribute, click the three dots on the right of the attribute row and select **Delete**.
{% endhint %}

7. Click **Save** to apply the configuration
8. Create a connection:

* Click the output connector of the **Data Source** node
* Drag the transition to the input connector of the **Initiate Attribute** node

For details on node configuration, see Initiate Attribute node.

For details on actions with attributes, see Managing attributes.

For sample calculation formulas, see Calculation examples.

#### Step 5: Configure data output

1. Drag an **Output Endpoint** node onto the canvas
2. Hover your mouse over the node to display quick actions, or double-click the node to open its configuration panel
3. Select **Endpoint type**:

* **Navixy endpoint** - default endpoint for sending processed data to Navixy platform. It is pre-configured and does not allow any changes
* **MQTT endpoint** - endpoint for sending data to 3rd-party destinations, using MQTT as a transport protocol. Requires manual configuration described in further steps

{% hint style="info" %}
Endpoints created within the account are available as **Presets**. You can select an already existing configuration instead of setting it up from scratch. **Navixy Output Endpoint** is always available as a preset.
{% endhint %}

4. Configure the following settings:

* **Endpoint name** - Enter a descriptive name to specify the destination where the data is sent
* **Protocol** - Select the data protocol (only “Navixy Generic Protocol (JSON)" is available at the moment)
* **IP/Domain** - Enter the destination address
* **Port** - Specify the port number (default: 1883 for standard MQTT, 8883 for SSL)
* (optional) **Enable SSL** - Toggle ON for secure connections
* **MQTT Version** - Select the appropriate version (**3.1.1** or 5.0)
* **Client ID** - Enter the identifier for your client to ensure the data is accepted by the receiving party
* (optional) **Topics** - Specify the MQTT topics for data transmission
* **QoS** - Select the Quality of Service level to determine the logic of data transmission (**0**, **1**, or **2**)

5. If authentication is required on the receiving side, toggle **MQTT Authentication** ON\
   The appearing fields are pre-filled automatically with your platform account credentials

{% hint style="danger" %}
The **Reset form** button discards all created attributes within a node. If you want to remove a certain attribute, click the three dots on the right of the attribute row and select **Delete**.
{% endhint %}

6. Click **Create** to apply the configuration
7. Connect your other nodes to this output node in needed order to finalize the flow structure

{% hint style="info" %}
Each flow should include a **Default Endpoint** node to ensure data is sent to the platform. Without this connection, device data won't be visible in the Navixy interface.
{% endhint %}

For details on node configuration, see Output Endpoint node.

#### Step 6: Save and activate your flow

1. Verify all nodes are properly connected in your flow
2. Click the **Save flow** button in the **Nodes** pane
3. Your flow is now active and processing data in real-time

### Flow validation

To confirm your flow is working correctly, use the **Data Stream Analyzer** tool:

1. Click the **Data analyzer** button in the flow settings bar
2. Select the devices you want to monitor from the dropdown list
3. Observe the incoming data attributes and their values
4. Use filtering options to focus on specific parameters
5. Verify that any calculated attributes show the correct values

For details on using the tool, see Data Stream Analyzer.

{% hint style="success" %}
Congratulations! Your first IoT Logic data flow is up and running.
{% endhint %}

### Next steps

Now that you've created your first IoT Logic flow, you can:

* Adapt this quick start example to your business needs
* Create more complex data transformations with multiple Initiate Attribute nodes
* Set up additional output destinations for your data that can become reusable profiles for consistent configurations
* Manage already created flows to adjust data processing to any changes you face
* Design advanced flows for specific business scenarios using different node combinations and configurations

#### Adapting this example

This example can be adapted to various industry use cases by modifying:

* **Device selection**: Choose devices relevant to your specific assets
* **Unit conversions**: Adjust formulas based on your standard measurement units
* **Calculated metrics**: Create industry-specific indicators based on your business needs
* **Output configuration**: Connect to your specific analysis platform or database

The foundational pattern of collecting, transforming, and forwarding remains consistent across industries, making this a versatile template for IoT data processing.

### API access

IoT Logic functionality can also be accessed programmatically through the Navixy API. This allows developers to automate flow creation, management, and monitoring.

{% hint style="info" %}
For security reasons, API access requires appropriate permissions. Contact your account administrator to ensure you have the necessary access rights.
{% endhint %}

For complete API documentation, parameters, request/response formats, and code examples, refer to the [Navixy IoT Logic API documentation](https://app.gitbook.com/o/YVLWhgAwCZPoU5vlRsCs/s/tx3J5BxnWyPV0nP2xr0z/).

### Frequently asked questions

**What happens to devices not assigned to a custom flow?**

Devices not explicitly assigned to any custom flow are automatically handled by the default flow, which sends their data directly to the Navixy platform.

**Can I use the same device in multiple flows?**

No, each device can only be assigned to one flow at a time. When added to a custom flow, a device is automatically removed from the default flow to prevent duplicate data processing.

**Will my flow continue working if I log out?**

Yes, once activated, flows operate independently of your user session. As long as the flow is enabled, it will process data even when you're not logged in.

**How do I know if my flow is working correctly?**

Use the Data Stream Analyzer to monitor real-time data transmission. This tool shows both raw device data and calculated attributes, allowing you to verify that your transformations are working as expected.

**What happens if I disable a flow?**

When you disable a flow, devices assigned to that flow will not transmit data to any destination, including the Navixy platform. The devices will appear offline in the Navixy interface until you re-enable the flow.
