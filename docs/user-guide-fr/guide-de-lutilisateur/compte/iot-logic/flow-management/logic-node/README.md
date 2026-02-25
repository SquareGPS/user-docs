# Logic node

### Technical overview and capabilities

{% columns %}
{% column %}
The **Logic** node creates intelligent branching points that route incoming data down different paths based on logical conditions. It receives data from other nodes, validates it against your defined conditions, and routes the results down different paths based on whether the validation succeeds or fails. The node enables you to build IF->THEN/ELSE workflows where different actions occur automatically based on real-time data conditions.
{% endcolumn %}

{% column %}
<figure><img src="https://2096203889-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F446mKak1zDrGv70ahuYZ%2Fuploads%2Fgit-blob-f162134f3cdc9d2aaf343b37804e3e45bc80cb05%2FLogic_node.webp?alt=media" alt="Logic node in the flow workspace"><figcaption></figcaption></figure>
{% endcolumn %}
{% endcolumns %}

{% hint style="info" %}
The **Logic** nodes are configured separately for each flow in the Navixy platform UI. Each node contains only one logical formula, relying on x[Navixy IoT Logic Expression Language](https://app.gitbook.com/s/tx3J5BxnWyPV0nP2xr0z/technologies/navixy-iot-logic-expression-language).\
For specific syntax options related to logical expressions, see Logic node expressions and syntax.
{% endhint %}

<figure><img src="https://2096203889-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F446mKak1zDrGv70ahuYZ%2Fuploads%2Fgit-blob-740dbc8a012a54d494a715b6210487c8be3b6d38%2FLogic-node-in-flow.webp?alt=media" alt="Logic node in flow context with other nodes showing connections"><figcaption></figcaption></figure>

#### How Logic nodes work

When data first reaches a **Logic** node, the system creates a user-defined boolean attribute that stores the evaluation results. Each subsequent data packet is evaluated against your logical expression, updating this attribute's value and routing the data accordingly:

* **True results**: Data flows through the THEN connection (green) with the boolean attribute set to `true`
* **False results**: Data flows through the ELSE connection (red) with the boolean attribute set to `false`

This evaluation happens independently for each data packet, allowing different records from the same device to follow different paths based on real-time conditions.

#### Flow architecture integration

The boolean attributes created by **Logic** nodes extend beyond flow routing and integrate with Navixy's broader monitoring capabilities. Since these are user-defined custom attributes, they can be:

* **Monitored in real-time**: View evaluation results in Data Stream Analyzer to troubleshoot conditions and verify logic
* **Added as custom sensors**: Integrate with Navixy's main interface for ongoing monitoring

As custom sensors, these Logic-generated attributes enable two key capabilities:

* **Triggering alerts**: You can create custom rules based on a sensor’s value to receive notifications in case of deviations. For details on rule creation, see Rules and notifications.
* **Monitoring entities**: You can add an attribute to the Object list widget to monitor its value along with other device readings. For details on how to create a custom sensor from an IoT Logic attribute, see Displaying new calculated attributes on the Navixy platform.

{% hint style="info" %}
The **Logic** node requires a connection to at least one preceding node (**Data Source** or other processing nodes) to receive input data for validation.
{% endhint %}

#### Node capabilities

The **Logic** node offers:

* **Conditional data routing**: Create branching workflows that automatically direct data based on logical expressions returning true or false results.
* **Real-time validation**: Test incoming device data against business rules and operational thresholds as data arrives.
* **Complex condition support**: Combine multiple parameters using logical operators (AND, OR, etc.) for sophisticated decision-making.
* **Attribute creation**: Generate boolean attributes that record validation results for use in other node, Navixy's monitoring systems and 3rd-party services.
* **Flexible output paths**: Route data through THEN (true) and ELSE (false) connections to trigger different subsequent actions.

### Configuration options

The **Logic** node allows you to define conditional expressions that evaluate incoming data and create branching paths in your flow based on the results.

<figure><img src="https://2096203889-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F446mKak1zDrGv70ahuYZ%2Fuploads%2Fgit-blob-5c99db0a392e8e57207b40af33642f892edd26f0%2Fimage-20250721-090630.png?alt=media" alt="Logic node configuration panel showing title, expression name, and expression fields"><figcaption></figcaption></figure>

Let's see what elements this node uses and what you can configure when working with it.

#### Configuration steps

{% stepper %}
{% step %}
**Specify node title**

Enter a descriptive name for this **Logic** node.

* Use a name that clearly identifies the validation purpose (e.g., _Temperature Alert Check_, _Speed Violation Detection_).
* This name will be displayed in the flow diagram for easy identification.
{% endstep %}

{% step %}
**Define expression name**

Enter the name for the boolean attribute that will store the validation result.

* This attribute will appear in Data Stream Analyzer and become available for use in subsequent nodes.
* Use descriptive names like _high\_temperature\_alert_ or speed\_violation\_detected.
* The system will auto-generate names like _logic\_1_, _logic\_2_ if not specified.
{% endstep %}

{% step %}
**Create a logical expression**

Build your conditional statement using the expression field.

* Use logical operators according to Navixy Expression Language syntax to reference device parameters and calculated attributes.
* The expression must return a boolean value (true/false) for proper node operation.
* Use the autocomplete feature to select available attributes from connected data sources.
{% endstep %}

{% step %}
**Connect output paths**

Establish connections for the validation results.

* **THEN connection** (green): Connects to nodes that should process data when the expression evaluates to true.
* **ELSE connection** (red): Connects to nodes that should process data when the expression evaluates to false or null.
* The THEN connection is mandatory, while the ELSE connection is optional.
{% endstep %}
{% endstepper %}

{% hint style="info" %}
When logical expressions cannot be evaluated due to null values, invalid data types, or syntax errors, the result is treated as `false`, and data flows through the ELSE path.
{% endhint %}

For detailed information on expression syntax, operators, and data flow behavior, see Logic node expressions and syntax.

### Output connections and data flow

The Logic node creates two distinct output paths based on the expression evaluation results.

#### THEN connection (<mark style="color:green;">green</mark>)

* **Activates when**: The logical expression returns `true`.
* **Connection requirement**: Mandatory — every Logic node must have at least one THEN output.
* **Multiple connections**: Can connect to multiple subsequent nodes for parallel processing.
* **Typical uses**: Triggering alerts, special processing, conditional calculations, or routing data to specific endpoints.

#### ELSE connection (<mark style="color:red;">red</mark>)

* **Activates when**: The logical expression returns `false`, `null`, or encounters evaluation errors.
* **Connection requirement**: Optional — use only when you need to handle negative results.
* **Error handling**: Processes cases where expressions cannot be evaluated due to missing data or syntax errors.
* **Typical uses**: Logging failed validations, routing data through alternative processing paths, or continuing normal operations.

<figure><img src="https://2096203889-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F446mKak1zDrGv70ahuYZ%2Fuploads%2Fgit-blob-97d0f75e343b61237fd54f079581ddd09c5a7cc2%2Fimage-20250721-091115.png?alt=media" alt="Logic node showing THEN and ELSE connections with green and red color coding"><figcaption></figcaption></figure>

### Frequently asked questions

**Can I use attributes created by other nodes in Logic expressions?**

Yes. **Logic** nodes can reference any attributes available from connected data sources, including original device parameters and attributes calculated by preceding **Initiate Attribute** nodes. The autocomplete feature helps you select from all available attributes.

**What happens if my expression contains syntax errors?**

If an expression contains syntax errors or cannot be evaluated, the **Logic** node treats the result as `false` and routes data through the ELSE connection. Check the expression syntax and ensure all referenced attributes exist in your data stream.

**Can I connect multiple nodes to the same Logic node output?**

Yes. Both THEN and ELSE connections support multiple outgoing connections, allowing you to trigger several different actions based on the same logical condition. This enables parallel processing for complex business workflows.

**How do I monitor Logic node results?**

Logic node results appear as boolean attributes in the Data Stream Analyzer table. Select your devices and look for the attribute name you specified in the expression name field. The values will display as `true` or `false` based on the evaluation results.

#### Can I chain multiple Logic nodes together?

Yes. You can connect **Logic** nodes sequentially to create complex decision trees. Each **Logic** node can reference the boolean attributes created by previous **Logic** nodes, enabling sophisticated multi-stage validation workflows.

<figure><img src="https://2096203889-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F446mKak1zDrGv70ahuYZ%2Fuploads%2Fgit-blob-aed48485c5262694648bad46958860e34ad32cd0%2Fimage-20250721-091554.png?alt=media" alt="Example flow showing multiple Logic nodes connected in sequence for complex decision trees"><figcaption></figcaption></figure>
