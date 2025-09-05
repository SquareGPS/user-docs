# Aparcamiento y tiempo de permanencia

## Visión general

La regla de tiempo de estacionamiento está diseñada para notificar a los usuarios cuando la duración del estacionamiento de un vehículo supera un límite especificado. Esta regla es crucial para controlar el tiempo que los vehículos permanecen estacionados, garantizando que los conductores respeten las normas de tiempo establecidas para el estacionamiento y los periodos de permanencia.

Por ejemplo, si la duración permitida del aparcamiento está fijada en 30 minutos, el sistema avisará a los usuarios siempre que un vehículo permanezca aparcado más allá de este límite. Estas notificaciones pueden enviarse a través de la interfaz de usuario, por correo electrónico o SMS, y los usuarios también pueden generar informes para revisar estos eventos históricamente.

## Configuración de reglas

**Tiempo de estacionamiento permitido**\
El tiempo de estacionamiento empieza a contar en cuanto el vehículo entra en estado estacionado. Los usuarios pueden configurar la duración permitida del estacionamiento, con opciones que van de 5 a 60.000 minutos. El temporizador se reinicia cuando el vehículo sale del estado de estacionamiento. Para obtener información más detallada sobre la detección de aparcamiento, consulte el artículo Detección de aparcamiento.

Para controlar el tiempo de permanencia en zonas específicas, vincule la regla a las geocercas designadas.

Para los ajustes habituales, consulte [Normas y notificaciones](../).

## Detalles del funcionamiento del sistema

* La alerta "Tiempo de aparcamiento" tiene un temporizador de restablecimiento de 10 segundos, lo que significa que la alerta no se activará con más frecuencia que una vez cada 10 segundos. Si se produce un evento mientras la regla está esperando el reinicio, la plataforma omitirá el evento, incluso en los informes.
* Esta regla se procesa en la nube y no está vinculada a ningún hardware específico, lo que permite aplicarla a varios rastreadores simultáneamente. Esta flexibilidad permite a los usuarios gestionar varios rastreadores con una sola regla.
