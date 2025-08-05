# Reporte sobre el tiempo de trabajo de los equipos

En el **Reporte de tiempo de trabajo de los equipos** en Navixy proporciona datos esenciales sobre el tiempo de actividad de cualquier equipo conectado a sus vehículos a través de entradas discretas o virtuales. Este reporte es crucial para los gestores de flotas que necesitan supervisar la eficiencia operativa de los equipos, analizar los tiempos de inactividad y garantizar un uso óptimo de los activos. A continuación encontrará una guía detallada sobre cómo funciona este reporte, los parámetros implicados y cómo interpretar los datos de forma eficaz.

## Visión general

El reporte Tiempo de trabajo de los equipos realiza un seguimiento del tiempo de funcionamiento de los equipos, distinguiendo entre periodos de actividad en movimiento y en ralentí. Este reporte incluye estadísticas detalladas, datos de actividad diaria y representaciones visuales como diagramas de actividad e histogramas para ayudarle a comprender y analizar los datos fácilmente.

## Cómo funciona el reporte

El reporte calcula el tiempo de trabajo de los equipos a partir de los puntos de datos recibidos por la plataforma Navixy. Tiene en cuenta el estado de las entradas discretas o sensores virtuales y el estado del aparcamiento para distribuir con precisión el tiempo de trabajo entre los periodos de movimiento y de inactividad. Para que los cálculos sean precisos, deben cumplirse las siguientes configuraciones y condiciones:

1. **Configuración de entrada discreta:**
  - La entrada discreta del dispositivo debe estar correctamente cableada y ser capaz de registrar el estado de entrada con precisión.
2. **Configuración del sensor virtual:**
  - [Sensores virtuales](../../dispositivos-y-ajustes/sensores-de-vehculos/sensores-virtuales.md) con dos estados también puede utilizarse. El sensor debe estar correctamente configurado para registrar estos estados.
3. **Ajustes de detección de aparcamiento:**
  - Los ajustes de detección de estacionamiento son cruciales para diferenciar entre el tiempo de funcionamiento en movimiento y el tiempo de inactividad. Si el estado de entrada es "encendido" mientras la plataforma detecta que el vehículo está aparcado (por ejemplo, moviéndose a menos de 3 km/h durante más de 5 minutos), este tiempo se registra como tiempo de inactividad.
4. **Puntualidad mínima:**
  - La plataforma calcula el tiempo de funcionamiento solo si el equipo está encendido durante una duración mínima, que puedes especificar (por ejemplo, 60 segundos).

### Ejemplo de cálculo

| Punto | Tiempo | Estado de entrada | Tiempo de actividad de los equipos |
| --- | --- | --- | --- |
| 1   | 10:00:00 | Fuera de | 0 minutos |
| 2   | 10:01:00 | En  | 0 minutos (la entrada estaba apagada en el último punto) |
| 3   | 10:01:32 | En  | 0 minutos (menos de 60 segundos) |
| 4   | 10:05:32 | Fuera de | 4 minutos y 32 segundos |

## Parámetros del reporte

El reporte Tiempo de trabajo del equipo incluye varios parámetros configurables que le permiten adaptar el resultado a sus necesidades específicas:

- **Duración mínima del periodo de trabajo:** Especifica el número mínimo de segundos que un sensor discreto debe estar encendido para que la hora se registre en el reporte. Para sensores virtuales, el valor debe ser mayor que 0.
- **Muestra el porcentaje de inactividad:** Realiza un seguimiento del estado del aparcamiento y distribuye el tiempo de funcionamiento del equipo entre movimiento y ralentí.
- **Utiliza un filtro inteligente:** Excluye los trayectos cortos del reporte. Los viajes cortos se definen como viajes de menos de 300 metros en los que el dispositivo envía menos de cuatro puntos de datos.
- **Selección de dispositivo:** El reporte solo incluye dispositivos con al menos un sensor discreto o virtual configurado.

## Visualizaciones

### Diagrama general de actividades

- Este diagrama ofrece una visión general del tiempo total de trabajo del equipo durante el periodo seleccionado. Muestra el tiempo que el equipo estuvo apagado, encendido y, si el seguimiento del porcentaje de inactividad está activado, diferencia entre el tiempo pasado en movimiento y el tiempo de inactividad.
- Para los sensores virtuales, el estado correspondiente a un valor 0 se muestra en gris, y cualquier otro valor se muestra en rojo.

### Histograma de actividad diaria

- El histograma desglosa el tiempo de trabajo del equipo en segmentos diarios. Si se controla el porcentaje de inactividad, también muestra la división entre tiempo de movimiento y de inactividad. Si se pasa el mouse por encima de cada día, se obtiene una vista más detallada de la actividad de ese día.

![image-20240815-010538.png](attachments/image-20240815-010538.png)

### Tabla horaria de funcionamiento diario del sensor

- Esta tabla presenta estadísticas diarias sobre el funcionamiento de los equipos, incluyendo:
  - **Date:** El día concreto para el que se calcula la información.
  - **Tiempo de funcionamiento (duración del estado del sensor virtual):** El tiempo total de funcionamiento del día.
  - **Intervalo medio:** La duración media del funcionamiento del equipo después de cada encendido.
  - **Kilometraje:** La distancia recorrida con el equipo encendido.
  - **Velocidad media:** La velocidad media del día.
  - **Intervalos:** El número de veces que se encendió el equipo durante el día.
  - **En movimiento (si el porcentaje de inactividad está activado):** La duración del trabajo en movimiento y su porcentaje sobre el tiempo total de trabajo.
  - **Ralentí (si el porcentaje de ralentí está activado):** El tiempo de funcionamiento sin movimiento y su porcentaje del tiempo total de funcionamiento.

![image-20240815-010619.png](attachments/image-20240815-010619.png)

## Interpretación del reporte

Para utilizar eficazmente el reporte Tiempo de trabajo de los equipos, tenga en cuenta lo siguiente:

- **Analizar los datos:** Utilice el reporte para controlar la frecuencia y la eficacia con que se utilizan los equipos. Identifique patrones de ralentí excesivo o infrautilización.
- **Eficacia operativa:** Evalúe el equilibrio entre los tiempos de actividad y de inactividad para determinar la eficiencia operativa de su equipo.
- **Planificación del mantenimiento:** El reporte ayuda a planificar el mantenimiento identificando los periodos de uso elevado o de arranques y paradas frecuentes, que pueden desgastar los equipos con mayor rapidez.
- **Gestión de costes:** Recalcule los costes de combustible y lubricante teniendo en cuenta los tiempos de inactividad junto con el uso activo, lo que es especialmente relevante para la maquinaria pesada.