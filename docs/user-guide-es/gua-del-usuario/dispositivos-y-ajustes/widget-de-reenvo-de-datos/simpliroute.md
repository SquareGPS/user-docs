# simpliroute

## Simpliroute

## SimpliRoute

SimpliRoute es un protocolo de retransmisión de datos que entrega datos de seguimiento de vehículos para que los usuarios envíen información desde su sistema a SimpliRoute.

_Categoría del Protocolo: Cumplimiento empresarial_

### ¿Qué es SimpliRoute?

SimpliRoute es un protocolo de retransmisión de datos que entrega datos de ubicación de vehículos y los vincula al sistema de pedidos de SimpliRoute. Esto permite a los usuarios la capacidad de rastrear pedidos que se gestionan dentro de este software y que se sincronizan con las posiciones de los vehículos obtenidas.

Este protocolo de retransmisión de datos es ideal para los usuarios que buscan cumplir con el reenvío de datos de Simpliroute para rastrear la ubicación de los vehículos.

### Información técnica general de SimpliRoute

El protocolo SimpliRoute utiliza el método POST para enviar datos JSON a través de HTTP a los servidores de SimpliRoute para su posterior procesamiento de datos.

Datos enviados a SimpliRoute:

* VIN del vehículo
* Matrícula
* Latitud
* Longitud
* Fecha/Hora
* Velocidad
* Ignición
* Proveedor de GPS - número de identificación fiscal especificado en la información del usuario

### Configuración SimpliRoute

#### Puesta en marcha

Parámetros requeridos

* Vehículo construido con matrícula y VIN asociados según los estándares [aquí](https://www.navixy.com/docs/user/web-interface-docs/fleet/).

Para configurar el reenvío de datos para el protocolo SimpliRoute, abra la configuración del dispositivo desde el menú principal presionando el icono de “Engranaje” en la parte inferior izquierda de la pantalla.

Luego, haga clic en el widget de “Reenvío de datos”.

Haga clic en “Gestión de retransmisores”.

Esto abrirá una ventana emergente donde ingresará los parámetros requeridos presionando el botón +.

Para el protocolo SimpliRoute, ingrese la siguiente información:

| Parámetro                                  | Explicación                                                                                                                                                                                         |
| ------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Nombre                                     | <p>- Dirección: <a href="http://unigis2.unisolutions.com.ar/HUB/UNIGIS/MAPI/SOAP/GPS/Service.asmx">http://unigis2.unisolutions.com.ar/HUB/UNIGIS/MAPI/SOAP/GPS/Service.asmx</a><br>- Puerto: 80</p> |
| Protocolo                                  | Seleccione el protocolo SimpliRoute del menú desplegable                                                                                                                                            |
| Dirección y puerto del servidor de destino | <p>- Dirección: <a href="https://k8k5azm77j.execute-api.sa-east-1.amazonaws.com/prod/gps">https://k8k5azm77j.execute-api.sa-east-1.amazonaws.com/prod/gps</a><br>- Puerto: 443</p>                  |

Una pantalla de gestión de retransmisión debería verse similar a la siguiente, con el inicio de sesión y contraseña de SimpliRoute. Asegúrese de que el botón "Habilitado" esté marcado y haga clic en el botón "Guardar" para completar el proceso.

![SimpliRoute](https://www.navixy.com/wp-content/uploads/2022/10/pasted-image-0-2-600x115.png)

A continuación, será necesario vincular el retransmisor al dispositivo en el lado de Unigis. Para hacerlo, seleccione el botón “Vincular” ![link image](https://www.navixy.com/wp-content/uploads/2022/08/image-3.png)

en el widget de reenvío de datos. Seleccione el retransmisor a conectar y haga clic en “Vincular” a continuación.

No se necesita ID externo para el protocolo SimpliRoute.

Seleccione “Guardar” una vez completado.

#### Administración

Para editar o detener el reenvío de datos, consulte los siguientes pasos:

Para detener el reenvío de datos, haga clic en el botón “Papelera”.

A continuación, confirme el cambio en la ventana emergente.

Para cambiar la configuración del retransmisor, como el nombre, la información de inicio de sesión o el habilitado, haga clic en “Gestión de retransmisores”.

Esto abrirá la ventana de gestión de retransmisores. Seleccione la fila para editar y haga clic en el lápiz en la parte superior izquierda, o haga doble clic en la fila en cuestión para permitir la edición. Guarde los cambios realizados.

![SimpliRoute](https://www.navixy.com/wp-content/uploads/2022/10/pasted-image-0-1-600x116.png)

#### Solución de problemas

Si los datos no se muestran en el sistema de terceros SimpliRoute, verifique lo siguiente:

* La URL se ingresó correctamente.
* El retransmisor está habilitado.
* El rastreador en Navixy está asociado con un vehículo en la plataforma con una matrícula y un VIN válidos.
