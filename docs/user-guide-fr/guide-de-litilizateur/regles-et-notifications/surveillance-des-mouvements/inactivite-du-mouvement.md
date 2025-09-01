# Inactivité du mouvement

## Vue d'ensemble

L'alerte "Inactivité de mouvement", également connue sous le nom d'alerte "Absence de mouvement", est conçue pour renforcer la sécurité et la sûreté. Elle déclenche une alerte lorsqu'aucun mouvement n'est détecté pendant une période prolongée, en s'appuyant sur des dispositifs GPS équipés d'accéléromètres et des capacités de microprogrammation nécessaires.

Cette règle est particulièrement utile dans trois domaines clés :

1. **Actifs mobiliers**: Appliquée aux équipements tels que les machines de construction et les remorques, l'alerte "inactivité du mouvement" permet de surveiller les arrêts non autorisés ou la marche au ralenti prolongée, ce qui garantit que les biens sont utilisés comme prévu et prévient le vol potentiel ou l'utilisation abusive.
2. **Suivi des cargaisons**: Pour les marchandises en transit, cette alerte peut s'avérer cruciale pour détecter les marchandises qui ont été laissées sans surveillance ou qui sont en danger, ce qui permet d'intervenir à temps pour sécuriser les expéditions de valeur.
3. **Sécurité personnelle**: Pour les personnes utilisant des traceurs GPS personnels, comme les personnes âgées ou les travailleurs isolés, l'alerte "Inactivité du mouvement" offre une protection supplémentaire en signalant une urgence potentielle lorsque l'appareil détecte une absence inhabituelle de mouvement, ce qui incite à réagir pour assurer le bien-être de la personne.

## Paramètres des règles

Comme l'inactivité du mouvement est un événement détecté par l'appareil, il n'y a pas de paramètre spécifique dans les règles et les notifications. Utilisez plutôt le widget Paramètres de l'appareil pour configurer à distance la limite de vitesse du côté de l'appareil.

Pour les réglages courants, veuillez vous référer à [Règles et notifications](../../regles-et-notifications.md).

## Détails du fonctionnement du système

- **Remise à zéro de la minuterie.** L'alerte "inactivité du mouvement" est assortie d'un délai de réinitialisation d'une minute, ce qui signifie que l'alerte ne se déclenchera pas plus d'une fois par minute. Si un événement se produit pendant que la règle attend la réinitialisation, la plate-forme ne tiendra pas compte de l'événement, y compris dans les rapports.
- **Alerte d'événement indépendante du GPS.** Le système peut générer une alerte d'inactivité de mouvement même si les données GPS ne sont pas disponibles. Si des coordonnées GPS non valides sont détectées, la plate-forme enregistre et affiche l'événement, qu'il se soit produit à l'intérieur ou à l'extérieur des zones géographiques désignées. La logique des paramètres de géofence intérieur/extérieur est ignorée dans ces cas afin de garantir que les événements critiques ne sont pas manqués.