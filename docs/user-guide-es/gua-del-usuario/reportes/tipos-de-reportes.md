# Tipos de reportes

Navixy proporciona un conjunto completo de reportes que le permiten supervisar diversos aspectos de las operaciones de su flota. Estos reportes están organizados en categorías, lo que facilita la búsqueda y generación de los datos que necesita. A continuación encontrará un resumen de las categorías de reportes disponibles y los reportes específicos que contienen.

## Reportes de actividad

Los reportes de actividad proporcionan información detallada sobre los movimientos y paradas de sus vehículos, lo que le permite controlar los historiales de viaje e identificar patrones en el uso de los vehículos.

- **Viajes**  
Este reporte ofrece un historial detallado de los viajes, incluida la duración, el tiempo de viaje, la duración de las paradas y la velocidad. También ofrece una visión general del consumo de combustible de los vehículos sin sensores de combustible.
- **Detiene**  
El reporte de paradas desglosa los detalles de las paradas y los estacionamientos, incluida la ubicación, la duración y el tiempo al ralentí (tiempo que el vehículo pasa con el motor encendido).
- **Viajes y paradas por turnos**  
Un reporte combinado que le permite ver los datos de viajes y paradas segmentados por turnos, ayudándole a analizar el uso de los vehículos durante intervalos de tiempo específicos.

## Reportes sobre monumentos

Los reportes de puntos de referencia le ayudan a realizar un seguimiento de las visitas a zonas geográficas predefinidas, como geocercas y puntos de interés (POI).

- **Visitas en geocercas**  
Registra el número de visitas a zonas geocercadas durante un periodo determinado, proporcionando detalles sobre entradas, salidas y duración de las estancias.
- **Visitas a PDI**  
De forma similar al reporte de geocercas, realiza un seguimiento de las visitas a puntos de interés, detallando la fecha y hora de cada visita.

## Reportes de seguridad

Estos reportes se centran en los eventos y alertas relacionados con la seguridad que genera el sistema, ayudándole a garantizar la seguridad de sus vehículos y conductores.

- **Seguridad del coche**  
Proporciona detalles sobre alarmas de coches, evacuaciones, choques y otros sucesos relacionados con la seguridad.
- **Botón de emergencia (SOS)**  
Captura los eventos activados por el botón SOS en dispositivos GPS equipados con botón de pánico.
- **Detección de caídas**  
Realiza un seguimiento de los eventos de caída detectados por dispositivos con sensores de caída, utilizados habitualmente en los rastreadores personales.
- **Desacoplamiento del rastreador**  
Informa de los casos en los que se ha retirado un dispositivo de seguimiento de su objeto asignado, a menudo utilizado para el seguimiento de cargas.
- **Reporte general de seguridad**  
Un reporte exhaustivo que agrega todos los incidentes de seguridad y protección.

## Reportes de uso de vehículos

Los reportes de uso del transporte le permiten controlar cómo se utilizan sus vehículos y sus recursos, incluido el consumo de combustible y el uso del motor.

- **Horas de motor**  
Muestra información detallada sobre las horas del motor, tanto en movimiento como en ralentí, junto con diagramas de actividad e histogramas. Más información:
  - [Reporte de horas de motor](detalles-especficos-del-reporte/reporte-de-horas-de-motor.md)
- **Volumen de combustible**  
Proporciona datos sobre consumo de combustible, llenados y vaciados, junto con los volúmenes de combustible inicial y final. Más información:
  - [Reporte de consumo de combustible](detalles-especficos-del-reporte/reporte-de-consumo-de-combustible.md)
- **Caudalímetro**  
Se centra en los datos de consumo de combustible recogidos de los caudalímetros, sin mostrar los niveles de combustible en momentos concretos.
- **Sensores de vehículos**  
Muestra los datos recibidos de los sensores del vehículo a través de CAN-bus u OBDII, incluyendo el kilometraje, RPM, velocidad y temperatura del refrigerante. Más información:
  - [Reporte de lecturas CAN / OBDII del vehículo](detalles-especficos-del-reporte/reporte-de-lecturas-can-obdii-del-vehculo.md)

