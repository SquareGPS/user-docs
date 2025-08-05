# Guía de inicio rápido

Esta guía le ayudará a configurar rápidamente su primer flujo de datos en IoT Logic y a empezar a procesar sus datos telemáticos.

## Requisitos previos

Antes de proceder a la creación de su primer flujo, asegúrese de que dispone de:

- Un rol de **Propietario** en su cuenta Navixy
- Dispositivos activados en su cuenta
- Comprensión de las fuentes de datos que desea procesar

> [!INFO]
> El espacio de trabajo IoT Logic sólo está disponible para los **Propietarios** de cuentas y no se muestra para los **Usuarios** normales . Para obtener más información sobre los roles de usuario, consulte [Usuarios y roles](https://squaregps.atlassian.net/wiki/spaces/USERDOCSOLD/pages/2909012400/Users+and+Roles).

## Configuración de flujos

Eche un vistazo a un breve vídeo que muestra el proceso de creación de un nuevo flujo con cálculos de atributos de datos y la adición de atributos personalizados a los dispositivos de la plataforma:

![video_1280.mp4](attachments/video_1280.mp4)

Ahora, vamos a desglosar el proceso de configuración del flujo paso a paso.

### Paso 1: Acceder al espacio de trabajo de IoT Logic

1. Acceda a su cuenta Navixy
2. Haga clic en el icono de su perfil en la esquina superior izquierda de la pantalla para acceder a **Configuración de la cuenta**
3. Seleccione **IoT Logic** en la barra lateral de ajustes

El espacio de trabajo de IoT Logic aparece con tres secciones principales:

- **Barra de configuración de flujos** - Contiene controles para gestionar los flujos.
- **Panel de nodos** - Enumera los nodos disponibles para construir su flujo
- **Lienzo** - El espacio de trabajo principal donde diseñará su flujo

Para obtener más información sobre el espacio de trabajo, consulte [Espacio de trabajo y flujo por defecto](https://squaregps.atlassian.net/wiki/spaces/UDOCES/pages/3232333880/Workspace+and+default+flow?atlOrigin=eyJpIjoiMmIyZDY3ZjExMTIzNDdhN2E3N2M2M2NmYzFmYTNiOTkiLCJwIjoiYyJ9).

### Paso 2: Crear un nuevo flujo

1. Haga clic en el botón **Nuevo flujo** de la barra de configuración de flujos
2. En el cuadro de diálogo **Nuevo flujo**
  - Introduzca un nombre descriptivo para su flujo (por ejemplo, "Procesamiento de telemetría de flota").
  - Añada una breve descripción que explique el propósito del flujo
  - Asegúrese de que la opción **Flujo** habilitado está activada.
3. Haga clic en **Guardar** para crear el flujo

Para más información sobre la configuración de flujos, consulte [Gestión de flujos -> Creación de un nuevo flujo](https://squaregps.atlassian.net/wiki/spaces/UDOCES/pages/3232334081/Flow+management#Creating-a-new-flow).

> [!INFO]
> Los flujos desactivados no procesan ningún dato. Cuando se desactiva un flujo, los dispositivos de ese flujo no transmitirán datos a ningún destino, incluida la plataforma Navixy.

### Paso 3: Configurar un nodo de Fuente de datos

1. En el panel **Nodos**, arrastre un nodo **Fuente de Datos** al lienzo.
2. Pase el ratón por encima del nodo para mostrar las acciones rápidas, o haga doble clic en el nodo para abrir su panel de configuración
3. Configure los siguientes ajustes:
  - **Nombre del nodo** - Introduzca un nombre descriptivo, especificando el origen de los datos enviados (por ejemplo, *Vehículos de personal*).
  - **Fuentes** \- Seleccione los dispositivos cuyas lecturas desea enviar a este flujo. Puede filtrar los dispositivos disponibles por **Fabricante de datos** y **Modelo de** **dispositivo**.
4. Haga clic en **Guardar** para aplicar la configuración

Para obtener más información sobre la configuración del nodo, consulte [Nodo de origen de datos](https://squaregps.atlassian.net/wiki/spaces/UDOCES/pages/3232334220/Data+Source+node?atlOrigin=eyJpIjoiMTlmNWM1ZmNmN2IxNDEwYTg3YzRiMzAwMjA1YjI0MDEiLCJwIjoiYyJ9).

### Paso 4: Añadir enriquecimiento de datos (Opcional)

1. Arrastre un nodo **Iniciar Atributo** al lienzo
2. Pase el ratón por encima del nodo para mostrar acciones rápidas, o haga doble clic en el nodo para abrir su panel de configuración
3. Añada un **nombre del Nodo** descriptivo para especificar su propósito y los cálculos que realiza (por ejemplo, *Temperatura °F a °C*)
4. Defina su atributo:
  - **Nombre del atributo** - Un nombre claro y descriptivo (por ejemplo, "velocidad\_mph").
  - **Fórmula**\- La expresión de cálculo (por ejemplo, `value('velocidad')/1.609` para convertir km/h a mph)
  - **Hora de generación** - Cuando se creó la entrada de datos en el dispositivo (por defecto `now()`)
  - **Hora del servidor** - Cuando los datos fueron recibidos por el servidor (por defecto `now()`)
5. Añada atributos adicionales si es necesario haciendo clic en **Agregar atributo**

> [!WARNING]
> El botón **Restablecer formulario** descarta todos los atributos creados dentro de un nodo. Si desea eliminar un determinado atributo, haga clic en los tres puntos situados a la derecha de la fila del atributo y seleccione **Eliminar**.

7. Haga clic en **Guardar** para aplicar la configuración
8. Cree una conexión:
  - Haga clic en el conector de salida del nodo **Fuente de Datos**
  - Arrastre la transición al conector de entrada del nodo **Iniciar Atributo**

Para obtener más información sobre la configuración del nodo, consulte [Iniciar nodo de atributos](https://squaregps.atlassian.net/wiki/spaces/UDOCES/pages/3232334272/Initiate+Attribute+node?atlOrigin=eyJpIjoiNjcyYzBhNzU3ZWNmNDIwOWIxYTVhNjc4YjA4YThlMGUiLCJwIjoiYyJ9).

Para obtener más información sobre las acciones con atributos, consulte [Gestión de atributos](https://squaregps.atlassian.net/wiki/spaces/UDOCES/pages/3232334380/Managing+attributes?atlOrigin=eyJpIjoiYWM0NmVhOGNhYzUwNDA0MzlkNjhmOTRkZGRiODI3YzkiLCJwIjoiYyJ9).

Para ver ejemplos de fórmulas de cálculo, consulte [Ejemplos de cálculo](https://squaregps.atlassian.net/wiki/spaces/UDOCES/pages/3232334409/Calculation+examples?atlOrigin=eyJpIjoiMjI1OTI1ZGViMDM0NDI2MGJiNzhhNTkyODY2YWNjODMiLCJwIjoiYyJ9).

### Paso 5: Configurar la salida de datos

1. Arrastre un nodo **Punto de Salida** al lienzo
2. Pase el ratón por encima del nodo para mostrar acciones rápidas, o haga doble clic en el nodo para abrir su panel de configuración
3. Seleccione **el tipo de Punto de Salida**:
  - **Punto de salida predeterminado**: punto final predeterminado para enviar los datos procesados a la plataforma Navixy. Está preconfigurado y no permite cambios.
  - **Punto de Salida MQTT** \- endpoint para enviar datos a destinos de terceros, utilizando MQTT como protocolo de transporte. Requiere la configuración manual descrita en los pasos siguientes

> [!INFO]
> Los puntos finales creados dentro de la cuenta están disponibles como **Preconfiguraciones**. Puede seleccionar una configuración ya existente en lugar de configurarla desde cero. **Punto de salida predeterminado** siempre está disponible como configuración preestablecida.

4. Configure los siguientes ajustes:
  - **Nombre del Punto de Salida** \- Introduzca un nombre descriptivo para especificar el destino al que se envían los datos.
  - **Protocolo** - Seleccione el protocolo de datos (por el momento sólo está disponible "Protocolo genérico Navixy (JSON)")
  - **IP/Dominio** - Introduzca la dirección de destino
  - **Puerto** - Especifique el número de puerto (por defecto: 1883 para MQTT estándar, 8883 para SSL)
  - (opcional) **Activar SSL** - Activar para conexiones seguras
  - **Versión MQTT** - Seleccione la versión apropiada**(3.1.1** o 5.0)
  - **ID de cliente** - Introduzca el identificador de su cliente para garantizar que los datos son aceptados por la parte receptora
  - **Temas** (opcional) - Especifique los temas MQTT para la transmisión de datos
  - **QoS** - Seleccione el nivel de Calidad de Servicio para determinar la lógica de la transmisión de datos**(0**, **1**, o **2**)
5. Si se requiere autenticación en el lado receptor, active la **autenticación MQTT**  
Los campos que aparecen se rellenan automáticamente con las credenciales de su cuenta de la plataforma.

> [!WARNING]
> El botón **Restablecer formulario** descarta todos los atributos creados dentro de un nodo. Si desea eliminar un determinado atributo, haga clic en los tres puntos situados a la derecha de la fila del atributo y seleccione **Eliminar**.

6. Haga clic en **Crear** para aplicar la configuración
7. Conecte sus otros nodos a este nodo de salida en el orden necesario para finalizar la estructura del flujo

> [!INFO]
> Cada flujo debe incluir un nodo **Punto de Salida Predeterminado** para garantizar que los datos se envían a la plataforma. Sin esta conexión, los datos del dispositivo no serán visibles en la interfaz Navixy.

Para obtener más información sobre la configuración del nodo, consulte [Nodo Punto de Salida](https://squaregps.atlassian.net/wiki/spaces/UDOCES/pages/3232334428/Output+Endpoint+node?atlOrigin=eyJpIjoiMWRhODIxODViOTVlNDhmYTkxZTU0YjdiYTQ2NjgxMWUiLCJwIjoiYyJ9).

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

Para obtener más información sobre el uso de la herramienta, consulte [Analizador de flujo de datos](https://squaregps.atlassian.net/wiki/spaces/UDOCES/pages/3232334554/Data+Stream+Analyzer?atlOrigin=eyJpIjoiZThhNDJjODJjYjFmNDNiMzhiMmVlMGZkMzQyYjkzOTciLCJwIjoiYyJ9).

> [!TIP]
> ¡Enhorabuena! Su primer flujo de datos de IoT Logic ya está en marcha.

## Pasos siguientes

Ahora que ha creado su primer flujo de IoT Logic, puede

- [Adaptar este ejemplo de inicio rápido](https://squaregps.atlassian.net/wiki/spaces/UDOCES/pages/3232334029/Quick+start+guide#Adapting-this-example) a sus necesidades empresariales
- Cree transformaciones de datos más complejas con múltiples [nodos Iniciar Atributo](https://squaregps.atlassian.net/wiki/spaces/UDOCES/pages/3232334272/Initiate+Attribute+node?atlOrigin=eyJpIjoiMTliMWExNWE3MzBlNGZlMTkzZmM5YTk0MDMwM2JjYzIiLCJwIjoiYyJ9)
- Establezca [destinos de salida](https://squaregps.atlassian.net/wiki/spaces/~7120201a6252f8d34242e3bdb7409b5d34d953/pages/3192816141/Output+endpoint+node) adicionales para sus datos que puedan convertirse en perfiles reutilizables para configuraciones coherentes
- [Gestionar flujos ya creados](https://squaregps.atlassian.net/wiki/spaces/UDOCES/pages/3232334081/Flow+management?atlOrigin=eyJpIjoiZmNkYWEyYzQ0NDNkNGMxZGI4NDI3OThmNzc1ZDg3M2YiLCJwIjoiYyJ9) para ajustar el procesamiento de datos a cualquier cambio al que se enfrente
- [Diseñar flujos avanzados](https://squaregps.atlassian.net/wiki/spaces/UDOCES/pages/3232334496/Flow+configuration+example?atlOrigin=eyJpIjoiYmIxZDIyZDAyODk1NGYzZmE2NGFlOGU3ZWI4ZmUxNzgiLCJwIjoiYyJ9) para escenarios empresariales específicos utilizando diferentes combinaciones y configuraciones de nodos

### Adaptación de este ejemplo

Este ejemplo puede adaptarse a diversos casos de uso industrial modificándolo:

- **Selección de dispositivos**: Elija los dispositivos pertinentes para sus activos específicos
- **Conversión de unidades**: Ajuste las fórmulas en función de sus unidades de medida estándar
- **Métricas calculadas**: Cree indicadores específicos del sector en función de sus necesidades empresariales
- **Configuración de salida**: Conéctese a su plataforma de análisis o base de datos específica

El patrón básico de recopilación, transformación y reenvío sigue siendo coherente en todos los sectores, lo que lo convierte en una plantilla versátil para el procesamiento de datos de IoT.

## Acceso API

También se puede acceder a las funciones de IoT Logic mediante programación a través de la API de Navixy. Esto permite a los desarrolladores automatizar la creación, gestión y supervisión de flujos.

> [!INFO]
> Por motivos de seguridad, el acceso a la API requiere los permisos adecuados. Póngase en contacto con el administrador de su cuenta para asegurarse de que dispone de los derechos de acceso necesarios.

Para obtener la documentación completa de la API, parámetros, formatos de solicitud/respuesta y ejemplos de código, consulte la [documentación de la Navixy IoT Logic API](https://developers.navixy.com/docs/iot-logic-api) .

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