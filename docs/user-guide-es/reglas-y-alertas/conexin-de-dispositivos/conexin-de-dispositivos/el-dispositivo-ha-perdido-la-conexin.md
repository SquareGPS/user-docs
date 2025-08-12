# El dispositivo ha perdido la conexión

## Visión general

La regla "Pérdida de conexión del dispositivo" está diseñada para controlar y notificar a los usuarios cuando un dispositivo GPS pierde su conexión con la plataforma. Esta pérdida de conexión puede deberse a varios motivos, como problemas de hardware (descarga de la batería, desconexión de la alimentación, fallo del hardware, problemas de cableado) o de comunicación (problemas de la red GSM, mala cobertura, fondos insuficientes o cortes del proveedor).

Esta regla ayuda a los usuarios a mantenerse informados sobre el estado operativo de sus dispositivos de seguimiento y permite responder con rapidez a posibles problemas, como averías en los equipos, interferencias GSM o robos de vehículos. También ayuda a recopilar datos valiosos para optimizar las operaciones, como la identificación de zonas con mala cobertura o la detección de fallos en el equipo o el proveedor de servicios.

> \[!INFO] Para supervisar en tiempo real el estado de la alimentación del dispositivo, se recomienda utilizar la función ["Función de autoinforme "Dispositivo interruptor ON/OFF](../../../../../wiki/pages/createpage.action)si el dispositivo GPS lo admite.

## Configuración de reglas

#### Tiempo fuera de línea más de

El ajuste "Tiempo de desconexión superior a" permite a los usuarios definir un temporizador personalizado que inicie la cuenta atrás después de que el rastreador pase a estado rojo (indicando pérdida de conexión). El periodo total de desconexión se calcula de la siguiente manera:

* **Tiempo de espera por defecto (10 minutos)**: Es el periodo estándar tras el cual se considera que un rastreador ha perdido la conexión si no se reciben datos del dispositivo.
* **Su tiempo de espera fuera de línea personalizado**: El tiempo adicional especificado por el usuario en el campo "Offline time more than".

Por ejemplo, si un dispositivo pierde la conexión a las 10:10 AM, tras el tiempo de espera predeterminado de 10 minutos, se marcará con un estado rojo a las 10:20 AM. Si el usuario establece el tiempo de espera sin conexión personalizado en 7 minutos, la notificación se activará a las 10:27 AM.

Para conocer la configuración habitual de las reglas, consulte [Normas y notificaciones](../../).

## Detalles del funcionamiento del sistema

* La alerta de "Conexión perdida del dispositivo" tiene un temporizador de restablecimiento de 10 segundos, lo que significa que la alerta no se activará más a menudo que una vez cada 10 segundos. Si se produce un evento mientras la regla espera el reinicio, la plataforma lo omitirá, incluso en los informes.
* Esta regla se procesa en la nube y no está vinculada a ningún hardware específico, por lo que es aplicable a varios rastreadores simultáneamente. Esta flexibilidad le permite gestionar varios rastreadores con una sola regla.
* Los diferentes modelos de dispositivos tienen diferentes tiempos de espera a nivel de transporte. Si incluye varios modelos de rastreador en la misma regla, los periodos de notificación pueden variar en función de la configuración de tiempo de espera específica del dispositivo. Esta variación se produce porque la notificación se activa mediante una combinación del tiempo de espera predeterminado del rastreador y el tiempo de espera sin conexión personalizado especificado en la configuración de la regla.

Al utilizar esta regla, los usuarios pueden asegurarse de que se les informa rápidamente de cualquier interrupción en la conectividad del rastreador, lo que les permite tomar medidas rápidas para solucionar posibles problemas.
