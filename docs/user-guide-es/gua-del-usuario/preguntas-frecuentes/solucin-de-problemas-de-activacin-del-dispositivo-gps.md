# Solución de problemas de activación del dispositivo GPS

La activación de dispositivos de localización GPS en la plataforma Navixy suele ser sencilla gracias a activación automática del Activate GPS device dispositivo. No obstante, si tiene problemas, esta guía le ayudará a solucionar los problemas más comunes de activación de dispositivos.

### **La configuración de la zona horaria del dispositivo difiere de UTC+0h**

Asegúrese de que los dispositivos de seguimiento GPS están configurados en UTC+0h para evitar que el servidor Navixy malinterprete los datos. Reconfigure cualquier dispositivo configurado manualmente o conectado previamente a UTC+0h antes de la activación en Navixy.

![](https://squaregps.atlassian.net/wiki/images/icons/grey_arrow_down.png)

Seguir leyendo

**Asunto:**  
Cuando el software del servidor Navixy recibe datos de un dispositivo de seguimiento GPS, los datos vienen con una marca de tiempo. El servidor procesa estos datos basándose en las preferencias de zona horaria del usuario, lo que garantiza la precisión de los detalles del seguimiento y la elaboración de reportes en distintas zonas horarias. Sin embargo, el servidor espera que todos los datos del dispositivo estén en UTC+0h. Los dispositivos configurados manualmente o conectados previamente a otra plataforma pueden tener una zona horaria diferente, haciendo que Navixy malinterprete las marcas de tiempo, marcando potencialmente los datos como obsoletos o defectuosos.

**Solución:**  
Para un procesamiento y visualización de datos precisos, todos los dispositivos de seguimiento GPS deben estar configurados en UTC+0h. Si el dispositivo no está configurado en UTC+0h, el servidor Navixy podría interpretar los datos de forma incorrecta, lo que afectaría a la fiabilidad de los detalles del seguimiento y de los reportes.

**Recomendaciones para la resolución de problemas:**

1. Asegúrese de que el dispositivo está ajustado a UTC+0h antes de activarlo en Navixy.
2. Evita configurar la zona horaria local en el dispositivo.

### El dispositivo está apagado o carece de conexión GSM

Asegúrese de que el dispositivo está encendido y conectado a la red GSM. Para ello, compruebe el estado de encendido del dispositivo y verifique que está registrado en la red GSM. Si es posible, envía un SMS de prueba para confirmar que el dispositivo recibe los mensajes correctamente.

![](https://squaregps.atlassian.net/wiki/images/icons/grey_arrow_down.png)

Seguir leyendo

**Asunto:**

Cuando el servidor Navixy intenta comunicarse con un dispositivo de seguimiento GPS, el dispositivo debe estar encendido y conectado a la red GSM. Si el dispositivo está apagado o carece de conexión GSM, no podrán enviarse los comandos de activación, por lo que el dispositivo aparecerá como desconectado o no responderá.

**Solución:**

Para garantizar una comunicación correcta entre el servidor Navixy y el dispositivo de localización GPS, compruebe que el dispositivo está encendido y que dispone de una conexión GSM estable. Esto permite al servidor recibir y procesar los datos correctamente.

**Recomendaciones para la resolución de problemas:**

- Si tiene acceso físico al dispositivo, compruebe sus indicadores LED para confirmar que está encendido y conectado a la red GSM.
- Envíe un SMS al dispositivo con confirmación de entrega para comprobar el registro GSM. Si falla la entrega del SMS, el dispositivo no está registrado en la red GSM.

### El saldo de la tarjeta SIM es bajo o no hay servicio de Internet

Asegúrate de que la tarjeta SIM tiene saldo suficiente y de que el servicio de Internet está activado en ella para que el dispositivo pueda conectarse a la plataforma. Comprueba el saldo de la tarjeta SIM y verifica que tiene fondos suficientes para soportar el uso de datos de Internet. Además, confirma que el plan de datos de la tarjeta SIM incluye el tráfico de Internet adecuado para mantener una conexión estable con la plataforma.

![](https://squaregps.atlassian.net/wiki/images/icons/grey_arrow_down.png)

Seguir leyendo

**Asunto:**  
Durante el proceso de activación del dispositivo, un dispositivo de seguimiento intenta conectarse a la plataforma Navixy y transmitir sus datos de localización a través de Internet. Si la tarjeta SIM del dispositivo no tiene saldo suficiente o se han agotado los límites de tráfico de Internet, el dispositivo no puede conectarse a la plataforma. Esto provoca un fallo en el envío de datos de localización y otra información esencial, lo que hace que el dispositivo de rastreo no funcione.

**Solución:**  
Para garantizar una conectividad y una transmisión de datos ininterrumpidas, compruebe que la tarjeta SIM utilizada en el dispositivo de seguimiento dispone de saldo y tráfico GPRS adecuados. Supervise y recargue regularmente el saldo de la tarjeta SIM para evitar problemas de conectividad.

**Recomendaciones para la resolución de problemas:**

- Comprueba el saldo de la tarjeta SIM para asegurarte de que tiene fondos suficientes para soportar el acceso a Internet. Comprueba que el plan de la tarjeta SIM incluye suficientes datos de Internet para cubrir las necesidades de comunicación del dispositivo.
- Asegúrese de que los ajustes de APN están correctamente configurados en su dispositivo. Obtén los ajustes APN correctos de tu proveedor de red móvil, que suelen incluir el nombre APN, el nombre de usuario y la contraseña. Estos datos suelen encontrarse en el sitio web del proveedor o poniéndose en contacto con su servicio de atención al cliente.
- Si persisten los problemas de conectividad, ponte en contacto con el proveedor de la tarjeta SIM para confirmar que no hay problemas relacionados con la red que afecten al tráfico de Internet.

### IMEI o número de teléfono introducido incorrectamente

Verifique el IMEI y el número de teléfono introducidos durante la activación para garantizar su exactitud. Compruebe dos veces cada dígito del IMEI y del número de teléfono con la documentación o la etiqueta del dispositivo para asegurarse de que no hay errores. Corrija cualquier discrepancia para evitar problemas de activación y garantizar una comunicación satisfactoria con la plataforma.

![](https://squaregps.atlassian.net/wiki/images/icons/grey_arrow_down.png)

Seguir leyendo

**Asunto:**

Al activar un dispositivo en la plataforma Navixy, un IMEI o un número de teléfono incorrectos pueden hacer que falle la activación. Este error suele producirse debido a un error tipográfico o de introducción de los datos del dispositivo, lo que provoca que la comunicación entre el dispositivo y el servidor no sea satisfactoria.

**Solución:**

Para garantizar el éxito de la activación, vuelva a comprobar el IMEI y el número de teléfono introducidos para el dispositivo. Confirma que todos los dígitos son correctos y se corresponden con la información del dispositivo.

**Recomendaciones para la resolución de problemas:**

- Verifica el IMEI y el número de teléfono volviendo a comprobar la documentación o la etiqueta del dispositivo.
- Si la activación falla, borre el dispositivo y repita la activación volviendo a introducir cuidadosamente el IMEI y el número de teléfono para corregir posibles errores.

### La configuración está protegida con contraseña o número maestro

Si el dispositivo tiene ajustes personalizados, como contraseñas o números de teléfono maestros, puede impedir la configuración automática por parte de Navixy, lo que provocaría fallos en la activación. Elimine cualquier contraseña personalizada o número maestro antes de intentar la activación automática.

![](https://squaregps.atlassian.net/wiki/images/icons/grey_arrow_down.png)

Seguir leyendo

**Asunto:**  
Durante la activación del dispositivo, la plataforma Navixy envía comandos SMS de configuración al dispositivo desde el número de teléfono de servicio. Si el dispositivo se configuró previamente para recibir comandos de configuración desde un número maestro dedicado o si se estableció una contraseña personalizada, estos comandos podrían fallar, lo que provocaría una activación fallida.

**Solución:**  
Para permitir la activación automática, elimine cualquier contraseña personalizada o número maestro del dispositivo. Como alternativa, configure manualmente el dispositivo utilizando los comandos de activación adecuados.

**Recomendaciones para la resolución de problemas:**

- Elimine cualquier contraseña personalizada o número maestro del dispositivo antes de intentar la activación automática.
- Si falla la activación automática, [configurar manualmente](https://squaregps.atlassian.net/wiki/spaces/USERDOCSOLD/pages/2909016770/Manual+device+activation) el dispositivo mediante los comandos de activación proporcionados.

### Dispositivo no compatible o modificación del dispositivo

Asegúrate de que tu dispositivo está en la lista [con el apoyo de Navixy](https://navixy.com/devices/). Si no está seguro del fabricante y/o modelo, consulte con el proveedor de su dispositivo. También se recomienda actualizar el firmware del dispositivo a la última versión.

![](https://squaregps.atlassian.net/wiki/images/icons/grey_arrow_down.png)

Seguir leyendo

**Asunto:**  
Al activar un dispositivo de localización GPS en la plataforma Navixy, es importante que el modelo del dispositivo se identifique e indique correctamente durante la activación. Si el dispositivo no se identifica correctamente, es posible que los datos enviados desde el dispositivo no se analicen correctamente o se malinterpreten. Además, la versión de firmware para el mismo modelo puede ser obsoleta o una versión personalizada, causando problemas de compatibilidad.

**Solución:**  
Para resolver estos problemas, comprueba que tu dispositivo está en la lista de dispositivos compatibles y asegúrate de que tiene la última versión de firmware. Si tu dispositivo no está en la lista de modelos compatibles o tiene una versión de firmware personalizada, ponte en contacto con tu proveedor de servicios para obtener ayuda.

**Recomendaciones para la resolución de problemas:**

- Consulta nuestra lista de dispositivos compatibles.
- Actualice el firmware del dispositivo a la última versión.
- Si el dispositivo no es compatible o utiliza una versión de firmware personalizada, póngase en contacto con el equipo de asistencia técnica de su [proveedor de servicios.](../inicio-rpido/proveedor-de-servicios.md)

### Teltonika y Ruptela lideran el problema de espacio (con algunas de las pasarelas SMS)

Asegúrese de configurar correctamente los dispositivos Teltonika y Ruptela para evitar problemas con los espacios a la izquierda en los comandos SMS. Configure los dispositivos [manualmente](https://squaregps.atlassian.net/wiki/spaces/USERDOCSOLD/pages/2909016770/Manual+device+activation) o consulta con tu proveedor de servicios la posibilidad de utilizar otra pasarela SMS optimizada para la comunicación M2M.

![](https://squaregps.atlassian.net/wiki/images/icons/grey_arrow_down.png)

Click here to expand...

**Asunto:**  
Durante la activación automática de los dispositivos Teltonika y Ruptela, los usuarios pueden encontrar problemas debido a que algunas pasarelas SMS eliminan los espacios iniciales. Estos dispositivos esperan que el usuario y la contraseña precedan al comando, como por ejemplo `<login> <password> command`. Cuando el nombre de usuario y la contraseña no están configurados (como se recomienda), aparecen espacios dobles a la izquierda. Algunas pasarelas SMS, no optimizadas para la comunicación M2M, recortan estos espacios, provocando que los comandos no sean reconocidos por los dispositivos.

**Solución:**  
Para resolver este problema, póngase en contacto con su proveedor de servicios para sustituir la pasarela SMS o configure manualmente estos dispositivos a través del software de configuración Teltonika o Ruptela utilizando los datos de IP y puerto del servidor Navixy.

**Recomendaciones para la resolución de problemas:**

- [Configurar manualmente los dispositivos](https://squaregps.atlassian.net/wiki/spaces/USERDOCSOLD/pages/2909016770/Manual+device+activation) mediante el software de configuración.
- Póngase en contacto con su proveedor de servicios para utilizar una pasarela SMS optimizada para la comunicación M2M que preserve los espacios principales.

### La tarjeta SIM no tiene número de teléfono

[Proceso a](../inicio-rpido/activar-el-dispositivo-gps.md)[utom](/wiki/pages/createpage.action?spaceKey=UDOCES&title=Activate%20GPS%20device&linkCreation=true&fromPageId=2922552268)[á](../inicio-rpido/activar-el-dispositivo-gps.md)[tic](/wiki/pages/createpage.action?spaceKey=UDOCES&title=Activate%20GPS%20device&linkCreation=true&fromPageId=2922552268)[o](../inicio-rpido/activar-el-dispositivo-gps.md) [de activa](/wiki/pages/createpage.action?spaceKey=UDOCES&title=Activate%20GPS%20device&linkCreation=true&fromPageId=2922552268)[c](../inicio-rpido/activar-el-dispositivo-gps.md)[i](/wiki/pages/createpage.action?spaceKey=UDOCES&title=Activate%20GPS%20device&linkCreation=true&fromPageId=2922552268)[ó](../inicio-rpido/activar-el-dispositivo-gps.md)[n](/wiki/pages/createpage.action?spaceKey=UDOCES&title=Activate%20GPS%20device&linkCreation=true&fromPageId=2922552268) [d](../inicio-rpido/activar-el-dispositivo-gps.md)[e](/wiki/pages/createpage.action?spaceKey=UDOCES&title=Activate%20GPS%20device&linkCreation=true&fromPageId=2922552268)[l di](../inicio-rpido/activar-el-dispositivo-gps.md)[s](/wiki/pages/createpage.action?spaceKey=UDOCES&title=Activate%20GPS%20device&linkCreation=true&fromPageId=2922552268)[po](../inicio-rpido/activar-el-dispositivo-gps.md)[s](/wiki/pages/createpage.action?spaceKey=UDOCES&title=Activate%20GPS%20device&linkCreation=true&fromPageId=2922552268)[itivo](../inicio-rpido/activar-el-dispositivo-gps.md) requiere introducir el número de teléfono de una tarjeta SIM, pero las tarjetas SIM para comunicación M2M pueden no tenerlo. En este caso, [configurar manualmente el dispositivo](https://squaregps.atlassian.net/wiki/spaces/USERDOCSOLD/pages/2909016770/Manual+device+activation) e introduzca el IMEI del dispositivo (o cualquier conjunto arbitrario de dígitos) como número de teléfono en el cuadro de diálogo de activación. Como alternativa, ponte en contacto con tu proveedor de servicios para solicitar la integración con la plataforma MVNO para habilitar la comunicación mediante ICCID.

![](https://squaregps.atlassian.net/wiki/images/icons/grey_arrow_down.png)

Seguir leyendo

**Asunto:**

Cuando se utilizan tarjetas SIM M2M de proveedores OMV, a menudo no tienen números de teléfono asociados. En su lugar, estas tarjetas SIM se identifican mediante otros identificadores, normalmente ICCID. Como resultado, los comandos de configuración no pueden enviarse a través de una pasarela SMS común como ocurre con las tarjetas SIM normales. Esto dificulta la activación y comunicación de los dispositivos.

**Solución:**

Para resolver este problema, tiene dos opciones: [configurar manualmente el dispositivo](https://squaregps.atlassian.net/wiki/spaces/USERDOCSOLD/pages/2909016770/Manual+device+activation) y coloque el IMEI del dispositivo (o cualquier conjunto arbitrario de dígitos) como número de teléfono en el cuadro de diálogo de activación, o póngase en contacto con su [proveedor de servicios](../inicio-rpido/proveedor-de-servicios.md) para solicitar la integración con la plataforma MVNO, permitiendo la comunicación bidireccional a través de SMS utilizando ICCID en lugar de un número de teléfono.

**Recomendaciones para la resolución de problemas:**

- Configurar manualmente el dispositivo e introduzca el IMEI del dispositivo como número de teléfono en el cuadro de diálogo de activación.
- Póngase en contacto con su proveedor de servidores solicitar la integración con la plataforma MVNO para permitir la comunicación mediante ICCID.