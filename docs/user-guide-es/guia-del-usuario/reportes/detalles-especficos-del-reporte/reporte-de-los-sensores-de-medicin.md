# Reporte de los sensores de medición

El **Reporte de los sensores de medición** en Navixy está diseñado para proporcionar datos detallados de sensores de medición configurados o sensores virtuales con un método de cálculo del valor de origen durante un periodo seleccionado.

Este reporte permite a los usuarios ver información gráfica y estadística de los sensores de sus dispositivos, lo que contribuye a una supervisión y una toma de decisiones eficaces.

## Requisitos para generar el reporte

Para generar correctamente el **reporte de los sensores de medición** deben cumplirse las siguientes condiciones:

* **Compatibilidad con dispositivos:** Asegúrese de que el dispositivo admite la lectura del sensor requerido en la plataforma. Puede verificarlo consultando la lista de entradas admitidas para el modelo específico.
* **Transmisión activa de datos:** El aparato y sus sensores deben estar configurados correctamente y transmitir datos de forma activa.
* **Sensores virtuales:** [Sensores virtuales](../../dispositivos-y-ajustes/sensores-de-vehculos/sensores-de-vehculos/sensores-virtuales/) debe tener un método de cálculo del valor de origen y proporcionar valores numéricos a la plataforma.
* **Configuración del sensor:** Los sensores de medición deben estar correctamente configurados en la plataforma.

## Parámetros del reporte

El reporte utiliza varios parámetros para adaptar el resultado a sus necesidades:

* **Detalles intervalo de tiempo:** Muestra las lecturas recibidas en incrementos de 5, 30 minutos, 1, 3 o 6 horas en la tabla de detalle de datos.
* **Eje X del gráfico:** Elija si desea mostrar la información por tiempo o por kilometraje.
* **Datos suaves:** Aplica suavizado al gráfico para filtrar los valores máximos y promediar los datos cuando haya una variación significativa.
* **Mostrar dirección:** Muestra la dirección recibida por la plataforma junto con los datos del sensor. La dirección mostrada corresponde a la primera lectura del segmento detallado.
* **Utiliza un filtro inteligente:** Excluir los datos de viajes cortos, definidos como viajes de menos de 300 metros con menos de 4 puntos de datos enviados por el dispositivo.

Para cada dispositivo, debe seleccionar el sensor para el que desea generar el reporte. Solo los dispositivos con [medición](../../dispositivos-y-ajustes/sensores-de-vehculos/sensores-de-vehculos/sensor-de-medicin/) o sensores [virtuales](../../dispositivos-y-ajustes/sensores-de-vehculos/sensores-de-vehculos/sensores-virtuales/) estarán disponibles en la lista. Si selecciona un sensor virtual de un tipo incorrecto, el reporte indicará "Este no es un sensor de medición".

## Visualizaciones

### Gráfico con las lecturas de los sensores

El gráfico del reporte muestra las lecturas de las mediciones o de los sensores virtuales en forma de gráfico, lo que le ayuda a visualizar las tendencias de los datos a lo largo del tiempo o de la distancia.

* **Pasar el ratón por encima de los puntos:** Si pasas el ratón por encima de un punto del gráfico, podrás ver la hora exacta a la que se registró y el valor del sensor. Si el eje X está configurado en kilometraje, también verás la distancia a la que se tomó la lectura.

### Cuadro con datos estadísticos

El reporte incluye una tabla de datos estadísticos que ofrece resúmenes diarios de las lecturas de los sensores.

**Columnas de la tabla de datos estadísticos:**

* **Fecha:** La fecha específica de los datos registrados.
* **Mínimo (unidades de medida):** El valor más bajo registrado por el sensor en esa fecha.
* **Máximo (unidades de medida):** El valor más alto registrado por el sensor en esa fecha.
* **Valor medio (unidades de medida):** La media de todas las lecturas de los sensores para esa fecha.

Nota: Las unidades de medida variarán en función de la configuración del sensor.

### Tabla de desglose de datos

La **tabla de desglose de datos** presenta las lecturas de los sensores en intervalos de tiempo especificados, como cada 30 minutos, a partir de una hora determinada. Ofrece una visión detallada de los datos de los sensores, lo que ayuda a identificar tendencias o problemas durante periodos concretos.

* **Interpretación de la tabla:** Si aparece "Sin datos", significa que no se han recibido lecturas durante ese tiempo. Esto puede deberse a que el dispositivo no transmite datos, está apagado o el sensor está desconectado.
