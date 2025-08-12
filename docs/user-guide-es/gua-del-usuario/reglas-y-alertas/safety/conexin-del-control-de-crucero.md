# Conexión del control de crucero

## Visión general

Recibir notificaciones cuando el Control de Crucero está activado o desactivado en un vehículo proporciona información valiosa para supervisar y gestionar el rendimiento del vehículo. Estas son algunas de las principales ventajas:

* **Control de la eficiencia del combustible:** El Control de Crucero ayuda a mantener una velocidad constante, lo que puede mejorar la eficiencia del combustible. Las notificaciones permiten a los usuarios hacer un seguimiento del uso del Control de Crucero y evaluar su impacto en el consumo de combustible.
* **Gestión de la batería:** En los vehículos eléctricos o híbridos, el uso del Control de Crucero puede afectar a la duración de la batería y a la autonomía. Las notificaciones ayudan a los usuarios a controlar su impacto en el uso de la batería, lo que permite una mejor gestión de la energía eléctrica del vehículo.
* **Análisis del comportamiento al volante:** El seguimiento de cuándo y dónde se utiliza el Control de Crucero ofrece información sobre el comportamiento del conductor. Estos datos pueden utilizarse para analizar los hábitos de conducción e identificar oportunidades de mejora, como la reducción del uso excesivo o el aumento del uso infrautilizado del control de crucero.
* **Evaluación del rendimiento:** La supervisión del uso del Control de Crucero puede ayudar a evaluar el rendimiento del vehículo. Los usuarios pueden comparar el Control de Crucero con otros modos de conducción para evaluar la eficiencia en diferentes rutas y condiciones de conducción.
* **Seguridad y comodidad:** El Control de Crucero aumenta el confort y la seguridad durante los viajes largos. Las notificaciones garantizan que los usuarios sepan si el Control de Crucero está activo, lo que les permite ajustar su estilo de conducción según sea necesario.

Estas prestaciones pueden variar en función de la marca, el modelo y las características adicionales del vehículo.

## Configuración de reglas

Esta regla no requiere ninguna configuración específica.

Para los ajustes habituales, consulte [Normas y notificaciones](../).

## Detalles del funcionamiento del sistema

* **Reinicia el temporizador:** La alerta "Control de crucero conectado/desconectado" tiene un Temporizador de 10 minutos, impidiendo que la alerta se active más de una vez cada 10 minutos. Si se produce otro evento dentro de este periodo de restablecimiento, se omitirá de la plataforma y de los informes.
* **Múltiples dispositivos:** Los usuarios pueden seleccionar varios rastreadores para recibir notificaciones. Los rastreadores seleccionados deben admitir eventos de Encendido/Apagado del Control de Crucero y tener esta función integrada en la plataforma. Esto permite supervisar los eventos de control de crucero en varios vehículos.
* **Alerta de eventos independiente del GPS:** La plataforma registra y muestra los eventos de Control de Crucero incluso si el paquete de datos carece de coordenadas GPS válidas. Los ajustes de geovalla Inside/Outside se ignoran para esta regla, lo que garantiza que no se pierdan eventos críticos.
