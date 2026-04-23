---
description: >-
  Pre-built Transformation Builder workflows for common Navixy transformations.
  Download, import, and adapt them to your scenario.
---

# Templates

Navixy provides workflow templates for common transformations available in the Transformation layer. Each template is a pre-built Transformation Builder workflow configuration that you can import, inspect, and adapt to your operational scenario before scheduling it as a custom transformation in `processed_custom_data`.

Templates are a starting point, not a finished product. Every template ships without an Output node so you can decide where and how results are written before committing to a schedule.

## How to use a template

The steps below apply to any template on this page. Template-specific values for the Output node and schedule are listed in the [Available templates](templates.md#available-templates) section.

{% stepper %}
{% step %}
#### Download the template&#x20;

Find the transformation you want in the Available templates section below and download its YAML file.
{% endstep %}

{% step %}
#### Open Transformation Builder and connect to your database&#x20;

Launch [Transformation Builder](./) and enter your PostgreSQL connection URL. Wait for the Builder to discover available tables and columns.
{% endstep %}

{% step %}
#### Import the workflow&#x20;

Click **Import** in the toolbar and select the downloaded `.yaml` file. The workflow graph loads with all nodes and edges in place.
{% endstep %}

{% step %}
#### Review and adjust the workflow&#x20;

Inspect the node graph. Each transformation's page in [Common transformations](../common-transformations/) describes the processing logic and lists customization options you can apply at this stage. Click Execute at any point to preview results against your live data (up to 100 rows).
{% endstep %}

{% step %}
#### Add an Output node&#x20;

A template has no Output node. Add one from the node panel and connect it to the final node in the graph. Use the Output node values listed for your template in the [Available templates](templates.md#available-templates) section below. When scheduled, the workflow writes to `processed_custom_data`. It produces a separate table from the built-in version maintained by Navixy in `processed_common_data`.
{% endstep %}

{% step %}
#### Schedule the workflow&#x20;

Click **Schedule** and set the execution frequency. Use the recommended schedule listed for your template in the Available templates section, or choose a different interval to match your reporting needs.
{% endstep %}
{% endstepper %}

## Available templates

The table below lists available templates with the values you need for the Output node and the recommended schedule. Each template links to its transformation page for algorithm details and customization guidance, and provides the YAML file for download.

### Tracks

Produces one row per vehicle trip from raw telematics data, with start and end times,\
distance, speed statistics, and zone detection. See the [Tracks](../common-transformations/tracks.md) page for the full output schema, algorithm description, and customization options.

{% file src="../../../../.gitbook/assets/Tracks.yaml" %}

When adding the **Output node**, use the following configuration:

| Parameter   | Value                           |
| ----------- | ------------------------------- |
| Table name  | `tracks`                        |
| Time column | `track_start_time`              |
| Primary key | `device_id`, `track_start_time` |
| Write mode  | `overwrite`                     |

Recommended schedule: `10 */8 * * *` (UTC, every 8 hours), matching the update frequency of the built-in `business_data.tracks` transformation.

## Next steps

* [**Common transformations**](../common-transformations/): Learn what each transformation produces, how it is built, and how to customize the logic before importing a template.
* [**Transformation Builder**](./): Full reference for the visual workflow editor, node types, and execution options.
* [**Workflow YAML reference**](workflow-yaml-reference.md): Specification for the YAML format used by these template files.
