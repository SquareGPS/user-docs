# Détachement du traceur

## Vue d'ensemble

La règle "Détachement du traceur de l'objet" alerte les utilisateurs lorsqu'un dispositif de suivi GPS est retiré du véhicule ou du bien qu'il surveille. La disponibilité de cette règle dépend des capacités et de la configuration du dispositif. Selon la conception du dispositif, celui-ci peut utiliser divers capteurs, tels que des points de contact ou des capteurs de lumière, pour détecter le détachement.

Cette règle est essentielle pour la sécurité des biens et la prévention des pertes, car elle permet aux entreprises de réagir rapidement en cas de vol, d'altération ou de manipulation non autorisée. Elle est particulièrement utile dans des secteurs tels que la logistique et le transport, où la protection des biens pendant le transit ou le stockage est essentielle.

## Paramètres des règles

Cette règle dépend entièrement des capacités et de la configuration de l'appareil. Il n'y a pas de paramètres spécifiques à configurer dans la règle elle-même.

Pour les réglages courants, veuillez vous référer à [Règles et notifications](../../../guide-de-litilizateur/regles-et-notifications.md).

## Détails du fonctionnement du système

* **Remise à zéro de la minuterie.** L'alerte "Détachement du traceur de l'objet" est assortie d'un délai de réinitialisation d'une minute, ce qui signifie que l'alerte ne se déclenchera pas plus d'une fois par minute. Si un événement se produit pendant la période de réinitialisation, il sera omis de la plateforme, y compris dans les rapports.
* **Plusieurs appareils.** Les utilisateurs ont la possibilité de sélectionner plusieurs dispositifs GPS pour recevoir des notifications lorsque le dispositif est détaché d'un objet. La seule condition est que les traceurs sélectionnés prennent en charge les événements "Détachement du traceur de l'objet" et que cette fonction soit intégrée à la plateforme.
* **Alerte d'événement indépendante du GPS.** Si la plate-forme reçoit un événement de détachement d'un traceur sans données GPS valides, l'événement est toujours considéré comme valide et affiché, qu'il se soit produit à l'intérieur ou à l'extérieur d'une géofence. Dans ce cas, les paramètres intérieur/extérieur des géofences sont ignorés afin de s'assurer que des événements potentiellement critiques ne sont pas manqués.
