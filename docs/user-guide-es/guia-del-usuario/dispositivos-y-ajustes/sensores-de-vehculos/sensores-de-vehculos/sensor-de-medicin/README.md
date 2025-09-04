# Sensor de medición

## Sensor de medición

Para agregar un sensor de medición, haga clic en “Dispositivos”, seleccione un “Objeto” dentro del recuadro ![Measurement sensor](https://www.navixy.com/wp-content/uploads/2021/10/add.png). De clic en “Sensores y botones” y seleccione “Sensor de medición”:

Especifique los parámetros necesarios del sensor:

* **Etiqueta del sensor:** Especifique el nombre del sensor en el sistema. Puede ser cualquier nombre de su elección.
* **Entrada:** Elija la entrada a la que está conectado el sensor (el número y los tipos de entradas disponibles vienen determinados por el modelo de dispositivo).
* **Tipo de sensor:** Elija el tipo de sensor
* **Unidades:** Elija las unidades de medida. Puede seleccionar las unidades disponibles en la lista desplegable o especificar unas personalizadas.
* **Añadiendo datos de calibración:** Solo aparecen cuando se elige el tipo específico de sensor. Por ejemplo, para un sensor de combustible, los parámetros de precisión y umbrales pueden ajustarse para ser utilizados en la detección de drenaje.

<figure><img src="../../../../../.gitbook/assets/image (1) (1).png" alt="" width="246"><figcaption></figcaption></figure>

#### Datos de calibración

Una vez configurados todos los parámetros, es necesario introducir los datos de calibración en la tabla.

Primero hay que obtener una lista de la correspondencia entre los valores brutos del sensor de medición (por ejemplo, voltios) y el valor real que mide el sensor (por ejemplo, litros). Para más información, [consulte este tutorial](https://docs.navixy.com/eco-fleet/fuel-level-sensors).

Para agregar una fila, haga clic en ![Measurement sensor](https://www.navixy.com/wp-content/uploads/2021/10/add.png).

En la línea creada, rellene el campo **Valor del sensor** con el valor obtenido y el campo **Cantidad** con la cantidad medida correspondiente.

Para borrar una fila, haga clic en ![Measurement sensor](https://www.navixy.com/wp-content/uploads/2021/10/del.png).

\[![Measurement sensor](https://www.navixy.com/wp-content/uploads/2021/10/measurement_sensor_calibration_table_en.png)

Para subir un archivo con la tabla de calibración, haga clic en ![Measurement sensor](https://www.navixy.com/wp-content/uploads/2021/10/upload.png). Los archivos de calibración pueden ser generados por la utilidad Omnicomm LLS Monitor. Solo se admite el formato de archivo XML.

\[![Measurement sensor](https://www.navixy.com/wp-content/uploads/2021/10/upload_calibration_table_en.png)

Para un ajuste más preciso, pulse el botón «Ajustes avanzados» ![Measurement sensor](https://www.navixy.com/wp-content/uploads/2021/10/advanced_settings.png). Estos ajustes son **Ignorar** valores y **Multiplicador**.

* **Ignorar valores:** esta configuración le permite ajustar un rango «válido» de valores de medición brutos. Cualquier valor por encima o por debajo del rango será omitido. Por ejemplo, esto se puede utilizar para omitir los valores cero del sensor de combustible cuando el encendido del vehículo está apagado.
* **Multiplicador:** se utiliza para corregir los valores de datos brutos del sensor multiplicándolos por algún número.

**Orden de filtrado:**

Tenga en cuenta que las restricciones **menos que** y **más que** se aplican antes que **Multiplicador**.

Todo el orden de filtrado:

1. Ignorar valores (**menos que** & **más que**)
2. **Multiplicador**
3. **Tabla de calibración**

Ejemplo: Valor bruto entrante - 1000, los límites son 3000 y 100, el multiplicador es igual a 0,2.

En este caso, el valor pasa por el filtro mín/máx, se multiplica por 0,2 y se convierte en 200. Y aquí es donde se aplica la tabla de calibración. La tabla de calibración toma 200 como **Valor del sensor** (valor de origen) y lo convierte en el valor objetivo de **Cantidad** que se mostrará en las instalaciones de la interfaz de usuario. Si un paquete de datos entrante contiene los datos del sensor con un valor superior a 3000, el valor no pasará los límites, se descarta, por lo tanto, no se aplica la multiplicación ni la calibración.

Los números aquí son para ejemplo y usted puede tener otras configuraciones, pero el principio permanece.

**Gráfica:**

A medida que se vayan introduciendo datos en la tabla, se irá trazando el gráfico.\
Si la tabla se rellena correctamente, el gráfico aumentará proporcionalmente:

![Measurement sensor](https://www.navixy.com/wp-content/uploads/2021/10/measurement_sensor_calibration_graph_en.png)

Si el gráfico no aumenta proporcionalmente (por ejemplo, al principio aumenta y luego disminuye, o parece ondulado), entonces la tabla de calibración es incorrecta:

![Measurement sensor](https://www.navixy.com/wp-content/uploads/2021/10/measurement_sensor_calibration_graph_wrong_en.png)

Para confirmar los cambios, haga clic en **Guardar**.

**Almacenamiento de datos brutos de sensores:**

Los datos brutos del sensor se almacenan en la plataforma por defecto. Esto permite a los usuarios recalibrar los datos del sensor representados en el historial del sensor del dispositivo. Cada vez que se modifican los datos del multiplicador, del máximo («menos que»), del mínimo («más que») o de la tabla de calibración, la plataforma recalcula el historial y representa los datos de acuerdo con los nuevos ajustes. La ventaja de este enfoque es que el usuario siempre puede recalibrar la tabla, cambiar los ajustes del sensor y elaborar un informe basado en los datos recalculados «sobre la marcha».

![Measurement sensor](https://www.navixy.com/wp-content/uploads/2021/10/measurement_sensor_advanced_en.png)
