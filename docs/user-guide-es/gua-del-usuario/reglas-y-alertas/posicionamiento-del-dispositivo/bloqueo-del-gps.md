# Bloqueo del GPS

## Visión general

La interferencia GPS se produce cuando las frecuencias GPS o GNSS se ven alteradas por interferencias de fuentes cercanas, un proceso conocido como enmascaramiento o máscara de frecuencia. Estas interferencias pueden hacer que el dispositivo pierda la conexión con los satélites, lo que provoca distorsiones o la pérdida total de los datos GPS. La interferencia del GPS difiere de [Interferencias GSM](../conexin-de-dispositivos/interferencias-gsm.md)ya que operan en bandas de frecuencia distintas. Cuando se produce una interferencia del GPS, el dispositivo puede perder la conexión con el satélite, lo que provoca que no haya ningún satélite visible o que las coordenadas no sean válidas y la plataforma de seguimiento no pueda recuperarlas.

La regla de interferencia de GPS mejora la seguridad de vehículos y activos al evitar robos en situaciones en las que la interferencia de la señal GPS se utiliza para desactivar los sistemas de seguimiento. Por ejemplo, si un vehículo es objeto de robo o secuestro, esta regla proporciona una alerta oportuna, lo que permite una acción rápida para evitar pérdidas o daños. Es una herramienta esencial para que las empresas protejan sus flotas y sus valiosos activos.

## Configuración de reglas

Esta regla depende totalmente de las capacidades del dispositivo y de la configuración del hardware. No hay ajustes específicos que configurar dentro de la propia regla.

Para los ajustes habituales, consulte [Normas y notificaciones](../../reglas-y-alertas.md).

## Detalles del funcionamiento del sistema

- **Reinicia el temporizador:** La alerta de "interferencia de GPS" tiene un temporizador de restablecimiento de 5 minutos, lo que significa que la alerta no se activará más de una vez cada 5 minutos. Si se produce un evento durante el periodo de restablecimiento, se omitirá de la plataforma, incluidos los informes.
- **Múltiples dispositivos:** Esta regla permite seleccionar varios rastreadores de los que recibir notificaciones, siempre que los rastreadores seleccionados admitan eventos de interferencia de GPS y la función esté integrada en la plataforma. Esta flexibilidad permite supervisar los eventos de interferencia de GPS en varios vehículos o dispositivos.
- **Alerta de eventos independiente del GPS:** La plataforma registrará y mostrará el evento aunque se reciba en un paquete sin coordenadas válidas. El evento se mostrará independientemente de si se ha producido dentro o fuera de las geovallas delimitadas, ya que la plataforma da prioridad a mostrar eventos potencialmente críticos frente a omitirlos.

## Ver también

- [Interferencias GSM](../conexin-de-dispositivos/interferencias-gsm.md)