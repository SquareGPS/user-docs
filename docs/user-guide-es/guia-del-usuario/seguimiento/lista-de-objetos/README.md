# Lista de objetos

La **Lista de objetos** es su centro principal para monitorear todos los dispositivos conectados en tiempo real. Proporciona una vista clara y de un vistazo de cada objeto rastreado, mostrando su estado actual y parámetros clave seleccionados. Diseñada para la eficiencia, se abre automáticamente cuando navega al módulo de **Seguimiento**, asegurando acceso instantáneo a la información que necesita. Desde aquí, puede profundizar en cada entidad a través de su widget del objeto dedicado, facilitando el seguimiento, análisis y gestión de sus objetos.

<figure><img src="../../../.gitbook/assets/Untitled (23).png" alt="Lista de objetos"><figcaption><p>Lista de objetos</p></figcaption></figure>

### Resumen de la lista <a href="#resumen-de-la-lista" id="resumen-de-la-lista"></a>

#### **Visibilidad y control de acceso** <a href="#visibilidad-y-control-de-acceso" id="visibilidad-y-control-de-acceso"></a>

La **Lista de objetos** responde a los roles de usuario y configuraciones de visibilidad dentro de la plataforma:

* **Propietarios** pueden ver todos los objetos dentro de la cuenta de la organización.
* **Usuarios** ven solo los objetos que han creado personalmente o aquellos asignados a ellos por el propietario.

Este control de acceso basado en roles asegura la seguridad de los datos mientras mantiene accesible la información necesaria. Para más información sobre los roles de la plataforma, consulte [Acceso del equipo](../../cuenta/acceso-del-equipo/).

#### **Estructura** <a href="#estructura" id="estructura"></a>

