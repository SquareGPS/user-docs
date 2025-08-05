# Sensor de nivel de combustible

Los sensores de combustible son esenciales para controlar los niveles de combustible en vehículos y depósitos, proporcionando datos clave para el seguimiento del consumo, la detección de repostajes y vaciados, y la optimización de la gestión del combustible. El uso eficaz de estos datos ayuda a prevenir las pérdidas de combustible, identificar los vehículos con un consumo elevado y mejorar la eficiencia general, lo que se traduce en un importante ahorro de costes.

## Comprender las lecturas de los sensores de combustible

La precisión de los datos de combustible depende de varios factores clave:

1. **El tipo de sensor de nivel de combustible**: La precisión del sensor y su compatibilidad con el dispositivo GPS.
2. **Instalación del sensor**: La instalación correcta es crucial, especialmente en el caso de depósitos no estándar. Deben seguirse las directrices del fabricante para obtener un rendimiento óptimo.
3. **Configuración del dispositivo**: Asegúrese de que el sensor está configurado correctamente y transmite datos a la plataforma. Es preferible realizar las calibraciones directamente en la plataforma que en el dispositivo.
4. **Ajustes de la plataforma**: Una configuración precisa en la plataforma es esencial no sólo para los datos que se muestran en los widgets, sino también para la funcionalidad de las alertas de vaciado/repostaje y los informes de nivel de combustible.

## Configuración de un sensor de combustible

Los sensores de combustible se clasifican como «[Sensores de medición](/wiki/pages/createpage.action?spaceKey=UDOCES&title=Measurement%20sensors&linkCreation=true&fromPageId=2922551803)» en la plataforma Navixy. Para añadir un sensor de combustible:

1. **Vaya a Dispositivos y configuración -> Sensores y botones**.
2. Haga clic en el icono **+** y seleccione **Sensor** de medición .
3. Configure el sensor:  
  - **Nombre del sensor**: Asigne un nombre claro para facilitar su identificación.
  - **Entrada**: Seleccione el canal de entrada desde el que se transmitirán los datos de combustible.
  - **Unidades**: Elija la unidad de medida apropiada (por ejemplo, litros).
  - **Precisión**: Defina el porcentaje de precisión, que se utilizará para calcular el error absoluto en el volumen de combustible.
  - **Umbrales para la detección de drenaje**: Defina umbrales para detectar drenajes de combustible en función de la tasa de cambio con el tiempo o el kilometraje.

### Ajustes avanzados del sensor de combustible

- **Ignorar en movimiento**: Excluye automáticamente cualquier drenaje o recarga que se produzca mientras el vehículo está en movimiento. Esto viene determinado por el ajuste «Detección de aparcamiento».
- **Tiempo de espera del filtro**: Ajuste el periodo de tiempo de espera para filtrar las lecturas inestables durante el movimiento del vehículo o inmediatamente después de repostar. Este ajuste es especialmente útil para vehículos con depósitos grandes.
- **Tabla de calibración**: Convierte las lecturas del sensor en unidades utilizables, como litros. Una calibración precisa es esencial para obtener datos fiables.
- **Filtros avanzados**: Configura filtros para ignorar lecturas por debajo o por encima de ciertos umbrales, y aplica multiplicadores para ajustar los datos del sensor según sea necesario.

### Procesamiento de datos de combustible en la plataforma

La plataforma Navixy lee y almacena los datos de los sensores de combustible a medida que se reciben. Los ajustes del sensor, incluidos los filtros y la calibración, se aplican cuando se emiten los datos. Esto significa que puede ajustar la configuración en cualquier momento y regenerar los informes para reflejar las configuraciones actualizadas.

### Detección y notificación de eventos de combustible

- **Vaciados y repostajes**: La plataforma utiliza una combinación de tablas de calibración y niveles de precisión para identificar y registrar los eventos de vaciado y rellenado de combustible.
- **Informes**: Los informes de combustible analizan la tasa de cambios en el nivel de combustible y aplican umbrales establecidos para identificar eventos significativos. Los eventos similares consecutivos se agrupan en una única entrada de informe.

### Ignorar los eventos de combustible durante el movimiento

Cuando la opción de ignorar repostajes o vaciados durante el movimiento está activada, la plataforma utiliza un algoritmo especializado para filtrar estos eventos. Si el repostaje comienza o termina dentro del tiempo de espera del filtro especificado antes o después de un viaje, el evento se registra. En caso contrario, se filtra.

