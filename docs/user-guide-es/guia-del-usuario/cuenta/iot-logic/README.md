# IoT Logic

## Su solución completa de gestión de datos

**IoT Logic** es una herramienta sin necesidad de conocimientos de coding integrada en la plataforma Navixy, diseñada para simplificar la gestión de datos telemáticos. Combina un sistema de flujo visual con un lenguaje de expresión basado en JEXL, lo que permite una transformación eficiente de los datos sin necesidad de conocimientos de coding. Como gestor del tráfico de datos, procesa datos sin procesar procedentes de dispositivos GPS, cámaras de salpicadero y sensores IoT, convirtiéndolos en información práctica a través de canales de datos personalizados.

<figure><img src="../../../.gitbook/assets/image (2).png" alt="Esquema general del componente IoT Logic"><figcaption><p>Esquema general del componente IoT Logic</p></figcaption></figure>

{% hint style="info" %}
**Navegación**

Los **propietarios** de cuentas pueden acceder a IoT Logic en la sección **Ajustes** (de cuenta). Para encontrarla:

1. Haga clic en el icono de perfil en la esquina superior izquierda de la pantalla para abrir la configuración de su cuenta.
2. En la barra lateral de ajustes, seleccione **IoT Logic.**
{% endhint %}

## Componentes de IoT Logic

**IoT Logic** aprovecha sus componentes para procesar, descodificar, enriquecer y convertir los datos entrantes en tiempo real, garantizando la compatibilidad con diversas plataformas y servicios. Al optimizar la gestión del flujo de datos, la solución mejora la precisión y la personalización de sus actividades relacionadas con los datos y ofrece un mayor control sobre los datos implicados en sus procesos en general.

### Flujo

El **flujo** es el elemento funcional central de IoT Logic, que proporciona un marco estructurado para diseñar, personalizar y gestionar el procesamiento de datos. Introduce un espacio de trabajo intuitivo de arrastrar y soltar que simplifica la creación de canalizaciones de datos. El proceso se articula en torno a tres etapas clave de interacción de datos, cada una de ellas gestionada por nodos específicos:

* **Recepción de datos**\
  [El nodo Fuente de Datos](gestin-de-flujos/el-nodo-fuente-de-datos.md) gestiona la recepción de datos conectando los rastreadores a la plataforma Navixy para una entrada sin fisuras.
* **Enriquecimiento** **de datos**\
  [El nodo Iniciar Atributo](gestin-de-flujos/el-nodo-iniciar-atributo/) permite el enriquecimiento de datos mediante el cambio de nombre y la personalización de los parámetros de entrada para satisfacer los distintos requisitos de las aplicaciones.\
  [El nodo Logic](./) permite el enrutamiento condicional de datos creando puntos de ramificación que dirigen el flujo de datos basándose en expresiones lógicas y condiciones en tiempo real.
* **Transmisión** **de** **datos**\
  [El nodo Punto de Salida](gestin-de-flujos/el-nodo-punto-de-salida.md) gestiona la transmisión de datos reenviando los datos procesados a servidores y aplicaciones de terceros, garantizando una entrega eficaz.

{% hint style="info" %}
Se puede interactuar con estos nodos directamente desde la interfaz de Navixy. Para obtener un desglose detallado de cada nodo e instrucciones de uso dentro de la interfaz de usuario, rediríjase a las descripciones dedicadas haciendo clic en las operaciones de datos de la lista.
{% endhint %}

### Analizador de flujo de datos

El analizador de flujo de datos es una herramienta de supervisión que ofrece funciones de solución de problemas en tiempo real para su flujo de datos. El analizador ofrece una visión detallada de los datos entrantes de los dispositivos, lo que lo convierte en el principal instrumento para evaluar la integridad de los datos. Además, tiene el potencial de minimizar los riesgos operativos, potenciar la toma de decisiones y mejorar la calidad del servicio al permitirle identificar rápidamente las incoherencias de los datos, optimizar el rendimiento de los dispositivos y mantener un funcionamiento sin interrupciones.

