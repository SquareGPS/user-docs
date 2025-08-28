# Pérdida y recuperación de la señal GPS

## Visión general

La regla "Pérdida/recuperación de la señal GPS" supervisa la disponibilidad de la señal GPS para sus dispositivos. Esta regla activa notificaciones cuando un dispositivo pierde su señal GPS, a menudo debido a que se encuentra en interiores, bajo tierra o en una zona con poca visibilidad del satélite, y cuando la señal se recupera posteriormente. Al recibir estas notificaciones, puede mantenerse informado sobre el estado de la ubicación de sus activos, incluso en entornos difíciles.

Esta regla es especialmente útil en entornos donde la cobertura de la señal GPS es poco fiable, como obras, almacenes o instalaciones subterráneas. Asegurarse de que su rastreador mantiene conexiones celulares y de Internet es crucial para recibir estas alertas cuando se pierde y se recupera la señal GPS.

## Configuración de reglas

Esta regla se procesa en la nube, lo que significa que el software del servidor controla cuándo se pierde la señal GPS y cuándo se recupera. Puedes aplicar esta regla a varios rastreadores simultáneamente, siempre y cuando los rastreadores admitan este tipo de evento y esté integrado en la plataforma.

Para conocer la configuración habitual de las reglas, consulte [Normas y notificaciones](../../).

## Detalles del funcionamiento del sistema

* **Reinicia el temporizador:** La alerta "Señal GPS perdida/recuperada" tiene un temporizador de restablecimiento de 10 segundos, lo que significa que la alerta no se activará con más frecuencia que una vez cada 10 segundos. Si se produce un evento durante el periodo de restablecimiento, la plataforma lo omitirá, incluso en los informes.
* **Múltiples dispositivos:** Puede seleccionar varios rastreadores para supervisar bajo esta regla, siempre que los rastreadores admitan eventos de pérdida/recuperación de señal GPS y la función esté integrada en la plataforma. Esto te permite gestionar varios dispositivos de forma eficiente.
* **Alerta de eventos independiente del GPS:** La plataforma registrará y mostrará este evento incluso si se recibe en un mensaje sin coordenadas válidas, asegurándose de que estés informado independientemente de la ubicación del evento. Los ajustes Dentro/Fuera de las geovallas se ignoran en estos casos, ya que la plataforma prioriza la visualización de eventos potencialmente críticos.
