# Desviación carretera

## Visión general

La regla de desviación de ruta permite supervisar las desviaciones de una ruta predefinida. Esta regla garantiza que los vehículos u objetos se adhieran a las rutas planificadas, mejorando la eficiencia y aumentando la seguridad al identificar y abordar rápidamente cualquier desviación. Los usuarios recibirán notificaciones cada vez que un vehículo u objeto se desvíe de la ruta especificada, lo que ayudará a mantener el cumplimiento y optimizar las operaciones.

## Configuración de reglas

#### Geocercas alrededor de los caminos

Para utilizar la regla de desvío de ruta, primero debe crear una o varias geocercas de corredor en la aplicación Seguimiento de la interfaz web. Siga estos pasos para configurar la regla:

1. **Crear geocercas de corredores**: Antes de configurar la regla, asegúrese de haber creado geocercas de corredor categorizadas como "ruta".
2. **Seleccionar geocercas**: Elija las geocercas de corredor que desea supervisar en busca de desviaciones. Solo se pueden utilizar para este fin las geocercas categorizadas como "ruta".

Para los ajustes habituales, consulte [Normas y notificaciones](../../reglas-y-alertas.md).

## Detalles del funcionamiento del sistema

- La alerta "Desviación de la ruta" tiene un temporizador de reinicio de 10 segundos, lo que significa que el evento de alerta no se producirá más de una vez cada 10 segundos. Si se produce un evento mientras la regla está esperando el reinicio, la plataforma omitirá el evento, incluso en los informes.
- Esta regla se procesa en la nube y no está vinculada a ningún hardware específico, lo que permite aplicarla a varios rastreadores simultáneamente. Esta flexibilidad le permite seleccionar varios rastreadores dentro de una única regla.