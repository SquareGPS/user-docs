# Coupure de courant externe

## Vue d'ensemble

La règle "Coupure d'alimentation externe" est conçue pour les traceurs GPS filaires qui dépendent du système électrique du véhicule. Cette règle est essentielle pour la gestion des flottes, car elle surveille l'alimentation électrique du dispositif GPS et alerte les utilisateurs en cas de coupure de l'alimentation externe.

Lorsqu'il détecte une coupure de courant, le dispositif GPS bascule automatiquement sur sa batterie interne (le cas échéant) afin de maintenir sa fonctionnalité et d'envoyer un rapport à la plateforme. Cette dernière enregistre ces événements et en informe les utilisateurs en fonction des paramètres de la règle.

## Paramètres des règles

Cette règle dépend entièrement des capacités et de la configuration matérielle de l'appareil. Il n'y a pas de paramètres spécifiques à configurer dans la règle elle-même.

Pour les réglages courants, veuillez vous référer à [Règles et notifications](../../regles-et-notifications.md).

## Détails du fonctionnement du système

- **Remise à zéro de la minuterie.** L'alerte "Coupure d'électricité externe" est assortie d'un délai de réinitialisation de 5 minutes, ce qui signifie que l'alerte ne se déclenchera pas plus d'une fois toutes les 5 minutes. Si un événement se produit pendant la période de réinitialisation, il sera omis de la plate-forme et ne sera pas inclus dans les rapports.
- **Événement détecté par l'appareil.** Cet événement est déclenché directement par l'appareil en fonction de sa configuration. Votre appareil et sa configuration doivent prendre en charge cette fonctionnalité afin d'utiliser la règle.
- **Alerte d'événement indépendante du GPS.** La plateforme enregistrera et affichera l'événement même s'il est reçu dans un message sans coordonnées valides, garantissant ainsi que les utilisateurs sont informés quel que soit l'emplacement de l'événement. Les paramètres intérieur/extérieur des géofences sont ignorés dans ce cas, car la plateforme affiche en priorité les événements potentiellement critiques.