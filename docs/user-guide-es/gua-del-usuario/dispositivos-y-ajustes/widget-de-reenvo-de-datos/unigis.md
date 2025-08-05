# Unigis

# Unigis

El protocolo de Unigis es un protocolo de reenvío de datos de ubicación entre Navixy y la plataforma TMS desarrollada por la empresa Unigis. Los casos de uso más frecuentes se relacionan con la recopilación en tiempo real de seguimiento GPS y datos de telemática de vehículos por parte de los departamentos de logística de grandes empresas de manufactura y retail. La mayoría de estas empresas están ubicadas en Estados Unidos, México, Colombia, Chile, Argentina, Brasil y España

*Categoría del protocolo: Cumplimiento empresarial*

## ¿Qué es Unigis?

A través de protocolo de retransmisión de Unigis, la información de seguimiento GPS de una flota, los datos se optimizan y comparten entre múltiples servidores, permitiendo la retransmisión de datos entre Navixy y los socios de Unigis.

Al usar el protocolo de Unigis, los usuarios pueden integrarse con cadenas de autoservicio y/o proveedores de productos y servicios dentro de la red Unigis como Walmart, Home Depot y Kimberly Clark. Los datos de la flota podrán ser transmitidos entre todas las partes sin necesidad de acceder a la plataforma de Navixy.

## Información general de Unigis

El protocolo Unigis utiliza el protocolo SOAP para enviar datos XML desde dispositivos de seguimiento a Unigis a través de HTTP como parte de la capa de aplicación OSI. Los datos se envían desde la plataforma Navixy a Unigis cada 5 minutos.

Información enviada a Unigis:

- Fecha y hora
- Longitud
- Latitud
- Altitud
- Velocidad
- Eventos de entrada
- Apertura de puertas
- Botón de pánico
- Apagado de motor
- Robo
- ID externo (Placa/Matricula )

Formato: ASCII

## Configuración de Unigis

### Puesta en marcha

Para iniciar la retransmisión de datos usando el protocolo de Unigis para Navixy, necesitará los siguientes parámetros: 

|     |     |
| --- | --- |
| Parámetro | Descripción |
| Dirección de servidor y puerto de destino | URL del endpoint y el puerto que utiliza Unigis TMS<br><br>Comúnmente:<br><br>- Dirección: `http://unigis2.unisolutions.com.ar/HUB/UNIGIS/MAPI/SOAP/GPS/Service.asmx`<br>- Puerto: `80` |
| Login y contraseña | Su usuario y contraseña de Unigis |
| ID Externo | La placa o matrícula de un vehículo |

Para configurar el reenvío de datos en Unigis, abra la configuración del dispositivo desde el menú principal al presionar el ícono de "engranaje" en la parte inferior izquierda de la pantalla.

- Después haga clic en el widget "Reenvío de datos"
- Selecciones “Administración de retransmisores”
- Esto abrirá una ventana popup donde se le pedirá ingresar los parámetros al seleccionar el botón de +

For the Unigis protocol, input the following information:

- Nombre
  - Ingrese un nombre que le permita identificar fácilmente este retransmisor.
- Protocolo
  - Seleccione el protocolo de Unigs de lista desplegable
- Login y contraseña de Unigis
- Dirección del servidor de destino
  - [http://unigis2.unisolutions.com.ar/HUB/UNIGIS/MAPI/SOAP/GPS/Service.asmx](http://unigis2.unisolutions.com.ar/HUB/UNIGIS/MAPI/SOAP/GPS/Service.asmx)
- Puerto de destino
  - 80

Una pantalla de administración de retransmisión debería ser similar a la siguiente, con el nombre de usuario y la contraseña de Unigis. Asegúrese de que el botón "Habilitado" esté marcado y haga clic en el botón "Guardar" para completar el proceso.

![Types and parameters](https://www.navixy.com/wp-content/uploads/2022/08/pasted-image-0-600x112.png)

A continuación, será necesario vincular el retransmisor al dispositivo en el lado de Unigis. Para hacerlo, seleccione el botón “Vincular” ![link image](https://www.navixy.com/wp-content/uploads/2022/08/image-3.png)

 en el widget de reenvío de datos. Seleccione el retransmisor a conectar y haga clic en “Vincular” a continuación.

Después, agregue el ID del dispositivo en el sistema de terceros, ya sea al hacer clic en el ícono de lápiz o en el campo de ID externo. Este valor deberá ser el número de placa/matrícula del lado de Unigis. Selecciones "Guardar" una vez completado.

### Administración

Para editar o detener la retransmisión de datos, por favor siga los siguientes pasos:

1. Seleccione el ícono de "Lápiz" o haga clic en la caja asociada para editar el ID externo usado para apuntar al dispositivo en el sistema de terceros.
2. Para detener la retransmisión de datos, haga clic en el botón de "Basurero".
3. A continuación, reconozca el cambio en la ventana emergente.
4. Para cambiar la configuración del retransmisor, como el nombre, la información de inicio de sesión o la habilitación, haga clic en "Gestión de retransmisores".

Esto abrirá la ventana de administración del retransmisor. Seleccione la fila para editar y haga clic en el lápiz en la parte superior izquierda o haga doble clic en la fila en cuestión para permitir la edición. Guarde cualquier cambio.

![data forwarding management](https://www.navixy.com/wp-content/uploads/2022/08/pasted-image-0-1-600x96.png)

### Solución de problemas

los datos no se muestran en el sistema de Unigis, verifique que:

- El nombre de usuario y la contraseña para Unigis se ingresaron correctamente.
- La URL se ingresó correctamente.
- El traductor está habilitado.
- La identificación externa coincide con la placa/matrícula en Unigis.