# Visualización de nuevos atributos calculados en la plataforma Navixy

Los nuevos atributos calculados dentro del nodo **Iniciar Atributo** se pueden monitorear igual que los atributos de datos reales que provienen de los dispositivos en el **Analizador de flujo de datos** y el módulo **Seguimiento**. Mientras que el **Analizador** los muestra de forma nativa, para mostrar los nuevos atributos en el módulo **Seguimiento**, necesita agregarlos primero como atributos personalizados a los dispositivos.

Después de crear atributos calculados en el nodo **Iniciar Atributo**, puede hacer uso adicional de ellos en la plataforma Navixy de dos formas principales:

* A través del **Analizador de flujo de datos** para solución de problemas
* Agregándolos como **atributos personalizados** a sus dispositivos para seguimiento continuo

Para producir valores reales, los atributos calculados deben cumplir los siguientes requisitos previos:

1. El flujo que los contiene debe guardarse con una configuración actualizada del nodo **Iniciar Atributo**.
2. El nodo **Iniciar Atributo** debe estar conectado a al menos 1 nodo **Punto de Salida**.
3. El dispositivo debe estar enviando datos activamente a través del flujo.

### Monitoreo de atributos calculados en el Analizador de flujo de datos

Todos los nuevos atributos de datos calculados dentro de un flujo aparecen automáticamente en el **Analizador de flujo de datos** tan pronto como se reciben y procesan datos reales a través del flujo. Esto le permite verificar cálculos y solucionar problemas en tiempo real.

Para monitorear atributos calculados en **Analizador de flujo de datos**:

1. Cree un atributo en un nodo **Iniciar Atributo**.\
   Para este ejemplo, tomemos una fórmula simple para convertir temperatura de C° a F° y guardarla en un atributo con el nombre _temperatureF_.
2. Asegúrese de conectar este **Iniciar Atributo** a un nodo **Punto de Salida**.
3. Haga clic en para abrir el Analizador.
4. Seleccione un dispositivo que envíe datos al nodo **Iniciar Atributo** que contiene el atributo de interés de la lista **Dispositivos**.
5. Encuentre el atributo en la tabla y monitoree sus valores. Para nuestro ejemplo, debería verse así:

Si su atributo calculado no aparece en **Analizador de flujo de datos**, verifique que:

* El flujo esté habilitado y guardado correctamente
* El dispositivo esté enviando datos (verifique que otros atributos se estén actualizando)
* Las conexiones del nodo **Iniciar Atributo** sean correctas
* El nombre del atributo esté escrito correctamente en la configuración del nodo

