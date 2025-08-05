# Logic node

## Technical overview and capabilities

![Logic node in the flow workspace](../../../iot-logic/flow-management/attachments/Logic_node.webp)

The **Logic** node creates intelligent branching points that route incoming data down different paths based on logical conditions. It receives data from other nodes, validates it against your defined conditions, and routes the results down different paths based on whether the validation succeeds or fails. The node enables you to build IF->THEN/ELSE workflows where different actions occur automatically based on real-time data conditions.

> \[!INFO] The **Logic** nodes are configured separately for each flow in the Navixy platform UI. Each node contains only one logical formula, relying on [Navixy IoT Logic Expression Language](https://www.navixy.com/docs/iot-logic-api/technologies/navixy-iot-logic-expression-language).\
> For specific syntax options related to logical expressions, see [Logic node expressions and syntax](https://squaregps.atlassian.net/wiki/spaces/USERDOCSOLD/pages/3361800221/Logic+node+expressions+and+syntax?atlOrigin=eyJpIjoiOWUxMmU1YTgyMGUzNGMwMWExMzdhZGI4OTNmYmY2NTAiLCJwIjoiYyJ9).

![Logic node in flow context with other nodes showing connections](../../../iot-logic/flow-management/attachments/Logic-node-in-flow.webp)

### How Logic nodes work

When data first reaches a **Logic** node, the system creates a user-defined boolean attribute that stores the evaluation results. Each subsequent data packet is evaluated against your logical expression, updating this attribute's value and routing the data accordingly:

* **True results**: Data flows through the THEN connection (green) with the boolean attribute set to `true`
* **False results**: Data flows through the ELSE connection (red) with the boolean attribute set to `false`

This evaluation happens independently for each data packet, allowing different records from the same device to follow different paths based on real-time conditions.

### Flow architecture integration

The boolean attributes created by **Logic** nodes extend beyond flow routing and integrate with Navixy's broader monitoring capabilities. Since these are user-defined custom attributes, they can be:

* **Monitored in real-time**: View evaluation results in [Data Stream Analyzer](https://squaregps.atlassian.net/wiki/spaces/USERDOCSOLD/pages/3037332703/Data+Stream+Analyzer?atlOrigin=eyJpIjoiNGI4ZGFiZjQyOTA3NDA3YWIzNWY1ODFhYzNhZDgzZDgiLCJwIjoiYyJ9) to troubleshoot conditions and verify logic
* **Added as custom sensors**: Integrate with Navixy's main interface for ongoing monitoring

As custom sensors, these Logic-generated attributes enable two key capabilities:

* **Triggering alerts**: You can create custom rules based on a sensor’s value to receive notifications in case of deviations. For details on rule creation, see [Rules and notifications](../../../../rules-and-notifications/).
* **Monitoring entities**: You can add an attribute to the [Object list](https://squaregps.atlassian.net/wiki/spaces/USERDOCSOLD/pages/2909015397/Objects+list?atlOrigin=eyJpIjoiZjQ0NjhkMDA0YzBhNGU4MTllNjY4YmIxNWFhNWNmNzAiLCJwIjoiYyJ9) widget to monitor its value along with other device readings. For details on how to create a custom sensor from an IoT Logic attribute, see [Adding custom attributes to objects on the Navixy platform](initiate-attribute-node-1/displaying-new-calculated-attributes-on-the-navixy-platform.md).

> \[!INFO] The **Logic** node requires a connection to at least one preceding node (**Data Source** or other processing nodes) to receive input data for validation.

### Node capabilities

The **Logic** node offers:

* **Conditional data routing**: Create branching workflows that automatically direct data based on logical expressions returning true or false results.
* **Real-time validation**: Test incoming device data against business rules and operational thresholds as data arrives.
* **Complex condition support**: Combine multiple parameters using logical operators (AND, OR, etc.) for sophisticated decision-making.
* **Attribute creation**: Generate boolean attributes that record validation results for use in other node, Navixy's monitoring systems and 3rd-party services.
* **Flexible output paths**: Route data through THEN (true) and ELSE (false) connections to trigger different subsequent actions.

## Configuration options

The **Logic** node allows you to define conditional expressions that evaluate incoming data and create branching paths in your flow based on the results.

![Logic node configuration panel showing title, expression name, and expression fields](../../../iot-logic/flow-management/attachments/image-20250721-090630.png)

Let's see what elements this node uses and what you can configure when working with it.

### Configuration steps

1. **Specify node title**: Enter a descriptive name for this **Logic** node.

* Use a name that clearly identifies the validation purpose (e.g., _Temperature Alert Check_, _Speed Violation Detection_).
* This name will be displayed in the flow diagram for easy identification.

2. **Define expression name**: Enter the name for the boolean attribute that will store the validation result.

* This attribute will appear in [Data Stream Analyzer](https://squaregps.atlassian.net/wiki/spaces/USERDOCSOLD/pages/3037332703/Data+Stream+Analyzer?atlOrigin=eyJpIjoiYzI4NGU2NjgyNjMyNDNiY2IzNDJjY2I3YWQzMmMwYzkiLCJwIjoiYyJ9) and become available for use in subsequent nodes.
* Use descriptive names like _high\_temperature\_alert_ or speed\_violation\_detected.
* The system will auto-generate names like _logic\_1_, _logic\_2_ if not specified.

3. **Create a logical expression**: Build your conditional statement using the expression field.

* Use [logical operators according to Navixy Expression Language syntax](https://squaregps.atlassian.net/wiki/spaces/USERDOCSOLD/pages/3361800221/Logic+node+expressions+and+syntax?atlOrigin=eyJpIjoiZjE4ZjMwNDAwNjJjNGRlYTg4Y2NkZTNjYWNmMjZmNjUiLCJwIjoiYyJ9) to reference device parameters and calculated attributes.
* The expression must return a boolean value (true/false) for proper node operation.
* Use the [autocomplete feature](initiate-attribute-node-1/managing-attributes.md) to select available attributes from connected data sources.

4. **Connect output paths**: Establish connections for the validation results.

* **THEN connection** (green): Connects to nodes that should process data when the expression evaluates to true.
* **ELSE connection** (red): Connects to nodes that should process data when the expression evaluates to false or null.
* The THEN connection is mandatory, while the ELSE connection is optional.

> \[!INFO] When logical expressions cannot be evaluated due to null values, invalid data types, or syntax errors, the result is treated as `false`, and data flows through the ELSE path.

For detailed information on expression syntax, operators, and data flow behavior, see [Logic node expressions and syntax](https://squaregps.atlassian.net/wiki/spaces/USERDOCSOLD/pages/3361800221/Logic+node+expressions+and+syntax?atlOrigin=eyJpIjoiNDNkZjU5MzY3YzgzNDc3YWIxNDgyNWJjNDRlYzgyY2EiLCJwIjoiYyJ9).

## Output connections and data flow

The Logic node creates two distinct output paths based on the expression evaluation results.

### THEN connection (green)

* **Activates when**: The logical expression returns `true`.
* **Connection requirement**: Mandatory — every Logic node must have at least one THEN output.
* **Multiple connections**: Can connect to multiple subsequent nodes for parallel processing.
* **Typical uses**: Triggering alerts, special processing, conditional calculations, or routing data to specific endpoints.

### ELSE connection (red)

* **Activates when**: The logical expression returns `false`, `null`, or encounters evaluation errors.
* **Connection requirement**: Optional — use only when you need to handle negative results.
* **Error handling**: Processes cases where expressions cannot be evaluated due to missing data or syntax errors.
* **Typical uses**: Logging failed validations, routing data through alternative processing paths, or continuing normal operations.

![Logic node showing THEN and ELSE connections with green and red color coding](../../../iot-logic/flow-management/attachments/image-20250721-091115.png)

## Frequently asked questions

### Can I use attributes created by other nodes in Logic expressions?

Yes. **Logic** nodes can reference any attributes available from connected data sources, including original device parameters and attributes calculated by preceding **Initiate Attribute** nodes. The autocomplete feature helps you select from all available attributes.

### What happens if my expression contains syntax errors?

If an expression contains syntax errors or cannot be evaluated, the **Logic** node treats the result as `false` and routes data through the ELSE connection. Check the expression syntax and ensure all referenced attributes exist in your data stream.

### Can I connect multiple nodes to the same Logic node output?

Yes. Both THEN and ELSE connections support multiple outgoing connections, allowing you to trigger several different actions based on the same logical condition. This enables parallel processing for complex business workflows.

### How do I monitor Logic node results?

Logic node results appear as boolean attributes in the [Data Stream Analyzer](https://squaregps.atlassian.net/wiki/spaces/USERDOCSOLD/pages/3037332703/Data+Stream+Analyzer?atlOrigin=eyJpIjoiZDU0NTc0MGM1MDNjNDAzNGIwYzIyMTQ5MzkyOTNmMjMiLCJwIjoiYyJ9) table. Select your devices and look for the attribute name you specified in the expression name field. The values will display as `true` or `false` based on the evaluation results.

### Can I chain multiple Logic nodes together?

Yes. You can connect **Logic** nodes sequentially to create complex decision trees. Each **Logic** node can reference the boolean attributes created by previous **Logic** nodes, enabling sophisticated multi-stage validation workflows.

![Example flow showing multiple Logic nodes connected in sequence for complex decision trees](../../../iot-logic/flow-management/attachments/image-20250721-091554.png)
