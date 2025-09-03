# Campos personalizados

Los **campos personalizados** permiten añadir información personalizada a la descripción de objetos como lugares. Los campos personalizados funcionan del mismo modo que los campos estándar, lo que permite almacenar datos valiosos que pueden utilizarse para filtrar y mejorar la eficacia operativa.

![](../../gua-del-usuario/cuenta/attachments/image-20240718-172504.png)

**Ejemplos:**

* En la **Gestión de servicios de campo**, los campos personalizados pueden complementar la información sobre los clientes o las instalaciones atendidas. Un empleado de campo que utilice el [Rastreador X-GPS](https://x-gps.app/). La aplicación móvil puede ver y editar información detallada sobre los lugares, como los datos del cliente y los requisitos del servicio, lo que mejora la realización de las tareas. [Leer más en el blog](https://www.navixy.com/blog/custom-fields-navixy/).

## Tipos de campos personalizados

| **Tipo de campo**      | **Descripción**                                                                                    |
| ---------------------- | -------------------------------------------------------------------------------------------------- |
| **Cadena de texto**    | Longitud hasta 700 caracteres, permite cualquier carácter.                                         |
| **Área de texto**      | Longitud hasta 20.000 caracteres, no clasificable.                                                 |
| **Correo electrónico** | Sólo para direcciones de correo electrónico.                                                       |
| **Teléfono**           | Sólo para números de teléfono.                                                                     |
| **Número decimal**     | Para valores decimales.                                                                            |
| **Número entero**      | Para valores enteros.                                                                              |
| **Empleado**           | Permite asignar un empleado responsable, haciendo visible el lugar en la aplicación X-GPS Tracker. |
| **Imagen**             | Permite añadir una imagen.                                                                         |
| **Archivo**            | Permite adjuntar un archivo.                                                                       |

### Añadir y editar campos personalizados

Para añadir un nuevo campo personalizado, vaya a **Configuración de la cuenta → Campos personalizados**.

1. **Seleccione el tipo de campo:** Elija el tipo de campo en la lista Elementos de la izquierda.
2. **Arrastrar y soltar:** Arrastre el tipo de campo seleccionado a la sección Principal de la derecha.
3. **Especifique la información:**
   1. **Nombre del campo:** Introduzca el nombre del campo.
   2. **Descripción:** Proporcione una descripción para el campo.
   3. **Necesario:** Indique si el campo es obligatorio. Al añadir un nuevo lugar, no se puede guardar hasta que se rellenen todos los campos obligatorios.

### Acciones adicionales para campos personalizados

* **Añade sección:** Distribuye los campos personalizados en diferentes secciones para una mejor organización.
* **Reordene:** Arrastre y suelte los campos y secciones para organizarlos en el orden que prefiera.
* **Borre:** Para eliminar un campo, selecciónelo y haga clic en el icono de la papelera. Tenga en cuenta que los campos primarios marcados con un icono de candado no se pueden eliminar.

#### Notas importantes

* **Máximo de campos personalizados:** Puede añadir hasta 50 campos personalizados.
* **Actualizaciones automáticas:** Al editar los campos, los cambios en su nombre, descripción y orden se reflejarán automáticamente en todos los lugares creados.
* **Supresión:** Borrar un campo lo eliminará de todos los sitios de forma permanente sin posibilidad de recuperación.

## Preguntas frecuentes y solución de problemas

* **¿Pueden añadirse campos personalizados a otros objetos además de lugares?** Actualmente, los campos personalizados solo pueden añadirse a los lugares, pero está previsto ampliar esta funcionalidad en el futuro.
* **¿Cómo se pueden rellenar campos personalizados desde sistemas CRM a través de la API de Navixy?** Sí, puede rellenar campos personalizados en Navixy realizando llamadas a la API para sincronizar datos desde su CRM. Esto permite una transferencia de datos y actualizaciones sin fisuras, garantizando que toda la información esté actualizada y accesible en ambos sistemas. Más información en [Documentación de la API Navixy](https://app.gitbook.com/s/6dtcPLayxXVB2qaaiuIL/general/readme).
