# Geocercas

## Visión general

Las geovallas son perímetros virtuales que permiten al sistema controlar si un objeto ha cruzado el límite de la geovalla ("dentro" o "fuera"). Estos eventos se registran, lo que permite a los usuarios generar informes de geovallas y [recibir alertas](../../reglas-y-alertas/control-de-movimientos/geocerca-de-entrada-o-salida.md). También se pueden asignar geocercas específicas [normas para eventos](../../reglas-y-alertas/) dentro de determinadas zonas, como recibir alertas de exceso de velocidad sólo dentro de una ciudad o a lo largo de una ruta.

![image-20240807-002528.png](../../gua-del-usuario/seguimiento/herramientas-cartogrficas/attachments/image-20240807-002528.png)

### Ver detalles de la geo-valla

Al pulsar el icono "i" (información) junto a una geo-valla, se muestra información detallada sobre la geo-valla seleccionada.

* **Etiquetas**: Las etiquetas asociadas a la geo-valla, como "central", ayudan a clasificar y organizar las geo-vallas para facilitar su identificación y gestión.
* **Ubicación**: La ubicación geográfica de la geo-valla. Por ejemplo: Condado de Queens, Nueva York, Estados Unidos de América.
* **Acontecimientos recientes**: Una lista de eventos recientes relacionados con la geo-valla, como inicios y finales de aparcamiento para el vehículo.

### Acontecimientos recientes dentro de una geo-valla

La lista de eventos recientes proporciona un registro detallado de las actividades dentro de la geo-valla, incluyendo:

* **Tipo de acontecimiento**: El tipo de evento, como "Inicio de aparcamiento" o "Fin de aparcamiento".
* **Objeto**: El objeto rastreado asociado al evento.
* **Ubicación**: La dirección en la que se produjo el suceso, proporcionando detalles precisos para cada actividad.

Esta vista detallada ayuda a los usuarios a supervisar y analizar las actividades dentro de la geo-valla, mejorando la supervisión y la toma de decisiones para la gestión de flotas y la seguridad.

### Objetos rastreados dentro de una geovalla

Haciendo clic con el botón izquierdo del ratón en una geo-valla del mapa, los usuarios pueden ver el número de objetos rastreados dentro de ella. Para acceder a la herramienta Geocercas, haga clic en el icono Polígono de la barra de herramientas del mapa. Aquí puede crear, importar o editar geocercas y mostrar las geocercas deseadas en el mapa marcando las casillas de verificación.

## Tipos de geovallas

Existen tres tipos esenciales de geovallas:

### Geocerca circular

Una geo-valla circular es un área geográfica con un centro determinado y una forma circular con un radio mínimo de 20 metros. Los usuarios pueden definir el radio y el centro del círculo.

### Geocerca poligonal

Una geo-valla poligonal es un área definida por un polígono arbitrario con múltiples vértices (hasta 500), lo que permite la creación de formas complejas. Este tipo de geo-valla es especialmente útil para definir con precisión áreas de forma irregular, como barrios, parques o cualquier zona específica que no quepa en un simple límite circular.

### Geocerca de corredor (ruta)

Una geo-valla de corredor (o, alternativamente, geo-valla de ruta) crea un perímetro virtual entre dos o más puntos. Este tipo de geovalla es especialmente útil para vigilar [cumplimiento de las rutas previstas](../../reglas-y-alertas/programacin-y-expedicin/desviacin-carretera.md) y garantizar que los vehículos no se desvíen de la trayectoria prevista. La geo-valla del corredor está definida por una serie de puntos que crean una ruta continua, con un radio especificado que determina la desviación permitida de la ruta.

![image-20240806-235506.png](../../gua-del-usuario/seguimiento/herramientas-cartogrficas/attachments/image-20240806-235506.png)

## Cómo crear una geo-valla

1. Localice la zona deseada en el mapa utilizando la herramienta "Búsqueda de direcciones".
2. Seleccione la herramienta "Cercas geográficas" haciendo clic en el botón **Cuadrado** en la esquina superior derecha del mapa.
3. Haga clic en el botón "Añadir geo-valla" y seleccione el tipo de geo-valla.
4. Dibuje la geo-valla en el mapa:

* **Círculo**: Mueve el círculo con el ratón, presionando el centro. Cambia el tamaño arrastrando el borde.
* **Polígono**: Empieza con un pentágono y ajústalo arrastrando vértices o añadiendo nuevos.
* **Ruta**: Seleccione los puntos inicial y final. El sistema construirá la ruta. Añade más puntos arrastrando la ruta y ajusta el tamaño de la vecindad.

