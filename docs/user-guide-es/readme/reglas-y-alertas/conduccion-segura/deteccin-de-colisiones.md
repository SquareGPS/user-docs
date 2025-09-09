# Detección de colisiones

## Visión general

La regla "Detección de colisiones" supervisa y le avisa de eventos de conducción significativos mediante la detección específica de colisiones de vehículos. Esta regla ayuda a mantener el conocimiento del comportamiento del conductor y permite a su equipo de despacho responder rápidamente a cualquier accidente.

Esta regla depende del hardware y se activa mediante los datos del acelerómetro del dispositivo GPS. El evento se genera en el dispositivo GPS y la plataforma muestra la alerta en función de los datos recibidos.

La detección precisa de colisiones requiere una instalación adecuada del rastreador, incluido el cableado correcto y la alineación a lo largo de los ejes x, y, z. El manual de usuario del rastreador suele incluir instrucciones detalladas para la instalación.

## Configuración de reglas

Como esta regla se procesa en el dispositivo GPS y no en la nube, no se requiere ninguna configuración adicional.

Para los ajustes habituales, consulte [Reglas y alertas](../../../guia-del-usuario/reglas-y-alertas/).

## Detalles del funcionamiento del sistema

* **Reinicia el temporizador:** La alerta "Detección de colisión" tiene un temporizador de restablecimiento de 1 minuto, lo que significa que la alerta no se activará con más frecuencia que una vez por minuto. Si se detecta otro evento de colisión dentro de este periodo de reinicio, se omitirá de la plataforma y de los informes.
* **Múltiples dispositivos:** Esta regla le permite seleccionar varios rastreadores para las notificaciones. El único requisito es que los rastreadores admitan eventos de Detección de Colisiones y tengan esta función integrada en la plataforma. Esto permite supervisar los eventos de colisión en varios vehículos.
* **Alerta de eventos independiente del GPS:** La plataforma registrará y mostrará un evento de Detección de Colisión incluso si el paquete de datos carece de coordenadas GPS válidas. El sistema prioriza la visualización de eventos críticos, independientemente de si ocurrieron dentro o fuera de las geocercas designadas. La configuración de la geocerca Dentro/Fuera se ignora en esta regla para garantizar que no se pierda ningún evento crucial...
