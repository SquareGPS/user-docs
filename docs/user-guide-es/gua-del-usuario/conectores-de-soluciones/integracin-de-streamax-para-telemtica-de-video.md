# Integración de Streamax para telemática de video

Streamax es un fabricante líder de MDVR, bien establecido en el mercado global. Con sus dispositivos, puede habilitar grabación de video 24/7 desde sus vehículos, recopilar datos telemáticos, acceder remotamente a las grabaciones de video y monitorear la seguridad de conducción utilizando tecnologías ADAS (Sistemas Avanzados de Asistencia al Conductor) y DSM (Monitoreo del Estado del Conductor).

Al integrar Streamax con Navixy, obtiene monitoreo integral de video combinado con gestión avanzada de flotas en una sola interfaz. Examinemos más de cerca cómo implementar esta poderosa combinación e integrar el panel de control de Streamax en la interfaz de Navixy.

## 1\. Establecimiento de la integración

Para establecer la integración, necesitará obtener credenciales de API de su cuenta de Streamax y solicitar la configuración de integración a nuestro equipo de soporte.

### Obtenga credenciales de API de Streamax

1. **Obtenga la Clave API y el Secreto**: Siga el proceso de autenticación como se describe en la [documentación de Autenticación de Firma de Streamax](https://ftcloud.streamax.com:20002/DOC/Sign%20Authentication) para obtener su clave API y secreto.
2. **Contacte a Navixy**: Una vez que tenga sus credenciales de API, contacte a su Gerente de Éxito del Cliente o use [este formulario](https://www.navixy.com/contact/). Envíe una solicitud para integrar Streamax con su cuenta de Navixy, que contenga la siguiente información:
  - Su clave API
  - Su secreto API
  - Los detalles de su cuenta de Navixy
  - Solicitud de activación de integración de Streamax
3. **Espere la confirmación**: Nuestros especialistas configurarán la integración en 1-3 días de nuestro lado y confirmarán cuando esté lista para usar.

> [!TIP]
> ¡Después de recibir la confirmación de nuestro soporte, su cuenta de Streamax está lista para la integración!

## 2\. Agregar un dispositivo Streamax a Navixy

Después de recibir confirmación de nuestro equipo de soporte de que la integración está lista, puede agregar su dispositivo Streamax a la plataforma. Para hacerlo, siga el procedimiento usual de activación de dispositivo:

1. Vaya a **Activación de dispositivo**.
2. Seleccione su dispositivo Streamax de la lista.
3. Seleccione la opción **Tarjeta SIM comprada por separado** y vaya al siguiente paso.
4. Ingrese un **ID de Dispositivo** correcto (IMEI del dispositivo)
5. Complete la configuración del dispositivo

Para instrucciones detalladas sobre cómo activar un dispositivo en Navixy, vea [Activar dispositivo GPS](https://squaregps.atlassian.net/wiki/spaces/UDOCES/pages/2922547365/Activar+el+dispositivo+GPS?atlOrigin=eyJpIjoiOGY3ZjVjNmQ3ZDZjNDIwOGJmMzQxZDdlMDNhYjZkY2YiLCJwIjoiYyJ9).

> [!TIP]
> ¡Su dispositivo y cuenta de Navixy están listos para la integración!

## 3\. Integrar Streamax en la interfaz de usuario de Navixy

En este paso, realizamos la integración real integrando el panel de control de Streamax en su interfaz de Navixy.  
Navixy ofrece funcionalidad de [Aplicaciones de usuario](https://squaregps.atlassian.net/wiki/spaces/UDOCES/pages/3020292107/Aplicaciones?atlOrigin=eyJpIjoiYzA1MDE3NmZhYTU1NGE5ZDg4YjI5ODQyYTUwNWRiNGQiLCJwIjoiYyJ9) que permite integrar aplicaciones de terceros directamente en la interfaz de la plataforma. La usaremos para integrar Mettax.

> [!NOTE]
> **Navegación**
> La sección **Aplicaciones de usuario** es accesible para los **Propietarios** de cuenta en la sección **Configuración de Cuenta**. Para encontrarla:
> 1. Haga clic en el ícono de perfil en la esquina superior izquierda de la pantalla para abrir la configuración de su cuenta
> 2. En la barra lateral de configuración, seleccione **Aplicaciones de usuario**

1. Cree una nueva aplicación  
Comience haciendo clic en el botón ![image-20250724-151029.png](attachments/image-20250724-151029.png)
 en la lista de **Aplicaciones de usuario**.
2. Configure la nueva aplicación
  1. Coloque el enlace a su cuenta de Streamax en el campo **URL de la App**, por ejemplo: `https://{su_instancia}.ifleetvision.com/ftv/ft/dashboard#`.
  2. Ingrese una **Etiqueta** para la aplicación (ej., Panel de control de Streamax).
  3. Seleccione **Integrado** en el campo **Mostrar como** para mostrar la funcionalidad de Streamax dentro de Navixy.
3. Haga clic en **Guardar** para completar la configuración.

> [!TIP]
> Su nueva aplicación aparece automáticamente en la barra lateral izquierda de Navixy. Ábrala e inicie sesión con sus credenciales de Streamax para acceder a su panel integral de telemática de video con monitoreo 360°, detección de eventos impulsada por IA y transmisiones de video multicanal, todo integrado con sus herramientas existentes de gestión de flotas de Navixy.
> ![336df60990234ac98e3c94d8e3f3f69a.png](attachments/336df60990234ac98e3c94d8e3f3f69a.png)