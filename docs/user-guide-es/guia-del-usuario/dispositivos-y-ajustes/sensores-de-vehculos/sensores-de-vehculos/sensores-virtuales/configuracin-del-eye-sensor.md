# Configuración del Eye Sensor

Como ejemplo adicional del uso de sensores virtuales, nos gustaría presentarle [Sensores oculares Teltonika](https://teltonika-gps.com/products/accessories/sensors-beacons/eye) que son capaces de registrar datos valiosos como la temperatura, la humedad, el movimiento y el estado de los imanes. La información sobre el estado de movimiento, en particular, no estaba disponible anteriormente, pero ahora se puede acceder a ella mediante el uso de sensores virtuales. Si desea saber más sobre estos sensores y cómo configurarlos para obtener información importante, estaremos encantados de proporcionarle instrucciones detalladas.

### Configuración de sensores en un dispositivo

Para configurar la transmisión de datos del sensor a la plataforma, se recomienda utilizar la función [Configurador Teltonika](https://wiki.teltonika-gps.com/view/Teltonika_Configurator_Introduction). Asegúrese de [descargar la versión](https://wiki.teltonika-gps.com/view/Teltonika_Configurator_versions) que corresponda al firmware y al modelo de dispositivo actuales. Una vez descargado e iniciado el configurador, vaya a la configuración del sistema y seleccione el protocolo de datos Codec 8 Extended.

<figure><img src="https://www.navixy.com/wp-content/uploads/2023/03/1-4.png" alt=""><figcaption><p>Activación del Codec 8 Extendido en el configurador de Teltonika</p></figcaption></figure>

En la sección Bluetooth 4.0, recomendamos desactivar la función de escaneo continuo y ajustar la "Frecuencia de actualización" y la "Duración del escaneo" a cada 30 segundos. Ajustando estas opciones, obtendrás resultados óptimos en el escaneo BLE, garantizando una recopilación de datos fiable y precisa.

<figure><img src="https://www.navixy.com/wp-content/uploads/2023/03/2-4.png" alt=""><figcaption><p>Frecuencia de exploración para sensores BLE</p></figcaption></figure>

A continuación, seleccione la Conexión # y establezca el modo de funcionamiento en Avanzado. De este modo accederá a los ajustes detallados del sensor. Busque los botones situados en la esquina superior derecha y seleccione la lista de preajustes. Esto le permitirá agilizar el proceso de configuración del sensor.

<figure><img src="https://www.navixy.com/wp-content/uploads/2023/03/3-2.png" alt=""><figcaption><p>Configuración del modo Avanzado para el sensor y la ubicación del botón de lista de Pre ajustes</p></figcaption></figure>

Cuando hagas clic en el botón de la lista de pre ajustes, se abrirá una nueva ventana con una selección de los sensores disponibles. Sólo tienes que elegir el que estés utilizando en ese momento, como el **Eye Sensor**. Esta tabla configurará automáticamente todos los ajustes necesarios. Después, navega a la pestaña E/S para configurar la transmisión de datos desde estos sensores dentro de los paquetes de tu dispositivo.

Para configurar la transmisión de datos desde estos sensores dentro de los paquetes de su dispositivo, navegue hasta la pestaña E/S. Aquí, necesitará configurar los parámetros apropiados para su configuración deseada. Por ejemplo, si el número de conexión de su sensor es 1, configure los parámetros con el mismo número. En la mayoría de los casos, es mejor establecer la prioridad en Baja para los parámetros que necesitan ser monitorizados en la plataforma. También es importante asegurarse de que todos los demás ajustes se dejan en sus valores por defecto, a menos que haya cambiado algo previamente. En tales casos, los ajustes recomendados son los siguientes:

* Prioridad = Baja
* Nivel bajo = 0
* Nivel alto = 0
* Sólo evento = No
* Operando = Control

<figure><img src="https://www.navixy.com/wp-content/uploads/2023/03/4-2.png" alt=""><figcaption><p>Configuración del envío de datos de sensores en paquetes de dispositivos</p></figcaption></figure>

### Configuración en la plataforma

#### Sensor de estado de movimiento

La lectura de este sensor es totalmente configurable con sensores virtuales con [el método de cálculo del índice Bit](https://www.navixy.com/docs/user/web-interface-docs/devices-doc/sensors-and-buttons/virtual-sensors/#1679330119395-5e95e66b-c1e9). Los datos del estado de movimiento vienen en el bit 16 del campo BLE 1 Custom 1. La configuración del estado de movimiento requerirá los siguientes pasos:

1. Cree un sensor virtual y especifique su nombre.
2. Seleccione [ID AVL adecuado](https://wiki.teltonika-mobility.com/view/Full_AVL_ID_List#BLE_Sensor_I.2FO_elements) como entrada. Por ejemplo, para BLE 1 Custom 1, utilice el número 331.
3. Defina el Número de Bit que corresponde a los datos de estado de movimiento. En este caso, debe seleccionarse el Bit 16 del campo BLE 1 Custom 1.
4. Defina los nombres de los estados según sea necesario. Por ejemplo, se pueden utilizar "Standstill" y "Moves".
5. Especifique los valores correspondientes, donde 0 indica ausencia de movimiento y 1 indica movimiento registrado por el sensor.

\[![Setting up the Virtual Sensor to read the Eye sensor's motion status.](https://www.navixy.com/wp-content/uploads/2023/03/5-2.png)

]\(https://www.navixy.com/wp-content/uploads/2023/03/5-2.png)

Configuración del sensor virtual para leer el estado de movimiento del sensor ocular.

En este punto, ha recuperado con éxito el estado de movimiento actual. Sin embargo, tenga en cuenta que la información solo se puede obtener en informes y reglas si el estado de movimiento está configurado como encendido.

La obtención de informes y reglas para sensores virtuales no encendidos no está soportada en este momento.

#### Sensores de temperatura y humedad

La configuración de estos sensores es similar a la de los sensores estándar [sensores de medición](https://www.navixy.com/docs/user/web-interface-docs/devices-doc/sensors-and-buttons/measurement-sensor/). Veamos un ejemplo de configuración para cada uno de estos sensores:

El aparato transmite la humedad en %.

* Especifique el nombre del sensor deseado.
* Seleccione la entrada apropiada BLE: Humedad \[N] y especifique su número.
* Seleccione el tipo de sensor Personalizado.
* Especifique la unidad de medida en %.
* No se requieren otros ajustes.

\[![Setting up the BLE humidity sensor.](https://www.navixy.com/wp-content/uploads/2023/03/6-4.png)

]\(https://www.navixy.com/wp-content/uploads/2023/03/6-4.png)

Configuración del sensor de humedad BLE.

El aparato transmite la temperatura en °C.

* Especifique el nombre del sensor deseado.
* Seleccione la entrada adecuada BLE: Temperatura \[N] y especifique su número.
* Seleccione el tipo de sensor Temperatura.
* Especifique la unidad de medida en °C.
* No se requieren otros ajustes.

\[![Setting up the BLE temperature sensor.](https://www.navixy.com/wp-content/uploads/2023/03/7-2.png)

]\(https://www.navixy.com/wp-content/uploads/2023/03/7-2.png)

Configuración del sensor de temperatura BLE.

A partir de las lecturas de los sensores, puede generar un informe de Sensores de medición que proporcione información útil sobre los datos recogidos por el sensor. Además, puede realizar un seguimiento de las lecturas configurando alertas mediante la regla "Parámetro en rango", que le permite recibir notificaciones cuando determinados parámetros quedan fuera de los rangos predeterminados.

Además, se pueden crear sensores virtuales y proporcionar nombres comprensibles para recibir los valores de los sensores en los widgets. Para ello, utilice [el método de cálculo Valor en rango](https://www.navixy.com/docs/user/web-interface-docs/devices-doc/sensors-and-buttons/virtual-sensors/#1679329407451-09b70c96-6385). Esto le permitirá personalizar los datos del sensor que se muestran y facilitar la interpretación de la información que presenta el sensor.

#### Sensor de estado magnético

La configuración de los sensores de estado magnético es un proceso sencillo y directo. De hecho, no se requiere ninguna configuración adicional más allá de conectar los sensores a la plataforma. Los datos del estado del imán se transmiten a la plataforma como campos de estado y se muestran en cuanto se reciben del dispositivo conectado.

Utilización de sensores virtuales con el [Método de cálculo del valor en origen](https://www.navixy.com/docs/user/web-interface-docs/devices-doc/sensors-and-buttons/virtual-sensors/#1679329407460-fa411058-510d) puede personalizar los valores de los campos de estado para que se muestren como "abierto" o "cerrado" y darles nombres fácilmente reconocibles.

Configurando la regla "Valor del campo de estado", puede realizar un seguimiento de los campos de estado y recibir alertas cuando se produzcan eventos específicos.

\[![Example of setting the magnet state sensor with its values and name.](https://www.navixy.com/wp-content/uploads/2023/03/8-2.png)

]\(https://www.navixy.com/wp-content/uploads/2023/03/8-2.png)

Ejemplo de configuración del sensor de estado magnético con sus valores y nombre.

Ha obtenido con éxito la información del sensor Eye y ahora está al alcance de su mano. Ya puedes hacer un seguimiento de estos valiosos datos.
