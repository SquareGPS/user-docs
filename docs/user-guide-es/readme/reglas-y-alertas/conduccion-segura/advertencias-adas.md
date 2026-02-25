# Advertencias ADAS

## Visión general

Los sistemas avanzados de asistencia al conductor (ADAS) están diseñados para mejorar la seguridad del conductor mediante alertas y controles en tiempo real durante la conducción. Los ADAS utilizan algoritmos avanzados y tecnologías de visión artificial basadas en inteligencia artificial para analizar los datos de las cámaras de vídeo y los sensores lidar. Esto permite al sistema detectar con precisión posibles peligros y comportamientos de conducción inseguros, garantizando un enfoque proactivo de la seguridad vial en línea con los últimos avances en telemática de vehículos.

La plataforma Navixy registra y puede alertar a los usuarios de los siguientes eventos:

| **Evento**                                       | **Descripción**                                                                                                                                                                      |
| ------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Aviso de salida de carril (LDW)**              | Alerta al conductor cuando el vehículo se desvía involuntariamente de su carril, ayudando a evitar posibles colisiones debidas a la falta de atención del conductor.                 |
| **Aviso de colisión frontal (FCW)**              | Avisa al conductor de una colisión inminente con un vehículo u objeto situado delante, lo que permite frenar a tiempo o realizar una acción evasiva para evitar un accidente.        |
| **Aviso de seguimiento de la trayectoria (HMW)** | Controla la distancia con el vehículo que circula por delante y alerta al conductor si la distancia de seguimiento se vuelve insegura, fomentando hábitos de conducción más seguros. |
| **Peatón en zona de peligro (PDZ)**              | Detecta cuando un peatón se encuentra cerca del vehículo, especialmente en los ángulos muertos, para evitar accidentes y mejorar la seguridad vial.                                  |
| **Aviso de colisión de peatones (PCW)**          | Emite un aviso cuando detecta una posible colisión con un peatón, dando tiempo al conductor para reaccionar y evitar un incidente.                                                   |
| **Reconocimiento de señales de tráfico (TSR)**   | Identifica y avisa al conductor de señales de tráfico importantes, como límites de velocidad o señales de stop, para garantizar el cumplimiento de la normativa vial.                |

La supervisión de estos eventos ayuda a mejorar la concienciación de los conductores, reducir el riesgo de accidentes y garantizar el cumplimiento de las normas de tráfico. Esto, a su vez, apoya los esfuerzos para mejorar el rendimiento del conductor, mitigar la responsabilidad y evitar costosas multas o reparaciones del vehículo.

## Configuración de reglas

### Selección de eventos

Dado que los eventos ADAS se procesan en el dispositivo telemático de vídeo en lugar de en la nube, no se requiere ninguna configuración adicional. Solo tienes que seleccionar los eventos que deseas supervisar para garantizar un seguimiento exhaustivo del comportamiento del conductor.

Para los ajustes habituales, consulte [Reglas y alertas](../../../guia-del-usuario/reglas-y-alertas/).

## Detalles del funcionamiento del sistema

* **No hay temporizador de reinicio:** La alerta "ADAS" no tiene temporizador de reinicio, lo que significa que se activará una alerta cada vez que se detecte un evento ADAS.
* **Múltiples dispositivos:** Los usuarios pueden seleccionar varios rastreadores para recibir notificaciones ADAS. El único requisito es que los rastreadores elegidos admitan eventos ADAS y que esta función esté integrada en la plataforma. Esto permite una supervisión eficiente de los comportamientos de conducción en toda una flota de vehículos.
* **Alerta de evento independiente del GPS:** La plataforma reconocerá y mostrará los eventos ADAS incluso si el paquete de datos del rastreador carece de coordenadas GPS válidas. En estos casos, se ignoran los ajustes de geocerca **Dentro/Fuera**, lo que garantiza que no se pierdan eventos críticos.
