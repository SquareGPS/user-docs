# Sensor de vibraciones

## Visión general

Un sensor de vibración, también conocido como sensor de sacudidas, se basa en el acelerómetro integrado de un dispositivo para detectar vibraciones o movimientos continuos, normalmente cuando un vehículo está aparcado. Esta regla está diseñada para activar alertas o notificaciones cuando se detectan vibraciones inusuales o continuas, señalando posibles actividades no autorizadas o perturbaciones. La sensibilidad del sensor puede ajustarse según las necesidades del usuario, en función de la configuración del dispositivo.

Esta norma es especialmente útil en diversas aplicaciones, como las empresas de construcción que protegen sus vehículos estacionados. Las vibraciones continuas podrían indicar un acceso no autorizado o un intento de robo. Las alertas generadas por esta regla permiten a las empresas responder con prontitud, lo que reduce el riesgo de robo de vehículos, minimiza los posibles daños y limita las pérdidas.

Es importante señalar que la eficacia de esta regla depende del hardware y de la configuración del rastreador GPS. Todos los escenarios relacionados con la detección de vibraciones deben configurarse en el entorno del rastreador. Por ejemplo, algunos rastreadores ofrecen opciones de configuración, como el estado de encendido o el tiempo de espera de movimiento.

## Configuración de reglas

Esta regla depende totalmente de las capacidades del dispositivo y de la configuración del hardware. No hay ajustes específicos que configurar dentro de la propia regla.

Para los ajustes habituales, consulte [Normas y notificaciones](../../reglas-y-alertas.md).

## Detalles del funcionamiento del sistema

- **Reinicia el temporizador:** La alerta "Sensor de vibración" tiene un temporizador de restablecimiento de 1 minuto, lo que significa que la alerta no se activará más de una vez cada minuto. Si se produce un evento mientras la regla está esperando el reinicio, la plataforma omitirá el evento, incluso en los informes.
- **Múltiples dispositivos:** Los usuarios pueden seleccionar varios rastreadores para recibir notificaciones de esta regla, siempre que los rastreadores admitan eventos del sensor de vibración y la función esté integrada en la plataforma.
- **Alerta de eventos independiente del GPS:** Si la plataforma recibe un evento de vibración de un rastreador sin coordenadas GPS válidas, el evento se sigue contando como válido y se muestra, independientemente de si se ha producido dentro o fuera de una geovalla. La lógica de los botones de opción Dentro/Fuera se ignora en este caso, ya que es mejor mostrar un evento potencialmente crítico que omitirlo.