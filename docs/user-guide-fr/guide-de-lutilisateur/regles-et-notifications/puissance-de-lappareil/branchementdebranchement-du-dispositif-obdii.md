# Branchement/débranchement du dispositif OBDII

## Vue d'ensemble

La règle "OBDII Device Plug / Unplug" est conçue pour fournir des alertes immédiates chaque fois qu'un traceur GPS OBDII est connecté ou déconnecté du port OBDII du véhicule. Cette règle permet aux utilisateurs de prendre rapidement des mesures pour maintenir un suivi continu et la fonctionnalité de l'appareil.

Par exemple, lorsque le traceur est débranché, il bascule sur sa batterie interne, qui a une durée de vie limitée. Les notifications immédiates en cas de déconnexion permettent aux utilisateurs de réagir rapidement, ce qui garantit un suivi et une transmission de données ininterrompus.

## Paramètres des règles

Cette règle dépend entièrement des capacités et de la configuration matérielle de l'appareil. Il n'y a pas de paramètres spécifiques à configurer dans la règle elle-même.

Pour les réglages courants, veuillez vous référer à [Règles et notifications](../).

## Détails du fonctionnement du système

* **Remise à zéro de la minuterie.** L'alerte "Branchement/débranchement d'un dispositif OBDII" est assortie d'un délai de réinitialisation de 5 minutes, ce qui signifie que l'alerte ne se déclenchera pas plus d'une fois toutes les 5 minutes. Si l'événement se produit pendant la période de réinitialisation de la règle, il sera omis par la plate-forme, y compris dans les rapports.
* **Plusieurs appareils.** **Plusieurs appareils :** Les utilisateurs peuvent sélectionner plusieurs dispositifs de suivi à surveiller dans le cadre de cette règle. La seule condition est que les dispositifs sélectionnés prennent en charge les événements de branchement/débranchement du port OBDII. Cette flexibilité permet aux utilisateurs de surveiller ce type d'événement sur plusieurs véhicules ou dispositifs de manière pratique.
* **Alerte d'événement indépendante du GPS.** Le système traite ces événements indépendamment de la disponibilité des données GPS. L'événement sera toujours enregistré et affiché, même s'il se produit en dehors des zones géographiques définies.
