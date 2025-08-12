# Wialon IPS

# Wialon IPS

Wialon IPS es un protocolo de reenvío de datos genérico y de acceso público de Gurtam para retransmitir rastreadores GPS y GLONASS personales y de vehículos que transfieren datos a servidores de monitoreo por satélite/recursos de terceros.

*Categoría del Protocolo: Consolidación de datos*

## ¿Qué es Wialon IPS?

El protocolo de reenvío de datos Wialon IPS se puede usar para reenviar datos de flotas/rastreadores de vehículos entre dos servidores Navixy (por ejemplo, si tiene versiones ServerMate y On-Premise).

Esto es ideal para socios con dispositivos conectados a Wialon que deseen que esos datos se envíen a Navixy. Los datos reenviados pueden incluir información sobre: posicionamiento del vehículo, monitoreo de combustible, sensores, temperatura, etc.

## Información técnica general de Wialon IPS

El protocolo Wialon IPS utiliza la capa de transporte TCP para enviar datos ASCII al servidor de terceros, recibir datos de terceros o enviar a un servidor Navixy separado para un procesamiento adicional de los datos.

Datos enviados a Wialon IPS:

- Fecha y hora
- Latitud
- Longitud
- Altitud
- Velocidad
- Satélites
- Entradas
- Salidas
- Sensores analógicos
- Millaje
- Nivel de batería
- ID del conductor
- Eventos

## Configuración de Wialon IPS

### Puesta en marcha

Para configurar el reenvío de datos para el protocolo Wialon IPS, abra la configuración del dispositivo desde el menú principal, presionando el ícono de “Engranaje” en la parte inferior izquierda de la pantalla..

Luego, haga clic en el widget de “Reenvío de datos”.

Haga clic en “Gestión de retransmisores”.

Esto abrirá una ventana emergente donde ingresará los parámetros requeridos presionando el botón +.

Para el protocolo Wialon IPS, ingrese la siguiente información:

- Nombre
  - Ingrese un nombre para identificar fácilmente este retransmisor.
- Protocolo
  - Seleccione el protocolo Wialon IPS del menú desplegable.
- Dirección del servidor de destino
  - Servidor de terceros.
  - Navixy A a Navixy B.
    - En A, ingrese la dirección del servidor para B
  - Si se recibe de Wialon
    - Dominio de la UE: [tracker.navixy.com](http://tracker.navixy.com)
    - Dominio de EE. UU.: [tracker.us.navixy.com](http://tracker.us.navixy.com)
- Puerto de destino
  - Información relacionada del servidor de terceros.
  - Navixy A a Navixy B, y de Wialon IPS.
    - 47768

Una pantalla de gestión de retransmisión debería verse similar a la siguiente, no se necesita contraseña. Asegúrese de que el botón "Habilitado" esté marcado y haga clic en el botón "Guardar" para completar el proceso.

![Wialon IPS setup](https://www.navixy.com/wp-content/uploads/2022/10/wialon-ips.png)

A continuación, será necesario vincular el retransmisor al dispositivo en el lado de Unigis. Para hacerlo, seleccione el botón “Vincular” ![link image](https://www.navixy.com/wp-content/uploads/2022/08/image-3.png)

 en el widget de reenvío de datos. Seleccione el retransmisor a conectar y haga clic en “Vincular” a continuación.

No se necesita ID externo para el protocolo Wialon IPS.

Seleccione “Guardar” una vez completado.

Nota:  
Si se reciben datos de Wialon IPS, será necesario crear un dispositivo compatible con Wialon IPS en la plataforma Navixy, como Bitrek.

### Gestión

Para editar o detener el reenvío de datos, consulte los siguientes pasos:

Para detener el reenvío de datos, haga clic en el botón “Papelera”.

A continuación, confirme el cambio en la ventana emergente.

Para cambiar la configuración del retransmisor, como el nombre, la información de inicio de sesión o el habilitado, haga clic en “Gestión de retransmisores”.

Esto abrirá la ventana de gestión de retransmisores. Seleccione la fila para editar y haga clic en el lápiz en la parte superior izquierda, o haga doble clic en la fila en cuestión para permitir la edición. Guarde los cambios realizados.

![Wialon IPS management](https://www.navixy.com/wp-content/uploads/2022/10/wialon-ips-management.png)

### Solución de problemas

Si los datos no se muestran en el sistema de terceros Wialon IPS o en la plataforma Navixy, verifique:

- La URL se ingresó correctamente con el puerto asociado.
- El retransmisor está habilitado.