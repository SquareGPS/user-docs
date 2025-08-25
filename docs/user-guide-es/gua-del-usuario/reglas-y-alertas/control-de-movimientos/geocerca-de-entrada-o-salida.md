# Geocerca de entrada o salida

## Visión general

Una geo-valla es un área designada en un mapa que actúa como un límite virtual. Esta regla rastrea cuando los rastreadores entran o salen del área de geovalla especificada. Los usuarios recibirán notificaciones cada vez que sus objetos crucen estos límites de la geo-valla. Por ejemplo, si una pieza de maquinaria de construcción sale de la zona designada, un empleado de la empresa puede recibir una notificación a través de la interfaz de usuario, correo electrónico o SMS si se configura en la regla.

![image-20240805-231934.png](attachments/image-20240805-231934.png)

Esta funcionalidad proporciona información valiosa y control sobre el movimiento de objetos, garantizando la adherencia a los límites predefinidos. Mejora la seguridad alertando a los usuarios de cualquier movimiento no autorizado o posible robo fuera de la zona de geovalla especificada. Además, permite una gestión eficaz de los activos al permitir a los usuarios realizar un seguimiento y optimizar la utilización de sus equipos dentro de las zonas designadas.

## Configuración de reglas

#### Geocercas

Especifique las geovallas que activarán notificaciones cuando se crucen. Puede incluir varias geocercas en una misma regla.

Para los ajustes habituales, consulte [Normas y notificaciones](../).

## Detalles del funcionamiento del sistema

* La alerta "Entrada o salida de geovalla" tiene un temporizador de restablecimiento de 60 segundos, lo que significa que la alerta no se activará más a menudo que una vez cada minuto. Si se produce un evento mientras la regla está esperando el reinicio, la plataforma omitirá el evento, incluso en los informes.
* Esta regla se procesa en la nube y no está vinculada a ningún hardware específico, lo que permite aplicarla a varios rastreadores simultáneamente. Esta flexibilidad le permite gestionar varios rastreadores con una sola regla.
* Tenga en cuenta que el sistema puede generar una alerta de entrada/salida aunque se produzcan desvíos del GPS. Aunque se filtren las coordenadas GPS no válidas, pueden aparecer pequeñas desviaciones GPS en el rastreo. Existen varios métodos para prevenir eventos de desvío de GPS, dependiendo de la funcionalidad del modelo de rastreador. Para más detalles sobre cómo evitar el desvío del GPS, consulte el manual del dispositivo.
