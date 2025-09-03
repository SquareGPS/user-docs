# Appui sur le bouton d'appel

## Vue d'ensemble

La règle du "bouton d'appel enfoncé" est conçue pour les appareils GPS équipés d'une fonction d'appel intégrée, que l'on trouve généralement dans les appareils capables de passer des appels vocaux ou de communiquer par radio.

Cette règle déclenche des notifications chaque fois que la fonction d'appel téléphonique de l'appareil est activée, ce qui permet d'établir rapidement une communication en temps réel. Cette fonction améliore la sûreté, la sécurité et l'efficacité opérationnelle en garantissant des réponses rapides dans les situations critiques et en contribuant à des opérations plus fluides.

## Paramètres des règles

La fonctionnalité de cette règle dépend des capacités et de la configuration de l'appareil, de sorte qu'aucune configuration spécifique n'est requise.

Pour les réglages courants, veuillez vous référer à [Règles et notifications](../../../guide-de-litilizateur/regles-et-notifications.md).

## Détails du fonctionnement du système

* **Remise à zéro de la minuterie :** L'alerte "Bouton d'appel enfoncé" est assortie d'un délai de réinitialisation d'une minute, ce qui signifie que l'alerte ne se déclenchera pas plus d'une fois par minute. Si un événement se produit pendant que la règle attend la réinitialisation, la plate-forme ne tiendra pas compte de l'événement, y compris dans les rapports.
* **Plusieurs appareils :** Cette règle permet aux utilisateurs de sélectionner plusieurs suiveurs dont ils souhaitent recevoir des notifications. Les suiveurs sélectionnés doivent prendre en charge l'événement "Appui sur le bouton d'appel", et cette fonctionnalité doit être intégrée à la plateforme de ces suiveurs. Cela permet aux utilisateurs de surveiller les événements sur plusieurs appareils de manière pratique.
* **Alerte d'événement indépendante du GPS :** La plate-forme reconnaît et comptabilise ce type d'événement matériel même si le paquet de données ne contient pas de coordonnées GPS valides. L'événement sera affiché, qu'il se soit produit à l'intérieur ou à l'extérieur des zones géographiques définies. Dans ce cas, les paramètres Inside/Outside geofence ne sont pas pris en compte, ce qui garantit qu'aucun événement critique n'est omis.
