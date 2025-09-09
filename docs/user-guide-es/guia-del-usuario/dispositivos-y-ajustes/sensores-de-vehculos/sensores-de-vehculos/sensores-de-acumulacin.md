# Sensores de acumulación

El widget de **Sensor de acumulación** es una potente herramienta que permite combinar datos de varios sensores y procesarlos mediante una función de acumulación. Esta funcionalidad es especialmente útil en situaciones en las que se utilizan varios sensores para controlar parámetros similares, como los niveles de combustible de un vehículo.

![](../../../../gua-del-usuario/dispositivos-y-ajustes/sensores-de-vehculos/attachments/image-20240815-205851.png)

## Opciones de la función de acumulación

#### Las dos funciones de acumulación disponibles son **Media (AVG)** y **Total (SUM)**.

* **AVG (Media)**: Esta función calcula el valor medio de los sensores seleccionados. Es útil cuando se desea suavizar las lecturas de múltiples sensores, proporcionando un valor más estable y representativo.
* **SUM**: Esta función suma los valores de los sensores seleccionados. Es ideal cuando es necesario controlar el valor total de un parámetro, como el nivel de combustible combinado de dos depósitos.

## Ejemplos prácticos: varios sensores de combustible en un vehículo

1. **Depósito único con dos sensores de nivel de combustible**:

* **Escenario**: Usted tiene un gran depósito de combustible con dos sensores situados en diferentes puntos dentro del depósito.
* **Objetivo**: Para obtener una lectura más precisa del nivel general de combustible, promediando las lecturas de ambos sensores.
* **Configuración**:
  * **Función de acumulación**: Seleccionar **AVG**.
  * **Sensores de acumulación**: Elija los dos sensores de nivel de combustible.
  * **Resultado**: El sistema mostrará el nivel medio de combustible, proporcionando una lectura equilibrada que compensa cualquier discrepancia entre los dos sensores.

2. **Dos depósitos comunicantes con sensores independientes**:

* **Escenario**: Tiene dos depósitos de combustible que se comunican entre sí, y cada depósito tiene su propio sensor de nivel de combustible.
* **Objetivo**: Para controlar el combustible total disponible en ambos depósitos.
* **Configuración**:
  * **Función de acumulación**: Seleccionar **SUM**.
  * **Sensores de acumulación**: Elige los sensores de ambos tanques.
  * **Resultado**: El sistema sumará los niveles de combustible de ambos depósitos, dándole el combustible total disponible.

## Configuración del sensor de acumulación

1. **Etiqueta**: Introduzca un nombre para su sensor de acumulación que identifique claramente su propósito.
2. **Función de acumulación**: Seleccione **AVG** (para promediar) o **SUM** (para la suma) en función de sus necesidades.
3. **Tipo de sensor**: Elija el tipo de sensor (por ejemplo, nivel de combustible).
4. **Precisión**: Especifique el margen de error aceptable. Por ejemplo, si la precisión se establece en 5% y el valor máximo es de 100 litros, se ignorarán los cambios de 5 litros o menos.
5. **Valor máximo**: Establece el límite superior del valor agregado. Esto evita que la lectura agregada supere un determinado umbral.
6. **Unidades**: Especifique la unidad de medida (por ejemplo, litros).
7. **Sensores de acumulación**: Seleccione los sensores individuales cuyos datos desea agregar.
8. **Guardar**: Después de configurar el sensor, haga clic en **Guardar** para aplicar los ajustes.

Esta configuración le permite supervisar y gestionar eficazmente los datos procedentes de múltiples fuentes, mejorando la precisión y utilidad de sus soluciones telemáticas y de gestión de flotas.
