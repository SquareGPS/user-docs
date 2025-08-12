# Widget de exportación de datos brutos

La herramienta de exportación de datos sin procesar de Navixy permite descargar datos sin procesar analizados y descodificados de cualquier rastreador GPS de la plataforma en formato CSV. Esta función es esencial para el diagnóstico de dispositivos, el análisis de datos y la integración de datos con programas de IA / ML.

[![Raw data export tool](https://www.navixy.com/wp-content/uploads/2023/12/browser_a0qszuge3l.png)

](https://www.navixy.com/wp-content/uploads/2023/12/browser_a0qszuge3l.png)

## Visión general

Con la herramienta de exportación de datos brutos, puedes:

- **Descargar datos brutos descodificados** desde cualquier localizador GPS de la plataforma.
- **Seleccionar parámetros específicos** para incluir en su archivo CSV, con una función de búsqueda fácil de usar.
- **Acceso a datos históricos** sin necesidad de activar previamente el ahorro de datos.
- **Ajustar marcas de tiempo** a su zona horaria preferida, lo que facilita la gestión de datos en distintas regiones.

Los datos brutos de salida consisten en toda la información descodificada de los protocolos propietarios del modelo de dispositivo. Una vez descodificados, los datos se almacenan en un formato universal, incluidos detalles clave como la ubicación y las lecturas de los sensores. Los datos se proporcionan en formato de archivo CSV para facilitar el acceso y la integración.

## Cómo utilizar la exportación de datos brutos

Para empezar, vaya a la sección "Dispositivos y configuración" y localice el dispositivo. A continuación, haz clic en el botón "Exportar datos" del recuadro "Datos sin procesar".

[![Raw data export tool file configuration window](https://www.navixy.com/wp-content/uploads/2023/12/browser_ybwmnfdh8h.png)

](https://www.navixy.com/wp-content/uploads/2023/12/browser_ybwmnfdh8h.png)

Se abrirá la herramienta "Exportación de datos brutos". Elija el intervalo de fechas, la zona horaria y los parámetros que deben incluirse en un archivo csv.

Para evitar el cierre accidental de ventanas, la herramienta "Exportación de datos brutos" solo puede cerrarse haciendo clic en la "X" de la esquina superior derecha. Además, si no has cambiado de dispositivo o actualizado la página, la herramienta recordará la configuración seleccionada anteriormente. Esta función facilita la revisión de la configuración del rastreador GPS o del sensor, el regreso y la continuación del trabajo.

### Seleccionar un intervalo de fechas

Puede seleccionar hasta los últimos 30 días o más, dependiendo de su plan. Las fechas pueden elegirse haciendo clic en el calendario o introduciéndolas manualmente. También se pueden fijar horas concretas. Aquí tienes algunas opciones de selección rápida:

- Ayer
- La semana pasada
- Últimos 30 días

Al hacer clic en ellos, se establecerá automáticamente el intervalo de fechas adecuado.

Para simplificar el proceso, un contador muestra cuántos días has seleccionado. Si intentas seleccionar una fecha con más de 30 días de antelación, recibirás un mensaje y se desactivará el botón de selección.

### Elegir una zona horaria

La zona horaria por defecto es la zona horaria de la cuenta del usuario, pero puede ajustarse mediante:

- Elegir entre una lista de zonas horarias disponibles.
- Introducir el nombre de la zona horaria.
- Introducir el desfase horario (por ejemplo, -8, +2).

### Selección de parámetros

Los parámetros disponibles varían según el modelo de dispositivo e incluyen todos los parámetros integrados en la plataforma para cada modelo. Se pueden seleccionar hasta 1000 parámetros por archivo.

Las opciones para la selección de parámetros incluyen:

- **Seleccionar todo**: Haga clic en la casilla para seleccionar todos los parámetros.
- **Seleccionar parámetros específicos**: Utilice las casillas de verificación situadas junto a cada parámetro.
- **Buscar en**: Busque parámetros específicos escribiendo su nombre o parte de su nombre.

Para varias entradas del mismo tipo, el sistema da prioridad a la entrada con el mayor número de índice. Puede especificar qué índices incluir introduciendo números separados por comas o definiendo un rango mediante un guión (por ejemplo, "1-2, 4, 7").

Aparecerá un recuento de los parámetros seleccionados, y cada parámetro elegido añadirá una columna al archivo CSV.

[![Raw data export tool file configuration window with chosen parameters](https://www.navixy.com/wp-content/uploads/2023/12/browser_imbnj05cft.png)

](https://www.navixy.com/wp-content/uploads/2023/12/browser_imbnj05cft.png)

## Cómo leer el archivo de datos brutos

Tras seleccionar los parámetros necesarios, haga clic en "Descargar CSV" para descargar el archivo.

- El archivo puede abrirse con cualquier editor de texto o visor de tablas que admita el formato CSV. Las columnas están separadas por comas.
- El nombre del archivo incluye el ID del dispositivo, la etiqueta del rastreador y el intervalo de fecha y hora especificados.
- Cada fila (empezando por la segunda) representa un mensaje enviado desde el dispositivo a la plataforma. La primera fila contiene la hora del mensaje en la zona horaria elegida, seguida de los parámetros seleccionados.

[![Raw data file columns example](https://www.navixy.com/wp-content/uploads/2023/12/nvidia_share_xbgmryofhf.png)

](https://www.navixy.com/wp-content/uploads/2023/12/nvidia_share_xbgmryofhf.png)

Esta herramienta es esencial para el diagnóstico y el análisis, ya que proporciona información detallada sobre los datos del dispositivo.