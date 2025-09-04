# Dispositivo encendido/apagado

## Visión general

La regla "Dispositivo encendido/apagado" permite a los usuarios controlar cuándo un dispositivo GPS está encendido o apagado. Esta regla es especialmente útil para los administradores que necesitan asegurarse de que los empleados utilizan los dispositivos GPS de acuerdo con las políticas prescritas durante las horas de trabajo. Proporciona información valiosa sobre los patrones de uso de los dispositivos, ayudando a prevenir su uso indebido y garantizando su correcto funcionamiento.

{% hint style="danger" %}
Esta regla sólo se aplica a los dispositivos que tienen la capacidad de informar sobre su estado de encendido. En otras palabras, el dispositivo GPS debe ser capaz de enviar notificaciones a la plataforma cuando está encendido o apagado. Si un dispositivo carece de esta funcionalidad, la regla no se puede aplicar, ya que la plataforma no recibiría los datos necesarios para activar las notificaciones, pero aún se puede utilizar el dispositivo independiente "[El dispositivo ha perdido la conexión](../../../readme/reglas-y-alertas/conexin-de-dispositivos/el-dispositivo-ha-perdido-la-conexin.md)".
{% endhint %}

## Configuración de reglas

### Rastreador encendido

La regla "Seguidor encendido" activa una notificación cuando se enciende un seguidor, siempre que el dispositivo disponga de las funciones de notificación necesarias.

**Puntos clave:**

* **Propósito:** Controla cuándo se enciende un rastreador, lo que te ayuda a realizar un seguimiento de cuándo vuelven a funcionar los dispositivos.
* **Reiniciar temporizador:** La alerta "Rastreador conectado" incluye un Temporizador de reinicio de 60 segundosque evita que se envíen varias alertas en un mismo minuto, reduciendo así las notificaciones innecesarias.
* **Configuración:** La regla requiere una configuración mínima y admite múltiples rastreadores siempre que tengan capacidad para informar de eventos de encendido.

### Rastreador apagado

La regla "Seguidor apagado" activa una notificación cuando un seguidor se apaga o pierde la conexión, siempre que el dispositivo pueda informar de este evento.

**Puntos clave:**

* **Propósito:** Le avisa cuando un rastreador se apaga o pierde la conexión, lo que le permite responder rápidamente a posibles problemas.
* **Reiniciar temporizador:** Esta alerta incluye un Temporizador de reinicio de 10 segundospara garantizar que las alertas no se activen más de una vez cada dos años. 10 segundosevitando el exceso de notificaciones.
* **Configuración:** Al igual que la regla "Seguidor encendido", esta regla también requiere una configuración mínima y puede aplicarse a varios seguidores que admitan la notificación de eventos de apagado.

Para los ajustes habituales, consulte [Reglas y alertas](../).

## Detalles del funcionamiento del sistema

* La regla "Seguidor encendido/apagado" funciona en función de los eventos de hardware generados por el seguidor cuando se enciende o se apaga. Estos eventos se transmiten a la plataforma y se procesan para su notificación.
* La regla es flexible y puede aplicarse a varios rastreadores simultáneamente, siempre que admitan la función de eventos ON/OFF.
* Si la plataforma identifica un evento de hardware de este tipo sin coordenadas válidas, el evento se sigue contando como válido y se muestra, lo que garantiza que no se pierda ningún evento crucial.
* El sistema le permite realizar un seguimiento de estos eventos independientemente de si se producen dentro o fuera de las geovallas definidas, ya que la lógica de geovallas se omite para estos eventos específicos con el fin de garantizar una supervisión exhaustiva.

Esta regla es fundamental para mantener la integridad operativa de su flota, garantizar que todos los rastreadores funcionan como se espera y permitir una respuesta rápida a cualquier cambio inesperado en el estado de los rastreadores.
