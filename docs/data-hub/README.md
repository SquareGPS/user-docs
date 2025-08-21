# Data Hub

## Introduction

Navixy's **Data Hub** gives you direct access to your valuable business and telematics data in a unified, SQL-queryable environment. This documentation will help you connect to your data, understand what's available, and start extracting insights right away.

## Your data journey

Every organization collects vast amounts of operational data through the Navixy platform. While the platform's interface provides standard reports and visualizations, your unique business questions often require deeper, more customized analysis.

That's where Data Hub comes in.

We've taken your complete dataset and made it directly accessible through a standard PostgreSQL connection, opening up new possibilities for analysis, integration, and insight discovery.

## Key benefits

|                                                                                                                             |                                                                                                                                                                                                                                   |                                                                                                                            |
| --------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- |
| <p><strong>Direct SQL access</strong><br><br>Query your data directly via PostgreSQL without API constraints</p>            | <p><strong>Complete data access</strong><br><br>Work with your full dataset beyond what's available on the Platform</p>                                                                                                           | <p><strong>Customization</strong><br><br>Build custom analytics, reports, and integrations for your specific scenarios</p> |
| <p><strong>Data integration</strong><br><br>Connect with BI and analytics tools for advanced visualization and research</p> | <p><strong>Structured data model</strong><br><br>Leverage a well-organized <a href="./#how-your-data-is-organized">multi-layer architecture</a>:<br><strong>Bronze</strong> → <strong>Silver</strong> → <strong>Gold</strong></p> | <p><strong>Client isolation</strong><br><br>Secure data environment with proper access controls at all levels</p>          |

## What data is available?

Your **Data Hub** contains two primary types of information:

### **Business data**

Includes approximately 40 tables containing your organization's structural information:

* Users and employees
* Devices and objects
* Vehicles and assignments
* Tasks, zones, and operational records

### **Telematics data**

Contains the continuous stream of information from your tracking devices:

* GPS coordinates and movement data
* Sensor readings
* States

The combination of data types enables both operational reporting and deeper analytical insights.

## How your data is organized

We've structured your data using a multi-layered architecture that balances immediate access with analytical performance. Each layer itself is sufficient for different scenarios:

1. **Bronze layer** (Available now) – A complete dataset , comprising telematics and business data, with minimal transformation, ready for exploration and detailed analysis
2. **Silver layer** (Coming soon) – Cleansed and transformed data optimized for reporting and analytics
3. **Gold layer** (Coming soon) – Business-ready data marts and aggregated metrics for specific use cases

### Data pipeline overview

Your data flows through a comprehensive pipeline before reaching the warehouse:

* **Business data** is collected from client’s cabinet
* **Telematics data** streams directly from devices
* **Reference metadata** is loaded to enable proper data mapping and relationships
* Data is stored in the appropriate layer based on its processing stage

## Who can benefit from this platform?

**Data analysts** will appreciate direct SQL access to build custom reports and extract insights that answer specific business questions.

**Data scientists** can leverage the complete dataset for advanced analytics, developing machine learning models and predictive capabilities.

**Developers** gain the ability to create seamless integrations between operational data and other business systems through standard database connections.

## Support and assistance

For technical support and assistance with Data Hub please contact our support team at [support@navixy.com](mailto:support@navixy.com).