### Análisis de la calidad de los datos del sensor de combustible

Navixy emplea métodos estadísticos avanzados para evaluar la calidad de los datos del sensor de combustible. Se asigna una puntuación de calidad en una escala de 10 puntos, siendo 1 la calidad más baja y 10 la más alta. Esta puntuación está disponible en los informes de volumen de combustible, tanto dentro de la interfaz como en los documentos descargados (PDF/XLS). La puntuación también se puede recuperar a través de solicitudes API.

# Sensor de nivel de combustible

Los sensores de combustible son un componente vital para el seguimiento de los niveles de combustible de diversos vehículos y depósitos estáticos. Con la ayuda de algoritmos de plataforma, los niveles de consumo de combustible, repostaje y descargas pueden supervisarse a través de los datos recogidos por estos sensores. La utilización eficiente de estos datos puede suponer un importante ahorro de costes al evitar las pérdidas de combustible e identificar los vehículos con un consumo excesivo, cuyos beneficios no cumplen las expectativas. Aprovechando la información proporcionada por los sensores de combustible, puede anticiparse a cualquier problema potencial y optimizar el consumo de combustible, aumentando así la rentabilidad global.

Los sensores de nivel de combustible son de varios tipos y cada uno sirve para un fin determinado. Puede encontrar información detallada sobre ellos en nuestra [Academia](https://docs.navixy.com/eco-fleet/types-of-fuel-level-sensors). Para el propósito de este artículo, nos centraremos en el funcionamiento del combustible de la plataforma. Además, vamos a discutir los ajustes del sensor de combustible y el impacto que tienen en el proceso general de gestión de combustible.

## ¿De qué dependen las lecturas del sensor de combustible?

La precisión de los datos de combustible mostrados depende de varios factores, entre los que se incluyen:

- El sensor de nivel de combustible - qué tipo y qué tan bien es capaz de leer del tanque, y qué tan bien interactúa con el rastreador GPS.
- Instalación del sensor del depósito - si tiene un depósito no estándar o requiere una instalación no estándar, lo mejor es consultar con el fabricante sobre cómo instalar dicho sensor.
- Configuración del dispositivo - asegúrese de que el sensor está configurado y el dispositivo envía sus datos a la plataforma. Es conveniente no realizar calibraciones adicionales en el lado del dispositivo, sino hacerlo directamente en la plataforma.
- Ajustes en el lado de la plataforma - de ellos dependen no sólo las lecturas en los widgets, sino también el funcionamiento de las alertas de vaciado y repostaje y los informes de nivel de combustible. Al optimizar estos ajustes, resulta más fácil identificar anomalías e irregularidades en las lecturas de datos de combustible que pueden requerir mayor atención.

## Creación de sensores

Los sensores de combustible son un tipo de [sensor de medición](/wiki/pages/createpage.action?spaceKey=UDOCES&title=Measurement%20sensors&linkCreation=true&fromPageId=2922551803) que puede crearse en una plataforma de seguimiento GPS. Para crear un sensor de combustible, vaya a la sección Gestión de Dispositivos y haga clic en el panel Sensores y Botones. A continuación, haga clic en el icono + y seleccione «sensor de medición» en el menú desplegable.

## Ajustes del sensor de combustible

Una vez que elija Nivel de combustible como tipo de sensor, aparecerán ajustes adicionales. La lista completa de opciones para el sensor de combustible incluye:

- Nombre del sensor - asigne un nombre claro y conveniente para el sensor. Este nombre será visible en los widgets, informes y reglas para ayudarle a identificar fácilmente el sensor.
- Entrada - seleccione la entrada desde la que el dispositivo transmite los datos de combustible.
- Unidades - seleccione una unidad de medida.
- Precisión - se refiere al porcentaje especificado utilizado para calcular el error absoluto en el volumen del tanque. Este valor de error se utilizará para calcular la cantidad para recargas y drenajes.
- Umbrales para la detección de vaciados - se utilizan para determinar los vaciados en los informes de combustible. Este parámetro puede ser representado como la tasa de cambio en el nivel de combustible. Ambos umbrales se comprueban siempre, y si el nivel de combustible cambia más rápido que al menos uno de los umbrales establecidos para más de nivel de precisión, el informe marcará el drenaje de combustible.
  - **Por tiempo**: el flujo máximo permitido se mide en unidades por hora y se puede configurar en los ajustes del sensor. Al calcular el cambio de velocidad en el tiempo, la plataforma compara el cambio de nivel de combustible entre puntos. Si no se configura, el valor por defecto es de 120 unidades por hora. Esto no significa que el combustible deba cambiar más de 120 por hora. Significa que el nivel de combustible debe cambiar más rápido que 120 por hora (igual a 20 L por 10 minutos o 2 L por minuto) para determinar el drenado en un informe. Este valor debe fijarse en unos puntos porcentuales por encima de la tasa de consumo probable durante cargas pesadas o cuando el vehículo está ascendiendo cuesta arriba.
  - **Por kilometraje**: la velocidad máxima permitida de cambio de nivel de combustible se mide en unidades por cada 100 km. No significa que el combustible deba cambiar más de lo establecido por cada 100 km. Por ejemplo, fijamos 100 L por 100 km. Significa que el nivel de combustible debe cambiar más rápido que 100 L por 100 km (igual a 10 L por 10 km o 1 L por km) para determinar el drenado en un informe. Este valor debe introducirse manualmente y no debe basarse únicamente en la tasa de consumo de combustible especificada por el fabricante. Recomendamos realizar pruebas y verificar la tasa de consumo de combustible real registrada en los informes y, a continuación, establecer los valores necesarios en consecuencia para obtener la máxima precisión.
- **Ignorar en movimiento** - la plataforma excluirá automáticamente de las reglas e informes los vaciados y rellenados que se produzcan durante el movimiento. El movimiento viene determinado por el [ajuste y detección de estacionado](https://www.navixy.com/docs/user/web-interface-docs/devices-doc/parking-detection/).
  - Drenajes: se excluirán los drenajes en movimiento.
  - Rellenos: se filtrarán los rellenos en movimiento.
  - Tiempo de espera del filtro: este ajuste aparece cuando está activada la función Ignorar. Determina el periodo de tiempo de espera en minutos que se utilizará para acortar los intervalos de conducción para el filtrado de combustible. Esta opción puede ser útil si el nivel de combustible se estabiliza sólo después de que ha pasado algún tiempo desde el repostaje, y el vehículo ya ha comenzado a moverse. Esto es más común en vehículos con grandes depósitos de combustible. El ajuste por defecto para esta función es de 5 minutos.
- **Tabla de calibración** \- este parámetro se utiliza para convertir las lecturas del sensor en unidades deseadas como litros. Algunos fabricantes de sensores pueden proporcionar los valores de conversión para la tabla. Sin embargo, en la mayoría de las situaciones, [la calibración](https://docs.navixy.com/eco-fleet/fuel-level-sensors) será necesaria para obtener lecturas precisas.
  - Volumen del tanque - es el volumen máximo del tanque, que se especifica en unidades en la tabla de calibración. Si no se especifican valores de calibración, se asume el valor por defecto de 100, que indica que los datos se transmiten en porcentaje.
  - Aunque su sensor ya envíe datos a la plataforma en litros, es mejor especificar la calibración como 0 = 0 litros y capacidad máxima del depósito = X litros.
  - Si se trata de un sensor que transmite la información del nivel de combustible en porcentajes, especifique la calibración 0 = 0 litros y 100 = capacidad máxima del depósito de combustible en litros.
- **Ajustes avanzados** - están debajo de la tabla de calibración.
  - Ignorar valores - los valores deben especificarse de la misma forma que llegan a la plataforma desde el dispositivo.
    - Menos - el filtro se puede utilizar para ignorar cualquier lectura que caiga por debajo de un cierto umbral, X. Esto es útil en situaciones en las que las lecturas de un sensor pueden caer por debajo de un cierto valor. Por ejemplo, un cable suelto o un sensor que envía una lectura de 0 cuando el encendido está desconectado.
    - Más - el filtro puede ser usado para ignorar cualquier lectura que exceda un cierto umbral, X. Esto es valioso cuando se trata de sensores cuyas lecturas pueden ocasionalmente aumentar dramáticamente. Por ejemplo, si se detecta un error o si hay un voltaje más alto de lo esperado.
  - Multiplicador - multiplica los valores resultantes por un determinado coeficiente. Si desea dividir valores, utilice decimales.

## ¿Cómo funciona el cálculo de combustible en la plataforma?

### Recepción y tratamiento de los datos del combustible

La plataforma lee y guarda las lecturas de los sensores de combustible a medida que se reciben de los dispositivos. Los datos de los sensores de combustible sólo se guardan una vez que se ha creado un sensor de combustible en el sistema.

Los filtros de mínimos y máximos, las tablas de calibración y otros ajustes del sensor sólo se aplican cuando se emiten los datos. Como resultado, puede cambiar los ajustes en cualquier momento y reconstruir los informes para ver cómo los cambios han afectado a los datos guardados. Esto proporciona flexibilidad en términos de configuración y garantiza que los datos estén siempre actualizados con los últimos ajustes.

### Reglas de drenado y repostaje

Las reglas de vaciado y repostaje se basan en la tabla de calibración y en el error absoluto, que se calcula como

`volumen del tanque * precisión`

La plataforma registrará la última lectura actual del sensor durante un intervalo de diez minutos. Basándose en esta lectura, se activarán los siguientes eventos:

- Si el nivel de combustible ha aumentado más que el error absoluto, se registrará un evento de «llenado».
- Si el nivel de carburante ha disminuido más que el error absoluto, se registrará un evento de «vaciado».

Por ejemplo, si la capacidad del depósito es de 100 litros y la precisión es del 5%, un cambio de 5 litros en el nivel de combustible en un plazo de 10 minutos activará la regla.

### Recargas y vaciados en los informes

El sistema de informes proporciona un método de análisis más avanzado, ya que se basa en un conjunto mayor de datos guardados. Todos los parámetros se tienen en cuenta en el análisis de los informes.

La plataforma utiliza la tasa de disminución del nivel de combustible y el error absoluto para identificar y registrar los vaciados de combustible. Se produce un «vaciado» cuando el nivel de combustible disminuye más que el error absoluto dentro de los umbrales especificados para vaciados por tiempo o kilometraje (si se han establecido).

En el informe, se registra un evento de «llenado» cuando el nivel de combustible aumenta más que el error absoluto. La plataforma agrupará los eventos de llenado o vaciado consecutivos, lo que significa que si la misma condición se activa repetidamente, la plataforma los agrupará en un único evento grande de llenado o vaciado.

### Ignorar drenados y repostajes en movimiento

Una vez que haya activado una o ambas opciones para ignorar - el siguiente algoritmo se utilizará para los informes y alertas, además de la norma:

- Si el repostaje comienza durante el tiempo de estacionamiento, se mostrará en el informe y será registrado por la regla. Además, si el repostaje comienza dentro de los X minutos del tiempo de espera del filtro antes de aparcar o dentro de los X minutos del tiempo de espera del filtro después de que comience el viaje, también será registrado por la regla y se mostrará en el informe.
- Sin embargo, si el repostaje comienza antes de X minutos desde el tiempo límite de filtrado antes de aparcar o después de X minutos desde el tiempo límite de filtrado desde el inicio del viaje, se filtrará.
- En los casos en los que no se especifique un tiempo límite de filtrado, se filtrarán todos los repostajes que se inicien durante los viajes.

### Análisis y clasificación de las lecturas del sensor de combustible

La aplicación de varios métodos estadísticos ha dado como resultado un modelo para analizar la calidad de los datos de los sensores. El equipo de Navixy ha desarrollado un algoritmo adaptativo que puede clasificar la calidad de las lecturas de los datos brutos de los sensores y proporcionar una puntuación en una escala de 10 puntos: de 1 - la calidad más baja, a 10 - datos de alta calidad.

Para probar esta innovación, es necesario generar un informe de volumen de combustible para el objeto u objetos investigados. La calificación de calidad estará disponible en la parte inferior del informe, tanto en la interfaz del armario como en los documentos (PDF/XLS) descargados a partir del informe generado. La calificación también puede obtenerse mediante solicitudes API.

## See also

- [Mejora de la precisión de la gestión del combustible con el índice de calidad del sensor de combustible](https://www.navixy.com/blog/enhancing-fuel-management-accuracy-with-fuel-sensor-quality-index/)
- [Dominio de las tablas de calibración para una gestión precisa del combustible](https://www.navixy.com/blog/calibration-tables/)