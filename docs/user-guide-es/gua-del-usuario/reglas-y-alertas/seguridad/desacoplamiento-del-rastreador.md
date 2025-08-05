# Desacoplamiento del rastreador

## Visión general

La regla "El rastreador se desprende del objeto" alerta a los usuarios cuando un dispositivo de localización GPS se desprende del vehículo o activo que está vigilando. La disponibilidad de esta regla depende de las capacidades y la configuración del dispositivo. Dependiendo del diseño del dispositivo, puede utilizar varios sensores, como puntos de contacto o sensores de luz, para detectar el desprendimiento.

Esta norma es esencial para la seguridad de los activos y la prevención de pérdidas, ya que permite a las empresas responder rápidamente a posibles robos, manipulaciones o manipulaciones no autorizadas. Es especialmente valiosa en sectores como la logística y el transporte, donde es fundamental proteger los activos durante el tránsito o el almacenamiento.

## Configuración de reglas

Esta regla depende totalmente de las capacidades y la configuración del dispositivo. No hay ajustes específicos que configurar dentro de la propia regla.

Para los ajustes habituales, consulte [Normas y notificaciones](../../reglas-y-alertas.md).

## Detalles del funcionamiento del sistema

- **Reinicia el temporizador.** La alerta "El rastreador se desprende del objeto" tiene un temporizador de restablecimiento de 1 minuto, lo que significa que la alerta no se activará con más frecuencia que una vez cada minuto. Si se produce un evento durante el periodo de restablecimiento, se omitirá de la plataforma, incluso en los informes.
- **Múltiples dispositivos.** Los usuarios tienen la flexibilidad de seleccionar varios dispositivos GPS para recibir notificaciones cuando el dispositivo se separa de un objeto. El único requisito es que los rastreadores seleccionados sean compatibles con los eventos "El rastreador se separa del objeto" y tengan esta función integrada en la plataforma.

- **Alerta de eventos independiente del GPS.** Si la plataforma recibe un evento de desprendimiento de un rastreador sin datos GPS válidos, el evento se sigue contando como válido y se muestra, independientemente de si se produjo dentro o fuera de una geovalla. En tales casos, se ignoran los ajustes Dentro/Fuera de las geocercas para garantizar que no se pierdan eventos potencialmente críticos.