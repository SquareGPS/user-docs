# Detección de manipulaciones

## Visión general

La regla "Detección de manipulaciones" está diseñada para dispositivos GPS que admiten una alerta cuando se manipula o abre la carcasa del dispositivo, lo que garantiza que se le notifique inmediatamente cualquier acceso no autorizado a sus dispositivos.

Esta regla es vital para mejorar la seguridad y la protección de cargas valiosas durante su tránsito o almacenamiento. Si utiliza rastreadores equipados con la regla de "detección de manipulaciones", podrá añadir una capa adicional de seguridad para salvaguardar sus activos.

## Configuración de reglas

Esta regla depende totalmente de las capacidades del dispositivo y de la configuración del hardware. No hay ajustes específicos que configurar dentro de la propia regla.

Para los ajustes habituales, consulte [Reglas y alertas](../).

## Detalles del funcionamiento del sistema

* **Temporizador de descanso.** La alerta "Detección de manipulaciones" tiene un temporizador de restablecimiento de 1 minuto, lo que significa que la alerta no se activará más de una vez cada minuto. Si se produce un evento durante el periodo de restablecimiento, se omitirá de la plataforma, incluso en los informes.
* **Múltiples dispositivos.** Puede seleccionar varios rastreadores GPS que activarán notificaciones cuando se produzca un evento de manipulación. El único requisito es que los rastreadores seleccionados admitan eventos de detección de manipulación y tengan esta función integrada en la plataforma.
* **Alerta de eventos independiente del GPS.** Esta regla funciona independientemente de las coordenadas GPS. Si la plataforma recibe un evento de manipulación de un rastreador sin datos GPS válidos, el evento se sigue contando como válido y se muestra, independientemente de si ocurrió dentro o fuera de una geocerca. En tales casos, se ignoran los ajustes de los botones de opción **Dentro/Fuera** de las geocercas para garantizar que no se pierdan eventos potencialmente críticos.
