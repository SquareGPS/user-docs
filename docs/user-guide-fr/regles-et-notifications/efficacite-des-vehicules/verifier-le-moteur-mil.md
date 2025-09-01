# Vérifier le moteur (MIL)

## Vue d'ensemble

La règle "Check engine (MIL)" est conçue pour surveiller l'état du témoin lumineux de dysfonctionnement (MIL), communément appelé "Check Engine", dans les véhicules. Cette règle est essentielle pour l'entretien des véhicules et la gestion des parcs automobiles, car elle alerte rapidement les utilisateurs lorsque le voyant MIL est activé.

Le MIL s'allume généralement lorsque le système de diagnostic embarqué du véhicule détecte un problème au niveau du moteur, des émissions ou d'autres systèmes critiques. En recevant des notifications en temps utile, les utilisateurs peuvent prendre des mesures immédiates pour résoudre les problèmes potentiels, ce qui permet d'éviter des dommages supplémentaires et de garantir la sécurité et la conformité du véhicule.

> [!INFO]
> Pour surveiller des codes DTC spécifiques, vous pouvez configurer une fonction d'enregistrement des codes DTC. [Valeur du champ État](../entrees-et-sorties/valeur-du-champ-etat.md) règle.

## Paramètres des règles

Cette règle dépend entièrement des capacités et de la configuration de l'appareil. Il n'y a pas de paramètres spécifiques à configurer dans la règle elle-même.

Pour les réglages courants, veuillez vous référer à [Règles et notifications](../../regles-et-notifications.md).

## Détails du fonctionnement du système

- **Remise à zéro de la minuterie.** L'alerte "Check engine (MIL)" a un délai de réinitialisation de 24 heures, ce qui signifie qu'elle ne se déclenchera pas plus d'une fois toutes les 24 heures. Si l'événement se produit pendant la période de réinitialisation, il sera omis de la plate-forme et des rapports.
- **Plusieurs appareils.** Cette règle peut s'appliquer à plusieurs appareils GPS, à condition qu'ils prennent en charge l'événement "Check Engine" (MIL) et que la fonction soit intégrée à la plate-forme.
- **Alerte d'événement indépendante du GPS.** La plateforme enregistre l'événement et déclenche des notifications, que le véhicule se trouve à l'intérieur ou à l'extérieur d'un périmètre, même si le paquet de données ne contient pas de coordonnées GPS valides. La plateforme donne la priorité à la capture et à l'affichage de ces événements critiques afin de s'assurer qu'ils ne sont pas manqués.