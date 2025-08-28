# Dispositivo OBDII plug/unplug

## Visión general

La regla "Conectar / Desconectar Dispositivo OBDII" está diseñada para proporcionar alertas inmediatas cada vez que un rastreador GPS OBDII se conecta o desconecta del puerto OBDII del vehículo. Esta regla garantiza que los usuarios puedan tomar medidas inmediatas para mantener el rastreo continuo y la funcionalidad del dispositivo.

Por ejemplo, cuando el rastreador se desconecta, pasa a utilizar su batería interna, que tiene una vida útil limitada. Las notificaciones inmediatas en caso de desconexión permiten a los usuarios responder rápidamente, garantizando un seguimiento y una transmisión de datos ininterrumpidos.

## Configuración de reglas

Esta regla depende totalmente de las capacidades del dispositivo y de la configuración del hardware. No hay ajustes específicos que configurar dentro de la propia regla.

Para los ajustes habituales, consulte [Normas y notificaciones](../).

## Detalles del funcionamiento del sistema

* **Reinicia el temporizador.** La alerta "Dispositivo OBDII Plug/Unplug" tiene un temporizador de reinicio de 5 minutos, lo que significa que la alerta no se activará con más frecuencia que una vez cada 5 minutos. Si el evento se produce mientras la regla está en el periodo de reinicio, será omitido por la plataforma, incluso en los informes.
* **Múltiples dispositivos.** **Múltiples dispositivos:** Los usuarios pueden seleccionar múltiples rastreadores para monitorear bajo esta regla. El único requisito es que los dispositivos seleccionados admitan eventos de conexión/desconexión del puerto OBDII. Esta flexibilidad permite a los usuarios supervisar este tipo de evento en varios vehículos o dispositivos cómodamente.
* **Alerta de eventos independiente del GPS.** El sistema procesa estos eventos independientemente de si hay datos GPS disponibles. El suceso se seguirá registrando y mostrando, aunque se produzca fuera de las geocercas definidas.
