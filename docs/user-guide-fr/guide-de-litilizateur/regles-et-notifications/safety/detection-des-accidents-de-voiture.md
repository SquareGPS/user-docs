# Détection des accidents de voiture

## Vue d'ensemble

La règle "Car Crash Detection" surveille et vous alerte en cas d'événements de conduite importants en détectant spécifiquement les collisions de véhicules. Cette règle permet de rester conscient du comportement des conducteurs et permet à votre équipe de dispatching de réagir rapidement en cas d'accident.

Cette règle dépend du matériel et est déclenchée par les données de l'accéléromètre du dispositif GPS. L'événement est généré par le dispositif GPS et la plateforme affiche l'alerte en fonction des données reçues.

Une détection précise des collisions nécessite une installation correcte du traceur, y compris un câblage et un alignement corrects le long des axes x, y et z. Des instructions d'installation détaillées sont généralement fournies dans le manuel de l'utilisateur du traceur. Des instructions d'installation détaillées sont généralement fournies dans le manuel d'utilisation du suiveur.

## Paramètres des règles

Comme cette règle est traitée au niveau de l'appareil GPS et non dans le nuage, aucun paramètre supplémentaire n'est nécessaire.

Pour les réglages courants, veuillez vous référer à [Règles et notifications](../../regles-et-notifications.md).

## Détails du fonctionnement du système

- **Remise à zéro de la minuterie :** L'alerte "Détection d'accident de voiture" est assortie d'un délai de réinitialisation d'une minute, ce qui signifie que l'alerte ne se déclenchera pas plus d'une fois par minute. Si un autre événement de collision est détecté au cours de cette période de réinitialisation, il sera omis de la plate-forme et des rapports.
- **Plusieurs appareils :** Cette règle vous permet de sélectionner plusieurs suiveurs pour les notifications. La seule condition est que les suiveurs prennent en charge les événements de détection des collisions de voitures et que cette fonction soit intégrée à la plateforme. Cela permet de surveiller les événements de collision entre plusieurs véhicules.
- **Alerte d'événement indépendante du GPS :** La plateforme enregistrera et affichera un événement de détection d'accident de voiture même si le paquet de données ne contient pas de coordonnées GPS valides. Le système donne la priorité à l'affichage des événements critiques, qu'ils se soient produits à l'intérieur ou à l'extérieur des géofences désignées. Les paramètres Inside/Outside geofence sont ignorés pour cette règle afin de s'assurer qu'aucun événement crucial n'est manqué...