5. Especifique el nombre de la geo-valla y guárdela. Las geovallas creadas se pueden editar o eliminar.

![](https://squaregps.atlassian.net/wiki/images/icons/grey_arrow_down.png)

Crear una geo-valla de corredor

Siga estos pasos para crear una geo-valla de corredor:

1. **Abra la configuración de Geofence** en la aplicación Seguimiento de la interfaz web.
2. **Seleccione la opción "Nueva geo-valla** para empezar a crear una nueva geo-valla de corredor.
3. **Nombre de la geo-valla** y añada etiquetas relevantes para facilitar su identificación.
4. **Definir el radio** del corredor. Este radio determina cuánto puede desviarse un vehículo o un activo de la trayectoria antes de que se detecte una desviación de la ruta.
5. **Establecer los puntos de ruta**: Añade el punto de inicio, varios puntos intermedios y el punto final de la ruta. Cada punto se define por sus coordenadas geográficas.
6. **Modo manual**: Si es necesario, puede ajustar los puntos manualmente para controlar con precisión la trayectoria de la ruta.

![](https://squaregps.atlassian.net/wiki/images/icons/grey_arrow_down.png)

Creación de geovallas poligonales

Para crear una geo-valla poligonal:

1. Localice la zona deseada en el mapa.
2. Seleccione la herramienta "Geocercas" haciendo clic en el icono cuadrado de la esquina superior derecha del mapa.
3. Haga clic en el botón "Añadir geo-valla" y seleccione "Polígono" como tipo de geo-valla.
4. Inicialmente, la geo-valla aparecerá como un pentágono. Ajusta la forma arrastrando vértices o añadiendo otros nuevos para ajustarla al área deseada.
5. Asigne un nombre a su geo-valla y guárdela. Puede editar o eliminar las geo-vallas creadas según sea necesario.

## Editar los detalles de la geo-valla

Para localizar la función de edición, haga clic en el icono del lápiz situado junto a la geo-valla que desea editar en la herramienta Geo-vallas. Al editar una geo-valla, puede personalizar varios elementos para mejorar la organización y la supervisión:

* **Etiqueta Geofence**: Asigne o edite el nombre de la geo-valla para facilitar su identificación.
* **Etiquetas**: Añada o modifique etiquetas para clasificar y organizar las geo-vallas. Etiquetas como "central" y "oeste" ayudan a clasificar y gestionar varias geovallas.
* **Ubicación**: El campo de ubicación muestra la dirección geográfica de la geo-valla, proporcionando un punto de referencia preciso para el área de la geo-valla.
* **Color**: Cambie el color de la geo-valla para una mejor visualización en el mapa. Esto resulta especialmente útil cuando se gestionan varias geovallas, ya que con colores diferentes se pueden diferenciar rápidamente varias zonas. La herramienta de selección de color permite elegir un color específico y ver su código HEX.

## Importar geocercas

Cuando necesite añadir un gran número de geo-vallas, es más rápido importarlas desde un archivo que crearlas manualmente. Puede importar geocercas desde archivos Excel o KML.

### Importación de geocercas circulares desde Excel

1. Elija la herramienta "Cercas geográficas".
2. Pulse el botón "Importar geovallas circulares".
3. Descargue el archivo de ejemplo proporcionado.
4. Añada información sobre sus geocercas al archivo (etiqueta, dirección, longitud, latitud, radio).
5. Cargue el archivo editado en el servicio de supervisión.
6. Si su fichero tiene cabeceras, active la opción "Utilizar cabeceras del fichero".
7. Verifique los campos de cabecera y haga clic en Siguiente.
8. Compruebe los registros y haga clic en Continuar.
9. Una vez finalizada la importación, las nuevas geo-vallas aparecerán en la lista.

### Importación de geocercas de corredores a partir de KML

1. Elija la herramienta "Cercas geográficas".
2. Pulse el botón "Importar geovallas desde KML".
3. Haga clic en el botón "Examinar" para seleccionar el archivo KML necesario en su ordenador.
4. Cambie el radio por defecto si es necesario.
5. Haga clic en "Cargar".
6. Una vez completada la importación, las nuevas geo-vallas aparecerán en la lista. Tenga en cuenta que el radio por defecto sólo se utiliza para las geovallas de ruta. Para otros tipos, este paso puede omitirse.
