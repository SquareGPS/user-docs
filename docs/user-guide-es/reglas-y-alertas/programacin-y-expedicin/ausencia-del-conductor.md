# Ausencia del conductor

## Visión general

El evento "Ausencia del conductor" está diseñado para supervisar y garantizar la presencia del conductor en el asiento del vehículo. Esta función es especialmente importante para evitar que el vehículo quede desatendido en situaciones en las que podría suponer un riesgo para la seguridad o infringir las políticas de la empresa.

### Cómo funciona

Esta función suele basarse en sistemas de vídeo a bordo equipados con inteligencia artificial y sensores para vigilar continuamente el asiento del conductor. Estos sistemas utilizan una combinación de reconocimiento visual (mediante cámaras) y datos de sensores para detectar la presencia o ausencia de un conductor. Si el sistema detecta que el asiento del conductor está desocupado cuando el vehículo está en marcha o cuando debería estar atendido, activa un evento de "Ausencia del conductor".

A continuación, este suceso se comunica a la plataforma telemática Navixy, que puede generar alertas, registrar el suceso y notificarlo al personal adecuado. Una alerta puede activarse, por ejemplo, si el vehículo está en movimiento y el sistema detecta que no hay conductor en el asiento, o si el conductor abandona el asiento sin asegurar correctamente el vehículo.

### Aplicaciones

* **Seguridad de la flota:** Garantizar que los vehículos no circulen sin conductor, evitando accidentes y usos no autorizados.
* **Seguridad:** Alertar a los gestores de flotas si un vehículo queda desatendido en una zona potencialmente peligrosa o de alto riesgo.
* **Conformidad:** Ayudar a las flotas a cumplir las normas de seguridad que exigen la presencia de un conductor durante el funcionamiento del vehículo.
* **Seguro:** Proporcionar pruebas en caso de incidentes en los que la ausencia del conductor pueda ser un factor, que pueden ser necesarias para reclamaciones de seguros o con fines legales.

El evento "Ausencia del conductor" es un componente fundamental para mejorar la seguridad de las flotas, ya que proporciona a los gestores de flotas las herramientas necesarias para controlar y responder a situaciones en las que se requiere la presencia del conductor.

## Configuración de reglas

No se requiere ninguna configuración específica para esta regla.

Para los ajustes habituales, consulte [Normas y notificaciones](../).

## Detalles del funcionamiento del sistema

* **Reinicia el temporizador:** La alerta "Ausencia del conductor" tiene un temporizador de restablecimiento de 10 segundos, lo que significa que la alerta no se activará con más frecuencia que una vez cada 10 segundos. Si se produce un evento mientras la regla está en el periodo de restablecimiento, la plataforma suprimirá la alerta, manteniendo las notificaciones y los informes claros y manejables.
* **Múltiples dispositivos:** Esta regla puede aplicarse a múltiples rastreadores, siempre que admitan eventos de "Ausencia del conductor" y tengan esta función integrada en la plataforma. Esto permite a los usuarios supervisar estos eventos en varios vehículos o dispositivos cómodamente.
* **Procesamiento de eventos independiente del GPS:** La plataforma procesa y muestra los incidentes de ausencia del conductor aunque el paquete de datos carezca de coordenadas GPS válidas. Estos eventos se registran independientemente de si se producen dentro o fuera de una geo-valla designada. En este caso, la configuración de la geovalla Inside/Outside se omite, lo que garantiza que no se pierda ningún evento crítico.
