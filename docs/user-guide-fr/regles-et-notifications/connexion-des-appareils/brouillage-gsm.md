# Brouillage GSM

## Vue d'ensemble

Le brouillage GSM désigne la perturbation des signaux GSM (signaux mobiles ou cellulaires) en raison d'interférences provenant de sources proches. Ces interférences, souvent appelées masquage ou masquage de fréquence, peuvent empêcher les appareils mobiles de se connecter aux réseaux mobiles, ce qui affecte des services tels que les données mobiles (2G, 3G, 4G, LTE), la messagerie texte et les appels vocaux. Dans le contexte du suivi GPS, le brouillage GSM peut entraîner la perte de la communication de données en temps réel, d'où l'importance de mettre en place des règles de détection.

Par exemple, une entreprise de logistique qui utilise des véhicules équipés de GPS pour transporter des marchandises de valeur s'appuie sur les signaux GSM pour le suivi de la localisation en temps réel. En cas de brouillage GSM, ces signaux sont perturbés, ce qui peut compromettre la sécurité des expéditions. En mettant en œuvre des règles de détection du brouillage GSM, l'entreprise peut recevoir des alertes immédiates, ce qui lui permet d'agir rapidement pour protéger ses actifs.

## Paramètres des règles

Cette règle dépend entièrement des capacités et de la configuration matérielle de l'appareil. Il n'y a pas de paramètres spécifiques à configurer dans la règle elle-même.

Pour les réglages courants, veuillez vous référer à [Règles et notifications](../../regles-et-notifications.md).

## Détails du fonctionnement du système

- **Remise à zéro de la minuterie :** L'alerte "brouillage GSM" est assortie d'un délai de réinitialisation de 5 minutes, ce qui signifie que l'alerte ne se déclenchera pas plus d'une fois toutes les 5 minutes. Si un événement se produit pendant la période de réinitialisation, il sera omis par la plate-forme et ne sera pas inclus dans les rapports.
- **Plusieurs appareils :** Les utilisateurs peuvent sélectionner plusieurs traceurs à surveiller dans le cadre de cette règle. La seule condition est que les traceurs sélectionnés prennent en charge les événements de brouillage GSM et soient intégrés à la plateforme. Cette flexibilité permet aux utilisateurs de surveiller ce type d'événement sur plusieurs véhicules ou appareils de manière pratique.
- **Alerte d'événement indépendante du GPS :** La plateforme enregistrera et affichera l'événement même s'il est reçu dans un message sans coordonnées GPS valides. Les utilisateurs sont ainsi informés de l'événement, quelles que soient les données de localisation. Les paramètres des boutons radio Intérieur/Extérieur pour les géofences sont ignorés dans ces cas, car la plateforme donne la priorité à l'affichage des événements potentiellement critiques.

## Voir aussi

- [Brouillage du GPS](../positionnement-de-lappareil/brouillage-du-gps.md)