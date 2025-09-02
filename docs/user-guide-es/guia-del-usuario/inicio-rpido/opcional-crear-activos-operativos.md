---
hidden: true
---

# (Opcional) Crear activos operativos

## ¿Qué son los activos operativos?

Los **activos operativos** transforman la gestión de su flota al cambiar el enfoque de los dispositivos GPS hacia entidades operativos reales. Esta funcionalidad permite crear unidades rastreables fácilmente identificables, como vehículos y personal, manteniendo su identidad e historial por separado.

Para obtener más información y una descripción detallada de esta funcionalidad, consulte **Activos operativos**.

## Aplicación práctica

Veamos cómo se puede implementar esta funcionalidad en un caso de uso ejemplo.

Una empresa con una flota de vehículos de reparto anteriormente rastreaba dispositivos GPS individuales, lo que generaba importantes desafíos operativos. La gestión de flota requería verificar manualmente la configuración de los dispositivos, ejecutar consultas separadas para cada uno a fin de calcular distancias recorridas, e identificar qué dispositivo estaba asignado a cada vehículo para una generación de informes precisa.

Al implementar la funcionalidad de activos operativos, la empresa logró una eficiencia operativa significativa. El sistema ahora permite monitorear entidades operativos reales (vehículos y personal) en lugar de dispositivos GPS abstractos. Cuando los conductores cambian de vehículo, los gestores pueden desvincular y volver a vincular activos de manera ágil. El sistema mantiene historiales separados tanto para conductores como para vehículos, preservando la integridad de los datos independientemente de los cambios.

A continuación, le guiaremos paso a paso para crear activos operativos en Navixy y aprovechar estos beneficios.

## Creación de activos operativos

1. **Elegir el tipo de activo**\
   Vaya al módulo **Activos operativos** en el menú lateral izquierdo. Verá la lista de sus activos: **Vehículos** y **Personal**. Decida qué tipo de activo desea crear.

> \[!NOTE] Ambos tipos de activos pueden rastrearse en mapas, configurarse y vincularse, manteniendo historiales separados y recepción de señal GPS. Los activos se listan en las pestañas correspondientes de **Vehículos** y **Personal**. Para obtener más información sobre los tipos de activos, consulte **Vehículos** y **Personal**.

> \[!INFO] Nuevos tipos de activos y funcionalidades estarán disponibles en próximas actualizaciones.

2. **Crear un activo**\
   Seleccione la pestaña correspondiente y haga clic en el ícono ![Untitled-20250430-103751.png](../../gua-del-usuario/inicio-rpido/attachments/Untitled-20250430-103751.png) en la esquina superior izquierda para abrir el formulario de creación. Complete los campos requeridos:
3. **Para vehículos**: 1. **Nombre** 2. **Matrícula** 3. **Tipo**
4. **Para personal**: 1. **Nombre**

> \[!INFO] Los activos también pueden importarse de forma masiva utilizando plantillas de Excel. Para más información sobre este proceso y la creación de activos en general, consulte [Agregar un vehículo](https://squaregps.atlassian.net/wiki/spaces/UDOCES/pages/3261792301#agregar-vehiculo) y [Agregar personal](https://squaregps.atlassian.net/wiki/spaces/UDOCES/pages/3261988902#agregar-personal).

3. **Asignar un dispositivo GPS al activo**\
   En el campo **Objeto**, seleccione un dispositivo GPS activado para asignarlo a su activo.

> \[!TIP] ¡Felicidades! Ha creado su primer activo.

## Próximos pasos

Después de crear sus activos operativos, podrá:

* Rastrearlos en el mapa dentro del módulo [Seguimiento](../seguimiento/).
* Ver su lista y detalles en [Activos operativos](../activos-operativos/).
* Supervisar sus notificaciones en el módulo [Alertas](../reglas-y-alertas/).
* Vincularlos entre sí y visualizar sus datos GPS en la [Lista de activos](../seguimiento/lista-de-objetos/) y en el [Widget de activos](https://squaregps.atlassian.net/wiki/spaces/USERDOCSOLD/pages/2909015126/Object+widget).
