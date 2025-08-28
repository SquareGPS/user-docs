# Antena GPS desconectada

## Visión general

La norma "antena GPS desconectada" está pensada para los dispositivos GPS que utilizan una antena externa, normalmente conectada mediante un cable y un enchufe. Cuando la antena se desconecta (o se corta), puede interrumpir la recepción de la señal del satélite, lo que puede provocar problemas de seguimiento. Esta regla le avisa inmediatamente cuando se produce una desconexión de este tipo, lo que le permite solucionar rápidamente el problema y mantener un seguimiento continuo de sus activos.

Por ejemplo, si gestiona una flota de vehículos de reparto equipados con rastreadores y antenas GPS externas, esta regla le ayuda a controlar la integridad de las conexiones GPS. Si una antena se desconecta debido a factores ambientales o a una manipulación, se le notificará inmediatamente. Esto le permite tomar medidas correctivas, como enviar a un técnico para restablecer la conexión, evitando posibles retrasos y manteniendo la eficacia de las operaciones.

> \[!INFO] La mayoría de los dispositivos GPS modernos vienen equipados con antenas integradas de alta sensibilidad, lo que hace obsoletas las antenas externas.

## Configuración de reglas

Esta regla depende totalmente de las capacidades del dispositivo y de la configuración del hardware. No hay ajustes específicos que configurar dentro de la propia regla.

Para los ajustes habituales, consulte [Normas y notificaciones](../../).

## Detalles del funcionamiento del sistema

* **Reinicia el temporizador:** La alerta "Antena GPS desconectada" tiene un temporizador de restablecimiento de 5 minutos, lo que significa que la alerta no se activará con más frecuencia que una vez cada 5 minutos. Si se produce un evento durante el periodo de restablecimiento, la plataforma lo omitirá y no se incluirá en los informes.
* **Múltiples dispositivos:** Puede supervisar varios rastreadores con esta regla, siempre que los rastreadores seleccionados admitan eventos de antena GPS desconectada y la función esté integrada en la plataforma. Esto permite una supervisión exhaustiva en varios vehículos o dispositivos.
* **Gestión de eventos sin coordenadas:** La plataforma registrará y mostrará el evento aunque se reciba en un paquete sin coordenadas GPS válidas. Esto garantiza que se le informe del evento de desconexión, independientemente de los datos de ubicación. La configuración de los botones de opción Dentro/Fuera de las geocercas se ignora en estos casos, dando prioridad a la visualización de eventos potencialmente críticos.
