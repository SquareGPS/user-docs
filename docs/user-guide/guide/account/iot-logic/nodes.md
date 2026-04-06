---
description: Reference overview of all node types available in IoT Logic, with links to configuration details for each.
---

# Nodes

Nodes are the building blocks of an IoT Logic flow. Each node handles a specific stage of the data lifecycle, from receiving raw device telemetry to forwarding enriched data to its destination. Every flow requires at minimum one input node and one output node. This page is a reference overview of all available node types — follow the links in the table for full configuration details.

| Node | Role | Description |
|---|---|---|
| [Data Source node](flow-management/data-source-node.md) | Input | Connects devices to the flow and receives their telemetry data as the entry point for all data processing. |
| [Initiate Attribute node](flow-management/initiate-attribute-node/) | Enrichment | Creates calculated attributes from incoming device parameters using the Navixy Expression Language. |
| [IF/THEN Logic](flow-management/logic-node/) | Routing | Routes data through conditional branches based on logical expressions evaluated against incoming values. |
| [Device action](flow-management/action-node.md) | Action | Sends commands back to devices when triggered by incoming data, and cannot have outgoing connections to other nodes. |
| [Webhook](flow-management/webhook-node.md) | Action | Sends HTTP POST requests to external systems when triggered by incoming data, and cannot have outgoing connections to other nodes. |
| [Output Endpoint node](flow-management/output-endpoint-node.md) | Output | Transmits processed data to the Navixy platform or third-party systems via MQTT. |

{% hint style="info" %}
**Device action** and **Webhook** are terminal nodes — they perform an action when triggered but do not pass data forward, so no outgoing connections can be added after them. If you place a terminal node on a conditional branch of an **IF/THEN Logic** node, connect the Logic node directly to an **Output Endpoint** node in parallel to ensure data continues flowing through the other branch.
{% endhint %}