Para más detalles e instrucciones de uso, consulte [Analizador de flujo de datos](https://app.gitbook.com/s/tx3J5BxnWyPV0nP2xr0z/technologies/navixy-generic-protocol).

### Navixy Generic Protocol

Navixy Generic Protocol (NGP) crea la base para el manejo de datos de IoT Logic. Se trata de un mecanismo de comunicación flexible diseñado para estandarizar los flujos de datos de diversos dispositivos GPS y sensores conectados a ellos, lo que permite una integración perfecta en un único sistema. Independientemente del formato original de los datos, NGP unifica las comunicaciones entre dispositivos convirtiendo todos los datos entrantes en un estándar común, lo que reduce los problemas de compatibilidad. El protocolo garantiza una transmisión de datos fiable, escalable y segura, por lo que resulta ideal para tareas complejas de gestión de flotas y seguimiento de activos.

Para obtener detalles técnicos y orientación sobre la implementación, [consulte la documentación específica del Navixy Generic Protocol](https://squaregps.atlassian.net/wiki/spaces/NAV/pages/3107553589/Navixy+Generic+Protocol?atlOrigin=eyJpIjoiYWI4MGE3M2MxNjEyNDhlNGFlOWRlNmFjZDcyZDJkMzEiLCJwIjoiYyJ9).

## Acceso a la API

También se puede acceder a las funciones de IoT Logic mediante programación a través de la API de Navixy. Esto permite a los desarrolladores automatizar la creación, gestión y supervisión de flujos.

{% hint style="info" %}
Por razones de seguridad, el acceso a la API requiere los permisos adecuados. Póngase en contacto con el administrador de su cuenta para asegurarse de que dispone de los derechos de acceso necesarios.
{% endhint %}

Para obtener la documentación completa de la API, parámetros, formatos de solicitud/respuesta y ejemplos de código, consulte la [documentación de la API de IoT Logic](https://app.gitbook.com/s/tx3J5BxnWyPV0nP2xr0z/).

## Contenido de la sección

Páginas secundarias

* [Espacio de trabajo y flujo por defecto](espacio-de-trabajo-y-flujo-por-defecto.md)
* [Guía de inicio rápido](gua-de-inicio-rpido.md)
* [Gestión de flujos](gestin-de-flujos/)
  * [El nodo Fuente de Datos](gestin-de-flujos/el-nodo-fuente-de-datos.md)
  * [El nodo ](gestin-de-flujos/el-nodo-iniciar-atributo/)[Iniciar Atributo](https://squaregps.atlassian.net/wiki/spaces/UDOCES/pages/3232334272/El+nodo+Iniciar+Atributo)
    * [Gestión de atributos](gestin-de-flujos/el-nodo-iniciar-atributo/gestin-de-atributos.md)
    * [Ejemplos de cálculo](gestin-de-flujos/el-nodo-iniciar-atributo/ejemplos-de-clculo.md)
    * [Visualización de nuevos atributos calculados en la plataforma Navixy](../../../readme/cuenta/iot-logic/gestin-de-flujos/el-nodo-iniciar-atributo/visualizacion-de-nuevos-atributos-calculados-en-la-plataforma-navixy.md)
  * [El nodo Logic](../../../readme/cuenta/iot-logic/gestin-de-flujos/el-nodo-logic/)
    * [Expresiones y sintaxis del nodo Logic](../../../readme/cuenta/iot-logic/gestin-de-flujos/el-nodo-logic/expresiones-y-sintaxis-del-nodo-logic.md)
  * [El nodo Punto de Salida](gestin-de-flujos/el-nodo-punto-de-salida.md)
  * [Ejemplo de configuración de flujo](gestin-de-flujos/ejemplo-de-configuracin-de-un-flujo.md)
* [Analizador de flujo de datos](analizador-de-flujo-de-datos.md)
