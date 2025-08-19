# Schema overview

This section provides an overview of the Private Telematics Lakehouse data schemas structure, helping you understand how data is organized and how to access it effectively. The warehouse is designed to give you full and flexible access to your Platform data through a structured database system.

**What you'll learn:**

* How data is structured in layers and schemas
* Key tables in each schema and what they contain
* How data tables relate to each other
* How to access data using SQL queries
* How data validation works
* Upcoming enhancements to the data structure

{% hint style="info" %}
**Key terms:**

* **Layer**: A level in a data warehouse that represents a stage of data processing, organization, or access, each with a distinct function.
* **Schema**: A logical grouping of database objects (tables, views, etc.)
{% endhint %}

## Data structure

The Private Telematics Lakehouse uses a multi-layered storage architecture to organize your data. This architecture provides reliability, performance, and scalability while ensuring proper data isolation between clients.

### Data layers

The system follows a three-layered model for data organization:

#### [**Bronze layer**](bronze-layer.md)

* Raw data with minimal transformation
* Direct ingestion from business and telematics data sources
* Original data structure with consistent naming conventions

#### **Silver layer**

* Already processed data with validation and enrichment
* Transformed structures for improved analytics
* Introduced data quality control and business rule application

**Gold layer**

* Business-ready datasets optimized for reporting
* Pre-aggregated metrics and denormalized structures
* Curated views aligned with specific business reporting processes

Further in this documentation section, you will find more detailed data schemas for each layer.

### Database architecture

Each client has a dedicated database instance to ensure data isolation and security. Within this database:

| **Schema**                | **Description**                        | **Content**                                                                             |
| ------------------------- | -------------------------------------- | --------------------------------------------------------------------------------------- |
| **raw\_business\_data**   | Business entities and operational data | Core entity tables, operational data, reference data, history data, relationship tables |
| **raw\_telematics\_data** | Device tracking and sensor data        | Core tracking data, input data, state data                                              |
| **Reference data**        | System reference data                  | description\_parameters table                                                           |

When querying data, you must specify both the schema (`raw_business_data`) and table (`objects`) name:

`SELECT * FROM raw_business_data.objects;`

### Client metadata and data isolation

The system uses metadata tables to enable proper data isolation and multi-tenant support:

* **Dealer metadata** tracks dealer-to-client relationships and infrastructure parameters
* **Client metadata** maps business and telematics data across schemas
* **Client-device mapping** ensures telematic data is correctly associated with the right client

This metadata layer ensures that:

* Each client can only access their own data
* Telematic and business data can be properly joined
* System-level operations are properly segmented by client
