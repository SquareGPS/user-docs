# Alarma de coche

## Visión general

La regla "Alarma de coche activada" está diseñada para mejorar la seguridad de su flota proporcionando notificaciones en tiempo real cuando se activa el sistema de alarma de un vehículo. Esta regla ayuda a salvaguardar sus activos alertando rápidamente a su equipo de posibles incidentes de robo, acceso no autorizado o manipulación.

Esta regla funciona controlando el sistema de alarma del vehículo a través de un dispositivo de localización GPS conectado. Normalmente, la señal de salida del sistema de alarma se conecta a la entrada del dispositivo GPS. Cuando se dispara la alarma, el dispositivo GPS detecta esta señal y envía una alerta a la plataforma.

## Configuración de reglas

No es necesario configurar reglas específicas. Para los ajustes habituales, consulte [Reglas y alertas](../).

## Detalles del funcionamiento del sistema

* **Reiniciar temporizador:** La alerta "Alarma de coche activada" tiene un temporizador de restablecimiento de 5 minutos, lo que significa que la alerta no se activará más de una vez cada 5 minutos. Si se produce un evento durante el periodo de restablecimiento, la plataforma suprimirá la alerta, manteniendo las notificaciones y los informes claros y concisos.
* **Múltiples dispositivos:** Esta regla puede aplicarse a varios rastreadores, siempre que admitan eventos de "activación de alarma de coche" y tengan esta función integrada en la plataforma. Esto le permite supervisar estas alertas a través de varios vehículos o dispositivos de manera eficiente.
* **Alerta de evento independiente del GPS:** La plataforma procesa y muestra los eventos de alarma del coche aunque el paquete de datos carezca de coordenadas GPS válidas. Estos eventos se registran independientemente de si se producen dentro o fuera de una geocerca designada. En este caso, la configuración de la geocerca **Dentro/Fuera** se omite, lo que garantiza que no se pierda ningún evento crítico.
