# Llamada de emergencia

## Visión general

La norma "Llamada de emergencia" está pensada para dispositivos GPS equipados con una función de llamada integrada, que suele encontrarse en dispositivos capaces de realizar llamadas de voz o comunicaciones por radio.

Esta regla activa las notificaciones cada vez que se activa la función de llamada telefónica del dispositivo, proporcionando una forma rápida de iniciar la comunicación en tiempo real. Esta función mejora la seguridad y la eficacia operativa al garantizar respuestas rápidas en situaciones críticas y contribuir a unas operaciones más fluidas.

## Configuración de reglas

La funcionalidad de esta regla depende de las capacidades y la configuración del dispositivo, por lo que no es necesario configurar ninguna regla específica.

Para los ajustes habituales, consulte [Normas y notificaciones](../).

## Detalles del funcionamiento del sistema

* **Reinicia el temporizador:** La alerta "Llamada de emergencia" tiene un temporizador de restablecimiento de 1 minuto, lo que significa que la alerta no se activará más de una vez por minuto. Si se produce un evento mientras la regla está esperando el reinicio, la plataforma omitirá el evento, incluso en los informes.
* **Múltiples dispositivos:** Esta regla permite a los usuarios seleccionar varios rastreadores de los que desean recibir notificaciones. Los rastreadores seleccionados deben admitir el evento "Llamada de emergencia", y esta función debe estar integrada en la plataforma para esos rastreadores. Esto permite a los usuarios supervisar los eventos en varios dispositivos cómodamente.
* **Alerta de eventos independiente del GPS:** La plataforma reconoce y contabiliza este tipo de evento de hardware aunque el paquete de datos carezca de coordenadas GPS válidas. El evento se mostrará independientemente de si se ha producido dentro o fuera de las geovallas definidas. En este caso se ignoran los ajustes de geofence Inside/Outside, lo que garantiza que no se omita ningún evento crítico.
