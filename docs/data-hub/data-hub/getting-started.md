# Getting started

## First steps

Your journey with Private Telematics Lakehouse begins with the connection credentials provided in your welcome email. These include:

- Database host and port
- Database name
- Username and password
- SSL mode settings

> [!INFO]
> If you are not administering your Platform accounts yourself, contact your [GPS / Telematics service provider](https://documentation-test-environment.scrollhelp.site/en/user-guide/Working-version/service-provider) for access to Private Telematics Lakehouse.

From there, your path forward is straightforward:

1. [Set up your connection](../private-telematics-lakehouse/connection-setup.md)  
Configure your SQL client or analytics tool
2. [Explore data schemas](../private-telematics-lakehouse/schema-overview.md)  
Discover the tables and relationships in your data
3. [Check example queries](../private-telematics-lakehouse/example-queries.md)  
Start with sample SQL that addresses common use cases

We also recommend familiarizing yourself with [Data types and field standards](https://squaregps.atlassian.net/wiki/spaces/DTP/pages/edit-v2/3208282138#Data-types-and-field-standards) and [Important considerations](https://squaregps.atlassian.net/wiki/spaces/DTP/pages/edit-v2/3208282138#Known-limitations) before proceeding.

## Data types and field standards

The Private Telematics Lakehouse uses consistent data type conventions that may differ from the source systems:

- **Date and time fields** use the `TIMESTAMP` format
- **Text fields** use `CHARACTER VARYING` or `TEXT` types
- **ID fields** follow a consistent naming pattern with their table prefix (e.g., \`user\_id\`, \`device\_id\`)
- **Boolean fields** use prefixes like `is_`, `has_`, or `can_` (e.g., `is_active`, `has_passport`)

## Important considerations

While working with the Private Telematics Lakehouse, be aware of these current limitations:

- **Error messaging** is minimal for SQL query issues
- **Silver and Gold layers** are still in development and not available yet
- **Historical data** availability depends on your Platform subscription plan

For detailed information on structure and capability, see [Schema overview](../private-telematics-lakehouse/schema-overview.md).