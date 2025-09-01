# Dispositif activé/désactivé

## Vue d'ensemble

La règle "Appareil allumé/éteint" permet aux utilisateurs de contrôler quand un appareil GPS est allumé ou éteint. Cette règle est particulièrement utile pour les responsables qui doivent s'assurer que les employés utilisent les appareils GPS conformément aux politiques prescrites pendant les heures de travail. Elle fournit des informations précieuses sur les habitudes d'utilisation des appareils, ce qui permet d'éviter les abus et de s'assurer que les appareils fonctionnent correctement.

> [!WARNING]
> Cette règle ne s'applique qu'aux dispositifs qui ont la capacité de signaler leur état d'alimentation. En d'autres termes, l'appareil GPS doit être en mesure d'envoyer des notifications à la plate-forme lorsqu'il est allumé ou éteint. Si un appareil ne dispose pas de cette fonctionnalité, la règle ne peut pas être appliquée, car la plate-forme ne recevrait pas les données nécessaires pour déclencher des notifications, mais vous pouvez toujours utiliser l'appareil indépendant "[L'appareil a perdu la connexion](../connexion-des-appareils/lappareil-a-perdu-la-connexion.md)La règle ".

## Paramètres des règles

### Traceur activé

La règle "Traceur allumé" déclenche une notification lorsqu'un traceur est mis sous tension, à condition que l'appareil dispose de la fonctionnalité de signalement nécessaire.

**Points clés :**

- **Objet :** Surveille la mise sous tension d'un traceur, ce qui vous permet de savoir quand les appareils se remettent à fonctionner.
- **Remise à zéro de la minuterie :** L'alerte "Tracker allumé" comprend un Minuterie de réinitialisation de 60 secondesqui empêche l'envoi de plusieurs alertes au cours d'une même minute, réduisant ainsi les notifications inutiles.
- **Configuration :** La règle ne nécessite qu'une configuration minimale et prend en charge plusieurs suiveurs à condition qu'ils aient la capacité de signaler les événements de mise sous tension.

### Traceur activé/désactivé

La règle "Traceur éteint" déclenche une notification lorsqu'un traceur est éteint ou perd la connexion, à condition que l'appareil puisse signaler cet événement et se déclenche à nouveau lorsqu'il est rallumé.

**Points clés :**

- **Objet :** Vous avertit lorsqu'un traceur est éteint ou perd sa connexion, ce qui vous permet de réagir rapidement à d'éventuels problèmes.
- **Remise à zéro de la minuterie :** Cette alerte comprend un Minuterie de remise à zéro de 10 secondesEn outre, les alertes ne sont pas déclenchées plus d'une fois par an, ce qui permet de s'assurer qu'elles ne sont pas déclenchées plus d'une fois par an. 10 secondesce qui permet d'éviter les notifications excessives.
- **Configuration :** Similaire à la règle "Tracker switched ON", cette règle nécessite également une configuration minimale et peut être appliquée à plusieurs trackers qui prennent en charge les rapports d'événements de mise hors tension.

Pour les réglages courants, veuillez vous référer à [Règles et notifications](../../regles-et-notifications.md).

## Détails du fonctionnement du système

- La règle "Tracker switched ON/OFF" fonctionne sur la base des événements matériels générés par le tracker lorsqu'il est allumé ou éteint. Ces événements sont transmis à la plateforme et traités en vue d'une notification.
- La règle est flexible et peut être appliquée à plusieurs suiveurs simultanément, à condition qu'ils prennent en charge la fonction d'événement ON/OFF.
- Si la plate-forme identifie un événement matériel de ce type sans coordonnées valides, l'événement est tout de même considéré comme valide et affiché, ce qui garantit qu'aucun événement crucial n'est manqué.
- Le système vous permet de suivre ces événements, qu'ils se produisent à l'intérieur ou à l'extérieur des géofences définies, car la logique de géofence est contournée pour ces événements spécifiques afin d'assurer une surveillance complète.

Cette règle permet de maintenir l'intégrité opérationnelle de votre flotte, de s'assurer que tous les traceurs fonctionnent comme prévu et de réagir rapidement à tout changement inattendu de l'état des traceurs.