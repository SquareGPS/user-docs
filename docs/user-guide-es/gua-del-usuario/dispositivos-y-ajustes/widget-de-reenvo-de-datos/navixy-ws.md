# Navixy WS

# Navixy Web Service— Protocolo de envío de datos XML

El protocolo de reenvío de datos de Navixy Web Service transmite datos de flotas desde el sistema de Navixy a cualquier sistema de terceros.

*Categoría del Protocolo: Protocolo de consolidación de datos* 

## ¿Qué es Navixy Web Service?

El protocolo de reenvío de datos de Navixy Web Service es flexible, lo que permite a terceros almacenar datos de flotas en sus bases de datos para usarlos con cualquier propósito o para mostrar datos en recursos web.

Dado que este protocolo de reenvío de datos es independiente de la plataforma, sería la opción ideal para cualquier socio que trabaje con archivos XML.

## Información técnica general de Navixy Web Service

El protocolo de Navixy Web Service utiliza SOAP para permitir la extracción de datos XML desde dispositivos de rastreo como parte de la capa de aplicación OSI. Los datos se extraen bajo demanda.

Campos de datos que se envían:

- DateGPS
  - Fecha y hora en UTC
- Ignition
  - Estado de encendido booleano
- Latitud
- Longitud
- SpeedGPS
  - km/h
- UnitPlate
  - Matrícula
- Altitude
  - Metros
- Course
  - Dirección en la que se dirige el vehículo, por ejemplo: N, S, E, O, NO, NE, SO, SE
- DeviceID
  - IMEI
- NumSat
  - Número de satélites GNSS que el dispositivo está utilizando
- Odometer
  - Distancia recorrida en km

## Configuración de Navixy Web Service

### Puesta en marcha

#### Parámetros requeridos de Navixy:

- Usuario y contraseña
  - Esto puede ser cualquier cosa siempre que no esté en uso

Para configurar el reenvío de datos en el protocolo de Navixy Web Service, abra la configuración del dispositivo desde el menú principal presionando el icono de “Engranaje” en la parte inferior izquierda de la pantalla.

Luego, haga clic en el widget de “Reenvío de datos”.

Haga clic en “Gestión de retransmisores”.

Esto abrirá una ventana emergente donde ingresará los parámetros requeridos presionando el botón +.

Para el protocolo de Navixy Web Service, ingrese la siguiente información:

| Parámetro | Explicación |
| --- | --- |
| Nombre | Ingrese un nombre para que este retransmisor sea fácilmente identificable |
| Protocolo y Usuario | Seleccione el protocolo del Navixy Web Service del menú desplegable;<br><br>Use cualquier nombre de usuario y contraseña siempre que no esté ya en uso. |
| Dirección y puerto del servidor de destino | Estos no son necesarios para el protocolo de Navixy Web Service, sin embargo, aún debe completarlos |

Una pantalla de gestión de retransmisión debería verse similar a la siguiente, con el usuario y contraseña de Navixy Web Service. Asegúrese de que el botón "Habilitado" esté marcado y haga clic en el botón "Guardar" para completar el proceso.

![Recurso Confiable](https://www.navixy.com/wp-content/uploads/2022/10/pasted-image-0-4-600x112.png)

A continuación, será necesario vincular el retransmisor al dispositivo en el lado de Unigis. Para hacerlo, seleccione el botón “Vincular” ![link image](https://www.navixy.com/wp-content/uploads/2022/08/image-3.png)

 en el widget de reenvío de datos. Seleccione el retransmisor a conectar y haga clic en “Vincular” a continuación.

No se necesita ID externo para el protocolo de Navixy Web Service.

Seleccione “Guardar” una vez completado.

### Acceso externo:

Parámetros requeridos

- Usuario y contraseña
  - Esto debe coincidir con lo que se ingresó anteriormente
- IDs de los dispositivos
  - Máximo de 100
- Fecha de inicio y final
  - El siguiente es un ejemplo para el 9 de septiembre de 2022 a las 12 am UTC hasta las 11:59:59 UTC:
  - 2022-09-01T00:00:00Z a 2022-09-01T11:59:59Z

La descripción del protocolo en WSDL se puede encontrar a continuación, según la ubicación del servidor:

EU [https://soap.navixy.com/LocationDataService?wsdl](https://soap.navixy.com/LocationDataService?wsdl)

US [https://soap.us.navixy.com/LocationDataService?wsdl](https://soap.us.navixy.com/LocationDataService?wsdl)

Se debe realizar una solicitud SOAP utilizando una de las páginas WSDL anteriores. La solicitud XML en sí es la siguiente, reemplazada con la información asociada:

<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:tem="http://tempuri.org">

   [soapenv:Header](#)

   [tem:authentication](#)

    <login>username</login>

    <password>password</password>

   </tem:authentication>

   </soapenv:Header>

   [soapenv:Body](#)

   [tem:dataRequest](#)

      <!--1 to 100 repetitions:-->

      <deviceIds>IMEI of device</deviceIds>

      <startDate>2022-08-30T00:00:00Z</startDate>

      <endDate>2022-08-31T00:00:00Z</endDate>

   </tem:dataRequest>

   </soapenv:Body>

</soapenv:Envelope>

Un ejemplo de respuesta puede verse algo así:

      <result>

         <dateGps>2022-08-30T00:02:55.000Z</dateGps>

         <ignition>false</ignition>

         <latitude>75.9270866</latitude>

         <longitude>-85.5207616</longitude>

         <speedGps>0.0</speedGps>

         <unitPlate>ss3ssj</unitPlate>

         <altitude>284.0</altitude>

         <course>E</course>

         <deviceId>866258048802349</deviceId>

         <numSat>15</numSat>

         <odometer>59845</odometer>

      </result>

### Administración

Para editar o detener el reenvío de datos, consulte los siguientes pasos:

Para detener el reenvío de datos, haga clic en el botón “Papelera”.

A continuación, confirme el cambio en la ventana emergente.

Para cambiar la configuración del retransmisor, como el nombre, la información de inicio de sesión o habilitado, haga clic en “Gestión de retransmisores.”

Esto abrirá la ventana de gestión de retransmisores. Seleccione la fila para editar y haga clic en el lápiz en la parte superior izquierda, o haga doble clic en la fila en cuestión para permitir la edición. Guarde los cambios realizados.

![Recurso Confiable](https://www.navixy.com/wp-content/uploads/2022/10/pasted-image-0-1-2-600x106.png)

### Solución de problremas

Para verificar y probar su solicitud SOAP a la plataforma, se sugiere usar SoapUI que se puede encontrar aquí: [https://www.soapui.org/downloads/soapui/](https://www.soapui.org/downloads/soapui/)

1. Instale Soap UI
2. Desde el menú archivo, seleccione “Nuevo Proyecto SOAP”
3. Pegue la ruta correcta en el campo WSDL según el servidor y seleccione “¿Crear solicitudes de muestra para todas las operaciones?”
  1. US: [https://soap.us.navixy.com/LocationDataService?wsdl](https://soap.us.navixy.com/LocationDataService?wsdl)
  2. EU: [https://soap.navixy.com/LocationDataService?wsdl](https://soap.navixy.com/LocationDataService?wsdl)