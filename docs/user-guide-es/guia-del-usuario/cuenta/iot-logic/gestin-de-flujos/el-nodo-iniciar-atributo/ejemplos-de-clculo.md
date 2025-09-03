# Ejemplos de cálculo

El nodo **Iniciar Atributo** en IoT Logic admite una amplia gama de cálculos a través de [Lenguaje de Expresión IoT Logic de Navixy](https://app.gitbook.com/s/tx3J5BxnWyPV0nP2xr0z/technologies/navixy-iot-logic-expression-language). Esta guía proporciona ejemplos prácticos de cálculos comunes para ayudarle a extraer el máximo valor de sus datos IoT.

## Consideraciones importantes

Al crear cálculos, tenga en cuenta estos puntos:

* **Validez de los nombres de atributos**: Asegúrese de utilizar nombres de atributos correctos en los cálculos. Puede consultar los nombres de atributos existentes con [Analizador de flujo de datos](https://squaregps.atlassian.net/wiki/spaces/UDOCES/pages/3232334554/Data+Stream+Analyzer?atlOrigin=eyJpIjoiNDU1MWY3OGI2NTJmNGFjM2IxNzU1ZWI2ZjYyN2NiM2QiLCJwIjoiYyJ9).
* **Validez de los datos**: Asegúrese de que sus expresiones gestionan correctamente los posibles valores nulos o lecturas no válidas.
* **Impacto en el rendimiento**: Los cálculos complejos con muchas funciones anidadas pueden afectar a la velocidad de procesamiento de datos de alta frecuencia.
* **Restricciones matemáticas**: Funciones como el logaritmo y la raíz cuadrada requieren valores de entrada positivos.
* **Referencias históricas**: Cuando utilice valores indexados (por ejemplo, `value('param', 1, 'valid')`), asegúrese de que dispone de suficientes datos históricos.

{% hint style="info" %}
Las funciones matemáticas pueden aplicarse a cualquier parámetro numérico o atributo calculado previamente. Valide siempre sus cálculos con datos de prueba antes de desplegarlos en los flujos de producción.
{% endhint %}

## Cálculos básicos

### Conversión de unidades

La conversión de medidas entre diferentes unidades es una de las operaciones más comunes en el procesamiento de datos IoT.

#### **Conversión de velocidad (km/h a mph)**

```
value('can_speed')/1.609
```

**Aplicación práctica:** Esta conversión estandariza los datos de velocidad de los vehículos para las regiones que utilizan medidas imperiales. Al realizar este cálculo en IoT Logic en lugar de en aplicaciones posteriores, se garantiza la coherencia en todos los sistemas que consumen los datos.

**Conversión de temperatura (Celsius a Fahrenheit)**

```
value('temperature')*1.8 + 32
```

**Aplicación práctica:** Esta conversión hace que las lecturas de temperatura sean comprensibles para los usuarios más familiarizados con las medidas en grados Fahrenheit. Resulta especialmente útil para organizaciones multinacionales que operan en regiones con distintos estándares de medición.

### Cálculo de diferencias

La comparación de las lecturas actuales con los valores anteriores ayuda a identificar cambios y tendencias en los datos.

#### **Detección de cambios de temperatura**

```
value('temperature', 0, 'valid') - value('temperature', 1, 'valid')
```

**Aplicación práctica:** Este cálculo ayuda a detectar fluctuaciones rápidas de temperatura que podrían indicar problemas en los equipos o cambios en el entorno. Al crear un atributo específico para esta diferencia, puede configurar alertas para cambios repentinos sin un complejo procesamiento posterior.

{% hint style="info" %}
**Ejemplo:** Para una flota de camiones frigoríficos, este cálculo puede identificar inmediatamente cuando la temperatura de la carga empieza a subir demasiado rápido, permitiendo a los expedidores ponerse en contacto con los conductores antes de que las mercancías perecederas se vean comprometidas. El atributo puede activar alertas cuando el cambio de temperatura supera los 3 grados en un periodo corto, lo que podría indicar un fallo del sistema de refrigeración o que se ha dejado una puerta abierta.
{% endhint %}

## Cálculos temporales

Los cálculos temporales le ayudan a comprender el comportamiento del dispositivo a lo largo del tiempo y a medir patrones operativos.

#### **Encontrar el tiempo transcurrido entre las últimas lecturas válidas**

```
srvTime('avl_25', 0, 'valid') - srvTime('avl_25', 1, 'valid')
```

**Aplicación práctica:** Este cálculo mide el intervalo entre transmisiones de datos consecutivas, lo que puede ayudar a identificar problemas de comunicación o validar que los dispositivos están informando a las frecuencias esperadas. Este ejemplo muestra el cálculo entre las dos últimas lecturas válidas, pero puede ajustarse para manejar dos valores históricos cualesquiera.

{% hint style="info" %}
**Ejemplo:** Para una flota de taxis, este cálculo puede ayudar a identificar problemas de conectividad con los rastreadores GPS. Si el tiempo entre lecturas aumenta repentinamente de los 30 segundos estándar a varios minutos, podría indicar zonas con mala cobertura de telefonía móvil o un mal funcionamiento del dispositivo, lo que permitiría a los equipos de mantenimiento abordar los problemas antes de que afecten a la calidad del servicio.
{% endhint %}

#### **Conversión de la marca de tiempo a un formato legible por humanos**

```
dtFormat(genTime('can_fuel_1', 0, 'all'))
```

**Aplicación práctica:** la conversión de marcas de tiempo Unix al formato ISO 8601 hace que los datos sean más legibles en registros e informes. Este formato es ampliamente soportado por herramientas de análisis y bases de datos, lo que simplifica la integración con otros sistemas.

## Funciones matemáticas avanzadas

IoT Logic soporta sofisticadas operaciones matemáticas a través de sus funciones matemáticas incorporadas.

### Redondear valores

**Redondear la temperatura al entero más próximo**

```
math:round(value('temperature_2', 0, 'valid'))
```

**Aplicación práctica:** el redondeo es útil cuando no se necesita una precisión exacta o cuando se quiere reducir el ruido en las lecturas de los sensores. Por ejemplo, el redondeo de los datos de los sensores medioambientales puede ser suficiente para la supervisión general del clima y, al mismo tiempo, reducir los requisitos de almacenamiento. Esta función también es útil para crear categorías o bandas de valores (por ejemplo, agrupar las lecturas de temperatura en incrementos de 5 grados).

{% hint style="info" %}
**Ejemplo:** En la gestión de flotas, las lecturas de temperatura del motor a menudo incluyen puntos decimales que no son significativos para las alertas al conductor o la programación del mantenimiento. El redondeo de estos valores simplifica la visualización del cuadro de mandos y facilita la definición de los umbrales de temperatura. Por ejemplo, las alertas de mantenimiento pueden activarse cuando la temperatura redondeada del motor supera los 90 °C, en lugar de tener que tratar con valores precisos como 89,7 °C.
{% endhint %}

### Cálculos logarítmicos

**Logaritmo natural de un valor**

```
math:log(value('temperature_2', 0, 'valid'))
```

**Aplicación práctica:** Las transformaciones logarítmicas son especialmente útiles para:

* Comprimir datos que abarcan varios órdenes de magnitud en un rango más manejable.
* Conversión de relaciones exponenciales en lineales para facilitar el análisis
* Trabajo con determinados tipos de sensores que tienen características de respuesta logarítmica
* Cálculos de nivel sonoro, donde los decibelios son unidades logarítmicas
* Mediciones del pH en la supervisión medioambiental

{% hint style="info" %}
**Ejemplo:** Al analizar el comportamiento del conductor con un acelerómetro, la función logarítmica puede ayudar a normalizar los datos de aceleración que van desde movimientos ligeros hasta frenazos bruscos. Esto facilita la creación de una puntuación significativa de la seguridad del conductor que no esté demasiado sesgada por eventos extremos ocasionales. Otro ejemplo práctico es cuando se trabaja con sensores de combustible que no proporcionan lecturas lineales. Algunos sensores de nivel de combustible tienen valores de resistencia no lineales que corresponden al nivel real de combustible. El uso de cálculos logarítmicos puede ayudar a traducir estas lecturas en porcentajes de nivel de combustible más precisos.
{% endhint %}

### Operaciones de raíz cuadrada

**Calcular la raíz cuadrada de una lectura**

```
math:sqrt(value('temperature_2', 0, 'valid'))
```

**Aplicación práctica:** Las funciones de raíz cuadrada son valiosas para:

* Convertir entre potencia y amplitud en mediciones eléctricas
* Cálculo de desviaciones estándar en el análisis estadístico de datos de sensores
* Determinación de los valores cuadráticos medios (RMS) de los parámetros eléctricos
* Cálculo de distancias en espacios multidimensionales (por ejemplo, trilateración para posicionamiento)
* Normalización de determinados tipos de datos de sensores

{% hint style="info" %}
**Ejemplo:** Al calcular la distancia real entre dos puntos GPS (latitud y longitud), es necesario utilizar la función de raíz cuadrada como parte de la fórmula de distancia. Por ejemplo, si está calculando la distancia que ha recorrido un vehículo entre dos lecturas de GPS utilizando la fórmula de distancia euclidiana, la función de raíz cuadrada es esencial. Otra aplicación común es el cálculo de la magnitud de los eventos de vibración o choque de múltiples ejes del acelerómetro (X, Y, Z). La raíz cuadrada de la suma de los valores al cuadrado de cada eje proporciona la magnitud global de la vibración, lo que resulta útil para detectar impactos de vehículos o condiciones adversas de la carretera.
{% endhint %}

## Operaciones combinadas

Puede crear cálculos aún más complejos combinando varias funciones y operaciones.

### **Media geométrica con redondeo**

```
math:round(math:sqrt(value('temperature_1', 0, 'valid') * value('temperature_2', 0, 'valid')))
```

**Aplicación práctica:** Este cálculo calcula la media geométrica de las lecturas de dos sensores de temperatura y redondea el resultado para proporcionar un valor más limpio. La media geométrica suele ser más adecuada que la media aritmética cuando se trata de tasas, relaciones o mediciones en las que la multiplicación es la forma natural de combinar valores.

{% hint style="info" %}
**Ejemplo:** en un transporte refrigerado, puede haber varios sensores de temperatura repartidos por la zona de carga. Este cálculo proporciona una lectura de temperatura equilibrada que tiene en cuenta ambos valores y minimiza la influencia de valores extremos. En lugar de activar alertas basadas en un solo sensor (que podría verse afectado por la apertura de puertas), este cálculo combinado proporciona una condición de temperatura global más representativa para la carga sensible.
{% endhint %}

### **Cálculo del valor normalizado**

```
(value('sensor_reading', 0, 'valid') - value('sensor_min', 0, 'valid')) / (value('sensor_max', 0, 'valid') - value('sensor_min', 0, 'valid')) * 100
```

**Aplicación práctica:** Esto normaliza la lectura de un sensor a una escala de porcentaje de 0-100%, permitiendo comparaciones estandarizadas entre diferentes sensores con rangos variados. Esto resulta especialmente útil para crear cuadros de mando uniformes o activar alertas basadas en valores relativos en lugar de mediciones absolutas.

{% hint style="info" %}
**Ejemplo:** Un gestor de flota supervisa vehículos de varios fabricantes, cada uno con diferentes lecturas de los sensores de combustible (ohmios, voltios, valores digitales brutos). Al normalizar estas diversas lecturas en una escala porcentual coherente, el gestor puede aplicar las mismas alertas de bajo nivel de combustible en toda la flota y generar informes de consumo de combustible estandarizados sin tener que tener en cuenta las características específicas de los sensores de cada modelo de vehículo.
{% endhint %}
