# Cambio de situación laboral

## Visión general

La regla "Cambio de estado de trabajo" está diseñada para supervisar y realizar un seguimiento en tiempo real de las actividades de los empleados móviles que utilizan la app X-GPS Tracker. Esta regla permite a los empleados actualizar su estado actual, como indicar cuándo están disponibles para una nueva tarea o cuándo han iniciado una nueva actividad.

Cuando la regla "Estado de trabajo" está activa, cualquier cambio en el estado de un empleado desencadenará notificaciones inmediatas a través de SMS, correo electrónico o alertas emergentes en la Interfaz de usuario. Esta funcionalidad garantiza que los supervisores y expedidores permanezcan informados sobre las actividades actuales y la disponibilidad de su equipo, lo que permite una mejor coordinación y gestión de las tareas.

## Configuración de reglas

#### Situación laboral

Defina los estados de trabajo específicos que activarán las notificaciones cuando sean seleccionados por los empleados. Los usuarios pueden elegir qué estados supervisar, asegurándose de que el sistema sólo alerta sobre las actualizaciones de estado más relevantes. Estos estados se crean y asignan a través del widget "Estados de trabajo" del menú Dispositivos y configuración.

Para los ajustes habituales, consulte [Normas y notificaciones](../../reglas-y-alertas.md).

## Detalles del funcionamiento del sistema

- Esta regla está diseñada específicamente para su uso con dispositivos habilitados para X-GPS Tracker, lo que significa que sólo estos dispositivos pueden ser seleccionados como fuentes para supervisar los cambios de estado de trabajo.
- La lista de estados de trabajo que activan esta regla puede variar en función de las listas personalizadas asignadas a los distintos seguidores. Si modifica la lista de dispositivos vinculados a la regla y esto altera la lista de estados de trabajo asociados, la regla incluirá tanto los estados antiguos como los nuevos. Sin embargo, los nuevos estados añadidos de la lista actualizada no estarán seleccionados por defecto. Puede editar la regla para incluir estos nuevos estados.
- A diferencia de muchas otras reglas, la regla "Estado de trabajo" no tiene un temporizador de reinicio, lo que permite la notificación inmediata de cualquier cambio de estado.

Esta configuración ayuda a las organizaciones a mantener una comunicación clara y una gestión eficaz de las tareas, manteniendo al equipo informado del estado actual del trabajo de cada miembro.