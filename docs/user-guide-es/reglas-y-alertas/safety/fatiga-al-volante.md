# Fatiga al volante

## Visión general

La regla de conducción fatigosa es una función esencial de la plataforma telemática, diseñada para mejorar la seguridad vial detectando y alertando a los equipos de expedición cuando se detectan signos de fatiga en el conductor. Utilizando cámaras de seguimiento avanzadas, el sistema vigila continuamente a los conductores en busca de indicadores de somnolencia o fatiga, que son factores clave que contribuyen a los accidentes de tráfico.

Cuando se detecta cansancio, se envía una alerta inmediata a la central, lo que permite una intervención rápida, como organizar pausas de descanso o proporcionar el apoyo necesario. La aplicación de esta norma no sólo ayuda a prevenir accidentes y reducir las pérdidas operativas, sino que también da prioridad al bienestar del conductor y promueve prácticas de conducción seguras.

## Configuración de reglas

Dado que esta norma depende del hardware, la configuración es mínima dentro de la propia plataforma. El principal requisito es garantizar que los rastreadores seleccionados estén equipados para admitir y detectar eventos de conducción por fatiga.

Para los ajustes habituales, consulte [Normas y notificaciones](../).

## Detalles del funcionamiento del sistema

* **Reinicia el temporizador:** La alerta "Conducción fatigada" se rige por un temporizador de reinicio de 5 segundos, lo que garantiza que las alertas no se activen con más frecuencia que una vez cada 5 segundos. Si se detecta un evento de fatiga durante este periodo de restablecimiento, se omitirá de la plataforma y de los informes.
* **Múltiples dispositivos:** Esta regla permite seleccionar varios dispositivos para su supervisión. Los dispositivos seleccionados deben ser compatibles con los eventos de conducción fatigosa y tener esta función integrada en la plataforma. Esto permite una supervisión exhaustiva en varios vehículos o dispositivos, lo que garantiza un seguimiento y una gestión coherentes de la fatiga del conductor.
* **Alerta de eventos independiente del GPS:** La plataforma registrará y mostrará los eventos de Conducción Fatigada incluso si el paquete de datos carece de coordenadas GPS válidas. En tales casos, no se tienen en cuenta los ajustes de geovalla interior/exterior, ya que el sistema prioriza la visualización de los eventos críticos, garantizando que no se pase por alto ninguna información crucial.
