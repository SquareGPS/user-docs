# Guía de inicio rápido

Esta guía le ayudará a configurar rápidamente su primer flujo de datos en IoT Logic y a empezar a procesar sus datos telemáticos.

## Requisitos previos

Antes de proceder a la creación de su primer flujo, asegúrese de que dispone de:

* Un rol de **Propietario** en su cuenta Navixy
* Dispositivos activados en su cuenta
* Comprensión de las fuentes de datos que desea procesar

{% hint style="info" %}
El espacio de trabajo IoT Logic solo está disponible para los propietarios de cuentas y no se muestra para los usuarios normales. Para obtener más información sobre los roles de usuario, consulte [Usuarios y roles](../acceso-del-equipo/).
{% endhint %}

## Configuración de flujos

Eche un vistazo a un breve vídeo que muestra el proceso de creación de un nuevo flujo con cálculos de atributos de datos y la adición de atributos personalizados a los dispositivos de la plataforma:

{% embed url="https://files.gitbook.com/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F446mKak1zDrGv70ahuYZ%2Fuploads%2FGAVD9gNxaRYpHDSAlOmf%2FIot%20Logic%20Demo%20Screencast.mp4?alt=media&token=94fd4cf6-bd45-4953-9263-52863288d9b9" %}

Ahora, vamos a desglosar el proceso de configuración del flujo paso a paso.

### Paso 1: Acceder al espacio de trabajo de IoT Logic

1. Acceda a su cuenta Navixy
2. Haga clic en el icono de su perfil en la esquina superior izquierda de la pantalla para acceder a **Configuración de la cuenta**
3. Seleccione **IoT Logic** en la barra lateral de ajustes

El espacio de trabajo de IoT Logic aparece con tres secciones principales:

* **Barra de configuración de flujos** - Contiene controles para gestionar los flujos.
* **Panel de nodos** - Enumera los nodos disponibles para construir su flujo
* **Lienzo** - El espacio de trabajo principal donde diseñará su flujo

Para obtener más información sobre el espacio de trabajo, consulte [Espacio de trabajo y flujo por defecto](espacio-de-trabajo-y-flujo-por-defecto.md).

### Paso 2: Crear un nuevo flujo

1. Haga clic en el botón **Nuevo flujo** de la barra de configuración de flujos
2. En el cuadro de diálogo **Nuevo flujo**

* Introduzca un nombre descriptivo para su flujo (por ejemplo, "Procesamiento de telemetría de flota").
* Añada una breve descripción que explique el propósito del flujo
* Asegúrese de que la opción **Flujo** habilitado está activada.

3. Haga clic en **Guardar** para crear el flujo

