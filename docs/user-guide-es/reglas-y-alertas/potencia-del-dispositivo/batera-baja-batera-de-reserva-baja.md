# Batería baja (Batería de reserva baja)

## Visión general

Un dispositivo GPS emite una alerta de batería baja cuando el nivel de carga de su batería interna desciende por debajo de un umbral predeterminado. Esta alerta se activa para notificar a los usuarios que la energía del dispositivo se está agotando, lo que indica que la batería debe recargarse o sustituirse pronto.

En el caso de los rastreadores portátiles, esta alerta indica que la fuente de alimentación principal se está agotando, mientras que para los rastreadores montados en vehículos, puede indicar que la batería de reserva se está agotando, lo que podría poner en peligro la capacidad del dispositivo para seguir rastreando si se pierde la fuente de alimentación principal.

![](https://squaregps.atlassian.net/wiki/images/icons/grey_arrow_down.png)

Función de las baterías internas en los dispositivos GPS

La batería interna de un dispositivo GPS es una fuente de energía integrada que desempeña un papel crucial en la funcionalidad del dispositivo. Dependiendo de la finalidad del rastreador GPS, esta batería interna puede desempeñar diferentes funciones.

* **En rastreadores GPS portátiles,** la batería interna suele ser la principal fuente de energía. Estas baterías son esenciales para el seguimiento de activos, personas o vehículos en situaciones en las que no se dispone de alimentación externa.
* **Para rastreadores GPS montados en vehículos,** la batería interna suele actuar como fuente de alimentación de reserva. Esta batería de reserva entra en funcionamiento cuando se interrumpe el suministro eléctrico principal del vehículo, ya sea por desconexión, manipulación o fallo de la batería del vehículo. La batería de reserva garantiza el seguimiento continuo y la transmisión de datos, proporcionando una capa extra de seguridad y fiabilidad, especialmente en aplicaciones críticas de gestión de flotas o antirrobo.

## Dos normas de control de la batería

En Navixy, hay dos reglas distintas diseñadas para controlar el estado de la batería de los dispositivos GPS: la regla "Batería baja" y la regla "Batería de reserva baja".

* **La regla de la "batería baja** se aplica a la fuente de alimentación primaria del dispositivo, normalmente utilizada en rastreadores portátiles o dispositivos que dependen únicamente de baterías internas.
* **La regla "Batería de reserva baja** controla específicamente el nivel de carga de las baterías secundarias o de reserva, que suelen encontrarse en los seguidores montados en vehículos.

Se trata de reglas basadas en hardware, lo que significa que el propio dispositivo o su configuración determinan el umbral de activación de la alerta de batería baja. Cuando la carga de la batería cae por debajo de este umbral, el dispositivo lo notifica y el sistema envía una notificación, lo que permite a los usuarios tomar medidas proactivas para recargar el dispositivo y evitar tiempos de inactividad.

## Configuración de reglas

Esta regla depende totalmente de las capacidades del dispositivo y de la configuración del hardware. No hay ajustes específicos que configurar dentro de la propia regla.

Para los ajustes habituales, consulte [Normas y notificaciones](../).

## Plataforma

Las alertas "Batería baja" y "Batería de reserva baja" comparten varias similitudes operativas, pero hay una diferencia en sus temporizadores de reinicio.

* **Reiniciar temporizadores**: La alerta "Batería de reserva baja" tiene un temporizador de restablecimiento de 1 minuto, lo que significa que la alerta no se activará con más frecuencia que una vez por minuto. Por el contrario, la alerta "Batería baja" tiene un temporizador de restablecimiento más largo de 30 minutos, por lo que no se activará con más frecuencia que una vez cada 30 minutos. Si se produce un evento durante el periodo de restablecimiento de cualquiera de las reglas, se omitirá de la plataforma, incluidos los informes.
* **Selección del rastreador**: Ambas reglas permiten a los usuarios supervisar varios rastreadores, siempre que los rastreadores admitan los eventos respectivos y la función esté integrada en la plataforma. Esta capacidad permite una supervisión eficaz de los niveles de batería en varios vehículos o dispositivos.
* **Inscripción**: Para ambas reglas, la plataforma registrará y mostrará el evento aunque se reciba en un paquete sin coordenadas válidas. Esto garantiza que los usuarios estén informados del evento independientemente de su ubicación, manteniendo una supervisión coherente de sus activos.
