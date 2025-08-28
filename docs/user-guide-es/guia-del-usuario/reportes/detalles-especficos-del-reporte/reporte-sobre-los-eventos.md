# Reporte sobre los eventos

El **reporte sobre los eventos** en Navixy es una herramienta completa que proporciona una visión detallada de cada evento registrado por la plataforma. Abarca una amplia gama de tipos de eventos, clasificados en eventos generales, eventos basados en la ubicación, eventos de hardware y notificaciones de servicio.

Este reporte es especialmente valioso cuando es necesario supervisar la actividad de los dispositivos durante un periodo determinado, analizar patrones de eventos y documentar incidentes específicos.

## Resumen del reporte

El reporte de todos los eventos incluye las siguientes características:

* **Registro de eventos:** Muestra cuándo y dónde se ha producido cada evento, junto con la información asociada del controlador si en ese momento había un controlador asignado al dispositivo.
* **Gráfico de distribución de eventos:** Representación visual de cómo se distribuyeron los eventos en el periodo de tiempo seleccionado.
* **Resumen global:** Resume el número total de eventos registrados para cada tipo durante el periodo del reporte.

Para asegurarse de que los eventos se registran correctamente, debe crear las reglas adecuadas para sus dispositivos. Este reporte también incluye una columna de controlador, que indica qué controlador se asignó al dispositivo cuando se registró cada evento.

## Parámetros del reporte

Además de los parámetros de reporte estándar, el reporte sobre todos los eventos incluye:

* **Agrupar por tipo de evento:** Organiza los eventos en tablas en función de su tipo. Si no se selecciona, los eventos se muestran en el orden en que fueron registrados por el dispositivo.
* **Selección del tipo de evento:** Permite filtrar el reporte por tipos de sucesos específicos, divididos en cuatro grupos. Una función de búsqueda rápida le ayuda a encontrar los eventos que necesita.

## Entender los tipos de eventos

Los sucesos de este reporte se clasifican en tres categorías principales:

1. **Eventos de hardware:** El dispositivo los procesa utilizando sus algoritmos y ajustes internos antes de enviarlos a la plataforma.
2. **Eventos de software:** Registrados a partir de los datos procesados por la plataforma.
3. **Siempre organizando eventos:** Eventos desencadenados continuamente que no corresponden a reglas específicas.

Aquí tienes un desglose de los tipos de eventos más comunes y sus reglas asociadas:

* **Actos generales:**
  * **Geocerca autocreada dentro/fuera:** Activado por la regla "movimiento no autorizado (por coordenadas)".
  * **Control de crucero on/off:** Asociado a la norma "control de crucero on/off".
  * **Rastreador adjunto:** Relacionado con la regla 'tracker detach from object'.
  * **Aviso de colisión frontal:** Vinculado a la norma sobre "sistemas avanzados de asistencia al conductor (ADAS)".
  * **Señal GPS perdida/recuperada:** Vinculado a la regla "señal GPS perdida/recuperada".
  * **Conducción dura:** Provocado por la norma de "conducción brusca".
  * **Inicio/fin del aparcamiento:** Relacionado con la norma de "detección del estado de aparcamiento".
* **Eventos basados en la localización:**
  * **Entrada/salida de Geocercas:** Registra cuándo un vehículo entra o sale de una geo-valla predefinida.
  * **Visitas a PDI:** Realiza un seguimiento de las visitas a puntos de interés (POI).
* **Eventos de hardware:**
  * **Activación del encendido:** Registra cuándo se conecta o desconecta el encendido.
  * **Interferencias GSM/GPS:** Indica intentos de interferir las señales GSM o GPS.
* **Notificaciones de servicio:**
  * **Batería baja:** Alerta cuando el nivel de batería del dispositivo desciende por debajo de un umbral determinado.
  * **Se enciende la luz de revisión del motor (MIL):** Registra cuándo se activa la luz de revisión del motor del vehículo.

## Visualización de datos

### Tabla de eventos

En **tabla de eventos** proporciona una lista detallada de todos los eventos, incluyendo:

* **Hora:** La hora exacta en que se produjo el suceso.
* **Nombre del evento:** El nombre del evento que se ha disparado.
* **Dirección:** Lugar donde tuvo lugar el evento.
* **Empleado:** El empleado asignado al dispositivo cuando se recibió el evento.

### Gráfico de distribución de eventos

En **gráfico de distribución de eventos** representa visualmente la frecuencia y distribución de los eventos durante el periodo de tiempo seleccionado. Esto puede ayudar a identificar patrones o picos inusuales de actividad.

### Número de actos por tipo

Esta sección del reporte recoge el número total de incidentes de cada tipo durante el periodo de referencia. Si no se ha producido un tipo específico de incidente, se marcará con un guión.
