# Conducción dura

## Visión general

La norma "Conducción dura" está diseñada para ayudar a las empresas a controlar y mejorar el comportamiento al volante, garantizando un funcionamiento más seguro de los vehículos y reduciendo el riesgo de accidentes. Esta norma es especialmente valiosa para flotas, empresas de alquiler de vehículos y operaciones logísticas, en las que la calidad de la conducción repercute directamente en los costes de mantenimiento de los vehículos, la seguridad y la satisfacción del cliente. Al detectar y responder a los incidentes de conducción accidentada, las empresas pueden gestionar mejor sus vehículos, reducir el desgaste y mantener un alto nivel de servicio.

Esta regla funciona utilizando el acelerómetro integrado en los dispositivos para controlar las aceleraciones repentinas, las frenadas bruscas y los giros bruscos. Cuando el dispositivo GPS detecta alguno de estos eventos, envía los datos a la plataforma, que genera alertas y registra los incidentes para su revisión. Para utilizar esta regla, asegúrese de que la función de detección de conducción brusca está configurada correctamente en la aplicación Ajustes del dispositivo o el configurador de seguidores.

## Configuración de reglas

Asegúrese de que la función de conducción dura está configurada en **Dispositivos y ajustes,** específicamente en el widget **Conducción temeraria**, o a través de la herramienta de configuración del dispositivo. Una vez configurada, los usuarios pueden crear y gestionar la regla desde la plataforma.

No se requiere ninguna otra configuración específica para esta regla. Para los ajustes habituales, consulte [Reglas y alertas](../../../guia-del-usuario/reglas-y-alertas/).

## Detalles del funcionamiento del sistema

* **Reinicia el temporizador:** La alerta "Conducción temeraria" tiene un temporizador de reinicio de 10 segundos, lo que significa que la alerta no se activará con más frecuencia que una vez cada 10 segundos. Si se produce un evento durante el periodo de restablecimiento, la plataforma suprimirá la alerta para que las notificaciones y los informes sean precisos y manejables.
* **Múltiples dispositivos:** Los usuarios pueden aplicar esta regla a varios rastreadores, siempre que admitan la detección de conducción temeraria y tengan esta función integrada en la plataforma. Esto permite a los usuarios controlar eficazmente los incidentes de conducción dura en varios vehículos o dispositivos.
* **Procesamiento de eventos independiente del GPS:** La plataforma procesa y muestra los incidentes de conducción difíciles aunque el paquete de datos carezca de coordenadas GPS válidas. Estos eventos se registran independientemente de si ocurren dentro o fuera de una geovalla designada. En este caso, la configuración de la geocerca Dentro/Fuera se omite para garantizar que no se pierda ningún evento crítico.
