# Sensor de pulsera (o tobillo)

La regla del "sensor de pulsera" (o "sensor de tobillo") está diseñada específicamente para aplicaciones de vigilancia legal con rastreadores GPS especializados. Es una herramienta esencial para la seguridad en contextos como el arresto domiciliario o la libertad condicional.

Esta regla está diseñada para notificar inmediatamente al personal de seguridad si se retira un dispositivo GPS sin autorización. En estas situaciones, la regla activa una alerta instantánea a las autoridades pertinentes, lo que permite actuar con rapidez para evitar cualquier movimiento no autorizado o el incumplimiento de las condiciones legales.

## Configuración de reglas

Esta regla depende totalmente de las capacidades del dispositivo y de la configuración del hardware. No hay ajustes específicos que configurar dentro de la propia regla.

Para los ajustes habituales, consulte [Normas y notificaciones](../).

## Detalles del funcionamiento del sistema

* **Reinicia el temporizador.** La alerta "Sensor de pulsera" tiene un temporizador de restablecimiento de 3 minutos, lo que significa que el evento de alerta no se producirá más de una vez cada 3 minutos. Si este tipo de evento se produce en el tiempo que la regla ha estado esperando el reinicio, este evento será omitido por la plataforma, incluyendo los informes.
* **Múltiples dispositivos:** Con esta regla, tiene la flexibilidad de seleccionar varios rastreadores para recibir notificaciones. El único requisito es que los rastreadores seleccionados sean compatibles con eventos de sensor de Pulsera y tengan esta función integrada en la plataforma. Esto le permite supervisar múltiples rastreadores compatibles simultáneamente, asegurándose de que recibe notificaciones de los eventos relevantes a través de varios vehículos o dispositivos de manera eficiente.
* **Alerta de eventos independiente del GPS:** Cuando la plataforma detecta este tipo de evento de hardware a partir de datos del rastreador que carecen de coordenadas válidas, seguirá registrando y mostrando el evento como válido. Esto se aplica independientemente de si el evento tuvo lugar dentro o fuera de las geovallas designadas. En estos casos, la plataforma hace caso omiso de la lógica dentro/fuera de la geovalla para garantizar que el suceso se captura y se notifica.
