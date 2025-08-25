# Getting started

## First steps

Your journey with Data Hub begins with the connection credentials provided in your welcome email. These include:

* Database host and port
* Database name
* Username and password
* SSL mode settings

{% hint style="info" %}
If you are not administering your Platform accounts yourself, contact your [GPS / Telematics service provider](https://app.gitbook.com/s/446mKak1zDrGv70ahuYZ/readme/quick-start/about-service-providers) for access to Data Hub.
{% endhint %}

From there, your path forward is straightforward:

1. [Set up your connection](connection-setup/)\
   Configure your SQL client or analytics tool
2. [Explore data schemas](schema-overview/)\
   Discover the tables and relationships in your data
3. [Check example queries](../example-queries/)\
   Start with sample SQL that addresses common use cases

We also recommend familiarizing yourself with [Data types and field standards](getting-started.md#data-types-and-field-standards) and [Important considerations](getting-started.md#important-considerations) before proceeding.

## Data types and field standards

Data Hub uses consistent data type conventions that may differ from the source systems:

* **Date and time fields** use the `TIMESTAMP` format
* **Text fields** use `CHARACTER VARYING` or `TEXT` types
* **ID fields** follow a consistent naming pattern with their table prefix (e.g., \`user\_id\`, \`device\_id\`)
* **Boolean fields** use prefixes like `is_`, `has_`, or `can_` (e.g., `is_active`, `has_passport`)

## Important considerations

While working with the Data Hub, be aware of these current limitations:

* **Error messaging** is minimal for SQL query issues
* **Silver and Gold layers** are still in development and not available yet
* **Historical data** availability depends on your Platform subscription plan

For detailed information on structure and capability, see [Schema overview](schema-overview/).
