# Historia del viaje

El historial de viajes en Navixy le permite revisar las actividades pasadas y las rutas tomadas por los vehículos de su flota. Esta función proporciona un registro detallado de los viajes, incluidas marcas de tiempo, ubicaciones, distancias y duraciones, lo que le ayuda a supervisar la actividad de los vehículos y optimizar la gestión de la flota.

Para ver el historial de viajes en Navixy, seleccione los objetos que le interesan y, a continuación, haga clic en el botón de historial (la flecha circular azul situada en la parte inferior derecha de la lista de objetos). Se le pedirá que elija un intervalo de fechas y horas. Seleccione el intervalo de fechas deseado para continuar.

![image-20240807-220924.png](attachments/image-20240807-220924.png)

![image-20240807-223844.png](attachments/image-20240807-223844.png)

## Breve historia del viaje

Tras seleccionar un intervalo de fechas, la vista Historial muestra un resumen de los viajes y eventos de los objetos elegidos. Cada entrada de viaje incluye detalles clave:

- **Marca de tiempo**: Muestra las horas de inicio y fin del viaje.
- **Ubicación**: Proporciona las direcciones de inicio y final del viaje.
- **Distancia recorrida**: Indica la distancia total recorrida durante el viaje.
- **Duración**: Muestra el tiempo total empleado en el trayecto.

Con el historial breve puede obtener rápidamente una visión general de la actividad y el historial de desplazamientos de su flota durante el periodo seleccionado.

## Historial detallado del viaje

Al hacer clic en una entrada de viaje en la vista breve del historial de viajes, verá un desglose detallado del viaje. Esto incluye:

- **Horas de inicio y fin**: Las horas exactas en que comenzó y terminó el viaje.
- **Distancia recorrida**: La distancia total recorrida durante el viaje.
- **Duración**: El tiempo total empleado en el viaje.
- **Detiene**: Información detallada sobre cada parada, incluida su ubicación y duración.

Cada segmento del viaje se enumera con direcciones y marcas de tiempo precisas, lo que le permite analizar a fondo el movimiento y las paradas de su flota durante el periodo seleccionado. Esta vista detallada ayuda a supervisar la actividad de los vehículos, comprender el comportamiento de los conductores y optimizar las rutas.

## Funciones de confort

| Característica | Descripción |
| --- | --- |
| **Métodos de combinación de colores** | Puede elegir diferentes esquemas de color para visualizar los datos del viaje:<br><br>- Colorear manualmente: Asigna colores manualmente a los diferentes viajes.<br>- Color por tracks: Colorea automáticamente los viajes en función de su pista.<br>- Colorear por estado: Diferencia los viajes por su estado, como en movimiento o parados.<br>- Colorear por velocidad: Visualiza los viajes en función de las variaciones de velocidad. |
| **Cambiar el color del segmento de viaje** | Personalice el color de determinados segmentos del viaje para resaltar secciones concretas y obtener un mejor análisis visual. |
| **Animar la reproducción del viaje** | Utilice el botón de reproducción para animar los desplazamientos en el mapa, mostrando el movimiento de los objetos a lo largo del tiempo. Ajuste la velocidad de reproducción con opciones como x1, x3, x10, x30, x100 y x300. Esta función es muy útil para comprender las pautas y la duración de los desplazamientos. |
| **Descargar viajes como archivo KML** | Descargue los datos de los trayectos como archivos KML para utilizarlos en otras aplicaciones SIG, lo que permite realizar análisis posteriores y compartirlos. |
| **Imprimir los viajes seleccionados** | Imprima informes de viaje detallados directamente desde la interfaz para documentarlos o compartirlos con los miembros del equipo. |
| **Cambiar entre vista contraída y detallada** | Alterna entre una vista resumida y una vista detallada de los viajes para ver más o menos información según necesites. |
| **Ajustar ancho de vía** | Ajuste la anchura de las huellas mostradas en el mapa. Esto resulta útil en aplicaciones como la agricultura para visualizar con mayor claridad la cobertura de los campos por las huellas de los tractores. |
| **Otros ajustes de vista** | Los ajustes adicionales incluyen mostrar paradas, datos LBS, agrupar puntos de datos para mayor claridad, utilizar filtros inteligentes para reducir el ruido y dividir los viajes por paradas para un análisis detallado. |

## Tipos de vía

Existen distintos tipos de seguimiento en función de la tecnología utilizada para determinar las ubicaciones y del modo de seguimiento establecido en la configuración del dispositivo.

- **Vías continuas**: Son las pistas más comunes, utilizadas normalmente en aplicaciones de seguimiento de vehículos. Se representan como polilíneas con puntos iniciales y finales claros.
- **Pistas de intervalo**: En el caso de los rastreadores GPS autónomos, la localización suele actualizarse a intervalos relativamente largos, como una vez por hora o una vez al día. Estas pistas se muestran como puntos de referencia numerados (1, 2... N). Para facilitar la visualización, se conectan con líneas grises transparentes, que pueden no representar con exactitud la trayectoria real.
- **Ubicaciones LBS**: Cuando los datos de localización se determinan utilizando tecnologías LBS alternativas, como señales GSM o Wi-Fi, pueden carecer de precisión. Estas ubicaciones se visualizan con círculos, cuyo radio indica la precisión.
- **Puntos de referencia agrupados**: Cuando un activo permanece en el mismo lugar durante un periodo prolongado, numerosos mensajes de intervalo o LBS pueden desordenar el mapa. Para mejorar la legibilidad, el servidor los consolida en un único hito agrupado, mostrando sólo un punto en el mapa. La hora de inicio/fin y la duración se añadirán a la nota de este hito.