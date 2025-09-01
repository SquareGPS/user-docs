# Identification du conducteur

## Vue d'ensemble

La règle "Identification du conducteur" est conçue pour aider les gestionnaires de flotte à surveiller et à contrôler l'utilisation des véhicules en identifiant précisément les conducteurs. Cette règle garantit que seuls les conducteurs autorisés peuvent conduire les véhicules, permet de savoir quel conducteur est au volant et enregistre la durée et les conditions de chaque session de conduite. Elle permet d'améliorer l'efficacité opérationnelle, de renforcer la responsabilité et de favoriser le respect des protocoles de sécurité.

La règle utilise les capacités intégrées de l'appareil pour vérifier l'identité du conducteur directement à la source. Les informations autorisées sur le conducteur sont stockées dans la mémoire interne de l'appareil. Lorsqu'un conducteur utilise un iButton, une clé RFID ou la reconnaissance faciale via une caméra intelligente pour s'authentifier, l'appareil vérifie son identité sur place. La plateforme enregistre ensuite ces événements d'identification et génère des alertes en temps réel, des rapports détaillés et des notifications selon les besoins.

**Cas d'utilisation de l'application :**

- **Véhicules partagés :** Suivre et gérer plusieurs conducteurs utilisant le même véhicule.
- **La sécurité :** Limiter l'utilisation du véhicule au seul personnel autorisé, avec des alertes en temps réel en cas de tentatives non autorisées.
- **Conformité :** Veiller à ce que l'utilisation du véhicule soit conforme aux politiques et réglementations de l'entreprise.
- **Efficiency:** Réduisez les erreurs et rationalisez le processus d'identification des conducteurs, en particulier dans les environnements à forte pression, grâce à la reconnaissance par caméra.

## Paramètres des règles

Aucun autre réglage spécifique de la règle n'est nécessaire.

Pour les réglages courants, veuillez vous référer à [Règles et notifications](../../regles-et-notifications.md).

## Détails de l'opération système

- **Remise à zéro de la minuterie :** L'alerte "Identification du conducteur" est assortie d'un délai de réinitialisation de 5 secondes, ce qui signifie que l'alerte ne se déclenchera pas plus d'une fois toutes les 5 secondes. Si un événement se produit pendant la période de réinitialisation de la règle, la plate-forme ne déclenche pas l'alerte, ce qui garantit que les notifications et les rapports restent clairs et faciles à gérer.
- **Plusieurs appareils :** Les utilisateurs peuvent appliquer cette règle à plusieurs traceurs, à condition qu'ils prennent en charge l'"identification du conducteur" par le biais d'événements RFID, iButton ou caméra. Cela vous permet de surveiller les événements d'identification du conducteur dans plusieurs véhicules ou dispositifs, assurant ainsi une couverture complète.
- **Traitement des événements indépendant du GPS :** La plate-forme traitera et affichera les événements d'identification du conducteur même si le paquet de données ne contient pas de coordonnées GPS valides. Ces événements sont enregistrés, qu'ils se produisent ou non à l'intérieur d'un périmètre géographique défini. Dans ce cas, les paramètres de géofence intérieur/extérieur sont contournés pour s'assurer qu'aucun événement critique n'est manqué.

## Voir aussi

- [**Règle de changement de conducteur**](changement-de-conducteur.md) - La règle est axée sur l'enregistrement lorsqu'un autre conducteur prend le contrôle du véhicule, la plateforme comparant les données du conducteur actuel et celles du conducteur précédent pour détecter les changements et générer des rapports après coup.