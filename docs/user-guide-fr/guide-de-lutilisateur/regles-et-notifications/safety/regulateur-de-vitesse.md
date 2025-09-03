# Régulateur de vitesse

## Vue d'ensemble

La réception de notifications lorsque le régulateur de vitesse est activé ou désactivé dans un véhicule fournit des informations précieuses pour le suivi et la gestion des performances du véhicule. En voici les principaux avantages :

* **Contrôle de l'efficacité énergétique :** Le régulateur de vitesse permet de maintenir une vitesse constante, ce qui peut améliorer le rendement énergétique. Les notifications permettent aux utilisateurs de suivre l'utilisation du régulateur de vitesse et d'évaluer son impact sur la consommation de carburant.
* **Gestion de la batterie :** Pour les véhicules électriques ou hybrides, l'utilisation du régulateur de vitesse peut affecter la durée de vie de la batterie et l'autonomie. Des notifications aident les utilisateurs à surveiller l'impact du régulateur de vitesse sur l'utilisation de la batterie, ce qui permet une meilleure gestion de l'énergie électrique du véhicule.
* **Analyse du comportement au volant :** Le suivi du moment et de l'endroit où le régulateur de vitesse est utilisé permet de mieux comprendre le comportement du conducteur. Ces données peuvent être utilisées pour analyser les habitudes de conduite et identifier les possibilités d'amélioration, telles que la réduction de l'utilisation excessive ou l'augmentation de l'utilisation sous-utilisée du régulateur de vitesse.
* **Évaluation des performances :** Le suivi de l'utilisation du régulateur de vitesse peut aider à évaluer les performances du véhicule. Les utilisateurs peuvent comparer le régulateur de vitesse avec d'autres modes de conduite pour évaluer l'efficacité sur différents itinéraires et dans différentes conditions de conduite.
* **Sécurité et confort :** Le régulateur de vitesse améliore le confort et la sécurité pendant les longs trajets. Des notifications permettent aux utilisateurs de savoir si le régulateur de vitesse est actif, ce qui leur permet d'adapter leur style de conduite en fonction des besoins.

Ces avantages peuvent varier en fonction de la marque, du modèle et des caractéristiques supplémentaires du véhicule.

## Paramètres des règles

Cette règle ne nécessite pas de paramétrage spécifique.

Pour les réglages courants, veuillez vous référer à [Règles et notifications](../../../guide-de-litilizateur/regles-et-notifications.md).

## Détails du fonctionnement du système

* **Remise à zéro de la minuterie :** L'alerte "Régulateur de vitesse activé/désactivé" a une durée de vie d'un an. Minuterie de 10 minutesLa période de réinitialisation permet d'éviter que l'alerte ne se déclenche plus d'une fois toutes les 10 minutes. Si un autre événement se produit au cours de cette période de réinitialisation, il sera omis de la plate-forme et des rapports.
* **Plusieurs appareils :** Les utilisateurs peuvent sélectionner plusieurs suiveurs pour recevoir des notifications. Les suiveurs sélectionnés doivent prendre en charge les événements de mise en marche et d'arrêt du régulateur de vitesse et avoir intégré cette fonction dans la plateforme. Cela permet de surveiller les événements liés au régulateur de vitesse sur plusieurs véhicules.
* **Alerte d'événement indépendante du GPS :** La plate-forme enregistre et affiche les événements de régulation de vitesse même si le paquet de données ne contient pas de coordonnées GPS valides. Les paramètres de géofence intérieure/extérieure sont ignorés pour cette règle, ce qui permet de ne pas manquer les événements critiques.
