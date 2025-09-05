# Lightmetrics

Lightmetrics es un proveedor líder de soluciones de telemática de video impulsadas por IA, especializado en tecnología de IA en el borde (edge AI) y despliegue de plataformas sin código. Su plataforma insignia RideView está diseñada específicamente para proveedores de servicios telemáticos (TSPs) y OEMs, permitiendo el despliegue de telemática de video avanzada en solo 3 semanas. Con capacidades agnósticas al hardware, RideView funciona con múltiples tipos de cámaras de tablero, incluyendo acceso exclusivo a la Suntech ST9730 y soporte para la popular Jimi JC450, al tiempo que ofrece una IA en el borde eficiente para el asesoramiento en tiempo real al conductor y la gestión de la seguridad de la flota.

Al integrar Lightmetrics con Navixy, obtienes análisis de video inteligente con procesamiento de IA en el borde combinado con la gestión de flotas en una sola interfaz. Examinemos cómo implementar esta combinación e integrar el panel de Lightmetrics en tu interfaz de Navixy.

{% stepper %}
{% step %}
#### **Establecimiento de la integración**

Para establecer la integración, necesitarás configurar tu cuenta Maestra de Lightmetrics y establecer la correspondencia de cuentas adecuada entre tus sistemas de Lightmetrics y Navixy.

**Solicitar la creación de una cuenta Maestra (configuración única)**

1. **Contacta a Navixy**: Envía una solicitud a tu Gerente de Éxito del Cliente o usa [este formulario](https://www.navixy.com/contact/) para solicitar la creación de una cuenta Maestra de Lightmetrics.
2. **Espera la confirmación**: Nuestros especialistas se coordinarán con Lightmetrics para crearte una cuenta. Recibirás las credenciales para iniciar sesión en tu cuenta de Lightmetrics.

{% hint style="success" %}
Después de completar estos pasos, tu cuenta Maestra de Lightmetrics está lista para la integración con Navixy. Ahora puedes proceder con la activación de dispositivos y la integración en la interfaz de usuario para cada cuenta de cliente que hayas configurado.
{% endhint %}
{% endstep %}

{% step %}
#### **Agregar dispositivos a Navixy**

Dado que Lightmetrics es agnóstico al dispositivo, puedes agregar cualquier dispositivo compatible a la plataforma siguiendo el procedimiento estándar de activación de dispositivos. El único requisito es que el dispositivo ya debe existir en tu cuenta de Lightmetrics.

{% hint style="info" %}
Asegúrate de que tu dispositivo esté correctamente configurado en tu cuenta de Lightmetrics antes de proceder con la activación en Navixy.
{% endhint %}

1. Ve a **Activación de dispositivo**.
2. Selecciona tu dispositivo de la lista.
3. Selecciona la opción **Tarjeta SIM comprada por separado** y ve al siguiente paso.
4. Ingresa un **ID de Dispositivo** correcto (IMEI del dispositivo).
5. Completa la configuración del dispositivo.

Para instrucciones detalladas sobre cómo activar un dispositivo en Navixy, consulta Activar dispositivo GPS.

{% hint style="success" %}
¡Tu dispositivo y cuenta de Navixy están listos para la integración!
{% endhint %}
{% endstep %}

{% step %}
#### **Integrar Lightmetrics en la interfaz de usuario de Navixy**

**Crear Clave de API**

Antes de la integración, necesitas crear una clave de API para esta integración en tu cuenta de Navixy.

1. En Navixy, ve a **Configuración de la cuenta** → **Claves de API**.
2. Haz clic en <img src="https://2096203889-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F446mKak1zDrGv70ahuYZ%2Fuploads%2Fgit-blob-8162eb61f85ccbbb68c97e0a17a48eef5e8b574b%2Fimage-20250422-143344.png?alt=media" alt="" data-size="line"> para añadir una nueva clave.
3.  En el campo **Etiqueta**, ingresa: `Lightmetrics FleetID = [ID]`

    Reemplaza **\[ID]** con el Fleet ID real de la flota de Lightmetrics. Por ejemplo: ![](https://2096203889-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F446mKak1zDrGv70ahuYZ%2Fuploads%2FH3TAUMSNfef8y03pvzig%2Fimage.png?alt=media\&token=7404dc3e-4cd5-431d-8b5e-bae16ea4cf7d)
4. Haz clic en **Guardar** y mantén esta clave a mano para el siguiente paso.

Para más detalles sobre cómo crear una clave de API en Navixy, consulta Claves de API.

**Crear nueva Aplicación de usuario**

En este paso, realizamos la integración real incrustando el panel de Lightmetrics en tu interfaz de Navixy. Navixy ofrece la funcionalidad de **Aplicaciones de usuario** que permite integrar aplicaciones de terceros directamente en la interfaz de la plataforma. La usaremos para integrar Lightmetrics.

{% hint style="info" %}
#### **Navegación**

La sección **Aplicaciones de usuario** es accesible para los **Propietarios** de la cuenta en la sección **Configuración de la cuenta**. Para encontrarla:

* Haz clic en el ícono de perfil en la esquina superior izquierda de la pantalla para abrir la configuración de tu cuenta.
* En la barra lateral de configuración, selecciona **Aplicaciones de usuario**.
{% endhint %}

1. Crear nueva aplicación Comienza haciendo clic en el botón <img src="https://2096203889-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F446mKak1zDrGv70ahuYZ%2Fuploads%2Fgit-blob-ce73c8e50f2c0264130f554788302c73bcaa6ece%2F5c189486-fbcd-47f6-ae65-953cb70ff9b2?alt=media" alt="chrome_py0qhiu5p8.webp" data-size="line"> en la lista de **Aplicaciones de usuario**.
   1. Configura la nueva aplicación.
   2. Se admite la integración de elementos de menú separados del panel de Lightmetrics (**Home**, **Trips**, **Live view**, etc.). Coloca el enlace a la vista seleccionada de tu panel de Lightmetrics en el campo **URL de la App**, y personaliza la ruta de redirección para definir qué página de Lightmetrics se abre después de iniciar sesión añadiendo un parámetro `redirect_path`.
      1. Servidor EU - `video-telematics.eu.navixy.com/sso?access_token={session_key}&redirect_path=`<mark style="color:green;">`home`</mark>
      2. Servidor US - `video-telematics.us.navixy.com/sso?access_token={session_key}&redirect_path=`<mark style="color:green;">`home`</mark>
   3. Ingresa una **Etiqueta** para la aplicación (ej., Panel de Lightmetrics).
   4. Selecciona **Integrado** en el campo **Mostrar como** para mostrar la funcionalidad de Lightmetrics dentro de Navixy.
   5. Selecciona tu clave de API preconfigurada del menú desplegable en el campo **Clave de API**. ¡Asegúrate de haber creado una clave correcta como se describe en Crear Clave de API!
2. **Guarda la configuración** Haz clic en **Guardar** para completar la configuración.

{% hint style="success" %}
Tu nueva aplicación de Lightmetrics aparece automáticamente en la barra lateral izquierda de Navixy. Ábrela para acceder a tu completo panel de telemática de video con detección de eventos impulsada por IA, asesoramiento en tiempo real para el conductor, transmisiones de video multicanal y análisis de seguridad avanzados, todo integrado con tus herramientas de gestión de flotas de Navixy existentes.

<img src="https://2096203889-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F446mKak1zDrGv70ahuYZ%2Fuploads%2Fgit-blob-88f8f78de47f2ca6026f67444a8c8ef0c79f7022%2FLightmetrics-embedded.webp?alt=media" alt="" data-size="original">
{% endhint %}
{% endstep %}
{% endstepper %}
