---
description: Templates are pre-configured IoT Logic flows for common data processing scenarios. Select a template from the start page to get started quickly.
---

# Templates

Templates are pre-configured IoT Logic flows for common data processing scenarios. You access them from the **Flow templates** gallery on the IoT Logic start page. Clicking a template card immediately creates a flow from that template and opens it on the canvas, where you can review the pre-configured nodes and complete any required setup.

[SCREENSHOT: Flow templates gallery on the IoT Logic start page]

## How to use a template

1. Open IoT Logic. The start page opens with the **Flow templates** gallery at the top.
2. Click the template card that matches your use case. The flow is created immediately and opens on the canvas. A description modal appears explaining the flow and its setup steps.
3. Read the description modal, then close it to view the canvas.
4. Assign your devices to the **Data Source** node.
5. Configure any credentials or settings specific to your setup, such as Webhook URLs, Device action commands, or parameter names.
6. Click **Save Flow**.

[SCREENSHOT: Template open on canvas with description modal visible]

{% hint style="info" %}
Clicking a template creates a flow immediately, with no separate confirmation step. Device assignment and credentials always require manual configuration regardless of which template you use.
{% endhint %}

## Available templates

<details>

<summary>Device healthcheck and reboot</summary>

This template monitors GPS signal quality, coordinate availability, and board voltage on each incoming data packet. If any parameter falls outside the defined thresholds, the flow sends a reboot command to the device to recover from potential hardware or software issues. The template includes reboot commands for Teltonika and Jimi/Concox devices.

**Nodes:** Data Source, IF/THEN Logic, Output Endpoint, Device action (×2, one per supported manufacturer)

**Prerequisite:** None.

#### Setup

- Remove the **Device action** node that does not match your hardware, or replace both commands with the correct ones for your device.
- Adjust the health check thresholds in the **IF/THEN Logic** node to match your requirements. The defaults are: satellites ≥ 4 and board voltage ≥ 11.5 V.

</details>

<details>

<summary>Metric to Imperial Universal Unit Converter</summary>

This template converts device telemetry between metric and imperial units, adding the converted values to each data packet. It covers temperature, speed, and fuel level in both directions. The two **Initiate Attribute** nodes convert in opposite directions; keep only the one that matches your use case.

**Nodes:** Data Source, Initiate Attribute (×2, one for metric output and one for imperial output), Output Endpoint

**Prerequisite:** None.

#### Setup

- Delete the **Initiate Attribute** node for the direction you do not need.
- Remove any individual conversions from the remaining node that do not apply to your data.
- Verify that the parameter names in the formulas match your device's actual parameter names.

</details>

<details>

<summary>Perform an action in external system</summary>

This template triggers a webhook to an external system when a condition is met. It is pre-configured with a speed threshold (speed > 120 km/h) and a Slack webhook as an example. You can adapt it to any device parameter and any system that accepts webhooks.

**Nodes:** Data Source, IF/THEN Logic, Webhook, Output Endpoint

**Prerequisite:** The target external system must have a webhook endpoint available.

#### Setup

- Replace the condition in the **IF/THEN Logic** node with your threshold or parameter check.
- Replace the **Webhook** node URL, headers, and body with your target system's endpoint configuration.
- Update the request body to include the device parameters relevant to your use case.

</details>

<details>

<summary>Idling detection</summary>

This template detects excessive idling by monitoring ignition state and speed. When a vehicle stays stationary with the engine on for more than 10 minutes, the flow sets an alert custom parameter in the data packet. You can use that parameter to trigger alerts or reports in the tracking system. The same pattern works for any duration-based condition.

**Nodes:** Data Source, IF/THEN Logic (×3), Initiate Attribute (×3), Output Endpoint

**Prerequisite:** None.

#### Setup

- Adjust the idle duration threshold in the "Idle for 10 min" **IF/THEN Logic** node. The default is 600,000 ms (10 minutes).
- To track a different condition, replace the ignition and speed check in the "Idle condition" **IF/THEN Logic** node with your own expression.

</details>

<details>

<summary>Driver access control</summary>

This template monitors hardware key authentication (iBeacon, RFID, or Dallas) on each ignition event. If the key is not on the authorized list, the flow blocks the engine and sends a messenger notification. The template is pre-configured for Telegram notifications and Teltonika engine block and unblock commands.

**Nodes:** Data Source, IF/THEN Logic, Webhook, Device action (×2, engine block and unblock), Output Endpoint

**Prerequisite:** Vehicles must have a hardware key reader installed and configured.

#### Setup

- Replace `ALLOWED_HW_KEY_1`, `ALLOWED_HW_KEY_2`, and `ALLOWED_HW_KEY_3` in the **IF/THEN Logic** node with your authorized key IDs.
- To use a different messenger, replace the **Webhook** node configuration entirely with your target system's endpoint configuration.
- For non-Teltonika devices, replace the engine block and unblock commands in the **Device action** nodes with the correct commands from your manufacturer's documentation.

</details>
