# Widget de reenvío de datos

En el widget de **Enviar datos GPS** en Navixy se permite transmitir datos de seguimiento GPS y telemáticos desde Navixy a otros servidores y aplicaciones de terceros mediante API y servicios web.

## ¿Qué es el reenvío de datos?

El reenvío de datos (o retransmisión de datos) es una función que permite enviar datos de seguimiento GPS y telemáticos desde Navixy a otros servidores o aplicaciones de terceros en tiempo real. Los tipos de datos que se pueden reenviar incluyen:

* Datos del vehículo
* Localización GPS
* Datos de dispositivos IoT

El reenvío de datos puede hacerse fuera de línea o casi instantáneamente a medida que se transmiten los datos.

### Principales objetivos de la transmisión de datos

1. **Cumplimiento de la normativa gubernamental:** En algunos países, las autoridades exigen que los vehículos transmitan datos (como la ubicación y la velocidad) utilizando protocolos específicos para cumplir la legislación local.
2. **Integraciones empresariales:** Las grandes empresas, sobre todo en sectores como el comercio minorista o la logística, suelen exigir a sus proveedores que envíen datos GPS y telemáticos a sus sistemas para cumplir obligaciones contractuales, como garantizar la puntualidad de las entregas o mantener unas condiciones específicas (como la temperatura) de la carga.
3. **Consolidación de datos:** La integración de diversos componentes en sistemas informáticos complejos suele requerir la normalización de los datos, sobre todo cuando estos componentes son suministrados por múltiples proveedores independientes.

### Cómo funciona el reenvío de datos

Los datos recogidos del vehículo se envían en un formato de protocolo especificado a una dirección y un puerto determinados por el usuario. Navixy ofrece varios protocolos de envío de datos que pueden seleccionarse en función de sus necesidades específicas dentro de la interfaz de usuario.

## Gestión de la transmisión de datos

Puedes gestionar el reenvío de datos a través del widget correspondiente en la sección "Dispositivos y configuración".

En este widget, puedes:

* Vincula uno o varios retransmisores a un dispositivo.
* Especifique el ID utilizado al enviar datos (por defecto, se utiliza el mismo ID que el propio dispositivo).
* Desvincula los retransmisores del dispositivo.
* Cree nuevos retransmisores y edite los existentes haciendo clic en el botón "Gestión de retransmisores".

### Gestión de retransmisores

Al gestionar un retransmisor, puede configurar los siguientes parámetros:

* **Nombre:** Una práctica etiqueta para facilitar su identificación.
* **Data transfer protocol:** Elige entre los protocolos admitidos.
* **Dirección y puerto del servidor de destino:** Especifique dónde deben enviarse los datos.
* **Nombre de usuario y contraseña:** Para la autorización en el servidor receptor (si es necesario).
* **Actividad de retransmisión:** Active o desactive el retransmisor según sea necesario.

Puede crear varios retransmisores si su plan de suscripción lo permite. Los perfiles de retransmisores pueden editarse, eliminarse o suspenderse.

### Protocolos

He aquí algunos ejemplos de protocolos disponibles para diversos fines:

#### Protocolos de cumplimiento de la normativa gubernamental

| Protocolo                      | Descripción                                                                                                                   |
| ------------------------------ | ----------------------------------------------------------------------------------------------------------------------------- |
| **Maquinaria Amarilla** (🇨🇴) | Protocolo basado en SOAP obligatorio para la maquinaria amarilla, que informa a los servidores policiales.                    |
| **Olympstroy** (🇷🇺)          | Protocolo basado en SOAP utilizado durante la preparación de los Juegos Olímpicos de 2014.                                    |
| **OSINERGMIN** (🇵🇪)          | Protocolo de envío de información telemática al gobierno peruano para unidades de monitoreo en industrias como minería y gas. |
| **RNIS** (🇷🇺)                | Utilizado en el sistema regional de navegación e información de Moscú para el control del movimiento de vehículos.            |

#### Cumplimiento de la normativa por parte de las empresas

| Protocolo                                     | Descripción                                                                                                               |
| --------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------- |
| **Altotrack Chep México**                     | Reenvía las posiciones de los vehículos desde la plataforma Chep al Altotrack HUB.                                        |
| **ArmCargo**                                  | Envía los datos a los servicios de Gestión de Riesgos de Activos para la evaluación de riesgos.                           |
| **Carga en línea**                            | Reenvía los datos al servicio CargoOnline.                                                                                |
| [**ILSP**](ilsp.md)                           | Permite que el software de ILSP comparta datos de vehículos a través de redes en México.                                  |
| **Encuéntrate**                               | Remite datos al proyecto logístico de Localizar-t, Forza.                                                                 |
| **Soluciones ReC**                            | Sends data to ReC Servicios Consultores servers.                                                                          |
| [**Recurso Confiable**](recurso-confiable.md) | Utilizado para el envío de datos con el software de Recurso Confiable a través de varias industrias en México y más allá. |
| **SafetyNet pulsian**                         | Reenvía las alarmas SOS a un servidor CAD SafetyNet para recibir ayuda de emergencia.                                     |
| [**SimpliRoute**](simpliroute.md)             | Protocolo de transmisión de datos de seguimiento de vehículos a SimpliRoute.                                              |
| **TraceReports**                              | Envía datos al sistema TraceReports.                                                                                      |
| [**Unigis**](unigis.md)                       | Permite compartir datos con la plataforma TMS de Unigis, utilizada a menudo por los departamentos de logística.           |
| **Wirtrack**                                  | Reenvía los datos a los servicios de Wirsolut.                                                                            |

#### Consolidación de datos

| Protocolo                               | Descripción                                                                                     |
| --------------------------------------- | ----------------------------------------------------------------------------------------------- |
| **Control AVL**                         | Envía datos a los servidores de AVL Control para la gestión de la seguridad y las estadísticas. |
| **Granito3**                            | Reenvía los datos a los servidores de navegación de Santel.                                     |
| **Startrack**                           | Protocolo basado en SOAP para el envío de datos al sistema logístico de Startrack.              |
| **Lacak.io**                            | Protocolo de reenvío de datos para Lacak.io.                                                    |
| [**Servicio Web Navixy**](navixy-ws.md) | Protocolo basado en SOAP para transmitir datos de flotas a sistemas de terceros.                |
| **SA-RM**                               | Protocolo general de transmisión de datos.                                                      |
| **Transnavegación**                     | Reenvía los datos a los servidores de Transnavigation.                                          |
| [**Wialon IPS**](wialon-ips.md)         | Protocolo público de Gurtam para retransmitir datos de rastreadores GPS y GLONASS.              |
| **Wisetrack**                           | Reenvía los datos a los servidores de Wisetrack.                                                |

Estas opciones proporcionan un marco sólido para el intercambio de datos, ayudándole a cumplir los requisitos normativos, integrarse con los sistemas de la empresa y consolidar los datos para un análisis exhaustivo.
