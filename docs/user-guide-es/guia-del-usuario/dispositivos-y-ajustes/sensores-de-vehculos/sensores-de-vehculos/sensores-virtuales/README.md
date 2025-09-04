# Sensores virtuales

Los sensores virtuales le permiten procesar los datos de telemetría con mayor eficacia. Al mapear la tensión de la placa, pueden ayudarle a calcular las horas del motor en función de las condiciones y los valores establecidos. Además, permiten convertir múltiples puntos de datos de distintos sensores conectados a un dispositivo en indicadores más fáciles de entender, como "caliente", "frío", "abierto" y "cerrado", independientemente del fabricante o modelo del dispositivo. Esto abre nuevas posibilidades de supervisión, seguimiento y predicción del rendimiento de tecnologías complejas.

<figure><img src="https://www.navixy.com/wp-content/uploads/2024/03/browser_clvf66ikbi.png" alt=""><figcaption><p>Interfaz de sensor virtual</p></figcaption></figure>

### Cómo crear un sensor virtual

El sensor virtual puede crearse a través del portlet "Sensores y botones" situado en la pestaña Dispositivos y configuración:

1. Entra en la sección de dispositivos y ajustes.
2. Selecciona un rastreador GPS.
3. Haz clic en "+".
4. Seleccione la opción "Sensor virtual".

Cada dispositivo puede tener hasta 100 sensores virtuales.

<figure><img src="https://www.navixy.com/wp-content/uploads/2024/03/browser_73sv6rayqh.png" alt=""><figcaption><p>Sensor virtual añadiendo en widget de sensores y botones</p></figcaption></figure>

Los pasos siguientes dependen del caso de uso que deba resolverse mediante el sensor virtual. A continuación encontrará ejemplos e instrucciones para diferentes métodos de cálculo.

### Métodos de cálculo

Los sensores virtuales tienen tres tipos de cálculo diferentes:

* Valor en rango.
* Valor de la fuente.
* Índice de bits.

Todos los valores de los sensores virtuales deben coincidir con la forma en que se reciben del dispositivo. Todos los estados son sus definiciones para estos valores.

A continuación describimos cómo funcionan los distintos métodos de cálculo. Haga clic en el nombre del método de cálculo para ampliarlo.

#### **Valor en rango**

Este tipo de sensor virtual ayuda a nuestros clientes a mantener parámetros importantes como el encendido virtual, la temperatura, la humedad y el nivel de combustible dentro de un rango especificado.

Funciona así:

* si el valor del sensor está dentro de los límites especificados, es 1 para la plataforma. Y 1 es igual a su valor A.
* si el valor del sensor esta fuera de estos marcos el valor del sensor virtual es 0 para la plataforma. Y 0 es igual a su valor B.

#### Ejemplo de encendido virtual

Si no dispone de una entrada de encendido o su dispositivo ya está funcionando a pleno rendimiento, puede utilizar una herramienta de encendido virtual para detectar el estado de encendido. El voltaje a bordo del coche aumentará significativamente cuando se encienda el motor, lo que permite utilizar el umbral de voltaje como indicador de si el motor está en marcha o no. Por lo general, la tensión de a bordo debe superar los 13,2 V para indicar que el motor está funcionando.

Para crear este sensor:

1. Empieza por darle un nombre.
2. Ajuste la entrada a Tensión de placa, o a cualquier otro sensor si es necesario.
3. Activar "Considerar como estado de ignición" en los ajustes.
4. Seleccione "Valor en rango" como método de cálculo.
5. Especifique un valor de rango mínimo, como 13,2 V. El máximo no es necesario ya que el voltaje de la placa puede variar con el encendido activado.
6. Por último, establece el significado de los estados 0 y 1, que suelen ser Encendido y Apagado respectivamente.

<figure><img src="https://www.navixy.com/wp-content/uploads/2024/03/browser_7qx9prhhxc.png" alt=""><figcaption><p>Ejemplo de configuración para el encendido virtual</p></figcaption></figure>

Una vez establecido el rango de umbral de tensión, si el valor entrante a bordo se encuentra dentro de ese rango, la plataforma cambiará el estado de encendido a "encendido". Por el contrario, si está fuera de ese rango, pasará a "apagado". El encendido virtual creado mediante este método también se tendrá en cuenta en informes y notificaciones basados en su estado; por ejemplo, puedes utilizarlo para generar informes de horas de motor o alertas por ralentí excesivo.

Además, este encendido se utilizará para la detección de viaje y aparcamiento con consideración de encendido.

#### Ejemplo con un sensor analógico

Este ejemplo es similar al anterior, pero en lugar de controlar el encendido del vehículo, controla la temperatura.

Supongamos que dispone de un sensor analógico que recoge datos de temperatura: digamos que emite 1020 para -10°C, y 1900 = 0°C. Los datos procedentes de los sensores analógicos no están calibrados, por lo que también deben especificarse de esta forma para el sensor virtual.

Podemos establecer nuestro rango: todo lo que esté entre 1020 y 1900 se clasificaría como "frío" (1) y todo lo que esté por encima de 1900 se consideraría "caliente" (0).

