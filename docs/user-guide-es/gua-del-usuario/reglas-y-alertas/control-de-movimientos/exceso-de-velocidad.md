# Exceso de velocidad

## Visión general

El objetivo de la norma de detección del exceso de velocidad es ayudar a las empresas a mejorar sus medidas generales de seguridad controlando y abordando los casos de exceso de velocidad. De este modo se garantiza el cumplimiento de los límites de velocidad, se fomenta un comportamiento responsable al volante entre los empleados y se reduce el riesgo de accidentes. La plataforma ofrece dos métodos para detectar el exceso de velocidad:

### Método I. Aceleración procesada en la nube

Este método se basa en los datos de velocidad de los rastreadores GPS para identificar el exceso de velocidad. La plataforma telemática analiza los datos de velocidad de los paquetes de datos GPS para comprobar si se ha superado el límite de velocidad especificado. Aunque este método es menos preciso que el exceso de velocidad detectado por el dispositivo, puede utilizarse con cualquier rastreador GPS que informe de la velocidad. Es una opción adecuada para dispositivos que no pueden detectar de forma nativa eventos de exceso de velocidad.

### Método II. Exceso de velocidad detectado por el dispositivo

Este método utiliza el hardware del rastreador GPS para detectar el exceso de velocidad. El propio dispositivo calcula cuándo se produce un exceso de velocidad mediante comandos remotos o software de configuración del dispositivo. La plataforma telemática genera entonces notificaciones basadas en estos cálculos. Este método es muy preciso y funciona con la mayoría de los rastreadores modernos que pueden enviar eventos de exceso de velocidad directamente a la plataforma.

## Configuración de reglas

#### Límite de velocidad, procesado en la nube

La configuración del límite de velocidad define el umbral a partir del cual se activa la regla. Cuando la plataforma recibe datos de velocidad del dispositivo, compara este valor con el límite especificado. Si la velocidad supera el límite, la plataforma genera una alerta de exceso de velocidad.

#### Límite de velocidad, Dispositivos procesados

Para los eventos de exceso de velocidad detectados por el dispositivo, no hay una configuración específica en las Reglas y Notificaciones. En su lugar, utilice el widget Configuración del dispositivo para configurar remotamente el límite de velocidad en el dispositivo.

Para los ajustes habituales, consulte [Normas y notificaciones](https://squaregps.atlassian.net/wiki/spaces/USERDOCS/pages/2761228324/Rules+and+Notifications#Manage-rules).

## Detalles del funcionamiento del sistema

* **Requisitos de hardware y procesamiento de eventos**
  * **Aceleración (procesamiento en la nube)**: Esta regla puede aplicarse a la mayoría de los rastreadores que envían datos de velocidad en sus paquetes. La regla se procesa en la nube, donde la plataforma utiliza los datos de velocidad de los paquetes del dispositivo para determinar si se ha superado el límite de velocidad. La alerta tiene un temporizador de reinicio de 15 minutos, lo que significa que la alerta no se activará más de una vez cada 15 minutos. Si se produce un evento mientras la regla está esperando el reinicio, la plataforma omitirá el evento, incluso en los informes.
  * **Exceso de velocidad (detectado por el dispositivo)**: Esta regla sólo es aplicable a los rastreadores que admiten el envío de eventos de exceso de velocidad basados en hardware. El propio dispositivo procesa la regla, y la plataforma genera notificaciones basadas en los cálculos realizados por el hardware. La alerta tiene un temporizador de restablecimiento de 1 minuto, lo que significa que la alerta no se activará más a menudo que una vez cada minuto. Si se produce un evento mientras la regla está esperando el reinicio, la plataforma omitirá el evento, incluso en los informes.
* **Múltiples rastreadores**: La regla permite la selección de varios rastreadores dentro de una misma regla, lo que permite una supervisión exhaustiva de varios vehículos o dispositivos.
* **Deriva del GPS**: El sistema puede generar una alerta de exceso de velocidad aunque se produzcan desvíos del GPS. Aunque se filtran las coordenadas GPS no válidas, pueden aparecer pequeñas desviaciones GPS en el seguimiento. Sin embargo, la plataforma ofrece varios métodos para minimizar estas ocurrencias, dependiendo de la funcionalidad del modelo de rastreador. Para obtener información detallada sobre cómo evitar el desvío del GPS, consulte el manual del dispositivo. Esto garantiza una detección de eventos más precisa y fiable, mejorando la eficacia general del seguimiento.