Por defecto, los objetos se muestran en **grupos**, estructurados de la misma manera que en [Dispositivos y ajustes](../../dispositivos-y-ajustes/) para asegurar consistencia en toda la plataforma. Los objetos no pueden moverse entre grupos desde la **Lista de objetos** — tales modificaciones solo pueden realizarse en **Dispositivos y configuración**. Los grupos son colapsables para una interacción conveniente con múltiples objetos.\
Para aprender más sobre grupos de objetos, consulte [Grupos en Dispositivos y Configuración](../../dispositivos-y-ajustes/#acciones-de-grupo).

La agrupación puede deshabilitarse con la opción **No agrupar** . Para detalles, consulte [Configuraciones adicionales](./#configuraciones-adicionales-inlineextension).

#### Navegación <a href="#navegacion" id="navegacion"></a>

La **Lista de objetos** incluye varias características para ayudarle a navegar su flota:

* **Búsqueda rápida** <img src="../../../.gitbook/assets/Untitled (24).png" alt="" data-size="line">: Le permite encontrar objetos específicos ingresando su nombre, [etiqueta](https://squaregps.atlassian.net/wiki/pages/createpage.action?spaceKey=udoces\&title=Tags\&linkCreation=true\&fromPageId=3395027007), o IMEI.
* **Filtro** <img src="../../../.gitbook/assets/Untitled (25).png" alt="" data-size="line"> : Le permite mostrar solo objetos específicos dependiendo de su **estado de movimiento** (por ejemplo, mostrar solo objetos en movimiento o estacionarios).
* **Opciones de ordenamiento** <img src="../../../.gitbook/assets/Untitled (26).png" alt="" data-size="line">: Cambia el orden de las entradas en la lista basado en ciertos parámetros:
  * Por nombre (A a Z o Z a A)
  * Por estado
  * Por distancia (útil para rastrear proximidad)

{% hint style="info" %}
El filtrado y ordenamiento no afectan la estructura de grupos pero reordenan objetos dentro de ellos. Los grupos sin objetos coincidentes se ocultan de la lista.
{% endhint %}

#### Configuraciones adicionales <a href="#configuraciones-adicionales-inlineextension" id="configuraciones-adicionales-inlineextension"></a>

La **Lista de objetos** también contiene el menú <img src="../../../.gitbook/assets/Untitled (27).png" alt="" data-size="line"> que proporciona acceso a configuraciones adicionales que influyen en la visibilidad de objetos e interacciones del mapa. Le ayuda a configurar el comportamiento del mapa relacionado con objetos y ajustar preferencias de visibilidad para una experiencia de seguimiento más enfocada.

<details>

<summary>Opciones del menú de tres puntos</summary>

* **Agrupar marcadores de objetos**: Agrupa múltiples objetos en proximidad cercana en un solo icono que muestra el número de objetos dentro. Esto ayuda a despejar el mapa cuando muchos objetos están en una área. Esta característica se aplica automáticamente cuando más de 300 objetos están a la vista.
* **Etiquetas de objetos**: Muestra el nombre del objeto cerca de su icono en el mapa.
* **Rastro**: Muestra un rastro de movimiento detrás del objeto mientras cambia de ubicación.
* **Animación**: Si está habilitada, el movimiento del objeto se anima suavemente en el mapa. Si está deshabilitada, la posición del objeto se actualiza estáticamente en intervalos basados en la recepción de datos.
* **Mostrar solo objetos seleccionados**: Por defecto, todos los objetos disponibles son visibles en el mapa. Cuando está habilitado, solo los objetos seleccionados de la lista se muestran.
* **Mostrar información al hacer clic**: Define cómo se abre el **Widget del objeto**. Si está habilitado, el widget se abre después de un solo clic en un objeto. Si está deshabilitado, necesita hacer clic ![](<../../../.gitbook/assets/Untitled (3).png>) en o hacer doble clic en el icono del objeto en el mapa para abrir el widget. Este botón aparece a la derecha del objeto cuando está seleccionado.
* **No agrupar**: Muestra todas las entradas en la lista individualmente en lugar de agruparlas. Si está habilitado, las reglas de ordenamiento y filtrado se aplican a toda la lista.
* **Seguir el objeto seleccionado**: Mantiene el mapa centrado en el objeto seleccionado mientras se mueve, evitando que se mueva fuera de la pantalla.

</details>

#### Historial de viajes y eventos <a href="#historial-de-viajes-y-eventos" id="historial-de-viajes-y-eventos"></a>

El **Historial de viajes y eventos** es accesible a través del botón <img src="../../../.gitbook/assets/Untitled (28).png" alt="" data-size="line"> en la **Lista de objetos**. Esta característica le permite revisar movimientos y eventos pasados de un objeto rastreado, proporcionando información sobre su actividad durante un período seleccionado. Le ayuda a analizar rutas, detectar anomalías y mejorar la eficiencia operacional.\
Para más detalles sobre esta característica, consulte [Historial](../historial/).

### Objetos <a href="#objetos" id="objetos"></a>

Cada entrada en la **Lista de objetos** representa un dispositivo de seguimiento conectado a la plataforma e incluye detalles críticos:

* **Etiqueta del objeto:** Muestra el nombre del dispositivo.
* **Información adicional**: Muestra la información de los bloques de datos marcados como Favoritos en el widget del objeto.\
  Para aprender más sobre mostrar estos datos, consulte [Favoritos](vista-detallada-del-objeto.md#favoritos).
* **Indicadores de estado**: Un indicador de estado de conexión que muestra el estado actualizado para el dispositivo. Para un desglose detallado del indicador de estado, consulte [Estado de conexión](estado-de-la-conexin.md).

#### **Acciones de objeto** <a href="#acciones-de-objeto" id="acciones-de-objeto"></a>

Hacer clic en un objeto en la lista centra el mapa en ese dispositivo.\
Cada objeto tiene un menú <img src="../../../.gitbook/assets/Untitled (27).png" alt="" data-size="line"> que ofrece más acciones rápidas:

* **Compartir ubicación**: Comparte instantáneamente la ubicación del objeto usando la herramienta de [Geo enlaces](../../../readme/geolinks/).
* **Cambiar icono**: Modifica la representación visual del objeto seleccionando [Iconos de objetos](iconos-de-objetos.md).
* **Abrir reglas de alerta**: Gestiona alertas para condiciones específicas en el módulo de [Alertas](../../reglas-y-alertas/).
* **Configuración del dispositivo**: Navega rápidamente a la configuración del dispositivo particular en [Dispositivos y ajustes](../../dispositivos-y-ajustes/).
* **Ver reportes**: Accede a reportes relacionados con la actividad del objeto en el módulo de [Reportes](../../reportes/).

Estas acciones permiten acceso rápido a herramientas de gestión esenciales directamente desde la lista.

#### **Widget del objeto** <a href="#widget-de-objeto" id="widget-de-objeto"></a>

Este widget es una vista detallada de un objeto seleccionado, mostrando parámetros de dispositivo disponibles, indicadores de estado y bloques de datos personalizables. Para acceder al **Widget del objeto**, haga doble clic en el icono del objeto en el mapa o pase el cursor sobre el objeto y haga clic en el icono ![](<../../../.gitbook/assets/Untitled (3).png>) que aparece.

{% hint style="info" %}
Si la opción **Mostrar información al hacer clic** está habilitada en las [Configuraciones adicionales](./#configuraciones-adicionales-inlineextension), hacer clic en un objeto también abre el [Widget del objeto](./#widget-de-objeto).
{% endhint %}

El widget proporciona acceso a métricas esenciales como nivel de batería, intensidad de señal y estado de movimiento, con opciones para configurar los datos mostrados. Dado que muchos de estos parámetros pueden ser esenciales para propósitos de resumen de seguimiento, ofrece un mecanismo de **Favoritos** que permite mostrar una selección de bloques de datos del dispositivo en la **Lista de objetos**, justo debajo de la etiqueta del dispositivo.\
Para más detalles sobre la funcionalidad del widget, consulte [Widget del objeto](vista-detallada-del-objeto.md).

### Contenido de la sección <a href="#contenido-de-la-seccion" id="contenido-de-la-seccion"></a>

* [Widget del objeto](https://squaregps.atlassian.net/wiki/spaces/UDOCES/pages/2922547998/Widget+del+objeto)
* [Estado de la conexión](https://squaregps.atlassian.net/wiki/spaces/UDOCES/pages/2922547931/Estado+de+la+conexi+n)
* [Iconos de objetos](https://squaregps.atlassian.net/wiki/spaces/UDOCES/pages/2922548025/Iconos+de+objetos)

&#x20;