<figure><img src="https://www.navixy.com/wp-content/uploads/2024/03/browser_kgzvrsdzb1.png" alt=""><figcaption><p>Ejemplo de configuración para leer la temperatura del sensor analógico</p></figcaption></figure>

#### **Fuente valor**

Con los sensores virtuales, puede asignar su definición a cualquier valor recibido. Este método funciona con conjuntos predefinidos de valores y cadenas, lo que facilita el trabajo con valores estáticos sin tener que especificar diferentes rangos. Además, puede trabajar con cualquier dato que necesite. Por ejemplo:

* 0/1,
* verdadero/falso,
* encendido/apagado,
* abrir/cerrar,
* armado/desarmado,
* estado 1/estado 2/estado 3,
* tecla 1/tecla 2/tecla 3, etc.

El modo funciona así:

* cuando entra el valor 1, ese es tu valor A;
* cuando entra el valor 2, ese es tu valor B;
* y cuando llega el valor 3, ese es tu valor C y así sucesivamente.

Ilustremos este tipo de funcionalidad con un ejemplo concreto.

#### Ejemplo con lecturas CAN de coche

Algunos sensores CAN pueden proporcionar diferentes valores numéricos a una plataforma. Por ejemplo, tenemos un camión con CAN: sensor de estado de la TDF que puede emitir sólo los siguientes valores:

* 0 - Desactivado
* 1 - Mantener
* 2 - Retención remota
* 3 - En espera
* 4 - Standby remoto
* 5 - Conjunto
* 6 - Desacelerar
* 7 - Curriculum vitae
* 8 - Acelerar

Para configurar dicho sensor:

1. Especifique su nombre.
2. Elige la entrada.
3. Considere como ignición debe estar apagado.
4. Seleccione "Valor fuente" como método de cálculo.
5. Rellena la tabla con tus propios valores en la parte izquierda y los valores de sus respectivos sensores en la derecha. Añade filas haciendo clic en el signo "+" y elimínalas con el botón de la papelera.

<figure><img src="https://www.navixy.com/wp-content/uploads/2024/03/browser_xlxdl1ak9e.png" alt=""><figcaption><p>Ejemplo de configuración del método de cálculo del valor de la fuente</p></figcaption></figure>

#### Lecturas clave de hardware para conductores, equipos y remolques

Algunos dispositivos pueden ser capaces de leer conductores y sus iButtons, llaves RFID o equipos conectados mediante sensores Bluetooth al dispositivo. La plataforma puede detectar el equipo o conductor más cercano al dispositivo, y el Sensor Virtual es capaz de mostrar dichos nombres.

La forma más sencilla de identificación es a través de etiquetas - cada unidad conectada a un equipo pesado tiene su propio sensor con una etiqueta adjunta, que es reconocida por la plataforma como una clave de hardware. Cuando se conecta a la máquina, esta clave se envía a la plataforma y su nombre asociado puede mostrarse de forma comprensible - de forma similar a como se nombraron los valores para la toma de fuerza.

<figure><img src="https://www.navixy.com/wp-content/uploads/2024/03/browser_vw7hkgdl0n.png" alt=""><figcaption><p>Ejemplo de configuración del método de cálculo del valor de origen para la lectura de la llave hardware o del sensor de campo de estado</p></figcaption></figure>

#### **Índice de bits**

Algunos dispositivos pueden proporcionar datos avanzados en sus paquetes, a veces fusionando varios parámetros [en un valor](https://www.navixy.com/blog/sensor-parameters-avl/). La herramienta **Sensores virtuales** permite trabajar con partes de valores telemáticos, descodificando así los datos transmitidos por el hardware GPS.

Por ejemplo, digamos que se transmite el valor 011 - primero debemos leer esta información en little endian según el protocolo:

* 1 - Muestra el estado del cinturón del conductor: 0 - abrochado, 1 - desabrochado. Bit 0
* 1 - Muestra el estado de la puerta del conductor: 0 - cerrada, 1 - abierta. Bit 1
* 0 - Indica el estado de la campana: 0 - cerrada, 1 - abierta. Bit 2

Cada posición del parámetro muestra el valor de diferentes sistemas del vehículo. Para configurarlos y mostrarlos, es necesario crear un sensor por separado para cada parámetro.

Para un sensor que muestre el estado del capó del coche en nuestro ejemplo, es necesario

1. Establezca el nombre del sensor.
2. Elija la entrada según la documentación del aparato.
3. Seleccione "Índice de bits" como método de cálculo
4. Elija el bit 2 para este campo.

A continuación se muestra un ejemplo de un sensor que muestra el estado del capó del coche.

<figure><img src="https://www.navixy.com/wp-content/uploads/2024/03/browser_2qcam8zclk.png" alt=""><figcaption><p>Ejemplo de configuración del sensor de cálculo del índice de bits</p></figcaption></figure>

Una vez que se ha configurado un sensor virtual y su sensor de dispositivo asociado ha proporcionado datos, estos pueden verse en el widget **Lecturas del sensor** de la pestaña **Información** del dispositivo. Los sensores de tu dispositivo ya pueden hablar en tu idioma.
