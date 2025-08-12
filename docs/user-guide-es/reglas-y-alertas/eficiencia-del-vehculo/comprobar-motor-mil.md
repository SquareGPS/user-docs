# Comprobar motor (MIL)

## Visión general

La regla "Check engine (MIL)" está diseñada para monitorizar el estado de la luz indicadora de mal funcionamiento (MIL), comúnmente conocida como luz "Check Engine", en los vehículos. Esta regla es crucial para el mantenimiento de vehículos y la gestión de flotas, ya que alerta rápidamente a los usuarios cuando se activa la MIL.

La MIL se enciende normalmente cuando el sistema de diagnóstico a bordo del vehículo detecta un problema con el motor, las emisiones u otros sistemas críticos. Al recibir notificaciones a tiempo, los usuarios pueden tomar medidas inmediatas para solucionar posibles problemas, evitando daños mayores y garantizando la seguridad y el cumplimiento de las normas del vehículo.

> \[!INFO] Para supervisar códigos DTC específicos, puede configurar un [Valor del campo Estado](../entradas-y-salidas/valor-del-campo-estado.md) regla.

## Configuración de reglas

Esta regla depende totalmente de las capacidades y la configuración del dispositivo. No hay ajustes específicos que configurar dentro de la propia regla.

Para los ajustes habituales, consulte [Normas y notificaciones](../).

## Detalles del funcionamiento del sistema

* **Reinicia el temporizador.** La alerta "Comprobar motor (MIL)" tiene un temporizador de reinicio de 24 horas, lo que significa que no se activará con más frecuencia que una vez cada 24 horas. Si el evento se produce durante el periodo de restablecimiento, se omitirá de la plataforma y de los informes.
* **Múltiples dispositivos.** Esta regla puede aplicarse a varios dispositivos GPS, siempre que admitan el evento Check Engine (MIL) y tengan la función integrada en la plataforma.
* **Alerta de eventos independiente del GPS.** La plataforma registrará el suceso y activará las notificaciones independientemente de si el vehículo se encuentra dentro o fuera de una geovalla, incluso si el paquete de datos carece de coordenadas GPS válidas. La plataforma prioriza la captura y visualización de estos eventos críticos para garantizar que no se pierdan.