Para más detalles sobre solución de problemas con datos en tiempo real, consulte [Analizador de flujo de datos](https://squaregps.atlassian.net/wiki/spaces/UDOCES/pages/3232334554/Analizador+de+flujo+de+datos?atlOrigin=eyJpIjoiYzEzNmMyYjY5MmJjNGNhN2JhZmRmNTNhNjdmZmJmOGYiLCJwIjoiYyJ9).

### Agregar atributos personalizados a objetos en la plataforma Navixy

Los nuevos atributos de datos calculados de los flujos de IoT Logic se pueden usar como sensores virtuales para dispositivos reales en su cuenta y mostrarse en el [Widget de objeto](https://squaregps.atlassian.net/wiki/spaces/UDOCES/pages/2922547998/Vista+detallada+del+objeto?atlOrigin=eyJpIjoiMzk2MWYxOGI1MDA2NDFhMTkwY2NkMTU1MDU2Mzc4Y2UiLCJwIjoiYyJ9) y la [Lista de objetos](https://squaregps.atlassian.net/wiki/spaces/UDOCES/pages/2922547887/Lista+de+objetos?atlOrigin=eyJpIjoiOTEzOTJhNTJmZWQ1NDllMjhiYmZmMTU1ZWZhOTJkYjMiLCJwIjoiYyJ9). Esto le permite monitorear métricas agregadas junto con lecturas reales del dispositivo en un solo lugar, lo que amplía significativamente sus posibilidades de [Seguimiento](https://squaregps.atlassian.net/wiki/spaces/UDOCES/pages/2922547869/Seguimiento?atlOrigin=eyJpIjoiZTVmMDJiNTI4ZDVkNDM3YWFkNDg2MmY1NDczNzNjNGIiLCJwIjoiYyJ9).

Para hacer visibles los atributos calculados en el módulo [Seguimiento](https://squaregps.atlassian.net/wiki/spaces/UDOCES/pages/2922547869/Seguimiento?atlOrigin=eyJpIjoiZTVmMDJiNTI4ZDVkNDM3YWFkNDg2MmY1NDczNzNjNGIiLCJwIjoiYyJ9) junto con los datos regulares del dispositivo, necesita agregarlos como sensores virtuales a sus dispositivos. Esto le permite:

* Monitorear métricas calculadas en el [widget de objeto](https://squaregps.atlassian.net/wiki/spaces/UDOCES/pages/2922547998/Vista+detallada+del+objeto?atlOrigin=eyJpIjoiMzk2MWYxOGI1MDA2NDFhMTkwY2NkMTU1MDU2Mzc4Y2UiLCJwIjoiYyJ9)
* Agregar cálculos importantes a la [lista de objetos](https://squaregps.atlassian.net/wiki/spaces/UDOCES/pages/2922547887/Lista+de+objetos?atlOrigin=eyJpIjoiNzc3ZGFkMzA2OTc3NGIyNmFiMDNmOGVkMjFkMDRlZWMiLCJwIjoiYyJ9) para acceso rápido
* Incluir valores calculados en [reportes](https://squaregps.atlassian.net/wiki/spaces/UDOCES/pages/2922549954/Reportes?atlOrigin=eyJpIjoiNjdmYjU4MTc3Mzc1NDAzM2IxYzUzMmNmZGRmMTAzZDYiLCJwIjoiYyJ9)
* Crear [reglas y alertas](https://squaregps.atlassian.net/wiki/spaces/UDOCES/pages/2922548483/Reglas+y+Alertas?atlOrigin=eyJpIjoiOTVhYTZlOTBmMTc5NGUwNTg4ODU2MTc3M2ViMzg3MGQiLCJwIjoiYyJ9) basadas en valores calculados

#### Crear un atributo personalizado para un dispositivo

Un sensor personalizado debe agregarse individualmente a cada dispositivo. Para agregar el mismo atributo a múltiples dispositivos, repita estos pasos para cada uno de ellos.

1. Vaya al menú **Dispositivos** en la barra lateral izquierda.
2. Seleccione el dispositivo al que desea agregar un nuevo sensor.
3. Haga clic en en la sección **Sensores y botones**, luego seleccione una de las opciones:
   1. **Sensor de medición/Lógica de IoT-** solo para atributos numéricos, como velocidad, temperatura, etc.
   2. **Sensor virtual/Lógica de IoT** - para cualquier otro valor de atributo no numérico.
4. Complete los siguientes campos en la pestaña **Main**:
   1. **Etiqueta**\
      Ingrese un nombre para su sensor. Se mostrará en el **widget de objeto**. La etiqueta puede ser la misma que el nombre del atributo en IoT Logic.
   2. **Parámetro**\
      Encuentre y seleccione el atributo personalizado necesario de la lista de parámetros disponibles. Los atributos de IoT Logic están separados visualmente de la lista estándar de parámetros de Navixy agregando el prefijo "IoT: {atributo}" (como "CAN:" o "OBD:")
   3. **Tipo de sensor**\
      Encuentre y seleccione el tipo apropiado según la naturaleza del atributo: **Combustible**, **Temperatura**, etc. Puede usar **Personalizado** si no hay un tipo adecuado para su atributo.
   4. **Unidades**\
      Seleccione las unidades de medida apropiadas según la naturaleza de su atributo. Las opciones en esta lista varían dependiendo del **tipo de sensor** seleccionado. Puede usar **Custom** si no hay una unidad adecuada para su atributo.
5. (Opcional) Vaya a la pestaña **Calibración** y configure la calibración si es necesario.\
   Para instrucciones sobre la configuración de esta pestaña, consulte [Calibración](https://squaregps.atlassian.net/wiki/pages/createpage.action?spaceKey=UDOCES\&title=Measurement%20sensors\&linkCreation=true\&fromPageId=3383984173).
6. Haga clic en **Guardar** para completar el proceso de configuración.

Después de guardar, el nuevo parámetro personalizado aparece automáticamente en el bloque de datos **Sensores** del **widget de objeto**. Por ejemplo, agregamos un parámetro personalizado **TempDelta**:

#### Agregar un atributo personalizado a la lista de objetos

El **widget de objeto** ofrece un mecanismo de **Favoritos** que permite mostrar una selección de entradas de bloques de datos en la **lista de objetos**, justo debajo de la etiqueta de un objeto. También se aplica a parámetros personalizados del bloque de datos **Sensores**.

Para mostrar directamente sus atributos calculados en la **lista de objetos**:

1. Abra el **widget de objeto** que contiene su atributo personalizado.
2. Encuentre su atributo personalizado en el bloque de datos **Sensores**.
3. Haga clic en el ícono de estrella junto al atributo para agregarlo a **Favoritos**.
4. El atributo ahora aparecerá en la **lista de objetos** bajo el nombre del objeto.

Para instrucciones sobre cómo mostrar un parámetro en la **lista de objetos**, consulte [Widget de objeto - Favoritos](../../../../../guia-del-usuario/seguimiento/lista-de-objetos/vista-detallada-del-objeto.md#favoritos).
