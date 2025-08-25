# Auto-geofencing

## Visión general

La función "Auto geofencing", disponible en determinados dispositivos de localización GPS, es una solución robusta diseñada para mejorar la seguridad de los vehículos evitando el remolque o robo no autorizados.

Esta función establece automáticamente una geocerca alrededor de la ubicación actual del vehículo cuando se apaga el contacto. Si el vehículo se mueve fuera de este límite predefinido sin que el encendido esté conectado, el sistema activa inmediatamente una alerta, proporcionando una capa adicional de protección. La utilización de la función de geovalla automática requiere un localizador GPS compatible con esta función.

## Configuración de reglas

Esta regla depende totalmente de las capacidades del dispositivo y de la configuración del hardware. No hay ajustes específicos que configurar dentro de la propia regla.

Para los ajustes habituales, consulte [Normas y notificaciones](../).

## Detalles del funcionamiento del sistema

* **Reiniciar temporizador**: La alerta "Geofencing automático" tiene un temporizador de restablecimiento de 1 minuto, lo que significa que no se activará más a menudo que una vez cada minuto. Si se produce un evento durante el periodo de restablecimiento, se omitirá de los informes.
* **Múltiples dispositivos**: Puede seleccionar varios rastreadores para esta regla, siempre que admitan eventos de Auto Geofencing y la función esté integrada en la plataforma. Esta flexibilidad le permite supervisar varios vehículos o activos simultáneamente.
* **Alerta de eventos independiente del GPS**: Si la plataforma recibe un evento de Auto Geofencing de un rastreador sin coordenadas GPS válidas, el evento seguirá contándose como válido y se mostrará. Esto garantiza que no se pierdan eventos críticos, independientemente de que se produzcan dentro o fuera de las geovallas definidas.
