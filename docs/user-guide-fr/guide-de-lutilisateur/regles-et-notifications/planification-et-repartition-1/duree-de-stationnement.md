# Durée de stationnement

## Vue d'ensemble

La règle relative à la durée de stationnement est conçue pour avertir les utilisateurs lorsque la durée de stationnement d'un véhicule dépasse une limite spécifiée. Cette règle est essentielle pour contrôler la durée d'immobilisation des véhicules et s'assurer que les conducteurs respectent les normes de temps fixées pour les périodes de stationnement et d'immobilisation.

Par exemple, si la durée de stationnement autorisée est fixée à 30 minutes, le système alertera les utilisateurs chaque fois qu'un véhicule restera stationné au-delà de cette limite. Ces notifications peuvent être envoyées par l'intermédiaire de l'interface utilisateur, d'un courrier électronique ou d'un SMS, et les utilisateurs peuvent également générer des rapports afin d'examiner l'historique de ces événements.

## Paramètres des règles

**Durée de stationnement autorisée**\
Le décompte du temps de stationnement commence dès que le véhicule entre en stationnement. Les utilisateurs peuvent configurer la durée de stationnement autorisée, avec des options allant de 5 à 60 000 minutes. La minuterie se réinitialise lorsque le véhicule quitte l'état de stationnement. Pour plus d'informations sur la détection de stationnement, veuillez consulter l'article Détection de stationnement.

Pour surveiller le temps de séjour dans des zones spécifiques, liez la règle aux géofences désignées.

Pour les réglages courants, veuillez vous référer à [Règles et notifications](../../../guide-de-litilizateur/regles-et-notifications.md).

## Détails du fonctionnement du système

* L'alerte "Durée de stationnement" est assortie d'un délai de réinitialisation de 10 secondes, ce qui signifie que l'alerte ne se déclenchera pas plus d'une fois toutes les 10 secondes. Si un événement se produit pendant que la règle attend la réinitialisation, la plate-forme ne tiendra pas compte de l'événement, y compris dans les rapports.
* Cette règle est traitée dans le nuage et n'est pas liée à un matériel spécifique, ce qui permet de l'appliquer à plusieurs suiveurs simultanément. Cette flexibilité permet aux utilisateurs de gérer plusieurs suiveurs dans le cadre d'une seule règle.
