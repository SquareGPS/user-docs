# El nodo Iniciar Atributo

## Resumen técnico y capacidades

{% columns %}
{% column %}
En IoT Logic, el nodo **Iniciar Atributo** transforma las lecturas de los dispositivos creando nuevos atributos de datos basados en la telemetría entrante. Este nodo le permite manipular datos mediante fórmulas matemáticas, renombrar parámetros existentes y realizar operaciones a nivel de bits utilizando el [Navixy Expression Language](https://app.gitbook.com/s/tx3J5BxnWyPV0nP2xr0z/technologies/navixy-iot-logic-expression-language). El nodo sirve como componente clave en un flujo, permitiéndole enriquecer los datos antes de enviarlos a sus sistemas de destino.
{% endcolumn %}

{% column %}
![](../../../../../gua-del-usuario/cuenta/iot-logic/gestin-de-flujos/attachments/image-20250404-083140.png)
{% endcolumn %}
{% endcolumns %}

El nodo **Iniciar Atributo** se configura para cada flujo en la interfaz de usuario de la plataforma Navixy. Para opciones de sintaxis específicas y referencia detallada del lenguaje de expresión, consulte [Navixy Expression Language](https://app.gitbook.com/s/tx3J5BxnWyPV0nP2xr0z/technologies/navixy-iot-logic-expression-language) en la documentación del usuario.

![](../../../../../gua-del-usuario/cuenta/iot-logic/gestin-de-flujos/attachments/Initiate-attribute-in-flow.webp)

### Integración en la arquitectura de flujos

El nodo **Iniciar Atributo** funciona dentro de la arquitectura de flujo proporcionando capacidades de transformación de datos y habilitando:

* Procesar datos de telemetría sin procesar en métricas empresariales significativas.
* Creación de campos calculados basados en múltiples valores de parámetros.
* Conversión de unidades de medida (por ejemplo, kilómetros a millas).
* Cálculo de las diferencias entre las lecturas actuales y las anteriores.
* Generación de análisis basados en el tiempo sobre el comportamiento del dispositivo.

{% hint style="info" %}
El nodo de atributo Iniciar requiere que al menos un nodo de **Fuente de Datos** esté conectado a él. No se realizarán cálculos sin conexiones de datos de entrada.
{% endhint %}

### Capacidades del nodo

El nodo **Iniciar Atributo** ofrece por sí mismo:

* **Transformación de atributos de datos**: Crear atributos completamente nuevos aplicando operaciones matemáticas a los procedentes de fuentes de datos.
* **Conversión de unidades**: Convierte unidades de medida (por ejemplo, velocidad de _km/h_ a _mph_, o temperatura de _°C_ a _°F_)
* **Cálculos basados en el tiempo**: Compara las lecturas actuales con los valores anteriores para determinar los cambios
* **Manipulación del tiempo**: Personalice las marcas de tiempo de cuándo se generó el atributo en un dispositivo y cuándo lo recibió el servidor para evitar incoherencias en la línea de tiempo y unificar los formatos de hora.

## Opciones de configuración

El nodo **Iniciar Atributo** permite definir cómo se transforman los parámetros del dispositivo en atributos, que estarán disponibles para su posterior procesamiento en el flujo de datos.

![](../../../../../gua-del-usuario/cuenta/iot-logic/gestin-de-flujos/attachments/image-20250403-160516.png)

Veamos qué elementos utiliza este nodo y qué se puede configurar al trabajar con él:

### Pasos de configuración

{% stepper %}
{% step %}
**Especifique el nombre del nodo**

Introduzca un nombre descriptivo para resaltar el propósito del nodo. Utilice un nombre que le ayude a identificar los cálculos que se realizarán dentro de este nodo. Este nombre se mostrará en el diagrama de flujo para facilitar su identificación.
{% endstep %}

{% step %}
**Active Especificar atributos de tiempo** si necesita manipular marcas de tiempo de eventos

Esto habilita dos opciones más:

* **Hora de generación**: Cuando se crearon los datos (por defecto es `now()`).
* **Hora del servidor**: Cuando los datos fueron recibidos por IoT Logic (por defecto es `now()`).
{% endstep %}

{% step %}
**Defina las propiedades del atributo**

Configure las siguientes opciones para el nuevo atributo.

* Este nombre se mostrará en el [Analizador de flujo de datos](../../analizador-de-flujo-de-datos.md),
* También puede usar este nombre para crear sensores personalizados en el módulo de [Seguimiento](../../../../seguimiento/). Para hacerlo, el nodo **Iniciar Atributo** que contiene este atributo debe estar conectado al nodo **Punto de Salida**.
{% endstep %}

{% step %}
**Defina la fórmula**

Use expresiones matemáticas para calcular valores de atributos.

* Use el formato `value('parameter_name' 0, 'valid')` para hacer referencia a parámetros de dispositivo existentes.\
  **Nota**: Haga clic en ![image-20250605-115154.png](../../../../../.gitbook/assets/image-20250605-115154.png) dentro del campo **Fórmula** para abrir la lista de atributos disponibles y seleccionar el necesario. Se añadirá al campo automáticamente en formato listo para usar. Para detalles sobre autocompletar nombres de atributos, consulte [Autocompletar nombres de atributos](gestin-de-atributos.md).
* Aplique operaciones matemáticas basadas en el [Lenguaje de Expresión IoT Logic de Navixy ](https://app.gitbook.com/s/tx3J5BxnWyPV0nP2xr0z/technologies/navixy-iot-logic-expression-language)para transformar valores.
* Use diferentes valores de índice de profundidad para acceder a valores históricos (el predeterminado es 0).
{% endstep %}

{% step %}
(Opcional) Haga clic en **Agregar Atributo**

Crear un nuevo atributo de datos si necesita que se realicen varios cálculos dentro del mismo nodo.\
Esto abre el cuadro de diálogo de configuración de atributos donde definirá todas las propiedades de los atributos.
{% endstep %}
{% endstepper %}

Veamos un ejemplo práctico de configuración de atributos:

![](../../../../../gua-del-usuario/cuenta/iot-logic/gestin-de-flujos/attachments/image-20250404-083703.png)

En este ejemplo, estamos creando un atributo que convierte la velocidad de kilómetros a millas por hora dividiendo el parámetro de velocidad CAN por 1,609.

Para obtener más información sobre los cálculos de nuevos atributos, consulte [Ejemplos de cálculo](ejemplos-de-clculo.md).

Además, puede encontrar un ejemplo detallado del uso de atributos calculados en un flujo en [Ejemplo de configuración de flujo → pasos 3 y 4](../ejemplo-de-configuracin-de-un-flujo.md#paso-3-configure-transformaciones-basicas-de-datos).

## Opciones de visualización <a href="#opciones-de-visualizacion" id="opciones-de-visualizacion"></a>

Los nuevos atributos calculados dentro del nodo **Iniciar Atributo** pueden monitorearse igual que los atributos de datos reales provenientes de dispositivos en el **Analizador de flujo de datos** y el módulo de **Seguimiento**.

Para más información sobre las opciones de visualización, consulte [Visualización de nuevos atributos calculados en la plataforma Navixy](../../../../../readme/cuenta/iot-logic/gestin-de-flujos/el-nodo-iniciar-atributo/visualizacion-de-nuevos-atributos-calculados-en-la-plataforma-navixy.md).

## Consideraciones sobre el flujo de datos

Después de configurar su nodo **Iniciar Atributo**, asegúrese de:

1. Conectar el nodo al menos a un nodo **Fuente de Datos** como entrada
2. Conecte la salida a un nodo de **Punto de Salida** para enviar los datos transformados

Dentro del nodo **Iniciar Atributo**, los valores de los parámetros se procesan según sus expresiones cada vez que el dispositivo proporciona datos. A la salida, recibirá:

* Todos los parámetros originales del dispositivo
* Todos los atributos calculados con sus valores
* Valores actualizados de la hora de generación y la hora del servidor según lo configurado

Si utiliza el mismo nombre para un atributo calculado que un parámetro existente, el atributo sustituirá al parámetro original en el paquete de datos de salida.

## Preguntas más frecuentes

### ¿Puedo hacer referencia a valores no más recientes en mis cálculos?

Sí. Utilice el parámetro index en la función value para acceder a valores históricos. Por ejemplo, `value('temperature', 1, 'valid')` hace referencia al valor válido anterior del parámetro temperatura.

### ¿Cómo puedo realizar cálculos con la hora?

Utilice las funciones `genTime()` y `srvTime()` para trabajar con marcas de tiempo. Puede calcular diferencias horarias, añadir desfases o dar formato a las marcas de tiempo para su visualización.

### ¿Qué ocurre si elimino un atributo?

El atributo dejará de calcularse para los nuevos datos recibidos, pero los datos históricos permanecerán inalterados. El atributo no aparecerá en ningún paquete de datos nuevo después de la eliminación.

### ¿Puedo utilizar atributos creados en un nodo Iniciar Atributo en otro?

Sí. Los atributos creados con anterioridad en el flujo pueden referenciarse en nodos **Iniciar Atributo** posteriores, lo que permite realizar cálculos en varias etapas.

![](../../../../../gua-del-usuario/cuenta/iot-logic/gestin-de-flujos/attachments/image-20250404-084039.png)

**¿Cómo evito errores tipográficos al hacer referencia a nombres de atributos en las fórmulas?**

Utilice la función de autocompletado en el campo Fórmula para seleccionar entre los atributos disponibles. Para instrucciones detalladas, consulte [Autocompletar nombres de atributos](gestin-de-atributos.md).
