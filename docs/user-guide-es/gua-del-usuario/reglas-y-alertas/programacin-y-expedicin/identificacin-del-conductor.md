# Identificación del conductor

## Visión general

La regla "Identificación del conductor" está diseñada para ayudar a los gestores de flotas a supervisar y controlar el uso de los vehículos mediante la identificación precisa de los conductores. Esta norma garantiza que sólo los conductores autorizados pueden manejar los vehículos, hace un seguimiento de qué conductor está al volante y registra la duración y las condiciones de cada sesión de conducción. Aumenta la eficacia operativa, mejora la rendición de cuentas y favorece el cumplimiento de los protocolos de seguridad.

La norma funciona utilizando las capacidades integradas del dispositivo para verificar la identidad del conductor directamente en la fuente. La información autorizada del conductor se almacena en la memoria interna del dispositivo. Cuando un conductor utiliza un iButton, una llave RFID o el reconocimiento facial a través de una cámara inteligente para autenticarse, el dispositivo verifica su identidad en el acto. A continuación, la plataforma registra estos eventos de identificación, generando alertas en tiempo real, informes detallados y notificaciones según sea necesario.

**Casos prácticos de aplicación:**

- **Vehículos compartidos:** Seguimiento y gestión de varios conductores que utilicen el mismo vehículo.
- **Seguridad:** Restrinja el uso del vehículo únicamente al personal autorizado, con alertas en tiempo real de intentos no autorizados.
- **Conformidad:** Garantizar que el funcionamiento del vehículo cumple las políticas y normativas de la empresa.
- **Eficiencia:** Reduzca los errores y agilice el proceso de identificación de conductores, especialmente en entornos de alta presión, con el reconocimiento basado en cámaras.

## Configuración de reglas

No se requiere ninguna otra configuración específica de las reglas.

Para los ajustes habituales, consulte [Normas y notificaciones](../../reglas-y-alertas.md).

## Detalles del funcionamiento del sistema

- **Reinicia el temporizador:** La alerta "Identificación del conductor" tiene un temporizador de restablecimiento de 5 segundos, lo que significa que la alerta no se activará con más frecuencia que una vez cada 5 segundos. Si se produce un evento mientras la regla está en el periodo de restablecimiento, la plataforma omitirá la alerta, garantizando que las notificaciones y los informes sigan siendo claros y manejables.
- **Múltiples dispositivos:** Los usuarios pueden aplicar esta regla a varios rastreadores, siempre que admitan "Identificación del conductor" a través de RFID, iButton o eventos de cámara. Esto le permite supervisar los eventos de identificación del conductor en varios vehículos o dispositivos, garantizando una cobertura completa.
- **Procesamiento de eventos independiente del GPS:** La plataforma procesará y mostrará los incidentes de identificación del conductor aunque el paquete de datos carezca de coordenadas GPS válidas. Estos eventos se registran independientemente de si ocurren dentro de una geo-valla definida. En este caso, los ajustes de geovalla Inside/Outside se omiten para garantizar que no se pierda ningún evento crítico.

## Ver también

- [**Norma de cambio de conductor**](cambio-de-conductor.md) - la norma se centra en registrar cuándo un conductor diferente toma el control del vehículo, y la plataforma compara los datos del conductor actual con los del anterior para detectar cambios y generar informes a posteriori.