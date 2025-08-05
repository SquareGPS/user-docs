# Gestión de vehículos

La pestaña de **Gestión de vehículos** en Navixy es esencial para el seguimiento y la gestión de su flota. Permiten supervisar diversos aspectos, como la ubicación, el consumo de combustible, los programas de mantenimiento y el rendimiento general de la flota, lo que permite realizar operaciones eficientes y tomar mejores decisiones.

## Ficha de Vehículos

La pestaña "Vehículos" presenta un resumen detallado de todos los vehículos de su flota. La información se organiza en forma de tabla, complementada por un menú visual en la parte derecha de la pantalla. Aquí puede añadir o editar fácilmente los detalles de los vehículos, asociarlos a depósitos específicos y vincularlos a los rastreadores activados en la plataforma.

### Añadir un nuevo vehículo

Para añadir un nuevo vehículo, basta con pulsar la tecla **Añadir vehículo** botón. También tiene la opción de cargar una imagen del vehículo para facilitar su identificación.

- **Pestaña principal:** Introduzca la información esencial del vehículo, incluidas las etiquetas y cualquier nota relevante.
- **Ficha de especificaciones:** Proporcione especificaciones detalladas, como las dimensiones del vehículo, el tamaño de la distancia entre ejes, el número de ruedas, la velocidad permitida, la disponibilidad de remolque y el año de fabricación.
- **Pestaña de combustible:** Registre la información relacionada con el combustible, incluido el tipo de combustible, la capacidad del depósito y la tasa de consumo por cada 100 km (o millas). Estos datos son cruciales para generar reportes precisos sobre el consumo de combustible.
- **Ficha del seguro:** Introduzca los datos del seguro del vehículo, incluido el número de póliza y la fecha de vigencia.

![](https://squaregps.atlassian.net/wiki/images/icons/grey_arrow_down.png)

Consumo de combustible en el perfil del vehículo y su función en los informes de combustible

En Navixy, la configuración del **Consumo de combustible** en el perfil del vehículo es un paso fundamental para realizar un seguimiento preciso e informar sobre el uso de combustible en toda la flota en función del kilometraje recorrido, incluso sin depender de los datos OBDII o de sensores de combustible especializados.

Este parámetro suele definirse en términos de litros por cada 100 kilómetros (L/100 km) o millas por galón (MPG), según las preferencias regionales.

#### Cómo se utiliza el consumo de combustible en los reportes.

1. **Estimación del consumo de combustible:**
  - El valor de consumo de combustible introducido en el perfil del vehículo sirve como referencia para estimar el uso de combustible de un vehículo en una distancia determinada. Por ejemplo, si un vehículo está configurado para consumir 10 L/100 km, el sistema estimará que utiliza 10 litros de combustible por cada 100 kilómetros recorridos.
2. **Cálculo de los costes previstos de combustible:**
  - Navixy utiliza la tasa de consumo de combustible establecida junto con el kilometraje registrado para calcular los costes de combustible previstos. Introduciendo el precio por litro o galón en los ajustes, el sistema puede generar reportes que calculan cuánto deberías gastar en combustible, lo que ayuda a elaborar presupuestos y planificar las finanzas.
3. **Comparación con los datos reales del combustible:**
  - Cuando se combina con los datos de los sensores de nivel de combustible, Navixy puede comparar el consumo de combustible estimado con el consumo real. Esta comparación ayuda a identificar discrepancias, como el robo de combustible, ineficiencias en el comportamiento de conducción o problemas con el motor del vehículo que podrían dar lugar a un consumo de combustible superior al previsto.

### Importación de vehículos

Si tiene una flota grande y necesita crear perfiles para varios vehículos, es más eficiente importar toda la información a la vez utilizando un único archivo, en lugar de crear perfiles de vehículos uno por uno. Los datos deben estar en formatos de archivo XLS, XLSX o CSV.

Para importar perfiles de vehículos:

1. Abre la aplicación "Gestión de flotas", haz clic en "Añadir vehículo" y selecciona "Importar desde archivo Excel".
2. En la ventana de importación, encontrará un archivo Excel de ejemplo que puede utilizar como plantilla.
3. Asegúrese de que las columnas de su archivo se corresponden con los campos correctos del sistema de seguimiento, introduciendo los campos del encabezado adecuados. Esto puede hacerse antes de la importación o durante el proceso.
4. En el archivo cargado, tendrás que especificar información clave como:
  - Etiqueta
  - Modelo
  - Tipo
  - Tipo de combustibleUna vez cumplimentado el formulario, guarde el archivo en su ordenador.

Para cargar el archivo en el sistema:

1. Haz clic en el botón "Seleccionar", busca tu archivo y haz clic en "Siguiente".
2. Se le pedirá que revise los campos de la cabecera. Si todo es correcto, vuelva a hacer clic en "Siguiente".
3. Si algún campo es incorrecto, el sistema le pedirá que lo corrija. Si algún campo obligatorio está vacío, esa información no se importará.
4. Una vez que la información sea correcta, la importación se completará con éxito y los nuevos perfiles de los vehículos aparecerán en la aplicación "Gestión de flotas".