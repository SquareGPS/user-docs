# Logic node expressions and syntax

## Expression fundamentals

The Logic node uses the [Navixy IoT Logic Expression Language](https://www.navixy.com/docs/iot-logic-api/technologies/navixy-iot-logic-expression-language), which is based on Java Expression Language (JEXL). All expressions must return a boolean value (true/false) for proper node operation.

**Expression evaluation**: Expressions are evaluated from left to right, and you can use parentheses to control the order of operations.

**Basic syntax example**:

```
condition1 && (condition2 || condition3 > condition4)
```

## Available operators

### Comparison operators

| Operator | Description |
| --- | --- |
| `==` | Checks if two operands are equal. If operands are of different types, JEXL converts them to one if possible |
| `!=` | Checks for inequality of two operands. Returns true if operands are not equal |
| `<` | Checks that the left operand is smaller than the right operand |
| `<=` | Checks that the left operand is smaller or equal to the right operand |
| `>` | Checks that the left operand is larger than the right operand |
| `>=` | Checks that the left operand is larger or equal to the right operand |

### Logical operators

| Operator | Description |
| --- | --- |
| `&&` or `and` | Logical AND - checks if two conditions are true. Returns true if both conditions are true |
| `\|` or `or` | Logical OR - checking for the truth of at least one of the two conditions |
| `!` or `not` | Logical NOT - converts the result of the condition to the opposite value |

### Pattern matching operators

| Operator | Description |
| --- | --- |
| `=~` | Checks if the value of the left operand is in the set of the right operand. For strings, checks for regex pattern match |
| `!~` | Checks if the value of the left operand is not in the set of the right operand. For strings, checks for regex pattern mismatch |
| `=^` | Checks that the left string operand starts with the right string operand |
| `!^` | Checks that the left string operand doesn't start with the right string operand |
| `=$` | Checks that the left string operand ends with the right string operand |
| `!$` | Checks that the left string operand doesn't end with the right string operand |

## Expression examples

![](https://squaregps.atlassian.net/wiki/images/icons/grey_arrow_down.png)

Basic condition examples

**Equality checks**:

```
value('lock_state', 0, 'valid') == 'sealed'
door_state_2 == 0
```

**Inequality checks**:

```
value('lock_state', 1, 'valid') != 'unknown'
avl_io_221 != null
```

**Numeric comparisons**:

```
value('humidity', 1, 'all') < 80
value('humidity', 1, 'all') <= 80
value('humidity', 0, 'valid') > 80
value('humidity', 0, 'valid') >= 80
```

**Temperature monitoring**:

```
value('temperature', 0, 'valid') > 75
```

This expression triggers when temperature exceeds 75 degrees, useful for overheating alerts.

**Speed violation detection**:

```
value('speed', 0, 'valid') > 80
```

This expression identifies when vehicles exceed 80 km/h speed limits.

**Device health monitoring**:

```
value('battery_voltage', 0, 'valid') < 11.5
```

This expression detects low battery conditions requiring maintenance attention.

**Fuel level alerts**:

```
value('fuel_level', 0, 'valid') < 20
```

This expression identifies when fuel levels drop below 20%, enabling proactive refueling.

![](https://squaregps.atlassian.net/wiki/images/icons/grey_arrow_down.png)

Logical operator examples

**AND operations**:

```
value('temperature', 0, 'valid') > 15 && value('humidity', 0, 'valid') > 80
value('temperature', 0, 'valid') > 15 and value('humidity', 0, 'valid') > 80
```

**OR operations**:

```
temperature < 10 || humidity > 80
temperature < 10 or humidity > 80
```

**NOT operations**:

```
!condition
not condition
```

![](https://squaregps.atlassian.net/wiki/images/icons/grey_arrow_down.png)

Pattern matching examples

**Set membership**:

```
value('lock_state', 0, 'valid') =~ ['locked','unlocked']
value('driver_name', 0, 'valid') !~ ['John', 'Steve']
```

**String pattern matching**:

```
driver_id =^ 'cc6f8216'
driver_id !^ 'cc6f8216'
value('engine_hours', 0, 'valid') =$ '1000'
value('driver_id', 0, 'valid') !$ '8b38851c3c68'
```

![](https://squaregps.atlassian.net/wiki/images/icons/grey_arrow_down.png)

Complex multi-condition examples

**After-hours speeding alert**:

```
value('speed', 0, 'valid') > 60 && (value('current_hour', 0, 'valid') >= 18 || value('current_hour', 0, 'valid') <= 6)
```

This combines speed monitoring with time-based conditions for enhanced safety oversight during night shifts.

**Comprehensive device diagnostics**:

```
value('gps_satellites', 0, 'valid') >= 4 && value('battery_voltage', 0, 'valid') > 11.5 && value('signal_strength', 0, 'valid') > -80
```

This validates multiple device health parameters simultaneously to ensure reliable operation.

**Driver safety monitoring**:

```
value('harsh_braking', 0, 'valid') == true && value('driver_identified', 0, 'valid') == false
```

This identifies unsafe driving behavior when the driver isn't properly identified in the system.

**Equipment maintenance scheduling**:

```
value('engine_hours', 0, 'valid') > 250 && value('last_maintenance', 0, 'valid') > 30
```

This triggers maintenance alerts when engine hours exceed thresholds and maintenance is overdue.

**Temperature range compliance**:

```
value('cargo_temperature', 0, 'valid') < -18 || value('cargo_temperature', 0, 'valid') > 4
```

This detects when refrigerated cargo temperatures fall outside the acceptable range.

![](https://squaregps.atlassian.net/wiki/images/icons/grey_arrow_down.png)

Expression complexity and parentheses

You can create complex expressions by combining multiple conditions with parentheses to control evaluation order:

**Complex safety validation**:

```
!driver_identified && (vibration_active || speed > 3)
```

**Multi-parameter equipment check**:

```
(value('oil_pressure', 0, 'valid') < 20 || value('coolant_temp', 0, 'valid') > 95) && value('engine_running', 0, 'valid') == true
```

## Error handling scenarios

| Scenario | Result | Flow Path | Attribute Value |
| --- | --- | --- | --- |
| Expression evaluates to `true` | Success | THEN connection | `true` |
| Expression evaluates to `false` | Success | ELSE connection | `false` |
| Referenced attribute is `null` | Treated as `false` | ELSE connection | `false` |
| Syntax error in expression | Treated as `false` | ELSE connection | `null` |
| Referenced attribute doesn't exist | Treated as `false` | ELSE connection | `null` |

## Practical implementation examples

![](https://squaregps.atlassian.net/wiki/images/icons/grey_arrow_down.png)

Fleet temperature monitoring

**Business requirement**: Monitor refrigerated vehicles to ensure cargo temperature compliance

```
value('cargo_temperature', 0, 'valid') > 4 || value('cargo_temperature', 0, 'valid') < -18
```

- **THEN path**: Send immediate alerts to dispatch, log compliance violations, trigger corrective actions
- **ELSE path**: Continue normal processing for compliant temperatures, update status dashboards

![](https://squaregps.atlassian.net/wiki/images/icons/grey_arrow_down.png)

Driver safety enforcement

**Business requirement**: Identify unsafe driving patterns during active shift hours

```
value('harsh_acceleration', 0, 'valid') == true && value('shift_active', 0, 'valid') == true
```

- **THEN path**: Generate driver coaching reports, send safety notifications, log incidents
- **ELSE path**: Process normal driving behavior data, update performance metrics

![](https://squaregps.atlassian.net/wiki/images/icons/grey_arrow_down.png)

Predictive maintenance alerts

**Business requirement**: Detect potential equipment failures before they occur

```
value('engine_temperature', 0, 'valid') > 95 && value('oil_pressure', 0, 'valid') < 30
```

- **THEN path**: Schedule maintenance appointments, send technician alerts, log diagnostic data
- **ELSE path**: Continue routine monitoring, update equipment health dashboards

![](https://squaregps.atlassian.net/wiki/images/icons/grey_arrow_down.png)

Geofence compliance monitoring

**Business requirement**: Ensure vehicles operate within authorized areas during business hours

```
(value('latitude', 0, 'valid') < 40.7489 || value('latitude', 0, 'valid') > 40.7589) && value('business_hours', 0, 'valid') == true
```

- **THEN path**: Generate unauthorized location alerts, notify security, log violations
- **ELSE path**: Continue normal operations logging, update location tracking