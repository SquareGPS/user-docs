# Action node

### Technical overview and capabilities

{% columns %}
{% column %}
**Action** nodes in IoT Logic enable automated device control by executing specific commands when triggered by incoming data flows. These nodes transform passive fleet monitoring into active automation systems, performing critical operations like output switching and GPRS command transmission.
{% endcolumn %}

{% column %}
<figure><img src="https://2096203889-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F446mKak1zDrGv70ahuYZ%2Fuploads%2Fgit-blob-62eee42a7c87bfb2f3aef6e4291ae244ae441f35%2Fimage.png?alt=media" alt=""><figcaption></figcaption></figure>
{% endcolumn %}
{% endcolumns %}

While Action nodes can receive data from any node type, they are most commonly connected to Logic nodes that evaluate conditions and trigger actions only when specific criteria are met, such as temperature thresholds, unauthorized movement, or harsh driving incidents.

The **Action** nodes are configured separately for each flow in the Navixy platform UI. Each node can contain multiple actions that execute sequentially when triggered by incoming data.

<figure><img src="https://2096203889-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F446mKak1zDrGv70ahuYZ%2Fuploads%2Fgit-blob-5149b87d6add69ddfb2e27fe720ef9fa71218a4b%2Fimage.png?alt=media" alt=""><figcaption></figcaption></figure>

### How Action nodes work

When data reaches an **Action** node, the system executes the configured actions for the devices that provided the incoming data. The execution process follows these steps:

* **Device identification**: The node identifies which specific devices sent the data that triggered the action
* **Sequential execution**: All configured actions within the node execute in the order they appear (top to bottom)
* **Command transmission**: Actions are sent only to the identified devices, ensuring targeted responses
* **Device processing**: Individual devices receive and process commands according to their capabilities

This targeting mechanism ensures that actions execute only for relevant devices. When connected to Logic nodes, actions trigger only for devices that caused the logical condition to evaluate as true, providing precise automation control.

### Flow architecture integration

**Action** nodes function as terminal nodes within the flow architecture, receiving triggers from upstream nodes without passing data forward. The automation capabilities integrate with Navixy's broader device management system through:

* **Conditional automation**: Integration with Logic nodes enables sophisticated IF-THEN workflows where actions execute only when specific conditions are validated
* **Real-time device control**: Commands are transmitted within seconds of receiving triggers, ensuring immediate response to critical conditions
* **Fleet-wide coordination**: When connected to multiple device sources, actions can coordinate responses across entire vehicle groups simultaneously
* **Device capability respect**: Individual device limitations are honored, with unsupported commands being received but not executed

{% hint style="info" %}
**Device connectivity requirement**: Actions are sent only to devices that are confirmed online (those providing recent data), ensuring reliable command delivery. In the rare event that a device goes offline immediately after sending data, or if multiple commands are pending, the actions are queued and executed as soon as the device is available again.
{% endhint %}

### Configuration options

Setting up an **Action** node determines what automated responses will be executed when the node receives triggers from upstream processing nodes.

<figure><img src="https://2096203889-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F446mKak1zDrGv70ahuYZ%2Fuploads%2Fgit-blob-3edf7c33f62a13048061b06c2092818e88a18212%2Fimage.png?alt=media" alt=""><figcaption></figcaption></figure>

Let's see what elements this node uses and what you can configure when working with it:

#### Configuration steps

{% stepper %}
{% step %}
**Specify Node name**

Enter a descriptive name that identifies the automated actions this node will perform

1. Use names like "Emergency Cooling Response" or "Security Alert Actions" for clarity
2. This name appears in the flow diagram for easy identification
{% endstep %}

{% step %}
**Select Action type**

Choose the type of automated response from the dropdown menu

1. **Switch Output**: Control device outputs by switching them on or off
2. **Send GPRS Command**: Transmit custom commands directly to devices
{% endstep %}

{% step %}
**Configure action parameters**

Set up the specific details based on your selected action type:

<details>

<summary>Switch Output configuration</summary>

