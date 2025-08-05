# Detección de caídas

## Visión general

La norma de "detección de caídas" tiene por objeto garantizar la seguridad y el bienestar de las personas detectando y notificando a los usuarios posibles caídas o accidentes.

Esta norma utiliza sensores y algoritmos avanzados para controlar los patrones de movimiento y la orientación de los dispositivos GPS personales. Si el sistema detecta un cambio repentino y significativo en la posición o la aceleración, lo identifica como una posible caída y activa una notificación.

Esta funcionalidad es especialmente valiosa para vigilar a personas mayores, trabajadores solitarios u otras personas que puedan ser vulnerables a las caídas. Al proporcionar alertas en tiempo real, el sistema permite una respuesta y asistencia inmediatas, mejorando la seguridad general y ofreciendo tranquilidad a cuidadores y seres queridos.

## Configuración de reglas

La funcionalidad de esta regla depende de las capacidades y la configuración del dispositivo, por lo que no es necesario configurar ninguna regla específica.

Para los ajustes habituales, consulte [Normas y notificaciones](../../reglas-y-alertas.md).

## Detalles del funcionamiento del sistema

- **Reinicia el temporizador:** La alerta "Detección de caídas" tiene un temporizador de restablecimiento de 30 segundos, lo que significa que la alerta no se activará con más frecuencia que una vez cada 30 segundos. Si se produce un evento mientras la regla está en el periodo de restablecimiento, la plataforma suprimirá la alerta, garantizando que las notificaciones y los informes sigan siendo claros y manejables.
- **Múltiples dispositivos:** Esta regla puede aplicarse a múltiples rastreadores GPS personales, siempre que admitan eventos de "Detección de caídas" y tengan esta función integrada en la plataforma. Esto permite a los usuarios supervisar los eventos de detección de caídas en varios dispositivos, lo que garantiza una cobertura completa.
- **Procesamiento de eventos independiente del GPS:** La plataforma procesa y muestra los eventos de detección de caídas incluso si el paquete de datos carece de coordenadas GPS válidas. Estos eventos se registran independientemente de si se producen dentro o fuera de una geovalla designada. En este caso, se omite la configuración de la geovalla Inside/Outside, lo que garantiza que no se pierda ningún evento crítico.