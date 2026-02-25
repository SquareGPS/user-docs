# Conducción distraída

## Visión general

La función de conducción distraída es un componente de los sistemas telemáticos avanzados, diseñado para detectar y alertar a los usuarios cuando los conductores realizan actividades que les distraen, como fumar o utilizar el teléfono móvil.

Esta función, que depende del dispositivo, se basa en la configuración del hardware, normalmente cámaras de salpicadero o dispositivos GPS con cámaras, para identificar y notificar las distracciones. La plataforma procesa estos eventos en tiempo real y envía notificaciones, lo que permite una rápida acción correctiva para mejorar la seguridad vial y promover un comportamiento responsable al volante.

Esta regla depende del dispositivo, lo que significa que depende de la configuración del hardware (normalmente cámaras de salpicadero o dispositivos GPS con funciones de cámara) para detectar y notificar eventos de distracción. La plataforma procesa estos eventos y envía notificaciones al usuario en consecuencia.

## Configuración de reglas

Dado que esta regla se basa en la configuración del hardware, se requiere una configuración mínima dentro de la propia plataforma. La clave es asegurarse de que los dispositivos seleccionados están configurados para detectar y notificar eventos de distracción del conductor.

Para los ajustes habituales, consulte [Reglas y alertas](../../../guia-del-usuario/reglas-y-alertas/).

## Detalles del funcionamiento del sistema

* **Reinicia el temporizador:** La alerta "Conducción distraída" se gestiona mediante un temporizador de restablecimiento de 10 segundos, lo que garantiza que no se generen alertas con una frecuencia superior a una vez cada 10 segundos. Si se produce un evento de distracción durante el periodo de restablecimiento, se omitirá de la plataforma y de los informes.
* **Múltiples dispositivos:** Los usuarios pueden configurar esta regla en varios rastreadores, siempre que admitan eventos de "Conducción distraída" y tengan esta función integrada en la plataforma. Esto permite un seguimiento exhaustivo en varios vehículos o dispositivos, garantizando una supervisión coherente del comportamiento del conductor.
* **Alerta de eventos independiente del GPS:** La plataforma registrará y mostrará eventos de "Conducción distraída" incluso si el paquete de datos carece de coordenadas GPS válidas. En estos casos, no se tiene en cuenta la configuración de la geocerca Inside/Outside, ya que el sistema prioriza la visualización de eventos potencialmente críticos para garantizar que no se pierda ninguna información importante.