Para más información sobre la configuración de flujos, consulte [Gestión de flujos -> Creación de un nuevo flujo](https://squaregps.atlassian.net/wiki/spaces/UDOCES/pages/3232334081/Flow+management#Creating-a-new-flow).

{% hint style="info" %}
Los flujos desactivados no procesan ningún dato. Cuando se desactiva un flujo, los dispositivos de ese flujo no transmitirán datos a ningún destino, incluida la plataforma Navixy.
{% endhint %}

### Paso 3: Configurar un nodo de Fuente de datos

1. En el panel **Nodos**, arrastre un nodo **Fuente de Datos** al lienzo.
2. Pase el ratón por encima del nodo para mostrar las acciones rápidas, o haga doble clic en el nodo para abrir su panel de configuración
3. Configure los siguientes ajustes:

* **Nombre del nodo** - Introduzca un nombre descriptivo, especificando el origen de los datos enviados (por ejemplo, _Vehículos de personal_).
* **Fuentes** - Seleccione los dispositivos cuyas lecturas desea enviar a este flujo. Puede filtrar los dispositivos disponibles por **Fabricante de datos** y **Modelo de** **dispositivo**.

4. Haga clic en **Guardar** para aplicar la configuración

Para obtener más información sobre la configuración del nodo, consulte [El nodo Fuente de Datos.](gestin-de-flujos/el-nodo-fuente-de-datos.md)

### Paso 4: Añadir enriquecimiento de datos (Opcional)

1. Arrastre un nodo **Iniciar Atributo** al lienzo
2. Pase el ratón por encima del nodo para mostrar acciones rápidas, o haga doble clic en el nodo para abrir su panel de configuración
3. Añada un **nombre del Nodo** descriptivo para especificar su propósito y los cálculos que realiza (por ejemplo, _Temperatura °F a °C_)
4. Defina su atributo:

* **Nombre del atributo** - Un nombre claro y descriptivo (por ejemplo, "velocidad\_mph").
* **Fórmula**- La expresión de cálculo (por ejemplo, `value('velocidad')/1.609` para convertir km/h a mph)
* **Hora de generación** - Cuando se creó la entrada de datos en el dispositivo (por defecto `now()`)
* **Hora del servidor** - Cuando los datos fueron recibidos por el servidor (por defecto `now()`)

5. Añada atributos adicionales si es necesario haciendo clic en **Agregar atributo**

{% hint style="danger" %}
El botón **Restablecer formulario** descarta todos los atributos creados dentro de un nodo. Si desea eliminar un determinado atributo, haga clic en los tres puntos situados a la derecha de la fila del atributo y seleccione **Eliminar**.
{% endhint %}

7. Haga clic en **Guardar** para aplicar la configuración
8. Cree una conexión:

* Haga clic en el conector de salida del nodo **Fuente de Datos**
* Arrastre la transición al conector de entrada del nodo **Iniciar Atributo**

Para obtener más información sobre la configuración del nodo, consulte [El nodo Iniciar Atributo](gestin-de-flujos/el-nodo-iniciar-atributo/).

Para obtener más información sobre las acciones con atributos, consulte [Gestión de atributos](gestin-de-flujos/el-nodo-iniciar-atributo/gestin-de-atributos.md).

Para ver ejemplos de fórmulas de cálculo, consulte [Ejemplos de cálculo](gestin-de-flujos/el-nodo-iniciar-atributo/ejemplos-de-clculo.md).

### Paso 5: Configurar la salida de datos

1. Arrastre un nodo **Punto de Salida** al lienzo
2. Pase el ratón por encima del nodo para mostrar acciones rápidas, o haga doble clic en el nodo para abrir su panel de configuración
3. Seleccione **el tipo de Punto de Salida**:

* **Punto de salida predeterminado**: punto final predeterminado para enviar los datos procesados a la plataforma Navixy. Está preconfigurado y no permite cambios.
* **Punto de Salida MQTT** - endpoint para enviar datos a destinos de terceros, utilizando MQTT como protocolo de transporte. Requiere la configuración manual descrita en los pasos siguientes

{% hint style="info" %}
Los puntos finales creados dentro de la cuenta están disponibles como **Preconfiguraciones**. Puede seleccionar una configuración ya existente en lugar de configurarla desde cero. **Punto de salida predeterminado** siempre está disponible como configuración preestablecida.
{% endhint %}

4. Configure los siguientes ajustes:

* **Nombre del Punto de Salida** - Introduzca un nombre descriptivo para especificar el destino al que se envían los datos.
* **Protocolo** - Seleccione el protocolo de datos (por el momento sólo está disponible "Protocolo genérico Navixy (JSON)")
* **IP/Dominio** - Introduzca la dirección de destino
* **Puerto** - Especifique el número de puerto (por defecto: 1883 para MQTT estándar, 8883 para SSL)
* (opcional) **Activar SSL** - Activar para conexiones seguras
* **Versión MQTT** - Seleccione la versión apropiada\*\*(3.1.1\*\* o 5.0)
* **ID de cliente** - Introduzca el identificador de su cliente para garantizar que los datos son aceptados por la parte receptora
* **Temas** (opcional) - Especifique los temas MQTT para la transmisión de datos
* **QoS** - Seleccione el nivel de Calidad de Servicio para determinar la lógica de la transmisión de datos\*\*(0\*\*, **1**, o **2**)

5. Si se requiere autenticación en el lado receptor, active la **autenticación MQTT**\
   Los campos que aparecen se rellenan automáticamente con las credenciales de su cuenta de la plataforma.

{% hint style="danger" %}
El botón **Restablecer formulario** descarta todos los atributos creados dentro de un nodo. Si desea eliminar un determinado atributo, haga clic en los tres puntos situados a la derecha de la fila del atributo y seleccione **Eliminar**.
{% endhint %}

6. Haga clic en **Crear** para aplicar la configuración
7. Conecte sus otros nodos a este nodo de salida en el orden necesario para finalizar la estructura del flujo

{% hint style="info" %}
Cada flujo debe incluir un nodo **Punto de Salida Predeterminado** para garantizar que los datos se envían a la plataforma. Sin esta conexión, los datos del dispositivo no serán visibles en la interfaz Navixy.
{% endhint %}

Para obtener más información sobre la configuración del nodo, consulte [El nodo Punto de Salida](gestin-de-flujos/el-nodo-punto-de-salida.md).

### Paso 6: Guarde y active su flujo

1. Compruebe que todos los nodos están conectados correctamente en su flujo
2. Haga clic en el botón **Guardar flujo** en el panel **Nodos**
3. Su flujo está ahora activo y procesando datos en tiempo real

## Validación del flujo

Para confirmar que su flujo funciona correctamente, utilice la herramienta **Analizador de flujo de datos**:

1. Haga clic en el botón **Analizador de** **datos** de la barra de configuración del flujo
2. Seleccione los dispositivos que desea supervisar en la lista desplegable
3. Observe los atributos de los datos entrantes y sus valores
4. Utilice las opciones de filtrado para centrarse en parámetros específicos
5. Comprobar que los atributos calculados muestran los valores correctos

Para obtener más información sobre el uso de la herramienta, consulte [Analizador de flujo de datos](analizador-de-flujo-de-datos.md).

{% hint style="success" %}
¡Enhorabuena! Su primer flujo de datos de IoT Logic ya está en marcha.
{% endhint %}

## Pasos siguientes

Ahora que ha creado su primer flujo de IoT Logic, puede

* [Adaptar este ejemplo de inicio rápido](gua-de-inicio-rpido.md#adaptacion-de-este-ejemplo) a sus necesidades empresariales
* Cree transformaciones de datos más complejas con múltiples [nodos Iniciar Atributo](gestin-de-flujos/el-nodo-iniciar-atributo/)
* Establezca [destinos de salida](gestin-de-flujos/el-nodo-punto-de-salida.md) adicionales para sus datos que puedan convertirse en perfiles reutilizables para configuraciones coherentes
* [Gestionar flujos ya creados](gestin-de-flujos/) para ajustar el procesamiento de datos a cualquier cambio al que se enfrente
* [Diseñar flujos avanzados](gestin-de-flujos/ejemplo-de-configuracin-de-un-flujo.md) para escenarios empresariales específicos utilizando diferentes combinaciones y configuraciones de nodos

### Adaptación de este ejemplo

Este ejemplo puede adaptarse a diversos casos de uso industrial modificándolo:

* **Selección de dispositivos**: Elija los dispositivos pertinentes para sus activos específicos
* **Conversión de unidades**: Ajuste las fórmulas en función de sus unidades de medida estándar
* **Métricas calculadas**: Cree indicadores específicos del sector en función de sus necesidades empresariales
* **Configuración de salida**: Conéctese a su plataforma de análisis o base de datos específica

El patrón básico de recopilación, transformación y reenvío sigue siendo coherente en todos los sectores, lo que lo convierte en una plantilla versátil para el procesamiento de datos de IoT.

## Acceso API

También se puede acceder a las funciones de IoT Logic mediante programación a través de la API de Navixy. Esto permite a los desarrolladores automatizar la creación, gestión y supervisión de flujos.

{% hint style="info" %}
Por motivos de seguridad, el acceso a la API requiere los permisos adecuados. Póngase en contacto con el administrador de su cuenta para asegurarse de que dispone de los derechos de acceso necesarios.
{% endhint %}

Para obtener la documentación completa de la API, parámetros, formatos de solicitud/respuesta y ejemplos de código, consulte la [documentación de la Navixy IoT Logic API](https://app.gitbook.com/s/tx3J5BxnWyPV0nP2xr0z/) .

## Preguntas más frecuentes

### ¿Qué ocurre con los dispositivos no asignados a un flujo personalizado?

Los dispositivos no asignados explícitamente a ningún flujo personalizado son gestionados automáticamente por el flujo predeterminado, que envía sus datos directamente a la plataforma Navixy.

### ¿Puedo utilizar el mismo dispositivo en varios flujos?

No, cada dispositivo sólo puede asignarse a un flujo a la vez. Cuando se añade a un flujo personalizado, un dispositivo se elimina automáticamente del flujo predeterminado para evitar el procesamiento duplicado de datos.

### ¿Seguirá funcionando mi flujo si cierro la sesión?

Sí, una vez activados, los flujos funcionan independientemente de su sesión de usuario. Mientras el flujo esté activado, procesará los datos aunque no esté conectado.

### ¿Cómo puedo saber si mi flujo funciona correctamente?

Utilice el Analizador de flujo de datos para supervisar la transmisión de datos en tiempo real. Esta herramienta muestra tanto los datos brutos del dispositivo como los atributos calculados, lo que le permite verificar que sus transformaciones funcionan según lo esperado.

### ¿Qué ocurre si desactivo un flujo?

Al desactivar un flujo, los dispositivos asignados a ese flujo no transmitirán datos a ningún destino, incluida la plataforma Navixy. Los dispositivos aparecerán desconectados en la interfaz Navixy hasta que vuelva a habilitar el flujo.
