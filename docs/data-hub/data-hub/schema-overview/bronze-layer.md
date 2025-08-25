# Bronze layer

There are 2 data schemes at Bronze layer:

* raw\_busidess\_data - containing tables, attributes and values related to business information, such as vehicles , employees, geofences added by users, etc.
* raw\_telematics\_data - containing tables, attributes and values, related to the telematics data transmitting from devices under monitoring, such as locations, inputs, outputs, events.

Please find detailed information about data schemas below.

## `raw_business_data` structure

This schema contains 40+ carefully selected tables to cover many business aspects and use cases. These tables represent your core business entities, organizational structure, and operational data.

!\[V2 business bronze.svg]\(attachments/V2 business bronze.svg)

{% hint style="info" %}
The interactive diagram of raw\_business\_data schema is available on **dbdiagram.io** - [https://dbdiagram.io/d/V2-business-bronze-67c1961c263d6cf9a0cb4e97](https://dbdiagram.io/d/V2-business-bronze-67c1961c263d6cf9a0cb4e97)
{% endhint %}

Find raw business data schema details below.

```sql
Table "vehicle_service_tasks" {
  "record_added_at" timestamp [not null]
  "start_mileage" numeric
  "comment" "character varying(255)"
  "status" "character varying(10)" [not null]
  "completion_date" timestamp
  "start_engine_hours" numeric
  "service_task_id" integer [not null]
  "is_notification_push_enabled" boolean [not null]
  "date_notification_interval" interval
  "predicted_datetime" timestamp
  "cost" numeric [not null]
  "mileage_limit" numeric
  "notification_emails" text
  "is_unplanned" boolean [not null]
  "is_repeat" boolean [not null]
  "completion_engine_hours" integer
  "engine_hours_limit" numeric
  "mileage_repeat_interval" integer
  "vehicle_id" integer [not null]
  "engine_hours_notification_interval" integer
  "start_date" timestamp
  "mileage_notification_interval" integer
  "date_repeat_interval" interval
  "description" "character varying(255)"
  "notification_sms_phone_numbers" text
  "end_date" timestamp
  "engine_hours_repeat_interval" integer
  "completion_mileage" integer
}

Table "garages" {
  "record_added_at" timestamp [not null]
  "garage_id" integer [not null]
  "longitude" numeric
  "mechanic_name" "character varying(255)"
  "radius" integer [not null]
  "latitude" numeric
  "organization_label" "character varying(255)"
  "user_id" integer [not null]
  "dispatcher_name" "character varying(255)"
  "address" "character varying(255)"
}

Table "driver_history" {
  "server_datetime" timestamp [not null]
  "address" "character varying(255)"
  "updated_by" integer [not null]
  "object_id" integer
  "longitude" numeric
  "latitude" numeric
  "driver_history_id" integer [not null]
  "hardware_key" "character varying(64)"
  "new_employee_id" integer
  "changed_datetime" timestamp
  "record_added_at" timestamp [not null]
  "old_employee_id" integer
}

Table "departments" {
  "record_added_at" timestamp [not null]
  "department_label" "character varying(255)" [not null]
  "latitude" numeric
  "department_id" integer [not null]
  "address" "character varying(255)"
  "radius" integer [not null]
  "longitude" numeric
  "user_id" integer [not null]
}

Table "checkins" {
  "radius" integer [not null]
  "latitude" numeric [not null]
  "employee_id" integer [not null]
  "longitude" numeric [not null]
  "record_added_at" timestamp [not null]
  "actual_datetime" timestamp [not null]
  "user_id" integer [not null]
  "form_id" integer [not null]
  "address" "character varying(255)"
  "planned_datetime" timestamp [not null]
  "object_id" integer [not null]
  "checkin_id" integer [not null]
  "comment" text
}

Table "statuses" {
  "order_sort" integer [not null]
  "listing_id" integer [not null]
  "color" "character varying(6)" [not null]
  "status_id" integer [not null]
  "status_label" "character varying(200)" [not null]
  "record_added_at" timestamp [not null]
  "is_deleted" boolean [not null]
}

Table "places_linked_entity_fields" {
  "value" bigint [not null]
  "record_added_at" timestamp [not null]
  "place_id" integer [not null]
  "field_id" integer [not null]
}

Table "places_text_fields" {
  "place_id" integer [not null]
  "record_added_at" timestamp [not null]
  "value" text [not null]
  "field_id" integer [not null]
}

Table "users2zones" {
  "zone_id" integer [not null]
  "record_added_at" timestamp [not null]
  "user_id" integer [not null]
}

Table "objects" {
  "record_added_at" timestamp [not null]
  "create_datetime" timestamp [not null]
  "client_id" integer [not null]
  "group_id" integer
  "object_label" "character varying(100)"
  "model" "character varying(64)"
  "is_clone" boolean [not null]
  "is_deleted" boolean [not null]
  "device_id" integer [not null]
  "object_id" integer [not null]
}

Table "device_output_name" {
  "device_id" integer [not null]
  "record_added_at" timestamp [not null]
  "label" "character varying(100)" [not null]
  "number" integer [not null]
}

Table "subusers2trackers" {
  "record_id" integer [not null]
  "record_added_at" timestamp [not null]
  "object_id" integer [not null]
  "subuser_id" integer [not null]
}

Table "geofence_points" {
  "longitude" numeric [not null]
  "number" integer [not null]
  "zone_id" integer [not null]
  "record_added_at" timestamp [not null]
  "latitude" numeric [not null]
}

Table "custom_fields" {
  "record_added_at" timestamp [not null]
  "entity_id" integer [not null]
  "is_required" boolean [not null]
  "custom_field_label" text [not null]
  "parameters" jsonb
  "custom_field_type" integer [not null]
  "description" text
  "custom_field_id" integer [not null]
}

Table "places_decimal_fields" {
  "field_id" integer [not null]
  "record_added_at" timestamp [not null]
  "place_id" integer [not null]
  "value" numeric [not null]
}

Table "task_history" {
  "task_id" integer [not null]
  "activity" integer [not null]
  "task_history_id" integer [not null]
  "record_added_at" timestamp [not null]
  "user_id" integer [not null]
  "event_datetime" timestamp [not null]
  "payload" text
}

Table "tags" {
  "tag_label" "character varying(64)" [not null]
  "color" "character varying(6)"
  "user_id" integer [not null]
  "record_added_at" timestamp [not null]
  "tag_id" integer [not null]
}

Table "places" {
  "description" text
  "custom_fields" jsonb
  "place_id" integer [not null]
  "external_id" "character varying(32)"
  "record_added_at" timestamp [not null]
  "user_id" integer
  "latitude" numeric
  "radius" integer
  "place_label" "character varying(256)"
  "assigned_datetime" timestamp
  "address" "character varying(256)"
  "longitude" numeric
}

Table "status_listings" {
  "user_id" integer [not null]
  "is_supervisor_controlled" boolean [not null]
  "is_deleted" boolean [not null]
  "status_listing_id" integer [not null]
  "is_employee_controlled" boolean [not null]
  "record_added_at" timestamp [not null]
  "status_listing_label" "character varying(200)" [not null]
}

Table "models" {
  "record_added_at" timestamp [not null]
  "model_id" integer [not null]
  "has_battery_level" boolean [not null]
  "alternative_label" "character varying(50)" [not null]
  "vendor" "character varying(30)" [not null]
  "is_clone" boolean
  "has_altitude" boolean [not null]
  "has_phone" boolean [not null]
  "type_output_control" "character varying(30)" [not null]
  "has_gsm_roaming" boolean [not null]
  "has_gsm_level" boolean [not null]
  "model" "character varying(255)" [not null]
  "type_special_control" "character varying(255)" [not null]
  "digital_amount" integer [not null]
  "has_detach_button" boolean [not null]
  "has_gsm_name" boolean [not null]
  "analog_amount" integer [not null]
  "outputs_amount" integer [not null]
}

Table "vehicle_trackers_history" {
  "vehicle_id" integer [not null]
  "record_added_at" timestamp [not null]
  "object_id" integer [not null]
  "changed_datetime" timestamp [not null]
  "vehicle_tracker_history_id" integer [not null]
}

Table "groups" {
  "group_id" integer [not null]
  "group_color" "character varying(6)" [not null]
  "group_label" "character varying(255)" [not null]
  "client_id" integer [not null]
  "record_added_at" timestamp [not null]
}

Table "sensor_description" {
  "record_added_at" timestamp [not null]
  "parameters" jsonb
  "input_id" integer [not null]
  "accuracy" numeric [not null]
  "sensor_units" "character varying(10)"
  "multiplier" doubleprecision [not null]
  "input_label" "character varying(64)"
  "sensor_label" "character varying(100)"
  "units_type" integer [not null]
  "divider" doubleprecision [not null]
  "group_id" integer [not null]
  "sensor_id" integer [not null]
  "device_id" integer [not null]
  "sensor_type" "character varying(45)" [not null]
  "group_type" integer [not null]
}

Table "entities" {
  "entity_label" jsonb
  "record_added_at" timestamp [not null]
  "entity_id" integer [not null]
  "builtin_type" integer [not null]
  "user_id" integer [not null]
}

Table "zones" {
  "address" "character varying(255)"
  "radius" integer [not null]
  "zone_id" integer [not null]
  "circle_center_latitude" numeric [not null]
  "client_id" integer [not null]
  "zone_label" "character varying(100)"
  "color" "character varying(6)" [not null]
  "zone_type" "character varying(20)" [not null]
  "circle_center_longitude" numeric [not null]
  "latitude" numeric [not null]
  "record_added_at" timestamp [not null]
  "longitude" numeric [not null]
}

Table "vehicles" {
  "vehicle_id" integer [not null]
  "payload_length" numeric
  "vin" "character varying(20)"
  "free_insurance_policy_number" "character varying(50)"
  "vehicle_label" "character varying(100)"
  "payload_width" numeric
  "color" "character varying(6)"
  "trailer" "character varying(255)"
  "object_id" integer
  "vehicle_status_id" integer
  "liability_insurance_valid_till" timestamp
  "manufacture_year" integer
  "fuel_grade" "character varying(16)"
  "fuel_cost" numeric
  "fuel_tank_volume" numeric
  "model" "character varying(100)"
  "garage_id" integer
  "payload_height" numeric
  "max_speed" numeric
  "registration_number" "character varying(32)"
  "tyre_size" "character varying(50)"
  "passenger_capacity" integer
  "record_added_at" timestamp [not null]
  "trailer_reg_number" "character varying(32)"
  "free_insurance_valid_till_date" timestamp
  "gross_weight" numeric
  "standard_fuel_consumption" numeric
  "fuel_type" integer
  "payload_weight" numeric
  "additional_info" text
  "vehicle_subtype" "character varying(32)"
  "liability_insurance_policy_number" "character varying(50)"
  "frame_number" "character varying(32)"
  "user_id" integer [not null]
  "vehicle_type" integer [not null]
  "chassis_number" "character varying(32)"
  "tyres_number" integer
  "wheel_arrangement" "character varying(16)"
}

Table "tag_links" {
  "entity_id" integer [not null]
  "record_added_at" timestamp [not null]
  "entity_type" integer [not null]
  "ordinal" integer [not null]
  "tag_id" integer [not null]
}

Table "rules" {
  "rule_id" integer [not null]
  "object_id" integer [not null]
  "parameters" jsonb
  "alert_phone" "character varying(210)" [not null]
  "event_type" "character varying(100)" [not null]
  "client_id" integer [not null]
  "is_push_enabled" boolean [not null]
  "event_comment1" "character varying(255)" [not null]
  "event_label" "character varying(255)" [not null]
  "description" "character varying(255)" [not null]
  "record_added_at" timestamp [not null]
  "alert_sms" text [not null]
  "event_group" integer [not null]
  "created_at" timestamp [not null]
  "maximum" integer [not null]
  "is_deleted" boolean [not null]
  "alert_email" text [not null]
  "event_comment2" "character varying(255)" [not null]
}

Table "status_history" {
  "longitude" numeric
  "new_status_id" integer
  "status_history_id" integer [not null]
  "device_id" integer [not null]
  "updated_by" integer [not null]
  "address" "character varying(255)"
  "latitude" numeric
  "record_added_at" timestamp [not null]
  "server_datetime" timestamp [not null]
  "changed_datetime" timestamp
  "old_status_id" integer
}

Table "rules2zones" {
  "zone_id" integer [not null]
  "record_added_at" timestamp [not null]
  "rule_id" integer [not null]
}

Table "forms" {
  "object_id" integer [not null]
  "description" text
  "form_label" "character varying(255)" [not null]
  "fields" text
  "created_at" timestamp [not null]
  "submission_address" "character varying(255)"
  "submission_latitude" numeric
  "form_id" integer [not null]
  "submission_longitude" numeric
  "is_submission_in_zone" boolean [not null]
  "values" text
  "record_added_at" timestamp [not null]
  "task_id" integer
  "submitted_at" timestamp
}

Table "sensor_calibration_data" {
  "value" numeric [not null]
  "sensor_id" integer [not null]
  "record_added_at" timestamp [not null]
  "volume" numeric [not null]
  "device_id" integer [not null]
  "sensor_calibration_id" bigint [not null]
}

Table "rules2objects" {
  "object_params" jsonb
  "param_group_number" integer [not null]
  "object_id" integer [not null]
  "record_added_at" timestamp [not null]
  "rule_id" integer [not null]
}

Table "tasks" {
  "time_from" timestamp
  "stay_duration_minutes" interval
  "external_id" "character varying(100)"
  "object_id" integer
  "task_type" integer
  "arrival_duration_minutes" interval
  "status" integer
  "arrival_datetime" timestamp
  "record_added_at" timestamp [not null]
  "task_id" integer [not null]
  "user_id" integer
  "status_change_datetime" timestamp
  "order_sort" integer
  "time_to" timestamp
  "max_delay_minuts" integer
  "is_stay_control_enabled" boolean
  "address" "character varying(255)"
  "task_label" "character varying(200)" [not null]
  "longitude" numeric
  "created_by" integer
  "description" text [not null]
  "radius" integer
  "latitude" numeric
  "stay_duration" integer
  "created_at" timestamp [not null]
  "custom_fields" jsonb
  "parent_task_id" integer
}

Table "places_bigint_fields" {
  "field_id" integer [not null]
  "value" bigint [not null]
  "place_id" integer [not null]
  "record_added_at" timestamp [not null]
}

Table "devices" {
  "is_sim_blocked" boolean [not null]
  "device_id" integer [not null]
  "device_imei" "character varying(64)" [not null]
  "network_label" "character varying(50)" [not null]
  "status_listing_id" integer [not null]
  "signal_level" numeric [not null]
  "phone" "character varying(32)" [not null]
  "has_roaming" boolean [not null]
  "created_at" timestamp [not null]
  "owner_id" integer [not null]
  "record_added_at" timestamp [not null]
}

Table "description_parametrs" {
  "description" "character varying(150)"
  "record_added_at" timestamp [not null]
  "type" "character varying(100)" [not null]
  "key" integer [not null]
}

Table "users" {
  "company_label" "character varying(255)" [not null]
  "registration_datetime" timestamp
  "first_name" "character varying(100)" [not null]
  "master_id" integer
  "last_name" "character varying(100)" [not null]
  "birth_date" timestamp
  "timezone_label" "character varying(30)"
  "middle_name" "character varying(100)" [not null]
  "user_id" integer [not null]
  "locale" "character varying(10)" [not null]
  "record_added_at" timestamp [not null]
}

Table "counters" {
  "sensor_id" integer
  "multiplier" numeric [not null]
  "counter_id" integer [not null]
  "device_id" integer [not null]
  "counter_type" integer [not null]
  "record_added_at" timestamp [not null]
}

Table "employees" {
  "driver_license_valid_till" timestamp
  "record_added_at" timestamp [not null]
  "last_name" "character varying(100)"
  "department_id" integer
  "citizen_id_number" "character varying(32)"
  "first_name" "character varying(100)"
  "driver_license_categories" "character varying(32)"
  "user_id" integer [not null]
  "phone_number" "character varying(32)"
  "object_id" integer
  "is_deleted" boolean [not null]
  "driver_license_issue_date" boolean
  "hardware_key" "character varying(64)"
  "middle_name" "character varying(100)"
  "address" "character varying(255)"
  "latitude" numeric
  "employee_id" integer [not null]
  "personnel_number" "character varying(15)"
  "fuel_cost" doubleprecision
  "driver_license_number" "character varying(32)"
  "email" "character varying(100)"
  "fuel_consumption" doubleprecision
  "radius" integer [not null]
  "longitude" numeric
}

Table "places_longtext_fields" {
  "field_id" integer [not null]
  "value" text [not null]
  "record_added_at" timestamp [not null]
  "place_id" integer [not null]
}


Table "raw_device_data" {
  "device_id" integer 
  "device_time" timestamp 
  "created_at" timestamp 
  "gps_fix_type" integer 
  "longitude" integer 
  "latitude" integer 
  "altitude" integer 
  "speed" integer 
  "satellites" integer 
  "hdop" integer [default:"'-1'::integer"]
  "event_id" integer 
  "inputs" jsonb 
  "states" jsonb 
}

// Relationships

Ref: checkins.employee_id > employees.employee_id
Ref: checkins.object_id > objects.object_id
Ref: checkins.form_id > forms.form_id
Ref: counters.sensor_id > sensor_description.sensor_id
Ref: counters.device_id > devices.device_id
Ref: custom_fields.entity_id > entities.entity_id
Ref: departments.department_id < employees.department_id
Ref: departments.user_id > users.user_id
Ref: description_parametrs.key < counters.counter_type
Ref: description_parametrs.key < custom_fields.custom_field_type
Ref: description_parametrs.key < driver_history.updated_by
Ref: description_parametrs.key < entities.builtin_type
Ref: description_parametrs.key < sensor_description.units_type
Ref: description_parametrs.key < status_history.updated_by
Ref: description_parametrs.key < tasks.status
Ref: description_parametrs.key < tasks.created_at
Ref: description_parametrs.key < tasks.task_type
Ref: description_parametrs.key < vehicles.fuel_type
Ref: description_parametrs.key < task_history.activity
Ref: description_parametrs.key < sensor_description.group_type
Ref: device_output_name.device_id > devices.device_id
Ref: devices.status_listing_id > status_listings.status_listing_id
Ref: driver_history.new_employee_id > employees.employee_id
Ref: driver_history.old_employee_id > employees.employee_id
Ref: driver_history.object_id > objects.object_id
Ref: employees.object_id > objects.object_id
Ref: employees.user_id > users.user_id
Ref: entities.user_id > users.user_id
Ref: forms.task_id > tasks.task_id
Ref: forms.object_id > objects.object_id
Ref: tasks.object_id > objects.object_id
Ref: garages.user_id > users.user_id
Ref: groups.client_id <> objects.client_id
Ref: models.model < objects.model
Ref: objects.device_id > devices.device_id
Ref: places.user_id > users.user_id
Ref: places_bigint_fields.field_id > custom_fields.custom_field_id
Ref: places_bigint_fields.place_id > places.place_id
Ref: places_decimal_fields.field_id > custom_fields.custom_field_id
Ref: places_decimal_fields.place_id > places.place_id
Ref: places_linked_entity_fields.field_id > custom_fields.custom_field_id
Ref: places_linked_entity_fields.place_id > places.place_id
Ref: places_longtext_fields.field_id > custom_fields.custom_field_id
Ref: places_longtext_fields.place_id > places.place_id
Ref: places_text_fields.field_id > custom_fields.custom_field_id
Ref: places_text_fields.place_id > places.place_id
Ref: rules.rule_id < rules2zones.rule_id
Ref: rules2objects.object_id > objects.object_id
Ref: rules2objects.object_id > rules.rule_id
Ref: rules2zones.zone_id > zones.zone_id
Ref: sensor_calibration_data.device_id > sensor_description.sensor_id
Ref: sensor_calibration_data.sensor_id > sensor_description.device_id
Ref: sensor_description.device_id > devices.device_id
Ref: status_history.new_status_id > statuses.status_id
Ref: status_history.old_status_id > statuses.status_id
Ref: status_history.device_id > devices.device_id
Ref: status_listings.user_id > users.user_id
Ref: statuses.listing_id > status_listings.status_listing_id
Ref: subusers2trackers.object_id > objects.object_id
Ref: subusers2trackers.subuser_id > users.user_id
Ref: tag_links.tag_id > tags.tag_id
Ref: tags.user_id > users.user_id
Ref: task_history.task_id > tasks.task_id
Ref: task_history.user_id > users.user_id
Ref: tasks.parent_task_id < tasks.task_id
Ref: tasks.user_id > users.user_id
Ref: users.master_id < users.user_id
Ref: users2zones.user_id > users.user_id
Ref: users2zones.zone_id > zones.zone_id
Ref: vehicle_service_tasks.vehicle_id > vehicles.vehicle_id
Ref: vehicle_trackers_history.object_id > objects.object_id
Ref: vehicle_trackers_history.vehicle_id > vehicles.vehicle_id
Ref: vehicles.garage_id > garages.garage_id
Ref: vehicles.object_id > objects.object_id
Ref: vehicles.user_id > users.user_id
Ref: geofence_points.zone_id > zones.zone_id
Ref: "sensor_calibration_data"."value" < "sensor_calibration_data"."device_id"
Ref: "devices"."device_id"	<	"raw_device_data"."device_id"
Ref: users.user_id < devices.owner_id
Ref: users.user_id < objects.client_id
```

### Update frequency

Data in this schema is synchronized with the core DB. Updates occur incrementally as changes happen in the source MySQL database, typically less than 5 minutes of the source change.

## `description_parametrs`

The system includes reference data to standardize values across the database:

| **Reference Type**     | **Description**               | **Example Values**                         |
| ---------------------- | ----------------------------- | ------------------------------------------ |
| Type definitions       | Standard entity types         | `vehicle_type: car, truck, bus`            |
| Status codes           | Task and system status values | `tasks_status: unassigned, assigned, done` |
| Unit definitions       | Measurement units for sensors | `units_type: liter, gallon, celsius`       |
| Entity classifications | Business entity categories    | `entities_type: place, task, customer`     |

### Key tables by category

The tables in the `raw_business_data` schema are organized into functional categories for easier navigation. The table below summarizes key tables by their business purpose:

| **Category**                 | **Table Name**                     | **Description**                        |
| ---------------------------- | ---------------------------------- | -------------------------------------- |
| **Organizational structure** | users                              | User accounts with profile information |
| departments                  | Departments with geolocation data  |                                        |
| employees                    | Employee and driver details        |                                        |
| groups                       | Tracker organization groups        |                                        |
| **Objects and devices**      | devices                            | Physical tracking devices              |
| models                       | Device model specifications        |                                        |
| objects                      | Monitored objects                  |                                        |
| vehicles                     | Vehicle details and specifications |                                        |
| sensor\_description          | Sensor configuration details       |                                        |
| **Places and zones**         | places                             | Points of interest with geolocation    |
| zones                        | Geofenced monitoring areas         |                                        |
| garages                      | Vehicle service locations          |                                        |
| tags                         | Organizational labels              |                                        |
| **Operational data**         | tasks                              | Task assignments and tracking          |
| forms                        | Data collection forms              |                                        |
| checkins                     | Location-based attendance records  |                                        |
| events                       | System events and notifications    |                                        |
| statuses                     | Status definitions                 |                                        |
| vehicle\_service\_tasks      | Vehicle maintenance records        |                                        |

## `raw_telematics_data` structure

The `raw_telematics_data` schema contains three primary table types that work together to provide comprehensive device data.

![Navixy PLT - Bronze layer raw telematics data ERD](attachments/image-20250401-075804.png)

{% hint style="info" %}
The interactive diagram of raw\_telematics\_data schema is available on **dbdiagram.io** - [https://dbdiagram.io/d/v1-schema-telematik-bd-67a0acef263d6cf9a0d8e750](https://dbdiagram.io/d/v1-schema-telematik-bd-67a0acef263d6cf9a0d8e750)
{% endhint %}

Find raw telematics data schema details below.

```sql
Table tracking_data_core {
  device_id integer
  device_time timestampz
  platform_time timestampz
  record_added_at timestampz [default: `now()`]
  latitude integer
  longitude integer
  speed integer
  altitude integer
  satellites integer
  event_id integer
  gps_fix_type integer
  hdop integer

  indexes {(device_id, device_time)}
}

Table inputs {
  input_id integer [primary key]
  device_id integer
  record_added_at timestampz [default: `now()`]
  device_time timestampz 
  sensor_name text
  value text
  
  indexes {(device_id, device_time)}
}

Table states {
  state_id integer [primary key]
  device_id serial
  record_added_at timestampz [default: `now()`]
  device_time timestampz 
  state_name text
  value text
  
  indexes {(device_id, device_time)}
}

Ref: inputs.(device_id, device_time) > tracking_data_core.(device_id, device_time)
Ref: states.(device_id, device_time) > tracking_data_core.(device_id, device_time)

```

Each table serves a specific purpose in capturing different aspects of device information:

#### `tracking_data_core`

**Purpose**: Core location and motion data

| **Attribute**     | **Details**                                                                                                                                                                                        |
| ----------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Key Fields**    | `device_id`, `device_time`, `platform_time`, `latitude`, `longitude`, `speed`, `altitude`, `satellites`, `hdop`, `event_id`                                                                        |
| **Indexing**      | Optimized with index on (`device_id`, `device_time`)                                                                                                                                               |
| **Special Notes** | <p>Location data (latitude and longitude) uses integer format with 10⁷ precision for optimal TimescaleDB performance<br><br>Speed is also stored in integer, so you need to divide it with 100</p> |

#### `inputs`

**Purpose**: Sensor readings from devices

| **Attribute**     | **Details**                                                                        |
| ----------------- | ---------------------------------------------------------------------------------- |
| **Key Fields**    | `input_id`, `device_id`, `device_time`, `sensor_name`, `value`                     |
| **Content**       | Analog readings (fuel level, temperature, voltage), calculated values (engine RPM) |
| **Relationships** | Linked to `tracking_data_core` via `device_id` and `device_time`                   |

#### `states`

**Purpose**: Device status indicators and operational modes

| **Attribute**    | **Details**                                                                          |
| ---------------- | ------------------------------------------------------------------------------------ |
| **Key Fields**   | `state_id`, `device_id`, `device_time`, `state_name`, `value`                        |
| **Content**      | Operating mode indicators (working, idle, off), component statuses (ignition, doors) |
| **Value Format** | Boolean values (1/0) or specific status codes                                        |

Data in this schema is ingested directly from devices, with minimal latency (typically seconds) . The schema is optimized for time-series data using TimescaleDB for efficient storage and retrieval.

## Additional information

### Data validation

The database enforces data integrity through multiple mechanisms:

* **CHECK constraints** validate that values fall within acceptable ranges
* **Foreign keys** ensure relationships between tables remain consistent
* **NOT NULL constraints** guarantee that required fields always have values
* **DEFAULT values** provide fallback when data isn't explicitly provided

### Query optimization

Tables are organized with specific indexing strategies:

* All tables include **time-based indexes** on `record_added_at`
* Foreign key columns have dedicated indexes for join performance
* Frequently used column combinations have **composite indexes**
* TimescaleDB provides specialized indexes for time-series queries
