# Gestión de atributos

El nodo **Iniciar Atributo** permite crear, editar y gestionar atributos de datos en todo el flujo de IoT Logic. Esta guía cubre las operaciones esenciales de gestión de atributos: crear, editar y eliminar.

## Creación de atributos

A continuación se explica cómo crear un nuevo atributo en el nodo **Iniciar Atributo**:

1. Haga clic en el botón **Agregar atributo**
2. Introduzca un nombre para el atributo (por ejemplo, "Velocidad mph")
3. Defina la expresión del valor (por ejemplo, `value('can_speed')/1.609`)
4. Opcionalmente, configure la hora de generación y la hora del servidor; para ello, active el conmutador **Especificar parámetros de tiempo**\
   Para más detalles, consulte [Ajustes de tiempo para atributos](gestin-de-atributos.md#ajustes-de-tiempo-para-atributos)
5. Haga clic en **Guardar** para confirmar la configuración del nodo

El nuevo atributo se guarda en el nodo y el cálculo configurado se aplica inmediatamente en el flujo.

### Ajustes de tiempo para atributos

La configuración de la hora le permite controlar las marcas de tiempo asociadas a sus atributos:

* **Hora generada**: Cuando se crearon los datos.
  * Utilice `now()` para establecer la hora actual en milisegundos.
  * Utilice `genTime('partameter_name', 0, 'valid')` para utilizar la hora de generación propia del parámetro.
* **Hora del servidor**: Cuando los datos fueron recibidos por IoT Logic.
  * Utilice `now()` para establecer la hora actual en milisegundos.
  * Utilice `srvTime('partameter_name', 0, 'valid')` para utilizar la hora del servidor del parámetro.
  * Añadir compensaciones para ajustar las zonas horarias (por ejemplo, `srvTime('can_speed', 0, 'valid') + 120000` añade 2 minutos).

{% hint style="info" %}
La configuración de la hora es importante para el análisis y la sincronización de los datos. Una configuración horaria adecuada garantiza que sus datos mantengan la integridad cronológica en todo el flujo.
{% endhint %}

### **Autocompletar nombres de atributos** <a href="#autocompletar-nombres-de-atributos-inlineextension" id="autocompletar-nombres-de-atributos-inlineextension"></a>

Al crear fórmulas de cálculo, necesita hacer referencia a nombres de atributos existentes de dispositivos físicos o atributos calculados de otros nodos. Para simplificar este proceso y evitar errores ortográficos, IoT Logic proporciona funcionalidad de autocompletado para nombres de atributos.

Para usar el autocompletado al construir fórmulas:

* Haga clic en <img src="../../../../../.gitbook/assets/image-20250605-130755.png" alt="image-20250605-130755.png" data-size="original"> en el campo **Fórmula**.
* Seleccione el atributo deseado de la lista que aparece, admite entrada de texto manual para fines de búsqueda.
* Haga clic en el nombre del atributo para insertarlo en su fórmula.

El atributo seleccionado se inserta automáticamente en formato listo para usar, con el nombre del atributo resaltado: _value('attribute\_name', 0, 'valid')_. Para su comodidad, aquí está el desglose de los elementos autocompletados:

* `value` - un elemento de sintaxis del [Lenguaje de Expresión IoT Logic de Navixy](https://app.gitbook.com/s/tx3J5BxnWyPV0nP2xr0z/technologies/navixy-iot-logic-expression-language).
* `'attribute_name'` - el nombre real del atributo de datos proveniente de un dispositivo físico u otro nodo **Iniciar Atributo**.
* `0` - índice de profundidad, definiendo el valor histórico exacto desde 0 (el más reciente) hasta 12 (el más antiguo). Refleja los índices mostrados en el [Analizador de flujo de datos](../../analizador-de-flujo-de-datos.md).
* `‘valid'` - bandera de validez que fuerza a considerar solo los valores no nulos.

{% hint style="warning" %}
Cuando se especifica `'valid'`, el sistema omite automáticamente cualquier valor histórico nulo (vacío). Esto significa que el índice de profundidad apuntará al valor **válido** más reciente en lugar del valor cronológico más reciente. Por ejemplo, si su lectura más reciente (índice `0`) es nula pero la lectura anterior (índice `1`) contiene datos reales, la fórmula usará el valor del índice `1` en lugar del valor nulo en el índice `0`.
{% endhint %}

Puede modificar los parámetros según sea necesario: cambiar el número de índice para valores históricos o ajustar la bandera de validez.

La lista se filtra basándose en las fuentes de datos de su flujo y coincide con lo que es visible en el [Analizador de flujo de datos](../../analizador-de-flujo-de-datos.md).

{% hint style="info" %}
La lista de autocompletado muestra solo atributos que cumplen todos los siguientes criterios simultáneamente:

* **Soportado por dispositivos** - El atributo debe ser soportado por al menos un dispositivo actualmente agregado a su flujo.
* **Realmente transmitido** - El dispositivo debe haber enviado datos reales para este atributo (no solo soportarlo teóricamente).
* **Disponible en flujo** - Esto incluye tanto parámetros de dispositivo como atributos calculados de otros nodos **Iniciar Atributo** dentro del mismo flujo.

**Ejemplo:** Si su dispositivo soporta sensores de velocidad y temperatura pero solo ha transmitido datos de velocidad (quizás debido a un sensor de temperatura defectuoso), la lista de autocompletado mostrará el atributo 'speed' pero no 'temperature'. El atributo de temperatura solo aparecerá una vez que el dispositivo realmente envíe lecturas de temperatura, aunque técnicamente el dispositivo lo soporte.
{% endhint %}

**Atributos indexados en autocompletado**

Algunos atributos de datos contienen múltiples valores indexados dentro de un solo atributo, como lecturas de múltiples sensores analógicos conectados a un dispositivo telemático principal. Para usar estos atributos en cálculos, necesita especificar el número de índice exacto correspondiente al sensor o entrada específica que desea referenciar.

Por ejemplo, si necesita trabajar con lecturas de voltaje de la tercera entrada analógica en su dispositivo, estos datos vienen a través del atributo `analog_2` (usando indexación basada en cero donde la primera entrada es índice 0). En su fórmula, esto aparecería como `value('analog_2', 0, 'valid')`.

El autocompletado también maneja este escenario:

* Los atributos indexados están marcados con el icono ![image-20250606-123725.png](../../../../../.gitbook/assets/image-20250606-123725.png) en la lista de autocompletado.
* Estas entradas muestran el rango de índices disponibles entre corchetes, como `analog_[1..4]` para atributos que soportan cinco valores indexados (índices 1 a 4).
* Cuando selecciona un atributo indexado, el cursor se posiciona automáticamente al final del nombre del atributo dentro de las comillas, permitiéndole escribir inmediatamente el número de índice específico que necesita.

## Edición de atributos existentes

Para modificar un atributo existente:

1. Abra la ventana de configuración del nodo pasando el ratón por encima del nodo para mostrar las acciones rápidas, o haciendo doble clic en el nodo
2. Busque el atributo que desea editar en la lista de atributos.
3. Realice los cambios necesarios en los campos de texto de las propiedades del atributo: **Nombre del atributo**, **Fórmula** o **Parámetros de tiempo**
4. Si necesita editar otros atributos en este nodo, repita el paso 3 para ellos
5. Haga clic en **Guardar** para aplicar los cambios a la configuración del nodo.

{% hint style="info" %}
Cuando edite un atributo, los cambios sólo se aplicarán a los nuevos datos recibidos después de guardar. Los datos históricos ya recogidos no se recalcularán.
{% endhint %}

## Eliminación de atributos

Para eliminar un atributo que ya no es necesario:

1. Abra la ventana de configuración del nodo pasando el ratón por encima del nodo para ver las acciones rápidas, o haciendo doble clic en el nodo.
2. Busque el atributo que desea eliminar en la lista de atributos y pase el ratón por encima para que aparezca el menú .
3. Haga clic en el menú que aparece y seleccione **Eliminar**
4. Confirme su decisión de eliminar el atributo
5. Haga clic en **Guardar** para aplicar los cambios a la configuración del nodo

![](../../../../../gua-del-usuario/cuenta/iot-logic/gestin-de-flujos/el-nodo-iniciar-atributo/attachments/image-20250402-102052.png)

{% hint style="info" %}
Al eliminar un atributo, éste ya no se calculará para los nuevos datos, pero los datos históricos que contengan este atributo permanecerán inalterados en la base de datos.
{% endhint %}
