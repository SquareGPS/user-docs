# Etiquetas definidas por el usuario (Galileosky)

Los [Dispositivos Galileosky](https://www.navixy.com/devices/galileosky/), conocidos por su versatilidad y capacidades avanzadas, destacan especialmente por su compatibilidad con etiquetas definidas por el usuario. La mayoría de los dispositivos GPS transmiten un conjunto predefinido de datos, incluida información esencial como coordenadas, altitud, aceleración, kilometraje y detalles específicos del vehículo como el estado del encendido y la temperatura del refrigerante. Sin embargo, estos datos suelen limitarse a los que admite el fabricante, lo que restringe la supervisión de parámetros adicionales.

Con los dispositivos GPS estándar [Dispositivos Galileosky](https://www.navixy.com/devices/galileosky/), especialmente los compatibles con Easy Logic, los usuarios pueden superar estas limitaciones definiendo etiquetas personalizadas, lo que permite la transmisión de una gama más amplia de datos. Esta flexibilidad permite a los usuarios controlar parámetros adicionales que no suelen admitir los dispositivos GPS estándar.

[![Data transfer in Galileosky user tags](https://www.navixy.com/wp-content/uploads/2019/09/configurator_2019-09-28_13-28-39-600x370.png)

](https://www.navixy.com/wp-content/uploads/2019/09/configurator_2019-09-28_13-28-39.png)[![Data transfer in Galileosky user tags](https://www.navixy.com/wp-content/uploads/2019/09/chrome_2019-09-28_13-40-07-600x296.png)

](https://www.navixy.com/wp-content/uploads/2019/09/chrome_2019-09-28_13-40-07.png)

## Ventajas de las etiquetas definidas por el usuario con los dispositivos Galileosky

1. **Transmisión de datos personalizada**: Los usuarios pueden definir parámetros específicos que deben supervisarse y transmitirse, ampliando el alcance más allá del conjunto de datos predefinidos.
2. **Análisis de datos mejorado**: Con Easy Logic, los usuarios pueden realizar operaciones aritméticas con los datos antes de enviarlos al servidor. Esto incluye sumar, promediar o convertir los datos de los sensores en información más significativa.
3. **reportes de datos condicionales**: Se pueden aplicar operaciones lógicas para garantizar que los datos solo se transmitan cuando se cumplan determinadas condiciones, optimizando el uso y la relevancia de los datos.
4. **Recuento e reportes de sucesos**: Los dispositivos Galileosky pueden contar eventos específicos e informar de ellos en tiempo real, proporcionando información crítica para la gestión de flotas o aplicaciones telemáticas.
5. **Acciones automatizadas**: Los dispositivos pueden programarse para realizar acciones específicas, como conmutar salidas o activar alertas, en función de las condiciones predefinidas, que luego se comunican al servidor.

### Aplicaciones prácticas

Con los dispositivos Galileosky e Easy Logic, puede:

- **Operaciones aritméticas**: Puede manipular los datos de los sensores antes de transmitirlos al servidor. Esto incluye sumar, promediar o convertir las lecturas de los sensores en formatos que se adapten mejor a tus necesidades de análisis.
- **Operaciones lógicas**: Transmitir datos solo cuando se cumplan determinadas condiciones, garantizando que los datos recogidos sean pertinentes y se utilicen eficazmente. Esto puede ayudar a optimizar la transmisión de datos y reducir la carga innecesaria de datos.
- **Recuento de eventos**: Realice fácilmente el seguimiento y recuento de eventos específicos basándose en criterios predefinidos. Esta función es especialmente útil para supervisar procesos repetitivos o cíclicos.
- **Acciones automatizadas**: Configure acciones, como la conmutación de salidas, en función de determinadas condiciones y haga que estas acciones se comuniquen al servidor. Esta funcionalidad es ideal para automatizar respuestas a entradas de datos en tiempo real.

## Cómo configurar las etiquetas definidas por el usuario de Galileo con Navixy

### Configurar los dispositivos Galileosky

1. **Instalar el configurador Galileosky**: Comience descargando e instalando el software Galileosky Configurator.
2. **Configuración en Easy Logic**: Utilice Easy Logic para definir las condiciones y operaciones necesarias para sus etiquetas personalizadas. Este proceso implica la creación de scripts dentro del entorno de Easy Logic para configurar los datos que desea supervisar y transmitir.

### Configurar sensores en Navixy

1. Diríjase hasta *Dispositivos y ajustes* en la plataforma Navixy.
2. Ir a *Sensores y botones* y cree un nuevo sensor de medición.
3. Seleccione la entrada adecuada (Etiqueta de usuario), el tipo de sensor y las unidades.
4. Tenga en cuenta que en el Configurador Galileosky, las etiquetas de usuario se numeran del 0 al 7, mientras que en Navixy, se numeran del 1 al 8. Por lo tanto, la etiqueta 0 en el Configurador corresponde a la entrada 1 en Navixy, y así sucesivamente. Por lo tanto, la etiqueta 0 en el Configurador corresponde a la entrada 1 en Navixy, y así sucesivamente.

Como con cualquier otro sensor, puede aplicar ajustes adicionales, como calibración, multiplicadores o umbrales, para refinar la salida de datos.

Una vez configuradas, estas etiquetas definidas por el usuario permiten mejorar las capacidades de supervisión y elaboración de reportes, proporcionando a los usuarios la posibilidad de capturar y analizar datos que van más allá de las limitaciones de los dispositivos GPS estándar.

4. **Configurar el sensor en Navixy**

- **Acción**:
- Cree un nuevo sensor de medición.
- Seleccione la entrada adecuada (etiqueta de usuario), el tipo de sensor y las unidades de medida.
- Tenga en cuenta la diferencia de numeración: las etiquetas de usuario en el Galileosky Configurator se numeran del 0 al 7, mientras que en Navixy, se numeran del 1 al 8. Así, la etiqueta 0 en Galileosky corresponde a la entrada 1 en Navixy. Así, la etiqueta 0 en Galileosky corresponde a la entrada 1 en Navixy, y así sucesivamente.
- **Propósito**: Una configuración correcta garantiza que los datos procesados por Easy Logic de Galileosky se interpreten y muestren correctamente en la plataforma Navixy.

5. **Aplicar ajustes adicionales del sensor**

- **Acción**: Mejora la funcionalidad de tu sensor configurando una tabla de calibración, aplicando multiplicadores para ajustar valores o estableciendo umbrales para filtrar valores atípicos.
- **Propósito**: Estos ajustes adicionales ayudan a refinar los datos para garantizar que sean los más precisos y útiles posibles.

6. **Seguimiento de reportes en Navixy**

- **Acción**: Utilice el widget de lecturas del sensor en Navixy para supervisar los datos en tiempo real. Además, puede generar reportes detallados basados en los datos de los sensores, lo que le proporcionará una visión completa de sus operaciones.
- **Propósito**: Esta integración permite la supervisión continua y el análisis en profundidad de los datos personalizados recopilados por sus dispositivos Galileosky.