# Cambio de nivel de combustible

## Visión general

Controlar los niveles de combustible es crucial para gestionar su consumo y detectar usos no autorizados. La regla de cambio de nivel de combustible está diseñada para proporcionar notificaciones en tiempo real siempre que se produzcan cambios significativos en los niveles de combustible, como aumentos o descensos repentinos.

Estas notificaciones pueden enviarse a través de la interfaz de usuario web, SMS o correo electrónico, y pueden consolidarse en informes. Esta supervisión proactiva ayuda a los usuarios a responder rápidamente a los cambios en el nivel de combustible, lo que puede reducir los costes de combustible y resolver disputas entre los empleados.

{% hint style="info" %}
Antes de configurar esta regla, asegúrese de que el sensor de nivel de combustible que pretende monitorizar está correctamente configurado. Para obtener instrucciones detalladas sobre la instalación y configuración de los sensores de nivel de combustible, consulte la página Sensor de medición.
{% endhint %}

## Configuración de reglas

#### Sensor

Especifique el sensor de nivel de combustible que se utilizará como fuente de notificaciones y análisis. El número de cambios de combustible indicados está regulado por el parámetro Precisión del sensor de nivel de combustible, que puede ajustarse en el menú Sensores y botones widget.

Para los ajustes habituales, consulte [Reglas y alertas](../).

## Detalles del funcionamiento del sistema

* La plataforma suaviza los datos del sensor y compara el cambio total en un intervalo de 10 minutos con el ajuste de precisión del sensor de combustible para determinar si debe activarse una notificación. Por ejemplo, con un ajuste de Precisión del 5%, un cambio de nivel de combustible de 5 litros o más para un depósito de 100 litros en 10 minutos activará una alerta. Si el cambio acumulado alcanza o supera este umbral, la plataforma enviará una notificación.
* La estimación del volumen de cambio de combustible no se incluye actualmente en las notificaciones, pero estará disponible en breve.
* La alerta "Cambio de nivel de combustible" tiene un temporizador de reinicio de 15 minutos, lo que significa que la alerta no se activará más a menudo que una vez cada 15 minutos. Si se produce un cambio en el nivel de combustible mientras la regla está en su periodo de reinicio, la plataforma omitirá el evento, incluso en los informes.
* Esta regla sólo admite un dispositivo por regla. Esta limitación se debe a las complejidades que conlleva la referencia cruzada de varios sensores de medición con diferentes rastreadores, tablas de calibración y otros aspectos de medición y filtrado.
