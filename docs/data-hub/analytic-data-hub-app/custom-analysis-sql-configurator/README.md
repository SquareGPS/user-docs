# Custom analysis & SQL Configurator

The **Custom Analysis & SQL Configurator** enables direct database access for custom fleet analysis beyond standard reports. Write SQL queries, explore your complete dataset, and create interactive visualizations in one integrated interface.

## Interface overview

![Database Schema browser showing raw\_business\_data and raw\_telematics\_data schemas with expandable table lists, SQL Query Execution panel with query input area and results display, and Visualization tab for chart creation](../../data-hub/analytic-data-hub-app/attachments/SQL-configurator-and-visualization.webp)

The workspace of **SQL Configurator** consists of 3 main sections:

1. **Database Schema browser** - View table structures and click on schemas for interactive relationship exploration on dbdiagram.io
2. **SQL Query Execution panel** - Write PostgreSQL queries and view results with immediate feedback
3. **Interactive visualization interface** - Transform query results into charts using drag-and-drop functionality

## Your data structure

Your PTL data appears through two primary schemas organized by source and purpose:

| **raw\_business\_data**                                                                                                                                                                                                                                                                                                                                                                    | **raw\_telematics\_data**                                                                                                                                                                                                                                                                                                           |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| <p>Organizational and operational information.<br><br>- <strong>Core entities:</strong> users, devices, objects, vehicles, employees<br>- <strong>Operational data:</strong> tasks, forms, zones, places, garages<br>- <strong>Reference data:</strong> models, entities, status information<br>- <strong>Relationship tables:</strong> vehicle-driver assignments, user-zone mappings</p> | <p>Real-time GPS tracking, sensor readings, and device status<br><br>- <strong>tracking_data_core:</strong> GPS coordinates, speed, altitude, event data<br>- <strong>inputs:</strong> Sensor readings (fuel, temperature, voltage)<br>- <strong>states:</strong> Device status indicators (ignition, doors, operational modes)</p> |

