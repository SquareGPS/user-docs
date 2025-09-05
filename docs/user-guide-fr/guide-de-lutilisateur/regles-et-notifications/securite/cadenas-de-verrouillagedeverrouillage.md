# Cadenas de verrouillage/déverrouillage

## Cadenas de verrouillage/déverrouillageAperçu

La règle "Verrouillage/déverrouillage du cadenas" est essentielle pour les organisations qui utilisent des serrures intelligentes dotées d'un GPS pour sécuriser les biens de valeur et les zones critiques. Cette règle surveille l'état de ces serrures et garantit que les utilisateurs sont instantanément informés lorsqu'une serrure est activée ou désactivée.

Spécialement conçue pour les serrures GPS, cette règle fournit des alertes en temps réel pour toutes les interactions de la serrure, qu'il s'agisse de sécuriser une zone ou de verrouiller une cargaison dans un conteneur.

## Paramètres des règles

Cette règle dépend entièrement des capacités et de la configuration matérielle de l'appareil. Il n'y a pas de paramètres spécifiques à configurer dans la règle elle-même.

Pour les réglages courants, veuillez vous référer à [Règles et notifications](../).

## Détails du fonctionnement du système

* **Remise à zéro de la minuterie :** L'alerte "Verrouillage/déverrouillage du cadenas" est assortie d'un délai de réinitialisation d'une minute, ce qui signifie qu'elle ne se déclenchera pas plus d'une fois par minute. Les événements survenant pendant cette période de réinitialisation ne seront pas pris en compte dans les notifications et les rapports.
* **Traqueurs multiples :** Cette règle prend en charge plusieurs trackers, à condition qu'ils puissent détecter les événements de verrouillage/déverrouillage (Padlock) et que cette fonction soit intégrée à la plateforme. Les utilisateurs peuvent ainsi surveiller efficacement ces événements sur plusieurs appareils.
* **Traitement indépendant du GPS :** La plateforme traite et affiche les événements de verrouillage/déverrouillage même si le paquet de données ne contient pas de coordonnées GPS valides. Ces événements sont enregistrés, qu'ils se produisent à l'intérieur ou à l'extérieur d'un périmètre géographique, ce qui garantit qu'aucun événement critique n'est manqué.
