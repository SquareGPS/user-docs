# Interferencias GSM

## Visión general

La interferencia GSM se refiere a la interrupción de las señales GSM (señales móviles o celulares) debido a interferencias de fuentes cercanas. Esta interferencia, a menudo denominada enmascaramiento o enmascaramiento de frecuencias, puede impedir que los dispositivos móviles se conecten a las redes móviles, afectando a servicios como los datos móviles (2G, 3G, 4G, LTE), los mensajes de texto y las llamadas de voz. En el contexto del seguimiento por GPS, la interferencia GSM puede provocar la pérdida de la comunicación de datos en tiempo real, por lo que es crucial disponer de normas de detección.

Por ejemplo, una empresa de logística que utilice vehículos equipados con GPS para transportar cargas valiosas depende de las señales GSM para el seguimiento de su ubicación en tiempo real. Si se produce una interferencia GSM, estas señales se interrumpen, lo que puede poner en peligro la seguridad de los envíos. Aplicando reglas para detectar las interferencias GSM, la empresa puede recibir alertas inmediatas, lo que le permite actuar con rapidez para proteger sus activos.

## Configuración de reglas

Esta regla depende totalmente de las capacidades del dispositivo y de la configuración del hardware. No hay ajustes específicos que configurar dentro de la propia regla.

Para los ajustes habituales, consulte [Normas y notificaciones](../../).

## Detalles del funcionamiento del sistema

* **Reinicia el temporizador:** La alerta "Interferencias GSM" tiene un temporizador de restablecimiento de 5 minutos, lo que significa que la alerta no se activará con más frecuencia que una vez cada 5 minutos. Si se produce un evento durante el periodo de restablecimiento, la plataforma lo omitirá y no se incluirá en los informes.
* **Múltiples dispositivos:** Los usuarios pueden seleccionar varios rastreadores para supervisarlos con esta regla. El único requisito es que los rastreadores seleccionados admitan eventos de interferencia GSM y estén integrados en la plataforma. Esta flexibilidad permite a los usuarios supervisar este tipo de evento en varios vehículos o dispositivos cómodamente.
* **Alerta de eventos independiente del GPS:** La plataforma registrará y mostrará el suceso aunque se reciba en un mensaje sin coordenadas GPS válidas. Esto garantiza que los usuarios estén informados del evento, independientemente de los datos de ubicación. La configuración de los botones de opción Dentro/Fuera de las geocercas se ignora en estos casos, ya que la plataforma prioriza la visualización de eventos potencialmente críticos.

## Ver también

* [Bloqueo del GPS](../../posicionamiento-del-dispositivo/posicionamiento-del-dispositivo/bloqueo-del-gps.md)
