# Cambio de conductor

## Visión general

La regla "Cambio de conductor" ayuda a los gestores de flotas a controlar qué conductor está operando un vehículo, especialmente cuando varios conductores comparten el mismo vehículo. Esta función funciona con tecnologías de identificación de conductores como iButton, lectores RFID o llaves hardware BLE.

## Configuración de reglas

Para utilizar esta regla, empiece por añadir todos sus controladores al directorio **Gestión de flotas** → **Sección de conductores**. Asigne a cada conductor su llave hardware única, como un iButton o una etiqueta RFID. Cuando se detecta un cambio de conductor, la plataforma relaciona el evento con el conductor correcto, garantizando informes y alertas precisos.

No se requiere ninguna otra configuración específica de las reglas. Para los ajustes habituales, consulte [Normas y notificaciones](../../reglas-y-alertas.md).

## Detalles del funcionamiento del sistema

- **Detección de cambio de conductor:** La plataforma identifica un cambio de controlador comprobando si los últimos datos de la clave de hardware recibidos del rastreador difieren de los datos anteriores. Si la clave ha cambiado, lo registra como un evento de cambio de controlador. Esto difiere del [Identificación del conductor](identificacin-del-conductor.md) en la que la alerta es activada directamente por el hardware tras la autenticación correcta del conductor, y la plataforma simplemente muestra el evento.
- **Anulaciones manuales:** Los cambios manuales de controlador realizados a través de la interfaz de usuario (es decir, en los widgets) no activan un evento de cambio de controlador. Estos cambios tampoco se incluyen en el "Informe sobre todos los eventos". Sin embargo, todos los cambios manuales y automáticos de conductor pueden revisarse en detalle a través del informe "Cambio de turno de conductor".
- **Temporizador de reinicio de alerta:** La alerta "Cambio de conductor" tiene un temporizador de reinicio de 10 segundos, lo que impide que se active más de una vez cada 10 segundos. Si se produce un evento de cambio de conductor durante este periodo, la plataforma suprimirá la alerta, manteniendo las notificaciones y los informes precisos y concisos.
- **Compatibilidad con varios dispositivos:** Esta regla puede aplicarse a varios rastreadores, lo que permite a los gestores de flotas supervisar los cambios de conductor en varios vehículos. Los rastreadores deben ser compatibles con el evento Cambio de conductor y tener esta función integrada en la plataforma.
- **Procesamiento de eventos independiente del GPS:** La plataforma procesa los eventos de cambio de conductor aunque falten datos GPS o no sean válidos. Estos eventos se registrarán y mostrarán, independientemente de si se han producido dentro o fuera de una geo-valla. Esto garantiza que todos los eventos críticos de cambio de conductor se capturen y se notifiquen con precisión.

## Ver también

- [**Norma de identificación del conductor**](identificacin-del-conductor.md) - la norma utilizada para verificar y autorizar al conductor antes o durante la operación del vehículo, proporcionando alertas inmediatas y garantizando que sólo los conductores autorizados puedan operar el vehículo.