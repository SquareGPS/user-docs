# Contrôle de proximité

## Vue d'ensemble

La règle "Proximity monitoring" exploite la fonctionnalité Bluetooth pour fournir des alertes en temps réel lorsque des événements de proximité se produisent. Cette règle est conçue pour détecter des distances précises entre des objets équipés de dispositifs GPS dotés de capacités BLE (Bluetooth Low Energy), ainsi qu'entre des dispositifs GPS et des balises BLE. Il s'agit d'un outil polyvalent qui offre de nombreuses applications dans divers secteurs d'activité.

Cette règle est particulièrement utile dans les environnements où le respect de distances spécifiques est essentiel. Voici quelques exemples :

* **Utilisation d'équipements dangereux :** Suivre la proximité des opérateurs par rapport aux équipements dangereux, afin de prévenir les accidents et de garantir le respect des règles de sécurité.
* **La distanciation sociale dans les environnements épidémiques :** Maintenir et appliquer des mesures d'éloignement social sur les lieux de travail ou dans les espaces publics pendant les épidémies, afin de contribuer à réduire la propagation des maladies contagieuses.

En appliquant cette règle, les organisations peuvent améliorer la sécurité, garantir le respect des réglementations et optimiser la gestion des activités liées à la proximité.

## Paramètres des règles

La fonctionnalité de cette règle dépend des capacités et de la configuration de l'appareil, de sorte qu'aucune configuration spécifique n'est requise.

Pour les réglages courants, veuillez vous référer à [Règles et notifications](../).

## Les spécificités de la plate-forme :

* **Remise à zéro de la minuterie :** L'alerte "Surveillance de proximité" est assortie d'un délai de réinitialisation de 10 secondes, ce qui signifie que l'événement d'alerte ne se produira pas plus d'une fois toutes les 10 secondes. Si ce type d'événement se produit pendant que la règle attend la réinitialisation, cet événement sera omis par la plate-forme, y compris dans les rapports.
* **Plusieurs appareils :** Cette règle permet aux utilisateurs de sélectionner plusieurs dispositifs à partir desquels ils souhaitent recevoir des notifications. Les suiveurs sélectionnés doivent prendre en charge l'événement "Proximité" et cette fonctionnalité doit être intégrée à la plateforme de ces suiveurs. Cela permet aux utilisateurs de surveiller les événements sur plusieurs appareils de manière pratique.
* **Alerte d'événement indépendante du GPS :** Lorsque la plateforme identifie un événement matériel de ce type à partir d'un paquet de données de suivi ne contenant pas de coordonnées valides, elle considère l'événement comme valide et l'affiche, que l'événement se soit produit à l'intérieur ou à l'extérieur des zones géographiques délimitées, afin de garantir l'envoi de notifications critiques.
