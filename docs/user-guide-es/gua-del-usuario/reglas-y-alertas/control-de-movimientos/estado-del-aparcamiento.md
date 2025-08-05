# Estado del aparcamiento

## Visión general

Los estados de aparcamiento pueden dividirse en dos categorías principales: Estacionado (Parado) y No estacionado (En movimiento, Parado). Esta regla permite a los usuarios recibir notificaciones cuando un estado de aparcamiento cambia de uno a otro. Por ejemplo, las organizaciones que desean controlar el tiempo de conducción de sus vehículos pueden utilizar esta regla para asegurarse de que los vehículos no se utilizan fuera de servicio. Esta regla proporciona notificaciones a la interfaz de usuario, dirección de correo electrónico o número de teléfono sobre los estados de aparcamiento de los objetos seleccionados.

La configuración de esta regla ayuda a los usuarios a mantenerse informados sobre el inicio y el final de los viajes, así como sobre los cambios en el estado de aparcamiento de sus vehículos. Esto mejora el control, la seguridad y la eficiencia en las operaciones de gestión de flotas.

## Configuración de reglas

**Configuraciones de detección de aparcamiento**

La configuración de una regla de detección de aparcamiento se gestiona exclusivamente dentro del widget Detección de aparcamiento. Para obtener información detallada sobre la configuración de la detección de aparcamiento, consulte el artículo Detección de aparcamiento.

Para los ajustes habituales, consulte [Normas y notificaciones](https://squaregps.atlassian.net/wiki/spaces/USERDOCS/pages/2761228324/Rules+and+Notifications#Manage-rules).

## Detalles del funcionamiento del sistema

- La alerta "Detección de estado de aparcamiento" tiene un temporizador de restablecimiento de 10 segundos, lo que significa que el evento de alerta no se producirá más de una vez cada 10 segundos. Si se produce un evento mientras la regla está esperando el reinicio, la plataforma omitirá el evento, incluso en los informes.
- Esta regla se detecta en el lado del servidor y no está vinculada a ningún hardware específico, lo que permite aplicarla a varios rastreadores simultáneamente. Esta flexibilidad le permite gestionar varios rastreadores con una sola regla.