# Activación de la salida

## Visión general

Los dispositivos GPS para vehículos suelen venir equipados con salidas configurables que permiten a los usuarios controlar diversas funciones del vehículo, como la inmovilización del motor o la activación de alarmas, entre otras. Estas salidas pueden gestionarse directamente desde el salpicadero de su plataforma telemática. Al configurar una regla para los cambios de estado de las salidas, puede recibir notificaciones a través de la interfaz de usuario, la aplicación móvil, SMS o correo electrónico cada vez que se produzca una modificación en el estado de la salida.

Esta función garantiza que permanezcas informado sobre cualquier cambio en los equipos conectados a tu dispositivo GPS. Tanto si estás activando como desactivando funciones específicas, esta regla proporciona una forma fiable de supervisar y gestionar el estado de las salidas de tu vehículo.

Por ejemplo, en la gestión de flotas, esta regla es especialmente útil para controlar el estado de un bloque motor o de un sistema de corte de combustible. Si se configura un dispositivo GPS para controlar estas salidas, la regla puede generar alertas cada vez que se active o desactive el bloqueo del motor. Esto permite a los gestores de flotas asegurarse de que las medidas de seguridad se aplican correctamente y de que se impide el uso no autorizado del vehículo.

## Configuración de reglas

#### Salida

Especifique la salida de hardware que desea supervisar seleccionando el número de salida adecuado. Consulte la documentación del fabricante del rastreador para determinar qué salida controla cada funcionalidad.

## Detalles del funcionamiento del sistema

- **Alerta de evento independiente del GPS:** Si la plataforma detecta un evento de cambio de salida (como un cambio de 1 a 0 o viceversa) de un paquete de datos de rastreador sin coordenadas válidas, seguirá contando el evento como válido y lo mostrará. Esto se aplica independientemente de si el evento se produjo dentro o fuera de una geovalla, ya que la lógica de geovalla Dentro/Fuera se ignora para garantizar que no se pasen por alto eventos potencialmente importantes.
- **Alertas selectivas:** Si desea recibir alertas sólo para cambios de salida específicos, como de "APAGADO a ENCENDIDO" y no de "ENCENDIDO a APAGADO", puede conseguirlo borrando el texto de notificación para el estado de salida no deseado en los ajustes.
- **Reinicia el temporizador:** La alerta "Salidas activadas" tiene un temporizador de restablecimiento de 10 segundos, lo que significa que no se activará con más frecuencia que una vez cada 10 segundos. Si se produce otro evento durante el periodo de restablecimiento, se omitirá de la plataforma, incluso en los informes.
- **Múltiples dispositivos:** Puede asignar varios seguidores a esta regla, utilizando cada uno de ellos el mismo número de salida especificado en la configuración de la regla. Por ejemplo, si selecciona la salida nº 2, la regla le notificará siempre que cualquiera de los seguidores seleccionados informe de un cambio en su salida nº 2.