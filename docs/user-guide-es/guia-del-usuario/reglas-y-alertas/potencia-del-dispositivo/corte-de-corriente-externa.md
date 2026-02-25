# Corte de corriente externa

La regla "Corte de alimentación externa" está diseñada para rastreadores GPS de vehículos con cable que dependen del sistema eléctrico del vehículo. Esta regla es crucial para la gestión de flotas, ya que supervisa el suministro eléctrico del dispositivo GPS y alerta a los usuarios cuando se desconecta la alimentación externa.

Al detectar un corte de energía, el dispositivo GPS cambia automáticamente a su batería interna (si está disponible) para mantener la funcionalidad e informar a la plataforma. La plataforma registra estos eventos y notifica a los usuarios según la configuración de la regla.

## Configuración de reglas

Esta regla depende totalmente de las capacidades del dispositivo y de la configuración del hardware. No hay ajustes específicos que configurar dentro de la propia regla.

Para los ajustes habituales, consulte [Reglas y alertas](../).

## Detalles del funcionamiento del sistema

* **Reinicia el temporizador.** La alerta "Corte de alimentación externa" tiene un temporizador de reinicio de 5 minutos, lo que significa que la alerta no se activará con más frecuencia que una vez cada 5 minutos. Si se produce un evento durante el periodo de restablecimiento, se omitirá de la plataforma y no se incluirá en los informes.
* **Evento detectado por el dispositivo.** Este evento lo activa directamente el dispositivo en función de su configuración. El dispositivo y su configuración deben admitir esta funcionalidad para poder utilizar la regla.
* **Alerta de eventos independiente del GPS.** La plataforma registrará y mostrará el evento incluso si se recibe en un mensaje sin coordenadas válidas, garantizando que los usuarios estén informados independientemente de la ubicación del evento. En estos casos se ignora la configuración de Dentro/Fuera de las geocercas, ya que la plataforma prioriza la visualización de eventos potencialmente críticos.
