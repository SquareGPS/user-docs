# ILSP

# ILSP — Protocolo de datos de vehículos de seguridad privada entre servidores

ILSP ofrece servicios de seguridad privada en México. El protocolo de reenvío de datos de ILSP permite que su software comparta datos de vehículos a través de redes.

*Protocol Category: Enterprise compliance*

## ¿Qué es ILSP?

El protocolo de reenvío de datos de ILSP está destinado a empresas que tienen centros de monitoreo comunes dedicados a temas de seguridad y necesitan monitorear la posición de los vehículos y compartir estos datos con terceros.

Con ILSP, los socios pueden actualizar su información con datos de Navixy, como datos de vehículos, posición, etc. Los usuarios pueden conectarse con múltiples empresas y enviar información a ILSP, agilizando los datos de flotas y seguridad.

## Información técnica general de ILSP

El protocolo ILSP utiliza el método POST para enviar datos JSON a través de HTTP a los servidores ILSP para su posterior procesamiento de datos.

Datos enviados a ILSP:

- ID del cliente
- ID de la línea de transporte
- Matrícula
- Evento del rastreador y hora
  - SOS, pérdida de energía y alarma de bloqueo GSM
- Latitud
- Longitud
- Velocidad
- Rumbo
- Odómetro
- Batería

## Configuración ILPS

### Puesta en marcha

Parámetros requeridos.

- Usuario y Contraseña
  - ILSP usuario y contraseña
- Dirección y puerto del servidor de destino
  - Dirección: https://www.ilspservices.com.mx/
  - Puerto: 443

Para configurar el reenvío de datos en el protocolo ILSP, abra la configuración del dispositivo desde el menú principal presionando el icono de “Engranaje” en la parte inferior izquierda de la pantalla.

Luego, haga clic en el widget de “Reenvío de datos”.

Haga clic en “Gestión de retransmisores”.

Esto abrirá una ventana emergente donde ingresará los parámetros requeridos presionando el botón +.

Para el protocolo ILSP, ingrese la siguiente información:

| Parámetro | Explicación |
| --- | --- |
| Nombre | Ingrese un nombre para que este retransmisor sea fácilmente identificable |
| Protocolo | Seleccione el protocolo ILSP del menú desplegable |
| Dirección y puerto del servidor de destino | - Dirección: [https://www.ilspservices.com.mx/](https://www.ilspservices.com.mx/)<br>- Puerto: 443 |

Una pantalla de gestión de retransmisión debería verse similar a la siguiente, con el usuario y contraseña de ILSP. Asegúrese de que el botón "Habilitado" esté marcado y haga clic en el botón "Guardar" para completar el proceso.

![ILSP](https://www.navixy.com/wp-content/uploads/2022/10/image-8-600x111.png)

Posteriormente, será necesario vincular el retransmisor al dispositivo en el lado de Unigis. Para hacerlo, seleccione el botón “Vincular” ![link image](https://www.navixy.com/wp-content/uploads/2022/08/image-3.png)

 en el widget de reenvío de datos. Seleccione el retransmisor a conectar y haga clic en “Vincular” a continuación.

Luego, agregue la información necesaria para identificar el dispositivo en ILSP en el campo ID externo, ya sea haciendo clic en el ícono del lápiz o en el campo de ID externo. Este valor debe incluir lo siguiente desde el lado de ILSP:

*UserId|MatrículaDelVehículo|RouteID*

### Gestión

Para editar o detener el reenvío de datos, consulte los siguientes pasos:

Para detener el reenvío de datos, haga clic en el botón “Papelera”.

A continuación, confirme el cambio en la ventana emergente.

Para cambiar la configuración del retransmisor, como el nombre, la información de inicio de sesión o habilitado, haga clic en “Gestión de retransmisores”.

Esto abrirá la ventana de gestión de retransmisores. Seleccione la fila para editar y haga clic en el lápiz en la parte superior izquierda, o haga doble clic en la fila en cuestión para permitir la edición. Guarde los cambios realizados.

![ILSP](https://www.navixy.com/wp-content/uploads/2022/10/image-9-600x100.png)

### Solución de problema

Si los datos no se muestran en el sistema de terceros ILSP, verifique lo siguiente:

- El nombre de usuario y la contraseña de ILSP están correctamente ingresados.
- La URL se ingresó correctamente.
- El retransmisor está habilitado.
- La información de ID externo es correcta.