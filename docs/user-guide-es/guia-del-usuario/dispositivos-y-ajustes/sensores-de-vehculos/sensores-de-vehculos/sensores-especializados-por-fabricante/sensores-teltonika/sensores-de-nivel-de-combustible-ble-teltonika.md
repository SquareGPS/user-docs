# Sensores de nivel de combustible BLE (Teltonika)

Muchos [Dispositivos GPS Teltonika](https://www.navixy.com/devices/teltonika/) admiten sensores de combustible inalámbricos que se conectan mediante Bluetooth. Las ventajas de utilizar estos sensores de combustible Bluetooth son significativas:

* **Sin cables**: El sensor y el seguidor no necesitan conexión física, lo que simplifica la instalación.
* **Independencia de fuentes de alimentación externas**: Estos sensores vienen con una batería integrada que puede durar varios años sin necesidad de recarga.
* **Datos complementarios**: Además de los niveles de combustible, el sensor también transmite datos sobre la temperatura, la humedad y el nivel de carga de la batería.

## Preparación del dispositivo GPS

Para preparar su dispositivo GPS Teltonika para la integración del sensor de combustible Bluetooth, siga estos pasos.

<figure><img src="https://www.navixy.com/wp-content/uploads/2019/09/teltonika.configurator_2019-09-28_13-56-33-600x365.png" alt=""><figcaption></figcaption></figure>

1. **Descargar el configurador Teltonika**: Obtén la aplicación desde el sitio web oficial de Teltonika.
2. **Actualizar el firmware**: Asegúrese de que su dispositivo está ejecutando la última versión del firmware.
3. **Ejecutar el configurador**:

* Ir a la **Sistema** ficha.
* Cambia el protocolo de transferencia de datos a **Códec 8 ampliado**.

4. **Conectar el sensor de combustible**:

* Navegue hasta el **Bluetooth** en el configurador.
* Conecte el sensor de combustible al rastreador.

5. **Habilitar los parámetros necesarios**:

* Ir a la **E/S** ficha.
* Asegúrese de que el parámetro correspondiente al sensor de combustible está activado.

{% hint style="warning" %}
**Codec 8 ampliado** es un protocolo de comunicación propiedad de Teltonika que admite hasta 65.535 parámetros de datos (AVL ID), lo que permite una transmisión de datos más detallada en comparación con el Codec 8 estándar, que sólo admite 255.
{% endhint %}

## Configuración del sensor en la plataforma Navixy

Una vez que el rastreador esté conectado y transmitiendo datos de combustible, sigue estos pasos para configurar los sensores correspondientes en la plataforma Navixy.

<figure><img src="https://www.navixy.com/wp-content/uploads/2019/09/chrome_2019-09-28_13-59-40-600x296.png" alt=""><figcaption></figcaption></figure>

1. **Crear un nuevo sensor de medición**:

* Navega hasta Dispositivos y ajustes → Sensores y botones.
* Haga clic en Crear un nuevo [sensor de medición](../../sensor-de-medicin/).

2. **Configurar el sensor**:

* Seleccione la entrada "BLE: Nivel LLS".
* Ajuste el tipo de sensor y las unidades. Si es necesario, rellene la tabla de calibración y ajuste otros parámetros.

3. **Repetir para los sensores adicionales**:

* Si tiene varios sensores de combustible, repita el proceso de configuración para cada sensor, seleccionando la entrada adecuada para cada uno.

4. **Supervisar e informar**:

* Una vez configurado, puedes controlar el nivel de combustible en el widget designado de la plataforma.
* También puede generar informes detallados sobre el consumo de combustible.

Esta configuración le permite utilizar plenamente las capacidades de los sensores de combustible Bluetooth Teltonika, proporcionando datos precisos y en tiempo real sobre los niveles de combustible, temperatura y más.
