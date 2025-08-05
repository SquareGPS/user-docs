# Recurso Confiable

# Recurso Confiable—Seguimiento GPS y envío de datos para empresas

Recurso Confiable es un software de seguridad y logística que monitorea, da visibilidad y genera predictibilidad en las operaciones de transporte. Navixy creó el protocolo de reenvío de datos de Recurso Confiable para ser utilizado por otras empresas que también trabajan con Recurso Confiable en múltiples industrias en México, Colombia, Estados Unidos y Centroamérica.

*Categoría del Protocolo: Protocolo empresarial*

## ¿Qué es Recurso Confiable?

Con el protocolo Recurso Confiable, los socios empresariales pueden transferir datos de rastreo GPS de manera segura y confiable a una ubicación única para optimizar los procesos de gestión de flotas. Esto permite al cliente trabajar y comunicarse con otros socios de Recurso Confiable.

Al desarrollar este protocolo, Navixy tomó en cuenta las necesidades de grandes empresas de logística y retail. Las empresas pueden optimizar importantes datos y capacidades de gestión de flotas y plataformas de rastreo GPS, como sistemas de control, planificación de viajes, rastreo en tiempo real, informes de modelado predictivo, implementación y edición de geocercas, optimización de rutas y más. Las empresas que antes estaban desconectadas entre sí en la red de Recurso Confiable ahora pueden comunicarse de manera eficiente y rápida.

## Información técnica general de Recurso Confiable

El protocolo Recurso Confiable utiliza SOAP para enviar datos XML cada 5 minutos a través de HTTP a Recurso Confiable.

Datos enviados a Recurso Confiable:

- Código de evento AVL
- Matrícula
- ID de envío
- Fecha
- Dirección
- Latitud
- Longitud
- Altitud
- Velocidad
- Curso
- Ignición
- Odómetro
- ID del cliente
- Nombre del cliente
- ID del dispositivo

## Configuración de Recurso Confiable

### Puesta en marcha

Parámetros requeridos

- Usuario y Contraseña de Recurso Confiable
- ID externo
- Dirección del servidor de destino
  - [http://gps.rcontrol.com.mx/Tracking/wcf/RCService.svc](http://gps.rcontrol.com.mx/Tracking/wcf/RCService.svc)
- Puerto del servidor de destino
  - 80

Para configurar el reenvío de datos en el protocolo Recurso Confiable, abra la configuración del dispositivo desde el menú principal, presionando el icono de “Engranaje” en la parte inferior izquierda de la pantalla

Luego, haga clic en el widget de “Reenvío de datos”.

Haga clic en “Gestión de retransmisores”.

Esto abrirá una ventana emergente donde ingresará los parámetros requeridos presionando el botón +.

Para el protocolo Recurso Confiable, ingrese la siguiente información:

| Parámetro | Explicación |
| --- | --- |
| Nombre | Ingrese un nombre para que este retransmisor sea fácilmente identificable |
| Protocolo y Usuario | Seleccione el protocolo Recurso Confiable del menú desplegable;<br><br>Utilice el Usuario y Contraseña de Recurso Confiable |
| Dirección y puerto del servidor de destino | - Dirección: [http://gps.rcontrol.com.mx/Tracking/wcf/RCService.svc](http://gps.rcontrol.com.mx/Tracking/wcf/RCService.svc)<br>- Puerto: 80 |

Una pantalla de gestión de retransmisión debería verse similar a la siguiente, con el usuario y contraseña de Recurso Confiable. Asegúrese de que el botón "Habilitado" esté marcado y haga clic en el botón "Guardar" para completar el proceso.

![Recurso Confiable](https://www.navixy.com/wp-content/uploads/2022/10/pasted-image-0-1-1-600x120.png)

A continuación, será necesario vincular el retransmisor al dispositivo en el lado de Unigis. Para hacerlo, seleccione el botón “Vincular” ![link image](https://www.navixy.com/wp-content/uploads/2022/08/image-3.png)

 en el widget de reenvío de datos. Seleccione el retransmisor a conectar y haga clic en “Vincular” a continuación.

Luego, agregue la información necesaria para identificar el dispositivo en Recurso Confiable en el campo ID externo, ya sea haciendo clic en el ícono del lápiz o en el campo de ID externo. Este valor debe incluir lo siguiente desde el lado de Recurso Confiable, donde solo la matrícula es obligatoria:

- Matrícula
- ID de Ruta
- ID de la Empresa
- Nombre de la Empresa

 El formato para el campo ID externo estará separado por una barra vertical. Por ejemplo:

*ABC123|1|123|John*

 Si solo está disponible la Matrícula, el ID externo se puede ingresar por sí solo:

*ABC123*

O si falta cualquier otra información, asegúrese de incluir las barras verticales, por ejemplo:

*ABC123||123|*

Seleccione “Guardar” una vez completado.

### Administración

Para editar o detener el reenvío de datos, consulte los siguientes pasos:

Seleccione el ícono de “Lápiz” o haga clic en el cuadro asociado para editar el ID externo utilizado para apuntar al dispositivo en el sistema de terceros.

Para detener el reenvío de datos, haga clic en el botón “Papelera”.

A continuación, confirme el cambio en la ventana emergente.

Para cambiar la configuración del retransmisor, como nombre, información de inicio de sesión o habilitado, haga clic en “Gestión de retransmisores”.

Esto abrirá la ventana de gestión de retransmisores. Seleccione la fila para editar y haga clic en el lápiz en la parte superior izquierda, o haga doble clic en la fila en cuestión para permitir la edición. Guarde los cambios realizados.

![Recurso Confiable](https://www.navixy.com/wp-content/uploads/2022/10/pasted-image-0-3-600x107.png)

### Solución de problemas

Si los datos no se muestran en el sistema de terceros Recurso Confiable, verifique lo siguiente:

- El nombre de usuario y la contraseña de Recurso Confiable están correctamente ingresados.
- La URL se ingresó correctamente.
- El retransmisor está habilitado.
- El ID externo coincide con la información relacionada de Recurso Confiable.