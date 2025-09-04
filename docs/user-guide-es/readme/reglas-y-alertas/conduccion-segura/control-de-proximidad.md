# Control de proximidad

## Visión general

La regla "Supervisión de proximidad" aprovecha la funcionalidad Bluetooth para proporcionar alertas en tiempo real cuando se producen eventos de proximidad. Esta regla está diseñada para detectar distancias precisas entre objetos equipados con dispositivos GPS que tienen capacidades BLE (Bluetooth Low Energy), así como entre dispositivos GPS y etiquetas BLE. Se trata de una herramienta versátil que ofrece numerosas aplicaciones en diversos sectores.

Esta regla es especialmente beneficiosa en entornos en los que es fundamental mantener distancias específicas. Por ejemplo:

* **Uso de equipos peligrosos:** Controle la proximidad de los operarios a equipos peligrosos, evitando accidentes y garantizando el cumplimiento de las normas de seguridad.
* **Distanciamiento social en entornos epidémicos:** Mantener y hacer cumplir las medidas de distanciamiento social en los lugares de trabajo o zonas públicas durante las epidemias, ayudando a reducir la propagación de enfermedades contagiosas.

Al emplear esta norma, las organizaciones pueden mejorar la seguridad, garantizar el cumplimiento de la normativa y optimizar la gestión de las actividades relacionadas con la proximidad.

## Configuración de reglas

La funcionalidad de esta regla depende de las capacidades y la configuración del dispositivo, por lo que no es necesario configurar ninguna regla específica.

Para los ajustes habituales, consulte [Reglas y alertas](../../../guia-del-usuario/reglas-y-alertas/).

## Los detalles de la plataforma:

* **Reinicia el temporizador:** La alerta "Supervisión de proximidad" tiene un temporizador de reinicio de 10 segundos, lo que significa que el evento de alerta no se producirá más de una vez cada 10 segundos. Si este tipo de evento se produce en el tiempo que la regla ha estado esperando el reinicio, este evento será omitido por la plataforma, incluyendo los informes.
* **Múltiples dispositivos:** Esta regla permite a los usuarios seleccionar varios dispositivos de los que desean recibir notificaciones. Los rastreadores seleccionados deben admitir el evento "Proximidad cercana", y esta función debe estar integrada en la plataforma para esos rastreadores. De este modo, los usuarios pueden supervisar cómodamente los eventos de varios dispositivos.
* **Alerta de eventos independiente del GPS:** Siempre que la plataforma identifique un evento de hardware de este tipo a partir de un paquete de datos del rastreador sin coordenadas válidas en él, la plataforma cuenta el evento como válido y lo muestra independientemente de si el evento se produjo dentro o fuera de las geocercas delimitadas para garantizar notificaciones críticas.