> \[!NOTE] **Configuration Impact**: Your system processes different data categories based on configuration settings. If expected tables seem unavailable, verify your data category settings in [system configuration](https://squaregps.atlassian.net/wiki/spaces/DTP/pages/3358163124/Settings+and+configuration?atlOrigin=eyJpIjoiOTdkZGIxZmE3N2Q2NDY1MmE3YjgyZGM5N2YxNTdjNDkiLCJwIjoiYyJ9).

> \[!INFO] For details on data schemas available in your Data Hub, see [Schema overview](https://squaregps.atlassian.net/wiki/spaces/DTP/pages/3208282180/Schema+overview?atlOrigin=eyJpIjoiOTcyOGU2M2Y4YjU2NDQxOThmYjA4M2IyYTI1NGU3ODYiLCJwIjoiYyJ9).

## Creating visualizations from query results

Transform your SQL query results into interactive visualizations through a structured workflow:

1. Verify data configuration\
   Check that all required data categories are enabled in your system settings:
2. Navigate to **PTL Configuration** in the left sidebar
3. Verify that needed data categories (**Tracking Data**, **Inputs**, **States**) are enabled for your analysis requirements
4. If changes are needed, update configuration and consider running historical data loading for retroactive application
5. Develop and execute your query\
   In the **SQL Query Execution panel**:
6. Write your analysis query using PostgreSQL syntax and the formatting requirements above
7. Include appropriate field names, data conversions, and filtering for your visualization needs
8. Click **Execute** to run your query and generate the dataset
9. Review results to ensure data quality and expected output format
10. Access visualization interface\
    Once your query executes successfully:
11. Switch to the **Visualization** tab that appears above your query results
12. Your query results automatically become available as data fields in the visualization interface
13. The interactive chart builder loads with your dataset ready for drag-and-drop visualization creation
14. Create interactive visualizations\
    Use the visualization interface to build charts:
15. Drag fields from your query results to chart configuration areas (X-axis, Y-axis, filters, colors)
16. Choose appropriate visualization types based on your data characteristics and analysis objectives
17. Apply filters and styling to refine your visual presentation
18. Export completed visualizations in multiple formats (PNG, SVG, CSV, base64) for sharing and reporting

> \[!NOTE] **Detailed Visualization Guide**: Complete step-by-step instructions for chart creation are covered in the [Create custom visualizations](https://squaregps.atlassian.net/wiki/spaces/DTP/pages/3358163096/Creating+custom+visualizations?atlOrigin=eyJpIjoiMzkzNzA2MDkyNjQ2NDM4YmIzMGJmM2FjMDhkYTlmNGMiLCJwIjoiYyJ9).

## Query development tips

Expand the sections below to discover recommended practices for working with queries in **SQL Configurator**.

![](https://squaregps.atlassian.net/wiki/images/icons/grey_arrow_down.png)

Data format requirements for telematics analysis

Your telematics data uses scaled integer storage that requires conversion:

| **Data Type**       | **Storage Format** | **Conversion Required**                                      |
| ------------------- | ------------------ | ------------------------------------------------------------ |
| **GPS coordinates** | Scaled integers    | Divide by 10,000,000 for decimal degrees                     |
| **Speed values**    | Integer format     | Divide by 100 for km/h                                       |
| **Timestamps**      | Two variants       | Use `device_time` for events, `platform_time` for processing |

![](https://squaregps.atlassian.net/wiki/images/icons/grey_arrow_down.png)

Performance and data quality optimization

### Essential practices for reliable analysis:

* **Apply time-based filtering**: Reduces dataset size and improves response times with `WHERE device_time > now() - INTERVAL '7 days'`
* **Use indexed fields**: Include `device_id` and `device_time` in WHERE clauses for optimal query performance
* **Validate data ranges**: Filter coordinate and speed bounds to identify anomalous readings
* **Verify relationships**: Cross-reference business data relationships to ensure joins produce expected results
* **Manage result sets**: Add appropriate LIMIT clauses for exploratory queries to avoid performance issues
* **Handle data gaps**: Expect normal variations like connectivity gaps during poor signal conditions

> \[!NOTE] **Expected Data Characteristics**: Sensor readings require periodic calibration validation, and recent data may still be processing during real-time analysis.

![](https://squaregps.atlassian.net/wiki/images/icons/grey_arrow_down.png)

Cross-schema analysis patterns

### Combine organizational and tracking data for comprehensive insights:

* **Business-telematics integration**: Join using `device_id` as primary relationship key between schemas
* **Employee-vehicle correlation**: Connect through objects table relationships for productivity analysis
* **Sensor interpretation**: Use description\_parameters reference table to translate coded values to readable labels
* **Geographic analysis**: Combine tracking coordinates with zone definitions for operational insights

### **Example: Complete fleet overview with LEFT JOIN**

When analyzing fleet operations, you often need to see all vehicles regardless of their current activity status. This example demonstrates how `LEFT JOIN` preserves complete vehicle records even when tracking data or driver assignments are missing.

```
-- Show all vehicles with driver assignments and latest activity
SELECT 
    o.object_label as vehicle_name,
    e.first_name || ' ' || e.last_name as assigned_driver,
    MAX(t.device_time) as last_seen,
    COUNT(t.device_id) as tracking_points_7days
FROM raw_business_data.objects o
LEFT JOIN raw_business_data.employees e ON o.object_id = e.object_id  
LEFT JOIN raw_telematics_data.tracking_data_core t ON o.device_id = t.device_id
    AND t.device_time > CURRENT_DATE - INTERVAL '7 days'
GROUP BY o.object_label, e.first_name, e.last_name
ORDER BY last_seen DESC NULLS LAST;
```

**Key insight**: LEFT JOIN ensures all vehicles appear in results, even without recent tracking or driver assignments.

> \[!NOTE] **Query Examples**: Complete use-case-specific patterns are available in the SQL Cookbook\[LINK].

## Next steps

* [Create custom visualizations](https://squaregps.atlassian.net/wiki/spaces/DTP/pages/3358163096/Creating+custom+visualizations?atlOrigin=eyJpIjoiMzkzNzA2MDkyNjQ2NDM4YmIzMGJmM2FjMDhkYTlmNGMiLCJwIjoiYyJ9) - Complete process for creating charts and visual analysis
* SQL Cookbook\[LINK] - Advanced query patterns organized by analytical scenario
* [Bronze layer documentation](https://squaregps.atlassian.net/wiki/spaces/DTP/pages/3208282197/Bronze+layer?atlOrigin=eyJpIjoiMjg3ZjNjYTg5ZmFmNDJjZTgxNzllMTk1OTM5NDM3ZWEiLCJwIjoiYyJ9) - Complete database schema reference and field definitions

> \[!INFO] **Production Analytics**: For enterprise-scale reporting and dashboards, consider dedicated BI tools that connect directly to your PTL instance for enhanced scalability and collaboration features. Learn more in [Selecting BI tools](https://squaregps.atlassian.net/wiki/spaces/DTP/pages/3247505491/Selecting+BI+tools?atlOrigin=eyJpIjoiZTc2NjFhNjk1YmYyNDY3ZWJmNDVkNGUwNTA1YTVkYTkiLCJwIjoiYyJ9).
