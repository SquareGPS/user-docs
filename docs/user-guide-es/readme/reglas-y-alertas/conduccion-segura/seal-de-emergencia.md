# Señal de emergencia

## Visión general

La función "Señal de emergencia", comúnmente conocida como "botón SOS", es una función de seguridad esencial diseñada para dispositivos GPS equipados con un botón de emergencia. Este botón puede ser un componente externo o estar integrado en un dispositivo de seguimiento personal. Sirve como salvavidas vital en situaciones críticas, permitiendo a empleados y particulares solicitar ayuda rápidamente cuando más se necesita.

## Configuración de reglas

La funcionalidad de esta regla depende de las capacidades y la configuración del dispositivo, por lo que no es necesario configurar ninguna regla específica.

Para los ajustes habituales, consulte [Reglas y alertas](../../../guia-del-usuario/reglas-y-alertas/).

<details>

<summary>Conexión de un botón externo a la entrada del dispositivo GPS de un vehículo</summary>

Dependiendo del dispositivo, el botón de Emergencia puede conectarse a una entrada dedicada, diseñada específicamente para esta función, o a una entrada discreta general. Si está conectado a una entrada discreta, debe crear la entrada dentro del menú Dispositivos y Ajustes, en la sección Sensores y Botones. En este caso, seleccione el tipo de regla "Disparo por entrada" para una configuración adecuada.

</details>

## Detalles del funcionamiento del sistema

* **Reinicia el temporizador:** La alerta "Señal de emergencia" tiene un temporizador de restablecimiento de 30 segundos, lo que significa que la alerta no se activará más de una vez cada 30 segundos. Si se produce un evento mientras la regla está esperando el reinicio, la plataforma omitirá el evento, incluso en los informes.
* **Múltiples dispositivos:** Esta regla permite a los usuarios seleccionar varios rastreadores de los que desean recibir notificaciones. Los rastreadores seleccionados deben admitir el evento "Señal de emergencia", y esta función debe estar integrada en la plataforma para esos rastreadores. De este modo, los usuarios pueden supervisar cómodamente las señales de emergencia en varios dispositivos.
* **Alerta de eventos independiente del GPS:** La plataforma reconoce y contabiliza este tipo de evento de hardware aunque el paquete de datos carezca de coordenadas GPS válidas. El evento se mostrará independientemente de si se ha producido dentro o fuera de las geocercas definidas. En este caso se ignoran los ajustes de geocerca Dentro/Fuera, lo que garantiza que no se omita ningún evento crítico.
