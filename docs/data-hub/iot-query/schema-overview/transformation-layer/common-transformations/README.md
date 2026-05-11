---
description: >-
  Ready-made analytical entities in the Transformation layer, available to query
  immediately and adaptable through Transformation Builder.
---

# Common transformations

The Transformation layer includes a set of common transformations developed and maintained by Navixy. These transformations run automatically on a schedule and populate the `processed_common_data` schema with normalized analytical entities derived from raw telematics and business data.

You can start querying this data immediately after connecting to IoT Query — no configuration required. Each transformation produces a specific table with a documented output schema, update schedule, and processing logic.

{% hint style="info" %}
To build a custom version of any listed transformation, download the corresponding workflow template from the [Templates](../transformation-builder/templates.md) page and import it into Transformation Builder.
{% endhint %}

## Available transformations

<table><thead><tr><th width="148">Transformation</th><th width="266">Table</th><th>Description</th></tr></thead><tbody><tr><td><a href="trips.md">Trips</a></td><td><code>processed_common_data.trips</code></td><td>Vehicle trips derived from raw telematics data, including start and end times, distance, speed statistics, and zone detection.</td></tr></tbody></table>

## Next steps

* [**Trips**](trips.md): Output schema, algorithm description, customization options, and workflow template download.
* [**Templates**](../transformation-builder/templates.md): Download workflow templates for common transformations and import them into Transformation Builder.
* [**Transformation layer**](../): How the Transformation layer organizes processed data into schemas and how to query it.
* [**Transformation Builder**](../transformation-builder/): Design and adapt transformation workflows using the visual interface.
