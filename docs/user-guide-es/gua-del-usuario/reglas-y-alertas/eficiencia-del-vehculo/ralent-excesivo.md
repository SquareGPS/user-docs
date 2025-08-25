# Ralentí excesivo

## Visión general

El ralentí excesivo es un evento importante de controlar en la gestión de flotas, ya que afecta directamente al consumo de combustible, al desgaste del vehículo y a la eficiencia operativa general. Navixy ofrece dos métodos para detectar el ralentí excesivo: procesado en la nube y detectado por el dispositivo. Cada método tiene sus propias ventajas y se adapta a diferentes tipos de necesidades de flota.

**La regla procesada en la nube** está gestionada por la plataforma y utiliza parámetros establecidos por el usuario, como la duración del ralentí y la detección de aparcamiento. Esta regla es ideal para quienes necesitan una solución flexible y personalizable que funcione con cualquier rastreador que comunique datos básicos como el estado de encendido y la ubicación GPS.

**La regla del dispositivo detectado,** por otro lado, se basa en la capacidad integrada del rastreador GPS para detectar eventos de ralentí. El hardware genera y transmite el evento de ralentí directamente a la plataforma. Este método es ventajoso para los rastreadores que tienen funciones avanzadas de detección de ralentí, ya que ofrece potencialmente una mayor precisión y funcionalidad adicional.

## Configuración de reglas

### Procesado en la nube

* **Duración del ralentí:** Establezca la duración después de la cual el ralentí se considerará excesivo. La regla supervisará cuando un vehículo esté aparcado (según lo determinado por los ajustes de Detección de Aparcamiento) y el encendido esté en ON. Si el vehículo permanece en este estado más allá de la duración especificada, se activará una notificación.

Para los ajustes habituales, consulte [Normas y notificaciones](../).

### Dispositivo detectado

* **Ajustes específicos del dispositivo:** Esta regla se basa en la configuración del hardware para detectar el ralentí. Debe consultar la documentación del dispositivo para configurar la detección de ralentí en el rastreador. La plataforma recibirá y mostrará los eventos de ralentí en función de la salida del dispositivo.

Para los ajustes habituales, consulte [Normas y notificaciones](../).

## Detalles del funcionamiento del sistema

* **Detección de ralentí procesada en la nube:** La plataforma supervisa continuamente el estado de encendido del vehículo y el estado de estacionamiento. Cuando el vehículo está aparcado con el contacto en ON, la plataforma empieza a contar la duración del ralentí. Si el ralentí supera el umbral definido por el usuario, el sistema envía una alerta. Este método funciona con una amplia gama de rastreadores y ofrece flexibilidad para establecer umbrales de ralentí personalizados.
* **Detección de ralentí detectado por el dispositivo:** El propio rastreador controla el ralentí y envía un evento a la plataforma cuando el ralentí supera el umbral predefinido en el dispositivo. La plataforma simplemente envía este evento al usuario. Este método puede ofrecer una mayor precisión y funciones avanzadas en función de las capacidades del rastreador.
* **Notificaciones:** Independientemente del método de detección, recibirá notificaciones a través de la interfaz de usuario, correo electrónico o SMS. Estas notificaciones ayudan a los gestores de flotas a tomar medidas inmediatas para reducir el ralentí innecesario, ahorrando así combustible y reduciendo el desgaste de los vehículos.
* **Informes:** Puede generar informes sobre el ralentí excesivo para analizar patrones y tomar decisiones basadas en datos para mejorar la eficiencia de la flota. Estos informes pueden ser especialmente útiles para identificar el ralentí habitual o evaluar el impacto del ralentí en los costes de combustible y el mantenimiento de los vehículos.
