# Appuyer sur le bouton SOS

## Vue d'ensemble

La fonction "Appuyer sur le bouton SOS", communément appelée "bouton SOS", est une fonction de sécurité essentielle conçue pour les appareils GPS équipés d'un bouton d'urgence. Ce bouton peut être un composant externe ou être intégré à un dispositif de suivi personnel. Il sert de bouée de sauvetage dans les situations critiques, permettant aux employés et aux personnes de demander rapidement de l'aide lorsqu'ils en ont le plus besoin.

## Paramètres des règles

La fonctionnalité de cette règle dépend des capacités et de la configuration de l'appareil, de sorte qu'aucune configuration spécifique n'est requise.

Pour les réglages courants, veuillez vous référer à [Règles et notifications](../../regles-et-notifications.md).

![](https://squaregps.atlassian.net/wiki/images/icons/grey_arrow_down.png)

Connexion d'un bouton externe à l'entrée du dispositif GPS d'un véhicule

Selon l'appareil, le bouton SOS peut être connecté soit à une entrée dédiée, spécialement conçue pour cette fonction, soit à une entrée discrète générale. S'il est connecté à une entrée discrète, vous devez créer l'entrée dans le menu Devices and Settings (Appareils et paramètres), dans la section Sensors and Buttons (Capteurs et boutons). Dans ce cas, sélectionnez le type de règle "Déclenchement d'entrée" pour une configuration correcte.

## Détails du fonctionnement du système

- **Remise à zéro de la minuterie :** L'alerte "Appui sur le bouton SOS" est assortie d'un délai de réinitialisation de 30 secondes, ce qui signifie que l'alerte ne se déclenchera pas plus d'une fois toutes les 30 secondes. Si un événement se produit pendant que la règle attend la réinitialisation, la plate-forme ne tiendra pas compte de l'événement, y compris dans les rapports.
- **Plusieurs appareils :** Cette règle permet aux utilisateurs de sélectionner plusieurs suiveurs dont ils souhaitent recevoir des notifications. Les traceurs sélectionnés doivent prendre en charge l'événement "Appui sur le bouton SOS" et cette fonctionnalité doit être intégrée à la plateforme de ces traceurs. Cela permet aux utilisateurs de surveiller les signaux d'urgence sur plusieurs appareils de manière pratique.
- **Alerte d'événement indépendante du GPS :** La plate-forme reconnaît et comptabilise ce type d'événement matériel même si le paquet de données ne contient pas de coordonnées GPS valides. L'événement sera affiché, qu'il se soit produit à l'intérieur ou à l'extérieur des zones géographiques définies. Dans ce cas, les paramètres Inside/Outside geofence ne sont pas pris en compte, ce qui garantit qu'aucun événement critique n'est omis.