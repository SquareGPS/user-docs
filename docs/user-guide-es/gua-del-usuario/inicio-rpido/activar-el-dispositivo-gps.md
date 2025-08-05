# Activar el dispositivo GPS

Activar un dispositivo significa simplemente añadir un nuevo dispositivo a tu cuenta de usuario. Puede activar cualquier [dispositivo de localización GPS compatible](https://navixy.com/devices/). Si su modelo aún no es compatible, póngase en contacto con su [proveedor de servicios](proveedor-de-servicios.md) para conseguir que este dispositivo se integre con Navixy o encontrar un dispositivo alternativo con una funcionalidad similar.

Existen dos métodos para activar un dispositivo de localización GPS:

- [**Activación automática del dispositivo (recomendado)**](https://squaregps.atlassian.net/wiki/spaces/USERDOCS/pages/edit-v2/2732916764#Activate-GPS-device-automatically) - simplifica la instalación configurando automáticamente el dispositivo sin intervención manual.
- [**Activación manual del dispositivo**](https://squaregps.atlassian.net/wiki/spaces/USERDOCS/pages/edit-v2/2732916764#Activate-GPS-device-manually) - requiere que introduzca manualmente los ajustes de configuración, como las credenciales APN, la dirección del servidor y el puerto. Esta opción es útil si la configuración automática no es factible debido a limitaciones técnicas o regionales específicas.

## Activar automáticamente el dispositivo GPS

Navixy ofrece la ventaja única de la activación totalmente automática de dispositivos, que en la mayoría de los casos libera a los usuarios de la necesidad de configurar manualmente sus dispositivos. El proceso incluye el envío de comandos de configuración inicial al dispositivo que se está conectando a través de texto (SMS). Sin embargo, si la activación automática no es adecuada en su caso, siempre puede [Configurar el dispositivo manualmente](https://squaregps.atlassian.net/wiki/spaces/USERDOCS/pages/edit-v2/2732916764#Activate-GPS-device-manually).

### Pasos de activación automática

Una vez que acceda a su cuenta de usuario, vaya a Activar dispositivo en el menú de la izquierda. Se iniciará el asistente de activación.

1. **Etiqueta del objeto:** Elija la etiqueta que prefiera (por ejemplo, "Vehículo ABC").
2. **Marca y modelo del aparato:** Seleccione de una lista ordenada alfabéticamente y agrupada por fabricantes.
3. **Introduzca el número de teléfono de la tarjeta SIM:** Introduzca el número de teléfono de la tarjeta SIM instalada en el dispositivo.
  - La plataforma Navixy intentará determinar los ajustes APN apropiados basándose en el número de teléfono que ha proporcionado. Si no se encuentra la configuración APN, deberá introducirla manualmente.
4. **Recibir SMS de configuración:** Tras introducir la información necesaria, se enviarán al dispositivo algunos mensajes SMS con comandos de configuración. Asegúrese de que el dispositivo está encendido y es capaz de recibir estos mensajes.

En aproximadamente un minuto, el dispositivo debería conectarse y estar listo para su uso.

![](https://squaregps.atlassian.net/wiki/images/icons/grey_arrow_down.png)

Detalles sobre la configuración automática

Con la activación automática, la configuración del dispositivo es sencilla y fácil de usar, sin necesidad de cables USB, controladores ni utilidades de configuración. El proceso es rápido, lo que permite que el dispositivo esté operativo en cuestión de minutos. Los parámetros de configuración, como los ajustes APN y los detalles del servidor, se envían automáticamente por SMS desde el servidor al dispositivo. Una vez conectado, el dispositivo recibe actualizaciones automáticas, como la configuración del modo de seguimiento, principalmente a través del canal IP.

![](https://squaregps.atlassian.net/wiki/images/icons/grey_arrow_down.png)

Código de activación: ¿qué es?

Un código de activación es un código especial que puede ser proporcionado por su [proveedor de servicios](proveedor-de-servicios.md) junto con el dispositivo adquirido. El proveedor de servicios puede exigirte que introduzcas el código si quiere restringir el uso de hardware adquirido de otra fuente, o dejarlo opcional si te da la bienvenida para añadir cualquier dispositivo.

## Activar manualmente el dispositivo GPS

Mientras Navixy ofrece [activación automática del dispositivo GPS](https://squaregps.atlassian.net/wiki/spaces/USERDOCS/pages/edit-v2/2732916764#Activate-GPS-device-automatically) que simplifica el proceso de configuración, hay casos en los que la configuración manual puede ser necesaria o preferible. Esta sección cubre los pasos para la configuración manual del dispositivo y los casos de uso particulares en los que se prefiere este método.

### Pasos de la activación manual

Configura manualmente los parámetros esenciales de tu dispositivo, incluidos:

1. **Credenciales APN** \- Complete la configuración APN necesaria para su proveedor de red GSM.
2. **Dirección del servidor** - Elija la dirección del servidor en función de sus preferencias de residencia de datos y/o de las recomendaciones de su proveedor de servicios:
  - Plataforma de la UE: `tracker.navixy.com` (recomendado) o `52.57.1.136`
  - Plataforma estadounidense: `tracker.us.navixy.com` (recomendado) o `13.52.37.2`
3. **Puerto del servidor** - Este parámetro depende de la marca y el modelo de su aparato y se encuentra en la sección [Sección de dispositivos](https://navixy.com/devices/) de nuestro sitio web. Por ejemplo, para [Queclink GV65](https://www.navixy.com/devices/queclink/queclink-gv65/) el puerto del servidor sería 47764.

> [!WARNING]
> La zona horaria del dispositivo debe ajustarse a UTC+0h sin aplicar ningún desfase para que funcione correctamente. La zona horaria puede ajustarse posteriormente en las preferencias de usuario para cada usuario individual.

Para obtener ayuda con la conexión de su dispositivo específico y su elección de conectividad, póngase en contacto con el equipo de asistencia de su [proveedor de servicios](proveedor-de-servicios.md) para obtener información detallada.

### Cuando se requiere o se prefiere la activación manual

![](https://squaregps.atlassian.net/wiki/images/icons/grey_arrow_down.png)

Dispositivos móviles con problemas de entrega de SMS

Aunque Navixy y sus socios utilizan pasarelas SMS de alta capacidad de entrega y cobertura mundial, algunos países tienen normativas locales y problemas técnicos que pueden dificultar la entrega de comandos M2M enviados a través de mensajes de texto SMS. Estos problemas incluyen:

- **Normativa antispam**: Restricciones locales sobre nombres de remitentes de mensajes, longitud del texto y textos binarios.
- **Cuestiones técnicas**: Es posible que los símbolos especiales como $, # y % que se utilizan en los comandos de configuración no pasen correctamente por todos los nodos de red de la cadena de entrega de SMS.

Si la configuración automática falla debido a estos problemas, puede configurar manualmente los parámetros básicos, como las credenciales APN, la dirección del servidor y el puerto. El puerto del servidor y la dirección IP para un modelo de dispositivo específico se pueden encontrar en la sección Dispositivos de nuestro sitio web. Para obtener instrucciones detalladas de configuración, consulte el manual del dispositivo o consulte al servicio técnico de su [proveedor de servicios](proveedor-de-servicios.md).

![](https://squaregps.atlassian.net/wiki/images/icons/grey_arrow_down.png)

Dispositivos conectados mediante el protocolo MQTT

Los dispositivos MQTT, que utilizan el modelo Editor/Suscriptor para la comunicación, requieren un proceso de configuración único. Estos dispositivos deben configurarse manualmente porque no siguen el modelo cliente-servidor tradicional. Es necesario:

- Configure el dispositivo con los ajustes adecuados del agente MQTT.
- Configure manualmente los parámetros de conexión del dispositivo, como la dirección y el puerto del broker MQTT.
- Asegúrese de que se han configurado los temas y las credenciales de seguridad correctos.

Consulte la sección [Activate Your MQTT Device on Navixy](https://squaregps.atlassian.net/wiki/spaces/SC/pages/2732589133/Activate+Your+MQTT+Device+on+Navixy) para más detalles.

![](https://squaregps.atlassian.net/wiki/images/icons/grey_arrow_down.png)

Dispositivos conectados a través de la red LoRa

Las redes LoRa (de largo alcance), que se utilizan habitualmente para aplicaciones IoT debido a su bajo consumo y a sus capacidades de largo alcance, también requieren una configuración manual. Esto se debe a que las redes LoRa funcionan de forma diferente a las redes celulares estándar que utilizan pasarelas LoRaWAN y tienen requisitos específicos:

- Introducir manualmente las credenciales LoRaWAN del dispositivo
- Configure la dirección del servidor y los parámetros de red para que coincidan con las especificaciones de la red LoRa

Esta configuración es algo único para cada integración. Por lo tanto, consulte con el soporte técnico de su [proveedor de servicios](proveedor-de-servicios.md) sobre cómo integrar sus dispositivos LoRa y su pasarela LoRaWAN con Navixy.

![](https://squaregps.atlassian.net/wiki/images/icons/grey_arrow_down.png)

Dispositivos conectados a través de la red Satélite

Los dispositivos que utilizan redes por satélite como Iridium, Globalstar o Starlink necesitan una configuración manual debido a la naturaleza distinta de la comunicación por satélite, que difiere significativamente de las redes terrestres.

Los dispositivos que utilizan un enlace por satélite y la plataforma Navixy se comunican a través de una pasarela proporcionada por el operador del satélite. Esta pasarela actúa como puente entre la red de satélites e Internet, garantizando una transmisión de datos sin fisuras.

Para configurar un dispositivo de satélite para que sea supervisado en Navixy, es necesario:

- Introduzca manualmente las credenciales de la red de satélites
- Configure la dirección del servidor y los parámetros de comunicación para que coincidan con las especificaciones del proveedor de servicios por satélite.
- Compruebe que el dispositivo está correctamente registrado y puede comunicarse con la red de satélites.

Dado que cada integración puede ser única, consulte al servicio técnico de su [proveedor de servicios](proveedor-de-servicios.md) para obtener orientación sobre la integración de sus dispositivos y pasarela con Navixy.

![](https://squaregps.atlassian.net/wiki/images/icons/grey_arrow_down.png)

Dispositivos conectados a través de otros sistemas telemáticos o pasarelas

Hay situaciones en las que los dispositivos ya están conectados a otros sistemas telemáticos, como plataformas telemáticas OEM u otros servidores GPS, y usted necesita que sean supervisados tanto en esa plataforma como en Navixy.

Para controlar dispositivos que forman parte de otros sistemas telemáticos con Navixy, es necesario:

- **Configuración de la transmisión de datos**: Configure la otra plataforma para que envíe datos a Navixy utilizando uno de los protocolos admitidos por Navixy.
- **Añadir un dispositivo virtual**: Crear un dispositivo virtual en la plataforma Navixy que se asigna a la fuente de datos utilizando un identificador de dispositivo único.

Para más información, lea cómo [Integrar datos IoT de servidores y puertas de enlace](https://squaregps.atlassian.net/wiki/spaces/SC/pages/2732621933/Integrate+IoT+Data+from+Servers+and+Gateways).

## Preguntas frecuentes y solución de problemas

Si tiene algún problema al activar sus dispositivos, consulte nuestro [Preguntas frecuentes y guía de solución de problemas](https://squaregps.atlassian.net/wiki/spaces/USERDOCS/pages/2761031686/GPS+Device+Activation+Troubleshooting) o póngase en contacto con su [Proveedor de servicios](proveedor-de-servicios.md) de asistencia.