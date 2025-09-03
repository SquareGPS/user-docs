# Widget del objeto

En Navixy, el **Widget de objeto** sirve como una colección integral de bloques de datos telemáticos para monitorear y gestionar su flota. Proporciona una vista detallada de sus activos comerciales, dispositivos GPS y los sensores conectados a ellos.

{% hint style="info" %}
**Navegación**

* Por defecto, para acceder a la vista detallada de un objeto específico, haga clic en el icono del objeto en el mapa o pase el cursor sobre él y haga clic en el botón <img src="../../../.gitbook/assets/Untitled (3).png" alt="" data-size="line"> que aparece.
* Si la opción **Mostrar información al hacer clic** está habilitada en la [Configuración adicional](https://squaregps.atlassian.net/wiki/spaces/UDOCES/pages/2922547887/Lista+de+objetos#additional-settings), hacer clic en un objeto también abre el **Widget de objeto**.
{% endhint %}

Una vez abierto, el panel muestra información extensa sobre el objeto seleccionado, incluyendo el estado actual, ubicación GPS y datos telemáticos adicionales. Todas las herramientas de gestión operacional están convenientemente ubicadas en un solo lugar, permitiendo una gestión eficiente de la flota y respuesta rápida a cualquier problema que surja.

<figure><img src="../../../.gitbook/assets/Untitled (1).png" alt=""><figcaption></figcaption></figure>

### Estructura

La sección superior del panel del widget contiene detalles esenciales sobre el objeto, incluyendo su nombre, estado de movimiento y estado de conexión. También incluye las siguientes opciones:

* **Opciones de personalización**\
  El diseño del widget proporciona capacidades de personalización robustas para ayudarle a organizar la información según sus necesidades:
  * **Bloques de datos**: Haga clic en <img src="../../../.gitbook/assets/Untitled (4).png" alt="" data-size="line"> para abrir la configuración del widget y seleccionar qué bloques de datos desea mostrar. Por defecto, todos los bloques disponibles para los objetos están seleccionados. Este menú también habilita la visualización del tiempo de actualización debajo de cada sensor.
  * **Gestión de diseño**: Haga clic en <img src="../../../.gitbook/assets/Untitled (5).png" alt="" data-size="line"> para cambiar al modo de gestión de diseño. Cuando está habilitado, puede arrastrar los bloques de datos a sus posiciones preferidas. En este modo, también puede cambiar el orden de la información dentro de los bloques manualmente de la misma manera arrastrando y soltando.
* **Acceso a vista de calle**\
  Hacer clic en el widget habilita la **Vista de calle**, mostrando las imágenes del mundo real de la posición del objeto en el mapa para mejorar el contexto y la navegación.
* **Monitoreo de video**\
  El botón <img src="../../../.gitbook/assets/Untitled (6).png" alt="" data-size="line">, disponible solo para dispositivos GPS con esta funcionalidad, abre la ventana de **Monitoreo de video**. Aquí, puede ver una transmisión en vivo desde su cámara o revisar grabaciones pasadas almacenadas en la memoria del dispositivo o en la nube. Para obtener más información sobre esta función, consulte Monitoreo de video.
* **Aplicar marcadores a todos los vehículos**\
  El botón <img src="../../../.gitbook/assets/Untitled (7).png" alt="" data-size="line"> le permite marcar instantáneamente todos los bloques de datos como **Favoritos**, asegurando que su información se muestre bajo el nombre del objeto en la **Lista de objetos**. Para detalles sobre esta función, consulte Favoritos.

### Bloques de datos

El **Widget de objeto** organiza información crucial a través de bloques de datos especializados. Cada componente sirve un propósito específico en proporcionar capacidades integrales de monitoreo y gestión.

La disponibilidad y contenido de los bloques depende del dispositivo GPS asignado al objeto seleccionado. Muestran solo la información transmitida por el dispositivo o sensores conectados a él. También puede personalizar su apariencia. Para detalles, consulte Opciones de personalización arriba.

Aquí hay una descripción detallada de los bloques disponibles:

| **Bloque**               | **Descripción**                                                                                                                                                                                                                                                                                                                   |
| ------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Ubicación**            | Proporciona datos de posicionamiento precisos, incluyendo la última ubicación conocida con una dirección de calle o coordenadas GPS, acompañada de marcas de tiempo. El widget también rastrea las mediciones actuales de velocidad y altitud.                                                                                    |
| **Dispositivo GPS**      | Proporciona información básica sobre el dispositivo GPS, incluyendo su estado de conexión, nivel de señal GPS/GSM y plan de suscripción.                                                                                                                                                                                          |
| **Estado**               | Proporciona estado de movimiento, velocidad y dirección.                                                                                                                                                                                                                                                                          |
| **OBD2 y CAN**           | Se conecta a los sistemas integrados del vehículo para proporcionar datos de diagnóstico en tiempo real, como nivel de combustible, velocidad del motor, temperatura del refrigerante y cualquier código de problema de diagnóstico cuando el dispositivo GPS está correctamente conectado al bus CAN del vehículo o puerto OBD2. |
| **Lecturas de sensores** | Monitorea y muestra datos de todos los sensores del dispositivo configurados, proporcionando lecturas recientes con marcas de tiempo. Los sensores individuales pueden marcarse como **Favoritos** para acceso rápido a mediciones críticas.                                                                                      |
| **Odómetro**             | Rastrea el kilometraje total del dispositivo. Estos datos pueden ajustarse manualmente a través del botón <img src="../../../.gitbook/assets/Untitled (8).png" alt="" data-size="line">, asegurando registros precisos de distancia.                                                                                              |
| **Horas del motor**      | Monitorea el tiempo total de funcionamiento del motor. Estos datos pueden ajustarse manualmente a través del botón <img src="../../../.gitbook/assets/Untitled (8).png" alt="" data-size="line"> para un seguimiento preciso del uso.                                                                                             |
| **Entradas**             | Monitorea el estado actual de varios sensores conectados, incluyendo el estado del encendido y otros sensores del vehículo como sensores de puertas, proporcionando retroalimentación en tiempo real sobre el estado del vehículo.                                                                                                |
| **Salidas**              | Permite control activo sobre dispositivos conectados al dispositivo GPS, incluyendo funciones como inmovilización remota del vehículo, permitiendo intervención directa cuando sea necesario.                                                                                                                                     |
| **Conductor**            | Muestra el conductor del vehículo y le permite asignarlo directamente a través del widget. También muestra su número de teléfono, llave y el tiempo en que se asignó el conductor.                                                                                                                                                |
| **Estados de trabajo**   | Gestiona estados operacionales mostrando y habilitando cambios al estado actual del objeto, ayudando a rastrear su historial de trabajo.                                                                                                                                                                                          |
| **Eventos recientes**    | Rastrea y muestra alertas relacionadas con el objeto. Por defecto, puede ver tres eventos recientes con una opción para ver todos ellos. Haga clic en <img src="../../../.gitbook/assets/Untitled (9).png" alt="" data-size="line"> junto al evento para abrir sus detalles.                                                      |
| **Candado electrónico**  | Proporciona gestión de seguridad para dispositivos equipados con funciones de cerradura inteligente, habilitando control remoto sobre el estado de la cerradura, incluyendo capacidades tanto de bloqueo como desbloqueo.                                                                                                         |

### Favoritos

La **Lista de objetos** puede mostrar no solo los nombres de los objetos y el estado de conexión, sino también datos telemáticos específicos de dispositivos GPS y sensores conectados. Para lograr eso, necesita marcar los bloques de datos como **Favoritos** siguiendo estos pasos:

1. Pase el cursor sobre el bloque de datos deseado dentro del **Widget de objeto**.
2. Haga clic en el botón <img src="../../../.gitbook/assets/Untitled (10).png" alt="" data-size="line"> que aparece para marcarlo como **Favorito**.

Una vez marcada como **Favorito**, la entrada de datos seleccionada aparecerá bajo el objeto correspondiente en la **Lista de objetos**, asegurando acceso rápido y fácil. Para eliminar un bloque de la visualización de la lista, haga clic en <img src="../../../.gitbook/assets/Untitled (10).png" alt="" data-size="line">nuevamente.

### Monitoreo de video

La ventana de **Monitoreo de video** proporciona acceso a video en tiempo real e histórico para dispositivos GPS con soporte de cámara. Esta función habilita capacidades de monitoreo visual a través de una interfaz dedicada accesible desde el **Widget de objeto**. El sistema soporta tanto transmisión en vivo como reproducción de video grabado desde múltiples fuentes de cámara.

#### Monitoreo de transmisión en vivo

La funcionalidad de transmisión en vivo entrega feeds de video en tiempo real desde cámaras de tablero instaladas o dispositivos MDVR directamente a su interfaz de monitoreo.

Para usar la función de transmisión en vivo, siga estos pasos:

1. Haga clic en para iniciar la transmisión en vivo.
2. Use los controles del reproductor para navegar a través del metraje reciente.
3. Seleccione el botón **En vivo** para regresar a la visualización en tiempo real.

{% hint style="warning" %}
La transmisión de video consume tráfico de datos significativo. Para conservar ancho de banda, la plataforma automáticamente detiene la transmisión cuando cierra la ventana de video o navega a otro módulo. Para la mayoría de navegadores, cerrar la pestaña también detendrá la transmisión, aunque algunas extensiones del navegador pueden interferir con esta función.
{% endhint %}

#### Reproducción de video

La funcionalidad de reproducción permite revisar metraje de video histórico almacenado ya sea en el dispositivo o en la plataforma de la nube. Esta capacidad soporta análisis de eventos, monitoreo del comportamiento del conductor e investigación de incidentes.

Para usar la función de reproducción, siga estos pasos:

1. Abra el menú de selección de fecha para elegir la fecha del video que desea ver.
2. Dependiendo de su historial, los siguientes iconos se mostrarán bajo la fecha:
   * **Punto gris**: La información está almacenada en la memoria del dispositivo. Verla requiere subirla desde el dispositivo a la nube. Esto se hace mientras reproduce el video.
   * **Punto azul**: Contenido ya disponible en el almacenamiento en la nube.
   * **Sin punto**: No hay contenido de video disponible para la fecha seleccionada
3. Seleccione su fecha deseada para acceder a la línea de tiempo por horas.
4. Elija segmentos de tiempo específicos de la línea de fragmentos para reproducción

{% hint style="warning" %}
Considere las implicaciones de uso de datos al descargar múltiples fragmentos.
{% endhint %}
