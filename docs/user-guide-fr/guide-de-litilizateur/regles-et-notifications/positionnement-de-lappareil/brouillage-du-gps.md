# Brouillage du GPS

## Vue d'ensemble

Le brouillage du GPS se produit lorsque les fréquences du GPS ou du GNSS sont perturbées par des interférences provenant de sources proches, un processus connu sous le nom de masquage ou de masquage de fréquence. Ces interférences peuvent faire perdre à l'appareil sa connexion avec les satellites, ce qui entraîne une distorsion ou une perte totale des données GPS. Le brouillage du GPS diffère de [Brouillage GSM](../connexion-des-appareils/brouillage-gsm.md)car ils fonctionnent sur des bandes de fréquences distinctes. En cas de brouillage du GPS, l'appareil peut perdre sa connexion satellite, ce qui se traduit par l'absence de satellites visibles ou par des coordonnées invalides que la plateforme de suivi ne peut pas récupérer.

La règle de brouillage du GPS renforce la sécurité des véhicules et des biens en empêchant le vol dans les scénarios où l'interférence du signal GPS est utilisée pour désactiver les systèmes de repérage. Par exemple, si un véhicule est la cible d'un vol ou d'un détournement, cette règle donne l'alerte en temps utile, ce qui permet d'agir rapidement pour éviter les pertes ou les dommages. Il s'agit d'un outil essentiel pour les entreprises afin de protéger leurs flottes et leurs biens de valeur.

## Paramètres des règles

Cette règle dépend entièrement des capacités et de la configuration matérielle de l'appareil. Il n'y a pas de paramètres spécifiques à configurer dans la règle elle-même.

Pour les réglages courants, veuillez vous référer à [Règles et notifications](../../regles-et-notifications.md).

## Détails du fonctionnement du système

- **Remise à zéro de la minuterie :** L'alerte "brouillage GPS" est assortie d'un délai de réinitialisation de 5 minutes, ce qui signifie que l'alerte ne se déclenchera pas plus d'une fois toutes les 5 minutes. Si un événement se produit pendant la période de réinitialisation, il sera omis de la plateforme, y compris des rapports.
- **Plusieurs appareils :** Cette règle vous permet de sélectionner plusieurs traceurs pour recevoir des notifications, à condition que les traceurs sélectionnés prennent en charge les événements de brouillage GPS et que la fonction soit intégrée à la plateforme. Cette flexibilité permet de surveiller les événements de brouillage GPS dans différents véhicules ou appareils.
- **Alerte d'événement indépendante du GPS :** La plate-forme enregistrera et affichera l'événement même s'il est reçu dans un paquet sans coordonnées valides. L'événement sera affiché, qu'il se soit produit à l'intérieur ou à l'extérieur des géofences délimitées, car la plateforme donne la priorité à l'affichage des événements potentiellement critiques plutôt qu'à leur omission.

## Voir aussi

- [Brouillage GSM](../connexion-des-appareils/brouillage-gsm.md)