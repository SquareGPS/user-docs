# Reporte de viajes

El **Reporte de viajes** de Navixy proporciona un análisis exhaustivo del historial de viajes de su vehículo, ofreciendo información sobre la distancia recorrida, el tiempo de viaje, la duración de las paradas, las velocidades y el consumo de combustible.

Este reporte tiene un valor incalculable para los gestores de flotas que necesitan controlar el uso de los vehículos, calcular los costes operativos y evaluar la eficacia de la conducción. A continuación encontrará una guía detallada sobre el funcionamiento del reporte de trayectos, los parámetros que intervienen y cómo interpretar los datos de forma eficaz.

![image-20240815-010251.png](../../gua-del-usuario/reportes/detalles-especficos-del-reporte/attachments/image-20240815-010251.png)

## Visión general

El reporte Viajes detalla cada viaje realizado por sus vehículos, incluyendo las horas de inicio y fin, distancias, velocidades y consumo de combustible. El reporte también ofrece un resumen de todos los viajes durante el periodo seleccionado, lo que permite una fácil visión general del rendimiento del vehículo.

## Utilidad del reporte

El reporte de Viajes proporciona información valiosa que puede utilizarse de varias maneras:

* **Análisis operativo:** Al revisar los patrones de uso del vehículo, puede evaluar las frecuencias, distancias y duraciones de los viajes. Estos datos son esenciales para calcular la depreciación y predecir el uso futuro del vehículo.
* **Gestión de costos:** El reporte ayuda a identificar viajes inesperados o no autorizados que podrían suponer un aumento de los gastos. También proporciona información detallada sobre el consumo de combustible, lo que permite evaluar los costes en función de las distintas rutas y cargas.
* **Rendimiento del conductor:** El reporte destaca el tiempo que pasan los conductores en rutas específicas, su velocidad media y máxima, y cuánto tiempo permanecen parados los vehículos después de los viajes.
* **Evaluación de la eficiencia:** Puede evaluar el uso de combustible para distintos tipos de viajes, como los viajes con mucha carga frente a los viajes ligeros o sin carga, para optimizar el gasto de combustible.

## Parámetros del reporte

El reporte de Viajes ofrece varios parámetros configurables para adaptar el reporte a sus necesidades:

* **Resumen de la pantalla:** Activa la visibilidad de una página de resumen que proporciona una visión general de todos los dispositivos.
* **Mostrar solo resumen:** Genera una hoja de resumen para todos los dispositivos seleccionados sin información detallada del viaje. Requiere que se seleccionen al menos dos dispositivos.
* **Divide por paradas:** Separa los viajes en función de los intervalos de aparcamiento. Si no se selecciona, el reporte considerará el primer punto registrado del día como el inicio del viaje y el último punto registrado como el final del viaje.
* **Muestra la duración de la parada:** Muestra la duración del tiempo de estacionamiento después de cada viaje.
* **Mostrar coordenadas:** Incluye las coordenadas GPS de los puntos inicial y final de cada viaje, además de las direcciones.
* **Utiliza un filtro inteligente:** Excluye del reporte los viajes breves (menos de 300 metros o menos de cuatro puntos de datos).
* **Agrupar por conductores:** Organiza viajes por [conductores](../../gestin-de-flotas/conductores.md). Si no se asignó un conductor durante el período del reporte, los viajes se atribuirán a un conductor no identificado.

### Columnas del reporte

El reporte organiza la información en las siguientes columnas:

| Nombre de la columna                | Descripción                                                                                                                                                                                                                   |
| ----------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Inicio del movimiento**           | Detalla cuándo y dónde comenzó el viaje, incluyendo la hora y la dirección. Si las coordenadas están ocultas, solo se muestran la hora y la dirección.                                                                        |
| **Fin del movimiento**              | Muestra cuándo y dónde concluyó el viaje. Si el viaje termina dentro de una geocerca o PDI, se incluye su nombre.                                                                                                             |
| **Duración total de los viajes**    | Indica la distancia completa del viaje medida por GPS.                                                                                                                                                                        |
| **Duración del viaje**              | Muestra el tiempo total empleado en el viaje.                                                                                                                                                                                 |
| **Velocidad media**                 | La velocidad media durante el viaje.                                                                                                                                                                                          |
| **Velocidad máxima**                | La velocidad máxima alcanzada durante el trayecto, registrada por el dispositivo.                                                                                                                                             |
| **Combustible consumido por norma** | El consumo estimado de combustible para el viaje basado en tarifas estándar, requiere datos de consumo de combustible del vehículo por cada 100 km en el [perfil del vehículo](../../gestin-de-flotas/gestin-de-vehculos.md). |
| **Coste del viaje por norma**       | Muestra el coste del combustible basado en la tasa de consumo estándar proporcionada en el [perfil del vehículo](../../gestin-de-flotas/gestin-de-vehculos.md).                                                               |
| **Consumo de combustible (sensor)** | Muestra el consumo real de combustible si hay un sensor de combustible instalado y transmitiendo datos a la plataforma. El sensor debe medir en litros o galones.                                                             |
| **Tiempo de aparcamiento**          | Indica la duración del estacionamiento entre este viaje y el siguiente.                                                                                                                                                       |

**Ejemplo:**

Una fila del reporte podría indicarlo:

* **Hora y lugar de inicio:** 7 de febrero de 2024, a las 00:00:06, 6750 Putnam Drive, Highland-on-the-Lake, Town of Evans, Erie County, New York, USA, 14047.
* **Hora y lugar de finalización:** 7 de febrero de 2024, a las 00:57:46, 49 Steinfeldt Road, Town of Lancaster, New York, USA, 14086.
* **Distancia recorrida:** 42,89 kilómetros.
* **Tiempo de viaje:** 57 minutos y 40 segundos.
* **Velocidad máxima:** 59 km/h.
* **Velocidad media:** 45 km/h.
* **Consumo de combustible:** 3,4 litros (según tarifas estándar), con un coste de 12,86 dólares.

### Bloque resumen

El reporte también proporciona un resumen de todos los viajes durante el periodo seleccionado. Por ejemplo

* **Total de viajes:** 34
* **Distancia total:** 1514,9 kilómetros
* **Tiempo total de viaje:** 33 horas, 56 minutos y 45 segundos
* **Velocidad máxima:** 59 km/h
* **Velocidad media:** 45 km/h
* **Consumo estimado de combustible:** 121,2 litros, que cuestan 454,50 dólares
* **Lectura del cuentakilómetros al final del periodo:** 762052,8 km
