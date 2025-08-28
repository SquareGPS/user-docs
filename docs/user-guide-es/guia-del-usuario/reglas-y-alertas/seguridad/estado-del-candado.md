# Estado del candado

## Visión general

La regla "Supervisión del estado de candados GPS" es esencial para las organizaciones que utilizan cerraduras inteligentes con GPS para proteger activos valiosos y áreas críticas. Esta regla supervisa el estado de estas cerraduras, garantizando que los usuarios reciban una notificación instantánea siempre que una cerradura esté activada o desactivada.

Específicamente diseñada para las esclusas GPS, esta regla proporciona alertas en tiempo real para todas las interacciones de la esclusa, ya sea asegurando una zona o bloqueando la carga en un contenedor.

## Configuración de reglas

Esta regla depende totalmente de las capacidades del dispositivo y de la configuración del hardware. No hay ajustes específicos que configurar dentro de la propia regla.

Para los ajustes habituales, consulte [Normas y notificaciones](../).

## Detalles del funcionamiento del sistema

* **Reinicia el temporizador:** La alerta "Supervisión del estado del candado GPS" tiene un temporizador de restablecimiento de 1 minuto, lo que significa que no se activará con más frecuencia que una vez cada minuto. Los eventos que se produzcan durante este periodo de reinicio se omitirán de las notificaciones e informes.
* **Múltiples rastreadores:** Esta regla admite múltiples rastreadores, siempre que puedan detectar eventos de Bloqueo/Desbloqueo (Candado) y tengan la función integrada en la plataforma. Los usuarios pueden supervisar estos eventos en varios dispositivos de forma eficaz.
* **Procesamiento independiente del GPS:** La plataforma procesa y muestra los eventos de Bloqueo/Desbloqueo incluso si el paquete de datos carece de coordenadas GPS válidas. Estos eventos se registran independientemente de si se producen dentro o fuera de una geovalla, lo que garantiza que no se pierda ningún evento crítico.
