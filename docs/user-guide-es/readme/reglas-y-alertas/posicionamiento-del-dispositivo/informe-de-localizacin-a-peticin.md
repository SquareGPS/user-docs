# Informe de localización a petición

## Visión general

En **Informe de localización a petición por SMS** permite a los usuarios solicitar manualmente la ubicación actual de un dispositivo GPS mediante el envío de un comando SMS. Esta función es especialmente útil en situaciones en las que el dispositivo no puede establecer una conexión celular con la plataforma sobre IP, como cuando se encuentra en una zona de itinerancia con cobertura de datos limitada o nula.

Cuando el dispositivo no puede transmitir sus datos de localización a través de los canales habituales (como GPRS o redes 3G/4G), el **Actualización de la ubicación a petición por SMS** ofrece una alternativa fiable. Enviando un SMS desde la plataforma al dispositivo, los usuarios pueden conocer su posición. El dispositivo responde con sus coordenadas GPS a través de SMS a la plataforma, garantizando el seguimiento de la ubicación incluso cuando las conexiones de datos estándar no están disponibles.

Para aumentar aún más la comodidad, Navixy ofrece un **Regla de actualización de ubicación por SMS**. Esta regla notifica a los usuarios en cuanto se recibe una actualización de la ubicación GPS por SMS. Dado que las actualizaciones de ubicación por SMS pueden tardar entre minutos y horas, en función de la disponibilidad de la red y del estado del dispositivo, esta regla garantiza que los usuarios reciban un aviso inmediato cuando se produce la actualización. Esta función de notificación agiliza el proceso, permitiendo a los usuarios centrarse en otras tareas sin necesidad de comprobar manualmente la llegada de la actualización.

## Configuración de reglas

No hay ajustes específicos para las reglas. Para conocer los ajustes habituales, consulte [Reglas y alertas](../../../guia-del-usuario/reglas-y-alertas/).

## Detalles del funcionamiento del sistema

* **Reinicia el temporizador.** La alerta "Informe de localización a petición" tiene un temporizador de restablecimiento de 1 minuto, lo que significa que el evento de alerta no se producirá más a menudo que una vez cada 1 minuto. Si este tipo de evento se produce en el tiempo que la regla ha estado esperando el reinicio, este evento será omitido por la plataforma, incluyendo los informes.
* **Múltiples dispositivos.** En este tipo de regla, los usuarios tienen la flexibilidad de seleccionar varios rastreadores de los que desean recibir notificaciones. El único requisito es que los rastreadores seleccionados sean compatibles con la notificación de eventos de localización bajo demanda y que la función esté integrada en la plataforma para los rastreadores en cuestión. Esto significa que los usuarios pueden elegir varios rastreadores compatibles para recibir notificaciones, lo que les permite supervisar los eventos de conducción difíciles en varios vehículos o dispositivos de una manera conveniente.
