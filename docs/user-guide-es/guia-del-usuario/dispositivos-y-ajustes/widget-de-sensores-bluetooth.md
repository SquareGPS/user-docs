# Widget de sensores Bluetooth

En **Widget de sensores Bluetooth** en Navixy le permite configurar sensores Bluetooth externos que se conectan a modelos de rastreador específicos. Estos sensores suelen transmitir datos sin procesar, incluyendo únicamente la dirección MAC y el valor del sensor.

Para garantizar que la plataforma interpreta correctamente estos datos, debes configurar manualmente cada sensor dentro de este widget.

#### Cómo configurar los sensores Bluetooth

{% stepper %}
{% step %}
**Accede al widget de sensores Bluetooth**

Vaya a la sección **Dispositivos y configuración**. Seleccione el dispositivo específico para el que desea configurar los sensores Bluetooth.
{% endstep %}

{% step %}
**Especifique la dirección MAC**

Introduzca la dirección MAC única del sensor Bluetooth que desea configurar. Esto garantiza que la plataforma reconozca y asocie el sensor con el dispositivo correcto.
{% endstep %}

{% step %}
**Seleccione el tipo de sensor**

Elija el tipo de sensor adecuado entre las siguientes opciones:

* **Sensor de temperatura y humedad**: Para controlar las condiciones ambientales.
* **Sensor de presión y temperatura de los neumáticos**: Para seguir el estado de los neumáticos en tiempo real.
* **Botón de pánico**: Para alertas de emergencia.
* **Clave de identificación**: Para el control de acceso y la seguridad.
* **Por sensor**: Para controlar el estado de la puerta (abierta/cerrada).
* **Relé**: Para controlar circuitos eléctricos.
{% endstep %}

{% step %}
**Guarda la configuración**

Una vez que haya introducido la dirección MAC y seleccionado el tipo de sensor, guarde la configuración. El sistema creará automáticamente los sensores correspondientes en el widget Sensores y botones, vinculándolos a las funcionalidades adecuadas dentro de la plataforma.
{% endstep %}
{% endstepper %}

Este proceso garantiza que sus sensores Bluetooth estén correctamente configurados y que sus datos sean interpretados con precisión por la plataforma Navixy, mejorando la funcionalidad y fiabilidad de sus operaciones de gestión de flotas y seguimiento de activos.
