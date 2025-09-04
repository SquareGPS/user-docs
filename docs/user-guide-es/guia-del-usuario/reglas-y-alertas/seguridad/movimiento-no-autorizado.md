# Movimiento no autorizado

## Visión general

La regla "Movimiento no autorizado" está diseñada para mejorar la seguridad de los vehículos alertando a los usuarios cuando un vehículo parado comienza a moverse sin autorización. Esta regla es especialmente valiosa en situaciones en las que se espera que el vehículo permanezca parado, como cuando se apaga, pero inesperadamente empieza a moverse. Ayuda a identificar rápidamente posibles robos o usos no autorizados, lo que permite a los usuarios actuar con rapidez.

**Aplicaciones típicas:**

* **Prevención de robos:** Alertas inmediatas si un vehículo se desplaza sin autorización.
* **Seguridad en el aparcamiento:** Vigilancia de vehículos en zonas de aparcamiento designadas para detectar movimientos no autorizados.
* **Protección de activos:** Garantizar que los vehículos o equipos estacionados permanezcan seguros fuera del horario de trabajo.

La regla funciona utilizando el acelerómetro integrado del dispositivo GPS y otros ajustes de configuración para detectar cualquier movimiento no autorizado. La precisión de esta regla depende de la correcta instalación y configuración del dispositivo, que varía según el modelo. Una vez que la plataforma recibe el paquete de datos que indica un movimiento no autorizado, procesa y muestra el evento, proporcionando a los usuarios alertas en tiempo real.

## Configuración de reglas

Esta norma depende totalmente de las capacidades del dispositivo y de la configuración del hardware. Normalmente, el dispositivo debe ser capaz de detectar cuándo el vehículo no está en uso, por ejemplo, controlando el estado del encendido.

No hay ajustes específicos que configurar dentro de la propia regla. Para los ajustes habituales, consulte [Reglas y alertas](../).

## Detalles del funcionamiento del sistema

* **Reinicia el temporizador:** La alerta "Movimiento no autorizado" tiene un temporizador de restablecimiento de 5 minutos, lo que significa que la alerta no se activará con más frecuencia que una vez cada 5 minutos. Si se produce un evento mientras la regla está en el periodo de restablecimiento, la plataforma suprimirá la alerta, garantizando que las notificaciones y los informes sigan siendo claros y manejables.
* **Múltiples dispositivos:** Esta regla puede aplicarse a varios rastreadores, siempre que admitan eventos de "Movimiento no autorizado" y tengan esta función integrada en la plataforma. Esto permite a los usuarios controlar los movimientos no autorizados en varios vehículos, garantizando una cobertura de seguridad completa.
* **Procesamiento de eventos independiente del GPS:** La plataforma procesa y muestra los eventos de movimiento no autorizados aunque el paquete de datos carezca de coordenadas GPS válidas. Estos eventos se registran independientemente de si ocurren dentro o fuera de una geocerca designada. En este caso, la configuración de la geocerca Dentro/Fuera se omite, lo que garantiza que no se pierda ningún evento crítico.
