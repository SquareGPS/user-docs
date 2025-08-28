# Geolinks

* [Descripción](geolinks.md#descripcin)
* [Crear geoenlaces](geolinks.md#crear-geoenlaces)
* [Actualizar y compartir Geolinks](geolinks.md#actualizar-y-compartir-geolinks)
* [Incrustación de enlaces](geolinks.md#incrustacin-de-enlaces)

## Descripción

Los Geolinks pueden aplicarse a diversos sectores empresariales e industriales. Por ejemplo, en logística, pueden ofrecer un seguimiento en tiempo real de las entregas, mejorando la información al cliente. Los geoenlaces también permiten controlar las condiciones de transporte, como la temperatura en el transporte refrigerado, crucial para los productos perecederos. La integración de los geoenlaces en los sistemas empresariales facilita el acceso automatizado a los datos, mejorando la eficacia operativa. Los geoenlaces pueden establecerse con una duración determinada, ideal para acceder temporalmente a la información de seguimiento, por ejemplo durante un periodo de entrega, tras el cual el enlace se desactiva automáticamente para garantizar la privacidad y la seguridad. Esta funcionalidad es especialmente útil para el transporte seguro de artículos sensibles o de gran valor, ya que proporciona visibilidad durante un periodo limitado o permanente.

El instrumento se utiliza para mostrar objetos rastreadores en el mapa, con acceso proporcionado por el enlace generado. Ofrece funciones como la configuración del enlace, que incluye el establecimiento de un tiempo de caducidad, la asignación de geovallas, el rastreo y otras opciones adicionales. Básicamente, un geoenlace es una URL generada automáticamente por la plataforma al crear una instancia de geoenlace. A través de este enlace, los usuarios finales pueden obtener acceso temporal o permanente a la interfaz de mapas, opciones de vehículos, etc.

> \[!INFO] Por ejemplo, he aquí un ejemplo de URL de geoenlace generada: `https://tracking.example/ls/#ecdd8c083d52a396ecdd8c083d52a396`

![Geo links](https://www.navixy.com/wp-content/uploads/2024/04/1.png)

_Una lista de geoenlaces en un armario de usuario._

![Geo links](https://www.navixy.com/wp-content/uploads/2024/04/10.png)

_Interfaz de geoenlace para el usuario final proporcionada por la URL generada automáticamente._

Un geoenlace puede asociarse a varios rastreadores, y estos rastreadores se indicarán en el mapa mediante el enlace generado. Hay varias opciones y atributos que se pueden especificar para un rastreador en particular o para todo el geoenlace, como el mapa, la etiqueta de objeto anulada, los atributos del rastreador (velocidad, dirección, etc.), y otros. Vamos a crear un geoenlace de ejemplo para profundizar en más detalles.

## Crear geoenlaces

Para crear un geoenlace, basta con hacer clic en el botón "+", y aparecerá el cuadro de diálogo de creación:

![Geo links](https://www.navixy.com/wp-content/uploads/2024/04/2.png)

El diálogo ofrece un par de opciones para configurar o rellenar:

![Geo links](https://www.navixy.com/wp-content/uploads/2024/04/3.png)

1. **Descripción (opcional)**

Campo de información que sirve para especificar información personalizada adicional sobre el enlace. La longitud máxima es de 100 caracteres.

2. **Seleccionar objetos y datos**

La lista de objetos disponibles por el enlace. Cada objeto tiene la siguiente lista de opciones que deben especificarse al añadir el objeto:

_Objeto_ - La baliza a rastrear.

_Etiqueta_ - La etiqueta específica que se mostrará en la interfaz de geoenlace sobrescribiendo la etiqueta actualmente configurada en el armario.

_Atributos_ - Los atributos del rastreador que se mostrarán en la interfaz de geoenlace. Los atributos incluyen:

* Velocidad
* Dirección
* Estado de los movimientos
* Nombre del conductor
* Número de teléfono
* Nombre del vehículo
* Matrícula
* Estado de la conexión

Utilice el botón de copia para aplicar la misma lista de atributos a todos los demás objetos del geoenlace. Esta función puede ahorrar mucho tiempo al configurar atributos para varios objetos.

![Geo links](https://www.navixy.com/wp-content/uploads/2024/04/4.png)

3. **Configuración del mapa**

_Proveedor de mapas_ - Seleccione el mapa que desea que vean los usuarios finales de su geoenlace mediante el geoenlace generado. La lista de mapas la especifica el proveedor de servicios de la plataforma.

_Duración de la traza_ - El rastro de seguimiento.

Este es el aspecto que podría tener un rastro fijado durante 5 minutos:

![Geo links](https://www.navixy.com/wp-content/uploads/2024/04/5.png)

_Escaleras_ - El zoom del mapa y el ajuste automático de la posición en el movimiento del rastreador múltiple.

_Geofence_ _ajustes_ - Se puede seleccionar mostrar u ocultar las ubicaciones de los rastreadores en función de la posición de la geo-valla. Por ejemplo, seleccionando la opción "Rastrear fuera de la geo-valla", los rastreadores se mostrarán en el mapa sólo cuando estén fuera de las geo-vallas seleccionadas. Esta función puede ser útil para escenarios como envíos o entregas, donde el usuario final no debe ver al rastreador siendo cargado con mercancías antes de partir. Respectivamente, la opción "Rastrear dentro de geovallas" mostrará los rastreadores sólo cuando estén dentro de las geovallas seleccionadas.

![Geo links](https://www.navixy.com/wp-content/uploads/2024/04/7.png)

4. **Validez limitada** - Especifique la duración del enlace. Puede seleccionarse rápidamente entre periodos predefinidos o establecerse un periodo de tiempo personalizado. Si la duración se establece para que comience a partir de un momento futuro, el enlace permanecerá inactivo hasta que llegue ese momento. Deje la opción sin seleccionar para una configuración permanente del geoenlace.
5. **Vista previa** - Compruebe el aspecto del geoenlace configurado desde la interfaz web de geoenlace desde la perspectiva del usuario final. La función de vista previa permite cambiar rápidamente entre las interfaces de usuario y de geoenlace para obtener una representación más precisa de la configuración del geoenlace.

Tras pulsar el botón "Crear", aparece un diálogo emergente con el enlace generado. El enlace puede copiarse y facilitarse a los usuarios finales o compartirse a través de los botones de las redes sociales:

![Geo links](https://www.navixy.com/wp-content/uploads/2024/04/9-1.png)

## Actualizar y compartir Geolinks

Cualquier actualización de un geoenlace conserva la URL generada. Si hay que cambiar la URL, hay que volver a crear el geoenlace.

Para editar un enlace geográfico, selecciónelo y utilice el botón del lápiz situado en la parte superior de la tabla, o pase el ratón por encima del enlace y aparecerán botones adicionales junto con el botón del lápiz:

![Geo links](https://www.navixy.com/wp-content/uploads/2024/04/11.png)

Para compartir un enlace geográfico existente, pase el ratón por encima del enlace (o seleccione la casilla de verificación) y pulse el botón "Compartir":

![Geo links](https://www.navixy.com/wp-content/uploads/2024/04/12.png)

Para desactivar un geoenlace, selecciónelo mediante la casilla de verificación y pulse el botón Desactivar en la parte superior de la lista:

![Geo links](https://www.navixy.com/wp-content/uploads/2024/04/13.png)

Volver a activar el geoenlace se hace desde el menú de la barra lateral:

![Geo links](https://www.navixy.com/wp-content/uploads/2024/04/14.png)

## Incrustación de enlaces

Los enlaces incrustables son una herramienta muy útil para la integración de interfaces y el desarrollo web. Los geoenlaces ofrecen la capacidad de generar y ajustar código incrustable iframe que puede reutilizarse para las necesidades de creadores e integradores.

Para acceder al código de incrustación, seleccione un geoenlace y desplácese al menú de la barra lateral derecha. En el menú, busque el botón "<>" y haga clic en él:

![Geo links](https://www.navixy.com/wp-content/uploads/2024/04/15.png)

![Geo links](https://www.navixy.com/wp-content/uploads/2024/04/16-1.png)

La anchura y la altura del elemento iframe pueden ajustarse directamente en la ventana "Incrustar enlace".
