# Sensor de puertas, maletero y capó

# Estado de puertas, maletero y capó

No requiere ninguna configuración especial. Sin embargo, hay que tener en cuenta varios factores.

En primer lugar, no todos los modelos de coche transmiten esta información a través del bus CAN. Lamentablemente, solo puedes averiguarlo por experiencia, o solicitando documentación detallada al fabricante.

En segundo lugar, debido a algunas peculiaridades del protocolo de transferencia de datos del dispositivo, no podrá seguir el estado de las puertas, etc., hasta que el sistema reciba el estado "Abierto" al menos una vez. Para un correcto funcionamiento, le recomendamos que deje el maletero, el capó y todas las puertas abiertas durante varios minutos con el motor en marcha.