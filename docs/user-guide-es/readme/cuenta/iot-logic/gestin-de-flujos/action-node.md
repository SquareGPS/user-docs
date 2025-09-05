# El nodo de Acción

### Resumen técnico y capacidades

{% columns %}
{% column %}
Los nodos de **Acción** en IoT Logic permiten el control automatizado de dispositivos mediante la ejecución de comandos específicos cuando se activan por flujos de datos entrantes. Estos nodos transforman la monitorización pasiva de la flota en sistemas de automatización activos, realizando operaciones críticas como la conmutación de salidas y la transmisión de comandos GPRS.
{% endcolumn %}

{% column %}
<figure><img src="../../../../.gitbook/assets/image (22).png" alt=""><figcaption></figcaption></figure>
{% endcolumn %}
{% endcolumns %}

Aunque los nodos de Acción pueden recibir datos de cualquier tipo de nodo, se conectan más comúnmente a [nodos Logic](el-nodo-logic/) que evalúan condiciones y activan acciones solo cuando se cumplen criterios específicos, como umbrales de temperatura, movimiento no autorizado o incidentes de conducción brusca.

Los nodos de **Acción** se configuran por separado para cada flujo en la interfaz de usuario de la plataforma Navixy. Cada nodo puede contener múltiples acciones que se ejecutan secuencialmente cuando son activadas por los datos entrantes.

<figure><img src="../../../../.gitbook/assets/image (6).png" alt=""><figcaption></figcaption></figure>

### Cómo funcionan los nodos de Acción

Cuando los datos llegan a un nodo de **Acción**, el sistema ejecuta las acciones configuradas para los dispositivos que proporcionaron los datos entrantes. El proceso de ejecución sigue estos pasos:

* **Identificación del dispositivo**: El nodo identifica qué dispositivos específicos enviaron los datos que activaron la acción.
* **Ejecución secuencial**: Todas las acciones configuradas dentro del nodo se ejecutan en el orden en que aparecen (de arriba a abajo).
* **Transmisión de comandos**: Las acciones se envían solo a los dispositivos identificados, asegurando respuestas dirigidas.
* **Procesamiento del dispositivo**: Los dispositivos individuales reciben y procesan los comandos según sus capacidades.

Este mecanismo de direccionamiento asegura que las acciones se ejecuten solo para los dispositivos relevantes. Cuando se conectan a [nodos **Logic**](el-nodo-logic/), las acciones se activan solo para los dispositivos que hicieron que la condición lógica se evaluara como verdadera, proporcionando un control de automatización preciso.

### Integración en la arquitectura del flujo

Los nodos de **Acción** funcionan como nodos terminales dentro de la arquitectura del flujo, recibiendo activadores de nodos anteriores sin reenviar datos. Las capacidades de automatización se integran con el sistema más amplio de gestión de dispositivos de Navixy a través de:

* **Automatización condicional**: La integración con [nodos Logic](el-nodo-logic/) permite flujos de trabajo sofisticados SI-ENTONCES donde las acciones se ejecutan solo cuando se validan condiciones específicas.
* **Control de dispositivos en tiempo real**: Los comandos se transmiten en segundos tras recibir los activadores, asegurando una respuesta inmediata a condiciones críticas.
* **Coordinación a nivel de flota**: Cuando se conectan a múltiples fuentes de dispositivos, las acciones pueden coordinar respuestas en grupos enteros de vehículos simultáneamente.
* **Respeto a las capacidades del dispositivo**: Se respetan las limitaciones individuales de los dispositivos; los comandos no compatibles son recibidos pero no ejecutados.

{% hint style="info" %}
**Requisito de conectividad del dispositivo**: Las acciones se envían solo a dispositivos que se confirman como conectados (aquellos que proporcionan datos recientes), asegurando una entrega de comandos fiable. En el raro caso de que un dispositivo se desconecte inmediatamente después de enviar datos, o si hay múltiples comandos pendientes, las acciones se ponen en cola y se ejecutan tan pronto como el dispositivo esté disponible de nuevo.
{% endhint %}

### Opciones de configuración

La configuración de un nodo de **Acción** determina qué respuestas automatizadas se ejecutarán cuando el nodo reciba activadores de los nodos de procesamiento anteriores.

<figure><img src="../../../../.gitbook/assets/image (25).png" alt=""><figcaption></figcaption></figure>

Veamos qué elementos utiliza este nodo y qué puede configurar al trabajar con él:

#### Pasos de configuración

{% stepper %}
{% step %}
**Especifique el nombre del nodo**

Introduzca un nombre descriptivo que identifique las acciones automatizadas que realizará este nodo.

1. Use nombres como "Respuesta de Refrigeración de Emergencia" o "Acciones de Alerta de Seguridad" para mayor claridad.
2. Este nombre aparece en el diagrama de flujo para una fácil identificación.
{% endstep %}

{% step %}
**Seleccione el tipo de Acción**

Elija el tipo de respuesta automatizada del menú desplegable.

1. **Conmutar Salida**: Controle las salidas del dispositivo encendiéndolas o apagándolas.
2. **Enviar Comando GPRS**: Transmita comandos personalizados directamente a los dispositivos.
{% endstep %}

{% step %}
**Configure los parámetros de la acción**

Configure los detalles específicos según el tipo de acción seleccionado:

<details>

<summary>Configuración de Conmutar Salida</summary>

<figure><img src="../../../../.gitbook/assets/image (24).png" alt=""><figcaption></figcaption></figure>

Al configurar acciones de Conmutar Salida:

* **Número de salida**: Seleccione qué salida del dispositivo controlar desde el menú desplegable.
  * Los números de salida disponibles dependen de las capacidades específicas de su dispositivo.
  * Consulte la documentación de su dispositivo para entender las funciones de las salidas.