<figure><img src="https://2096203889-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F446mKak1zDrGv70ahuYZ%2Fuploads%2Fgit-blob-8b6690390e3542595bbabce1e2b3a3b955e7a5d1%2Fimage.png?alt=media" alt=""><figcaption></figcaption></figure>

When configuring Switch Output actions:

* **Output number**: Select which device output to control from the dropdown menu
  * Available output numbers depend on your specific device capabilities
  * Refer to your device documentation to understand output functions
* **On/Off toggle**: Set whether the action switches the output ON or OFF
  * Use the toggle switch to select the desired state

</details>

<details>

<summary>Send GPRS Command configuration</summary>

<figure><img src="https://2096203889-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F446mKak1zDrGv70ahuYZ%2Fuploads%2Fgit-blob-7dc8633627afb6c27d2bb957714c439561b04300%2Fimage.png?alt=media" alt=""><figcaption></figcaption></figure>

When configuring GPRS Command actions:

* **Command string**: Enter the exact command text to send to devices
  * Commands must match your device's supported command syntax
  * Consult device documentation for available commands and proper formatting
  * There are no character restrictions in the input field

{% hint style="danger" %}
Action execution depends on individual device capabilities. Ensure your devices support the specific commands you're configuring. Information on the commands supported by a specific device is available in manufacturer resources like device documentation.
{% endhint %}

</details>
{% endstep %}

{% step %}
**Add additional actions (optional)**

Click **ADD ACTION** to create multiple actions within the same node

* Actions execute sequentially in the order they appear in the configuration
* Each action can be a different type (Switch Output or GPRS Command)
* Use the bin icon to remove unnecessary actions
{% endstep %}

{% step %}
**Save configuration**

Click **APPLY** to save your node configuration

* Use **CANCEL** to discard changes
* Use **RESET FORM** to clear all configured actions and start over
{% endstep %}
{% endstepper %}

{% hint style="danger" %}
**Device compatibility note:** Action execution depends on individual device capabilities. Ensure your devices support the specific outputs or commands you're configuring. Please look for supported commands in manufacturer resources like device documentation. List of supported devices is available at [Navixy integrated devices](https://www.navixy.com/devices/).
{% endhint %}

### Action execution and targeting

The Action node provides precise control over when and where commands are executed, ensuring efficient and targeted automation responses.

#### Execution sequence

When triggered, the Action node follows this execution pattern:

1. **Device targeting**: Actions are sent only to devices that provided data in the current trigger event
   1. This ensures commands reach only the specific devices involved in the condition
   2. Prevents unnecessary commands to unaffected devices in the fleet
2. **Sequential processing**: Multiple actions within a node execute in the configured order from top to bottom
   1. Each action completes transmission before the next action begins
   2. Total execution time is typically within seconds of receiving the trigger
3. **Device validation**: Individual devices process received commands according to their capabilities
   1. Supported commands execute immediately upon receipt
   2. Unsupported commands are received but ignored by the device
   3. Device safety mechanisms may prevent inappropriate commands (e.g., engine shutdown while moving)

#### Connection behavior

**Logic node integration**: When connected to Logic nodes, actions execute only for devices where the logical condition evaluated to `true`. This provides precise conditional automation.

**Direct connections**: When connected directly to other node types (Data Source, Initiate Attribute), actions execute for all devices in the data stream each time data is received.

### Frequently asked questions

**How do I know if my actions were executed successfully?**

Currently, action execution feedback is limited. Commands are sent to devices that are confirmed online (those providing recent data) without execution time gap, which eliminates the possibilityu of the device going offline between trigger and execution. You can monitor device behavior during test stage, or use separate test flows to verify action results in a controllable environement.

**Can I connect multiple nodes to the same Action node?**

Yes. Action nodes can receive triggers from multiple upstream nodes, but be aware that actions will execute for any device that triggers any connected node. When designing complex flows, consider the cumulative effect of multiple trigger sources to ensure actions execute only for intended scenarios.

**What happens if I connect an Action node directly to a Data Source?**

The Action node will execute its configured actions every time any device in the Data Source sends data. This creates continuous action execution rather than conditional responses. For most use cases, connecting Action nodes to Logic nodes provides better control over when actions should execute.
