# Integración de Mettax para telemática de video

La telemática de video es una funcionalidad vital para muchas empresas. Existen soluciones propietarias que manejan la transmisión de video desde cámaras de tablero, pero ofrecen posibilidades limitadas para las lecturas telemáticas de dichos dispositivos. Por esta razón, ampliamos nuestro enfoque hacia las integraciones para que nuestros clientes puedan aprovechar las aplicaciones de terceros existentes para video y beneficiarse de las características telemáticas extendidas de Navixy al mismo tiempo.

Mettax es un gran ejemplo de este escenario. Veamos qué tan fácil es integrar sus capacidades directamente dentro de la interfaz de usuario de Navixy.

## 1. Establecimiento de la integración

Primero, necesita realizar las preparaciones necesarias del lado de Mettax.

> \[!WARNING] En Mettax, los datos del dispositivo se almacenan bajo cuentas de usuario individuales. Si su organización utiliza una estructura de cuenta principal, **necesitará realizar los siguientes pasos para cada cuenta de usuario que tenga dispositivos**. Aunque esto puede requerir iniciar y cerrar sesión en diferentes cuentas, garantiza una cobertura integral y dirigida en toda su flota de dispositivos.

1. Inicie sesión en una cuenta de usuario que contenga dispositivos reales.
2. Active el modo **Desarrollador** para habilitar las configuraciones necesarias para nuestra integración:![f3b775ba99794a95aec4bd87a05930a1.png](../gua-del-usuario/conectores-de-soluciones/attachments/f3b775ba99794a95aec4bd87a05930a1.png)
3. Haga clic en el nombre de su cuenta en la esquina superior derecha de la ventana.
4. Vaya a **Configuración del Cliente**.
5. Abra la pestaña **Configuración de la Aplicación**.
6. Habilite la opción **Desarrollador**.
7. Instale **Webhooks** para establecer una conexión entre las dos soluciones:
8. Haga clic en el icono de aplicaciones y seleccione **Desarrollador**.![07fa7b1a0f6e404a8e7abb4f147bd267.png](../gua-del-usuario/conectores-de-soluciones/attachments/07fa7b1a0f6e404a8e7abb4f147bd267.png)
9. Vaya a **Detalles**.
10. Abra la pestaña **WEBHOOK**.
11. Encuentre estos tres webhooks, necesitará editarlos:![9466c0c3da4c470599dacbdff68b44a8.png](../gua-del-usuario/conectores-de-soluciones/attachments/9466c0c3da4c470599dacbdff68b44a8.png) 1. **pushDeviceInfo** 2. **pushAlarm** 3. **pushGpsInfo**
12. Haga clic en **Editar** en la fila del webhook necesario para abrir sus parámetros.
13. Complete el campo URL con la dirección de su instancia de Navixy, dependiendo de la región: 1. EU - https://mettax-tracker.navixy.com 2. US - https://mettax-tracker.us.navixy.com
14. Repita el paso de la URL para los 3 webhooks.
15. (opcional) Repita los pasos anteriores para todas las cuentas de usuario requeridas.

> \[!TIP] ¡Su cuenta de Mettax está lista para la integración!

## 2. Agregar un dispositivo Mettax a Navixy

La plataforma Navixy maneja la funcionalidad GPS de los dispositivos de video y sus capacidades telemáticas. Para aprovechar al máximo la integración, necesita agregar su dispositivo Mettax a la plataforma, siguiendo el procedimiento habitual:

1. Vaya a **Activación de dispositivo**.
2. Seleccione su dispositivo Mettax de la lista.
3. Seleccione la opción **Tarjeta SIM comprada por separado** y vaya al siguiente paso.
4. Ingrese un **ID de Dispositivo** correcto
5. Complete la configuración del dispositivo

Para instrucciones detalladas sobre cómo activar un dispositivo en Navixy, consulte [Activar dispositivo GPS](https://squaregps.atlassian.net/wiki/spaces/UDOCES/pages/2922547365/Activar+el+dispositivo+GPS?atlOrigin=eyJpIjoiYzFkZmNlYjBjMjI3NDdmZDhhY2MzNTE1YjA2OGVlMGQiLCJwIjoiYyJ9).

> \[!TIP] ¡Su dispositivo y cuenta de Navixy están listos para la integración!

## 3. Integrar Mettax en la interfaz de usuario de Navixy

En este paso, realizamos la integración real.\
Navixy ofrece funcionalidad de [Aplicaciones de usuario](https://squaregps.atlassian.net/wiki/spaces/UDOCES/pages/3020292107/Aplicaciones?atlOrigin=eyJpIjoiOWZlZDBlMmZlYzcwNDE2MWE5MDRkYjZlMDQ4NTFkZTEiLCJwIjoiYyJ9) que permite integrar aplicaciones de terceros directamente en la interfaz de la plataforma. La usaremos para integrar Mettax.

> \[!NOTE] **Navegación** La sección **Aplicaciones de usuario** es accesible para los **Propietarios** de cuenta en la sección **Configuración de Cuenta**. Para encontrarla:
>
> 1. Haga clic en el icono de perfil en la esquina superior izquierda de la pantalla para abrir la configuración de su cuenta
> 2. En la barra lateral de configuración, seleccione **Aplicaciones de usuario**

1. Crear nueva aplicación\
   Comience haciendo clic en el botón ![image-20250724-151119.png](../gua-del-usuario/conectores-de-soluciones/attachments/image-20250724-151119.png) en la lista de **Aplicaciones de usuario**.
2. Configurar la nueva aplicación
3. Coloque [https://www.mettaxiot.com/#/dashboard](https://www.mettaxiot.com/#/dashboard) en el campo **URL de la Aplicación**.
4. Ingrese una **Etiqueta** para la aplicación (por ejemplo, Panel de Mettax).
5. Seleccione **Integrado** en el campo **Mostrar como** para mostrar la funcionalidad de Mettax dentro de Navixy.
6. Haga clic en **Guardar** para completar la configuración.

> \[!TIP] Su nueva aplicación aparece automáticamente en la barra lateral izquierda de Navixy. Ábrala e inicie sesión con sus credenciales de Mettax. ![0413c419716f464f90a16f9db5ed0d34.png](../gua-del-usuario/conectores-de-soluciones/attachments/0413c419716f464f90a16f9db5ed0d34.png)
