# Workspace

## Start page

When you open IoT Logic, you land on the start page. The start page is the central hub for accessing your flows and creating new ones from scratch or from a template.

[SCREENSHOT: IoT Logic start page showing both the Flow templates gallery and the Created flows table]

### Flow templates

The **Flow templates** gallery shows five pre-configured flow structures for common data processing scenarios. Each template card displays the template name and a brief description.

Clicking a template card immediately creates a flow from that template and opens it on the canvas. A description modal appears over the canvas explaining the flow and its required setup steps.

[SCREENSHOT: Template open on canvas with description modal visible]

{% hint style="info" %}
Clicking a template creates a flow immediately. You still need to assign devices to the **Data Source** node and configure any credentials, such as Webhook URLs or Device action commands, before the flow can process data.
{% endhint %}

### Created flows

The **Created flows** table lists all existing flows in your account. The table includes the following columns: Flow name, Last modified, Connected devices, and Status.

Each row provides the following controls: a status toggle to enable or disable the flow, a download icon to export the flow as a file, and a **"..."** menu with the options **Edit**, **Download**, and **Delete**.

[SCREENSHOT: Created flows table with per-row controls visible]

The page-level buttons at the top of the table are **Upload Flow** and **Create Flow**.

## IoT Logic workspace

The flow workspace consists of two sections: **Nodes pane (1)** and **Canvas (2)**.

<figure><img src="../../../.gitbook/assets/IoT_Logic_workspace_example.webp" alt="IoT Logic workspace example (with a basic 3-step flow) visually divided by the numbered sections"><figcaption></figcaption></figure>

### 1 - Nodes pane

Available nodes are located in a separate pane on the left. You can drag-and-drop them onto the canvas of the current flow. The option to save the current flow configuration is also located on this pane. At the moment, the following nodes are available:

* [Data Source](flow-management/data-source-node.md)**:** A node that defines where the data is coming from to the current flow. A flow can contain multiple actual sources.
* [Initiate Attribute](flow-management/initiate-attribute-node/): A node that handles data enrichment through custom calculations before sending to a destination.
* [IF/THEN Logic](flow-management/logic-node/): A node that creates conditional branching based on logical expressions, routing data through different paths depending on real-time conditions.
* [Action](flow-management/action-node.md): A node that performs automated operations on device data, such as sending commands back to devices or triggering external system actions based on defined conditions.
* [Output Endpoint](flow-management/output-endpoint-node.md): An outbound transmitting node that defines where the data is sent from the current flow.

A flow can contain multiple nodes of each type. Combining various nodes in the same flow allows you to create complex data pipelines.

The nodes pane also includes flow management options at the bottom:

* **Save flow** button saves the current flow configuration. If you edit something in the flow, don't forget to save the changes. Unsaved changes can be discarded by the page reload.
* **Download flow** button exports the current flow configuration as a JSON file. This is useful for backing up your flow configurations, sharing them with team members, or migrating flows to other accounts.

{% hint style="info" %}
The **Save flow** button saves the current flow configuration. If you edit something in the flow, don’t forget to save the changes. Unsaved changes can be discarded by the page reload.
{% endhint %}

### 2 - Canvas

This is the main interactive element of the workspace where your flows are visualized:

* **Node blocks**: All nodes you drag-and-drop to the canvas appear as blocks. You can place them however you like to make the image of your flow clear and intuitive. Hovering your mouse over a node displays an edit window.\
  **Note**. You can also open the editing window by double-clicking a node.
* **Transitions**: The arrows represent connections between nodes, defining the path your data follows within the flow. Node blocks also show hints on which connection directions they support. To create a transition, simply click a connection element on a start node and drag it to the target one. If you try to connect nodes in an unsupported direction (e.g. from an **Output Endpoint** to a **Data Source**), the attempt will fail. This way, the platform prevents an accidental configuration of an incorrect data flow.
* **Center** <img src="../../../.gitbook/assets/image-20250403-153008 (3).png" alt="image-20250403-153008.png" data-size="line">: This button allows you to quickly focus on the canvas area that contains actual elements, ensuring that the whole flow is visible. It is especially helpful for large and complex flows, but at the same time offers a handy shortcut to autosize the flowchart to fit the window.
* **Zoom in/out** <img src="../../../.gitbook/assets/image-20250403-153042 (3).png" alt="image-20250403-153042.png" data-size="line">: Common functionality to manage the scale of the flowchart. You can also zoom in or out using your mouse wheel.

## Default flow

Navixy includes a pre-configured flow in every account that processes data from all devices and sends it to the Navixy platform. This flow cannot be edited or deleted. For full details on how it works and how it relates to your custom flows, see [Default flow](flow-management/default-flow.md).
