# Mostrador de pasajeros (Galileosky)

Los [Dispositivos Galileosky](https://www.navixy.com/devices/galileosky/) cuando se integran con los sensores de flujo de pasajeros PP-01, proporcionan una solución robusta para contar el número de pasajeros que entran y salen de los vehículos de transporte público. Esta integración aprovecha la tecnología Easy Logic de Galileosky, lo que permite la recopilación y el análisis avanzados de datos, que pueden supervisarse a través de la plataforma Navixy.

#### Ejemplo de uso

Imagine un operador de autobuses urbanos que necesita hacer un seguimiento del número de pasajeros para optimizar las rutas y mejorar la eficiencia del servicio. Integrando el dispositivo Galileosky con sensores PP-01 y utilizando la plataforma de Navixy, el operador puede supervisar con precisión el flujo de pasajeros, analizar tendencias y tomar decisiones informadas sobre ajustes de rutas y mejoras del servicio.

## Principales características y ventajas

* **Recuento de pasajeros:** El sensor PP-01 conectado al dispositivo Galileosky permite contar con precisión los pasajeros que entran y salen del vehículo.
* **Registro de datos basado en eventos:** Los datos pueden registrarse en función de eventos específicos, como la apertura o el cierre de puertas, para garantizar que los datos de los pasajeros se registran solo durante los momentos pertinentes.
* **Registro de datos acumulativos:** El sistema también puede configurarse para registrar los datos acumulados de los pasajeros, proporcionando un total de pasajeros durante todo el viaje.

## Pasos de la integración

1. **Conecte el sensor PP-01:**

* El sensor PP-01 se conecta al dispositivo Galileosky a través de la interfaz RS485. Asegúrese de que la conexión es correcta siguiendo las instrucciones de cableado suministradas.
* Configure la interfaz RS485 con los siguientes parámetros:
  * Velocidad: 19200 bits/s
  * Bits de datos: 8
  * Bit de parada: 1

2. **Configure el sensor PP-01:**

* Conecte el sensor PP-01 a un PC mediante un adaptador RS485-USB.
* Utilice la Utilidad de Configuración PP-01 para configurar el sensor. Ajuste la dirección del sensor según sea necesario, eligiendo entre el rango de 1 a 8.
* Utilice el Galileosky Configurator para cargar el script Easy Logic adecuado en función del modo elegido (grabación basada en eventos o acumulativa).
* Asegúrese de que la secuencia de comandos se ha cargado y configurado correctamente en el dispositivo Galileosky.

3. **Integración con Navixy:**

* En la plataforma Navixy, navega hasta la sección "Dispositivos y Ajustes" y ve a "Sensores y Botones."
* Cree un nuevo sensor de medición y seleccione la entrada correspondiente a la etiqueta de usuario del dispositivo Galileosky.
* Mapear los datos del sensor PP-01 a la plataforma Navixy, asegurando la correcta correspondencia entre los datos del sensor y la interfaz Navixy.

## Seguimiento e informes

* **Vista en tiempo real.** Una vez integrados, los datos de los pasajeros pueden controlarse en tiempo real mediante el widget "Lecturas de los sensores" dentro del [Widget del objeto](../../../../../seguimiento/lista-de-objetos/vista-detallada-del-objeto.md).
* **Informes.** También puede generar [Reportes](../../../../../reportes/detalles-especficos-del-reporte/reporte-de-los-sensores-de-medicin.md) que incluyen datos sobre el recuento de pasajeros, lo que permite realizar análisis exhaustivos y obtener información sobre el flujo de pasajeros.
