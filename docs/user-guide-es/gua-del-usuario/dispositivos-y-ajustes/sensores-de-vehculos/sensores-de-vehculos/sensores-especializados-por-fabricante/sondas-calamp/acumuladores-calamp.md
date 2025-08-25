# Acumuladores CalAmp

Los [Dispositivos CalAmp](https://www.navixy.com/devices/calamp/) están equipados con acumuladores (variables) que almacenan diversos tipos de datos, en función de cómo se haya configurado el dispositivo, el usuario.

Para agilizar la integración y el uso de estos acumuladores en la plataforma Navixy, se ha introducido un widget específico. Este widget permite a los usuarios configurar y recuperar fácilmente los datos de los siguientes acumuladores:

## Acumuladores compatibles

* **Tensión de la placa**: Supervisa el nivel de voltaje de la placa interna del dispositivo, que es crucial para evaluar la salud y el estado de alimentación del dispositivo.
* **Sensores de temperatura externos (1-8)**: Captura datos de hasta 8 sensores de temperatura externos conectados al dispositivo CalAmp, lo que permite una supervisión detallada de las condiciones ambientales.
* **Kilometraje de hardware**: Estos son los datos de kilometraje calculados directamente por el propio dispositivo, proporcionando una medida precisa de la distancia recorrida basada en la entrada de hardware en lugar de sólo los datos del GPS.
* **Valores de los sensores analógicos (1-8)**: Recupera lecturas de hasta 8 sensores analógicos conectados al dispositivo, lo que permite monitorizar una amplia gama de entradas, como presión, humedad u otras señales analógicas.
* **IO\_States (Estados de entrada/salida)**: Muestra el estado de los canales de entrada y salida del dispositivo, esencial para comprender la interacción en tiempo real entre el dispositivo y los periféricos conectados.
* **iButton ID (Partes baja y alta)**: Captura el identificador único de los dispositivos iButton en dos partes (baja y alta), que se suele utilizar para la identificación de conductores o el control de acceso en aplicaciones de gestión de flotas.

## Configuración de los acumuladores CalAmp en Navixy

Para configurar y supervisar estos acumuladores en la plataforma Navixy, siga estos pasos:

1. Acceda a la sección "Dispositivos y ajustes“.
2. Seleccione el dispositivo CalAmp deseado.
3. Abra el widget Acumuladores. Puede seleccionar qué acumuladores desea monitorizar. Dependiendo de sus necesidades, puede habilitar la monitorización del voltaje de la placa, los sensores de temperatura externos, el kilometraje del hardware, los valores de los sensores analógicos, los estados de E/S y las partes de ID de iButton.
4. Guarde la configuración.

## Control de los datos del acumulador

Una vez configurados, puede ver los datos en tiempo real de los acumuladores seleccionados directamente en la plataforma Navixy. Estos datos pueden utilizarse para diversos fines de supervisión y elaboración de informes, en función de sus necesidades operativas.

## Aplicaciones prácticas

* **Gestión de flotas**: Controla el kilometraje del hardware para realizar un seguimiento preciso de las distancias y programar el mantenimiento.
* **Control medioambiental**: Utilice sensores de temperatura externos para realizar un seguimiento de las condiciones ambientales en el interior de la carga o alrededor de los vehículos.
* **Identificación del conductor**: Implemente la supervisión iButton ID para garantizar que solo el personal autorizado maneja sus vehículos.
* **Supervisión de entradas analógicas**: Realice el seguimiento de varias entradas analógicas para aplicaciones especializadas, como la supervisión de niveles de fluidos o la presión en depósitos.