## Impulsar los reportes de calidad

Estos reportes son esenciales para controlar el comportamiento de los conductores, sobre todo en relación con el exceso de velocidad y otras acciones potencialmente peligrosas.

- **Infracción de velocidad**  
Detalla los casos en los que el vehículo superó el límite de velocidad, incluida la fecha, el lugar y la velocidad real. Véase también:
  - [Conducción brusca en normas y notificaciones](../reglas-y-alertas/safety/conduccin-dura.md)
  - [Conducción ecológica en la gestión de flotas](../gestin-de-flotas/conduccin-ecolgica-eco-driving.md)

### Reportes de estado de los dispositivos

Los reportes de estado de los dispositivos proporcionan información sobre el estado operativo de sus dispositivos de seguimiento, lo que le ayuda a garantizar una supervisión ininterrumpida.

- **Conexión/desconexión del dispositivo**  
Registra los casos en los que el dispositivo GPS se encendió o apagó manualmente. Véase también:
  - [Dispositivo activado/desactivado en Reglas y notificaciones](https://squaregps.atlassian.net/wiki/pages/createpage.action?spaceKey=USERDOCSOLD&title=Device%20switched%20ON%20%2F%20OFF)
- **Conexión GSM perdida**  
Informa de los periodos en los que el dispositivo GPS perdió su conexión GSM, lo que indica una falta de comunicación con el servidor de monitorización. Véase también:
  - [Dispositivo perdido conexión en Reglas y notificaciones](../reglas-y-alertas/conexin-de-dispositivos/el-dispositivo-ha-perdido-la-conexin.md)

## reportes sobre dispositivos conectados

Estos reportes se centran en los sensores y equipos conectados a sus dispositivos de seguimiento, proporcionando datos operativos detallados.

- **Sensores de medición**  
Proporciona un historial detallado de las lecturas de los sensores, como la temperatura, los niveles de combustible y el voltaje.
- **Tiempo de funcionamiento del equipo**  
Registra la actividad y el tiempo de inactividad de los equipos conectados al dispositivo de seguimiento mediante entradas digitales. Más información:
  - [Reporte de horas de trabajo del equipo](detalles-especficos-del-reporte/reporte-sobre-el-tiempo-de-trabajo-de-los-equipos.md)

## reportes comerciales

Los reportes empresariales están diseñados para ayudarle a supervisar las tareas operativas y el rendimiento de su personal de campo.

- **Reporte de tareas**  
Resume el estado de las tareas asignadas a los empleados, ayudándole a seguir su progreso y finalización.
- **Valores del formulario de tareas**  
Muestra los datos de los formularios enviados por los empleados al completar tareas a través de la aplicación X-GPS Tracker.
- **reporte sobre la situación laboral**  
Registra los cambios en los estados de trabajo, ya sean realizados por empleados u operadores.
- **Registros**  
Enumera todos los registros realizados por los empleados en el mapa mediante la aplicación X-GPS Tracker.
- **Cambio de conductor**  
Realiza un seguimiento de los turnos del conductor, ayudándole a controlar qué conductor conducía un vehículo en un momento dado.
- **Viajes por ubicación geográfica**  
Un reporte de viaje especializado que agrupa los datos por región o país.

## Otros reportes

Estos reportes cubren una variedad de eventos y actividades adicionales, ofreciendo una amplia visión de las operaciones de su flota.

- **Todos los eventos**  
Un reporte completo que agrega todos los tipos de eventos integrados por la plataforma, agrupados por categoría de evento.
- **Entrada/salida de geocercas**  
Rastrea los eventos de entrada y salida de las zonas geocercadas, proporcionando datos detallados sobre los movimientos dentro y fuera de estas regiones.
- **Reporte de localizaciones por SMS**  
Lista las solicitudes de localización enviadas por SMS cuando el dispositivo GPS carece de conexión a Internet.
- **Reporte de puntos**  
Muestra el movimiento del dispositivo a lo largo del tiempo por puntos, incluyendo coordenadas y enlaces a mapas.