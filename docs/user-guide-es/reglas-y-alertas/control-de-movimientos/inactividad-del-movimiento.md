# Inactividad del movimiento

## Visión general

La alerta de "inactividad por movimiento", también conocida como alerta de "ausencia de movimiento", está diseñada para mejorar la seguridad. Activa una alerta cuando no se detecta movimiento durante un periodo prolongado, basándose en dispositivos GPS equipados con acelerómetros y las capacidades de firmware necesarias.

Esta norma es especialmente útil en tres ámbitos clave:

1. **Bienes muebles**: Aplicada a equipos como la maquinaria de construcción y los remolques, la alerta de "inactividad por movimiento" ayuda a controlar las paradas no autorizadas o el ralentí prolongado, garantizando que los activos se utilizan según lo previsto y evitando posibles robos o usos indebidos.
2. **Control de la carga**: En el caso de la carga en tránsito, esta alerta puede ser crucial para detectar cuándo las mercancías se han dejado desatendidas o corren peligro, lo que permite intervenir a tiempo para proteger envíos valiosos.
3. **Seguridad personal**: Para las personas que utilizan rastreadores GPS personales, como ancianos o trabajadores solitarios, la alerta de "inactividad por movimiento" proporciona una capa adicional de protección al señalar una posible emergencia cuando el dispositivo detecta una falta de movimiento inusual, lo que provoca una respuesta para garantizar el bienestar de la persona.

## Configuración de reglas

Dado que la "Inactividad de movimiento" es un evento detectado por el dispositivo, no hay ningún ajuste específico en las Reglas y Notificaciones. En su lugar, utilice el widget Configuración del dispositivo para configurar remotamente el límite de velocidad en el dispositivo.

Para los ajustes habituales, consulte [Normas y notificaciones](https://squaregps.atlassian.net/wiki/spaces/USERDOCS/pages/2761228324/Rules+and+Notifications#Manage-rules).

## Detalles del funcionamiento del sistema

- **Reinicia el temporizador.** La alerta "Inactividad del movimiento" tiene un temporizador de restablecimiento de 1 minuto, lo que significa que la alerta no se activará con más frecuencia que una vez cada minuto. Si se produce un evento mientras la regla está esperando el reinicio, la plataforma omitirá el evento, incluso en los informes.
- **Alerta de eventos independiente del GPS.** El sistema puede generar una alerta de "Inactividad de movimiento" aunque no se disponga de datos GPS. Si se detectan coordenadas GPS no válidas, la plataforma seguirá registrando y mostrando el evento, independientemente de si se ha producido dentro o fuera de las geovallas designadas. En estos casos se ignora la lógica de la configuración de la geovalla Dentro/Fuera para garantizar que no se pierdan eventos críticos.