# Expresiones y sintaxis del nodo Logic

### Fundamentos de expresiones

El nodo Logic utiliza [Lenguaje de Expresión IoT Logic de Navixy](https://app.gitbook.com/s/tx3J5BxnWyPV0nP2xr0z/technologies/navixy-iot-logic-expression-language), que se basa en Java Expression Language (JEXL). Todas las expresiones deben devolver un valor booleano (verdadero/falso) para el funcionamiento adecuado del nodo.

**Evaluación de expresiones**: Las expresiones se evalúan de izquierda a derecha, y puede usar paréntesis para controlar el orden de las operaciones.

**Ejemplo de sintaxis básica**:

```
condicion1 && (condicion2 || condicion3 > condicion4)
```

### Operadores disponibles

#### Operadores de comparación

| Operador | Descripción                                                                                                             |
| -------- | ----------------------------------------------------------------------------------------------------------------------- |
| ==       | Verifica si dos operandos son iguales. Si los operandos son de diferentes tipos, JEXL los convierte a uno si es posible |
| !=       | Verifica la desigualdad de dos operandos. Devuelve verdadero si los operandos no son iguales                            |
| <        | Verifica que el operando izquierdo sea menor que el operando derecho                                                    |
| <=       | Verifica que el operando izquierdo sea menor o igual al operando derecho                                                |
| >        | Verifica que el operando izquierdo sea mayor que el operando derecho                                                    |
| >=       | Verifica que el operando izquierdo sea mayor o igual al operando derecho                                                |

#### Operadores lógicos

| Operador  | Descripción                                                                                                   |
| --------- | ------------------------------------------------------------------------------------------------------------- |
| && o and  | Y lógico - verifica si dos condiciones son verdaderas. Devuelve verdadero si ambas condiciones son verdaderas |
| \|\| o or | O lógico - verifica la veracidad de al menos una de las dos condiciones                                       |
| ! o not   | NO lógico - convierte el resultado de la condición al valor opuesto                                           |

#### Operadores de coincidencia de patrones

| Operador | Descripción                                                                                                                                        |
| -------- | -------------------------------------------------------------------------------------------------------------------------------------------------- |
| =\~      | Verifica si el valor del operando izquierdo está en el conjunto del operando derecho. Para cadenas, verifica la coincidencia de patrón regex       |
| !\~      | Verifica si el valor del operando izquierdo no está en el conjunto del operando derecho. Para cadenas, verifica la no coincidencia de patrón regex |
| =^       | Verifica que el operando de cadena izquierdo comience con el operando de cadena derecho                                                            |
| !^       | Verifica que el operando de cadena izquierdo no comience con el operando de cadena derecho                                                         |
| =$       | Verifica que el operando de cadena izquierdo termine con el operando de cadena derecho                                                             |
| !$       | Verifica que el operando de cadena izquierdo no termine con el operando de cadena derecho                                                          |

### Ejemplos de expresiones

<details>

<summary>Ejemplos de condiciones básicas</summary>

**Verificaciones de igualdad**:

```
value('lock_state', 0, 'valid') == 'sealed'
door_state_2 == 0
```

**Verificaciones de desigualdad**:

```
value('lock_state', 1, 'valid') != 'unknown'
avl_io_221 != null
```

**Comparaciones numéricas**:

```
value('humidity', 1, 'all') < 80
value('humidity', 1, 'all') <= 80
value('humidity', 0, 'valid') > 80
value('humidity', 0, 'valid') >= 80
```

**Monitoreo de temperatura**:

```
value('temperature', 0, 'valid') > 75
```

Esta expresión se activa cuando la temperatura supera los 75 grados, útil para alertas de sobrecalentamiento.

**Detección de violación de velocidad**:

```
value('speed', 0, 'valid') > 80
```

Esta expresión identifica cuando los vehículos superan los límites de velocidad de 80 km/h.

**Monitoreo de salud del dispositivo**:

```
value('battery_voltage', 0, 'valid') < 11.5
```

Esta expresión detecta condiciones de batería baja que requieren atención de mantenimiento.

**Alertas de nivel de combustible**:

```
value('fuel_level', 0, 'valid') < 20
```

Esta expresión identifica cuando los niveles de combustible caen por debajo del 20%, permitiendo reabastecimiento proactivo.

</details>

<details>

<summary>Ejemplos de operadores lógicos</summary>

**Operaciones Y**:

```
value('temperature', 0, 'valid') > 15 && value('humidity', 0, 'valid') > 80
value('temperature', 0, 'valid') > 15 and value('humidity', 0, 'valid') > 80
```

**Operaciones O**:

```
temperature < 10 || humidity > 80
temperature < 10 or humidity > 80
```

**Operaciones NO**:

```
!condition
not condition
```

</details>

<details>

<summary>Ejemplos de coincidencia de patrones</summary>

**Pertenencia a conjunto**:

```
value('lock_state', 0, 'valid') =~ ['locked','unlocked']
value('driver_name', 0, 'valid') !~ ['John', 'Steve']
```

**Coincidencia de patrones de cadena**:

```
driver_id =^ 'cc6f8216'
driver_id !^ 'cc6f8216'
value('engine_hours', 0, 'valid') =$ '1000'
value('driver_id', 0, 'valid') !$ '8b38851c3c68'
```

</details>

<details>

<summary>Ejemplos complejos de múltiples condiciones</summary>

**Alerta de exceso de velocidad fuera de horario**:

```
value('speed', 0, 'valid') > 60 && (value('current_hour', 0, 'valid') >= 18 || value('current_hour', 0, 'valid') <= 6)
```

Esto combina el monitoreo de velocidad con condiciones basadas en tiempo para una supervisión de seguridad mejorada durante turnos nocturnos.

**Diagnósticos integrales del dispositivo**:

```
value('gps_satellites', 0, 'valid') >= 4 && value('battery_voltage', 0, 'valid') > 11.5 && value('signal_strength', 0, 'valid') > -80
```

Esto valida múltiples parámetros de salud del dispositivo simultáneamente para asegurar un funcionamiento confiable.

**Monitoreo de seguridad del conductor**:

```
value('harsh_braking', 0, 'valid') == true && value('driver_identified', 0, 'valid') == false
```

Esto identifica comportamiento de conducción inseguro cuando el conductor no está debidamente identificado en el sistema.

**Programación de mantenimiento de equipos**:

```
value('engine_hours', 0, 'valid') > 250 && value('last_maintenance', 0, 'valid') > 30
```

Esto activa alertas de mantenimiento cuando las horas del motor superan los umbrales y el mantenimiento está atrasado.

**Cumplimiento de rango de temperatura**:

```
value('cargo_temperature', 0, 'valid') < -18 || value('cargo_temperature', 0, 'valid') > 4
```

Esto detecta cuando las temperaturas de carga refrigerada caen fuera del rango aceptable.

</details>

<details>

<summary>Complejidad de expresiones y paréntesis</summary>

Puede crear expresiones complejas combinando múltiples condiciones con paréntesis para controlar el orden de evaluación:

**Validación de seguridad compleja**:

```
!driver_identified && (vibration_active || speed > 3)
```

**Verificación de equipo multiparámetro**:

```
(value('oil_pressure', 0, 'valid') < 20 || value('coolant_temp', 0, 'valid') > 95) && value('engine_running', 0, 'valid') == true
```

</details>

### Escenarios de manejo de errores

| Escenario                          | Resultado          | Ruta de flujo | Valor del atributo |
| ---------------------------------- | ------------------ | ------------- | ------------------ |
| La expresión se evalúa como true   | Éxito              | Conexión THEN | true               |
| La expresión se evalúa como false  | Éxito              | Conexión ELSE | false              |
| El atributo referenciado es null   | Tratado como false | Conexión ELSE | false              |
| Error de sintaxis en la expresión  | Tratado como false | Conexión ELSE | null               |
| El atributo referenciado no existe | Tratado como false | Conexión ELSE | null               |

### Ejemplos de implementación práctica

<details>

<summary>Monitoreo de temperatura de flota</summary>

**Requisito empresarial**: Monitorear vehículos refrigerados para asegurar el cumplimiento de temperatura de la carga

```
value('cargo_temperature', 0, 'valid') > 4 || value('cargo_temperature', 0, 'valid') < -18
```

* **Ruta THEN**: Enviar alertas inmediatas al despacho, registrar violaciones de cumplimiento, activar acciones correctivas
* **Ruta ELSE**: Continuar procesamiento normal para temperaturas conformes, actualizar paneles de estado

</details>

<details>

<summary>Aplicación de seguridad del conductor</summary>

**Requisito empresarial**: Identificar patrones de conducción insegura durante horas de turno activo

```
value('harsh_acceleration', 0, 'valid') == true && value('shift_active', 0, 'valid') == true
```

* **Ruta THEN**: Generar reportes de entrenamiento del conductor, enviar notificaciones de seguridad, registrar incidentes
* **Ruta ELSE**: Procesar datos de comportamiento de conducción normal, actualizar métricas de rendimiento

</details>

<details>

<summary>Alertas de mantenimiento predictivo</summary>

**Requisito empresarial**: Detectar fallas potenciales de equipos antes de que ocurran

```
value('engine_temperature', 0, 'valid') > 95 && value('oil_pressure', 0, 'valid') < 30
```

* **Ruta THEN**: Programar citas de mantenimiento, enviar alertas a técnicos, registrar datos de diagnóstico
* **Ruta ELSE**: Continuar monitoreo rutinario, actualizar paneles de salud del equipo

</details>

<details>

<summary>Monitoreo de cumplimiento de geocerca</summary>

**Requisito empresarial**: Asegurar que los vehículos operen dentro de áreas autorizadas durante horas de trabajo

```
(value('latitude', 0, 'valid') < 40.7489 || value('latitude', 0, 'valid') > 40.7589) && value('business_hours', 0, 'valid') == true
```

* **Ruta THEN**: Generar alertas de ubicación no autorizada, notificar a seguridad, registrar violaciones
* **Ruta ELSE**: Continuar registro de operaciones normales, actualizar seguimiento de ubicación

</details>
