# Changement de niveau de carburant

## Vue d'ensemble

La surveillance des niveaux de carburant est essentielle pour gérer la consommation de carburant et détecter les utilisations non autorisées. La règle de changement de niveau de carburant est conçue pour fournir des notifications en temps réel lorsque des changements significatifs se produisent dans les niveaux de carburant, tels que des augmentations ou des diminutions soudaines.

Ces notifications peuvent être envoyées par l'intermédiaire de l'interface utilisateur web, par SMS ou par courrier électronique, et peuvent être consolidées dans des rapports. Cette surveillance proactive aide les utilisateurs à réagir rapidement aux changements de niveau de carburant, ce qui permet de réduire les coûts de carburant et de résoudre les conflits entre les employés.

> \[!INFO] Avant de configurer cette règle, assurez-vous que le capteur de niveau de carburant que vous avez l'intention de surveiller est correctement configuré. Pour obtenir des instructions détaillées sur l'installation et la configuration des capteurs de niveau de carburant, veuillez vous référer à la section [Section du capteur de niveau de carburant](../../appareils-et-parametres/capteurs-pour-vehicules-1/measurement-sensors-1/fuel-level-sensor.md).

## Paramètres des règles

#### Capteur

Spécifiez le capteur de niveau de carburant qui sera utilisé comme source pour les notifications et l'analyse. Le nombre de changements de carburant indiqué est régulé par le paramètre de précision du capteur de niveau de carburant, qui est expliqué dans la section [Section du capteur de niveau de carburant](../../appareils-et-parametres/capteurs-pour-vehicules-1/measurement-sensors-1/fuel-level-sensor.md).

Pour les réglages courants, veuillez vous référer à [Règles et notifications](../../../guide-de-litilizateur/regles-et-notifications.md).

## Détails du fonctionnement du système

* La plateforme lisse les données du capteur et compare le changement total dans une fenêtre de 10 minutes avec le paramètre de précision du capteur de carburant pour déterminer si une notification doit être déclenchée. Par exemple, avec une précision de 5 %, une variation du niveau de carburant de 5 litres ou plus pour un réservoir de 100 litres dans un délai de 10 minutes déclenchera une alerte. Si la variation cumulée atteint ou dépasse ce seuil, la plate-forme envoie une notification.
* L'estimation du volume de changement de combustible n'est pas encore incluse dans les notifications mais sera bientôt disponible.
* L'alerte "Changement de niveau de carburant" est assortie d'un délai de réinitialisation de 15 minutes, ce qui signifie que l'alerte ne se déclenchera pas plus d'une fois toutes les 15 minutes. Si un changement de niveau de carburant se produit pendant la période de réinitialisation de la règle, la plate-forme ne tiendra pas compte de l'événement, y compris dans les rapports.
* Cette règle ne prend en charge qu'un seul dispositif par règle. Cette limitation est due à la complexité des références croisées entre plusieurs capteurs de mesure avec différents suiveurs, tables d'étalonnage et autres aspects de mesure et de filtrage.