* **Selector ON/OFF**: Establezca si la acción enciende (ON) o apaga (OFF) la salida.
  * Use el interruptor para seleccionar el estado deseado.

</details>

<details>

<summary>Configuración de Enviar Comando GPRS</summary>

<figure><img src="../../../../.gitbook/assets/image (23).png" alt=""><figcaption></figcaption></figure>

Al configurar acciones de Enviar Comando GPRS:

* **Cadena del comando**: Introduzca el texto exacto del comando a enviar a los dispositivos.
  * Los comandos deben coincidir con la sintaxis de comandos admitida por su dispositivo.
  * Consulte la documentación del dispositivo para ver los comandos disponibles y el formato adecuado.
  * No hay restricciones de caracteres en el campo de entrada.

{% hint style="danger" %}
La ejecución de la acción depende de las capacidades individuales del dispositivo. Asegúrese de que sus dispositivos admiten los comandos específicos que está configurando. La información sobre los comandos admitidos por un dispositivo específico está disponible en los recursos del fabricante, como la documentación del dispositivo.
{% endhint %}

</details>
{% endstep %}

{% step %}
**Añadir acciones adicionales (opcional)**

Haga clic en **AÑADIR ACCIÓN** para crear múltiples acciones dentro del mismo nodo.

* Las acciones se ejecutan secuencialmente en el orden en que aparecen en la configuración.
* Cada acción puede ser de un tipo diferente (Conmutar Salida o Enviar Comando GPRS).
* Use el icono de la papelera para eliminar acciones innecesarias.
{% endstep %}

{% step %}
**Guardar configuración**

Haga clic en **APLICAR** para guardar la configuración de su nodo.

* Use **CANCELAR** para descartar los cambios.
* Use **RESTABLECER FORMULARIO** para borrar todas las acciones configuradas y empezar de nuevo.
{% endstep %}
{% endstepper %}

{% hint style="danger" %}
**Nota de compatibilidad del dispositivo:** La ejecución de la acción depende de las capacidades individuales del dispositivo. Asegúrese de que sus dispositivos admiten las salidas o comandos específicos que está configurando. Por favor, busque los comandos admitidos en los recursos del fabricante, como la documentación del dispositivo. La lista de dispositivos compatibles está disponible en [Dispositivos integrados de Navixy](https://www.navixy.com/devices/).
{% endhint %}

### Ejecución y direccionamiento de la acción

El nodo de Acción proporciona un control preciso sobre cuándo y dónde se ejecutan los comandos, asegurando respuestas de automatización eficientes y dirigidas.

#### Secuencia de ejecución

Cuando se activa, el nodo de Acción sigue este patrón de ejecución:

1. **Direccionamiento de dispositivos**: Las acciones se envían solo a los dispositivos que proporcionaron datos en el evento de activación actual.
   1. Esto asegura que los comandos lleguen solo a los dispositivos específicos involucrados en la condición.
   2. Evita comandos innecesarios a los dispositivos no afectados de la flota.
2. **Procesamiento secuencial**: Múltiples acciones dentro de un nodo se ejecutan en el orden configurado, de arriba a abajo.
   1. La transmisión de cada acción se completa antes de que comience la siguiente.
   2. El tiempo total de ejecución suele ser de segundos tras recibir el activador.
3. **Validación del dispositivo**: Los dispositivos individuales procesan los comandos recibidos según sus capacidades.
   1. Los comandos admitidos se ejecutan inmediatamente al recibirlos.
   2. Los comandos no admitidos son recibidos pero ignorados por el dispositivo.
   3. Los mecanismos de seguridad del dispositivo pueden impedir comandos inapropiados (p. ej., apagar el motor mientras está en movimiento).

#### Comportamiento de la conexión

**Integración con el nodo Logic**: Cuando se conecta a [nodos Logic](el-nodo-logic/), las acciones se ejecutan solo para los dispositivos donde la condición lógica se evaluó como `true`. Esto proporciona una automatización condicional precisa.

**Conexiones directas**: Cuando se conecta directamente a otros tipos de nodos (**Fuente de Datos**, Iniciar **Atributo**), las acciones se ejecutan para todos los dispositivos en el flujo de datos cada vez que se reciben datos.

### Preguntas más frecuentes

**¿Cómo sé si mis acciones se ejecutaron correctamente?**

Actualmente, la retroalimentación sobre la ejecución de acciones es limitada. Los comandos se envían a dispositivos que se confirman como conectados (aquellos que proporcionan datos recientes) sin un intervalo de tiempo entre la activación y la ejecución, lo que elimina la posibilidad de que el dispositivo se desconecte en ese lapso. Puede monitorizar el comportamiento del dispositivo durante la fase de prueba o usar flujos de prueba separados para verificar los resultados de la acción en un entorno controlable.

**¿Puedo conectar varios nodos al mismo nodo de Acción?**

Sí. Los nodos de Acción pueden recibir activadores de múltiples nodos anteriores, pero tenga en cuenta que las acciones se ejecutarán para cualquier dispositivo que active cualquiera de los nodos conectados. Al diseñar flujos complejos, considere el efecto acumulativo de múltiples fuentes de activación para asegurar que las acciones se ejecuten solo en los escenarios previstos.

**¿Qué sucede si conecto un nodo de Acción directamente a una Fuente de Datos?**

El nodo de Acción ejecutará sus acciones configuradas cada vez que cualquier dispositivo en la Fuente de Datos envíe datos. Esto crea una ejecución continua de acciones en lugar de respuestas condicionales. Para la mayoría de los casos de uso, conectar los nodos de Acción a [nodos Logic](el-nodo-logic/) proporciona un mejor control sobre cuándo deben ejecutarse las acciones.
