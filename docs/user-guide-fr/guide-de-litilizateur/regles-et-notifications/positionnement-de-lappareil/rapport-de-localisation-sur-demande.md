# Rapport de localisation sur demande

## Vue d'ensemble

Le **Rapport de localisation sur demande par SMS** permet aux utilisateurs de demander manuellement la position actuelle d'un appareil GPS en envoyant une commande SMS. Cette fonction est particulièrement utile dans les situations où l'appareil ne peut pas établir de connexion cellulaire avec la plateforme sur IP, par exemple lorsqu'il se trouve dans une zone d'itinérance où la couverture de données est limitée ou inexistante.

Lorsque l'appareil n'est pas en mesure de transmettre ses données de localisation par les canaux habituels (tels que les réseaux GPRS ou 3G/4G), la fonction de localisation est activée. **Mise à jour de la localisation sur demande par SMS** offre une alternative fiable. En envoyant une commande SMS de la plateforme à l'appareil, les utilisateurs peuvent toujours récupérer la position de l'appareil. L'appareil répond en envoyant ses coordonnées GPS par SMS à la plateforme, assurant ainsi le suivi de la localisation même lorsque les connexions de données standard sont indisponibles.

Pour plus de commodité, Navixy propose un service d'aide à la décision. **Mise à jour de la localisation par SMS**. Cette règle avertit les utilisateurs dès qu'une mise à jour de la position GPS est reçue par SMS. Étant donné que les mises à jour de localisation par SMS peuvent prendre de quelques minutes à quelques heures, en fonction de la disponibilité du réseau et de l'état de l'appareil, cette règle permet de s'assurer que les utilisateurs sont rapidement alertés lorsque la mise à jour a lieu. Cette fonction de notification rationalise le processus, permettant aux utilisateurs de se concentrer sur d'autres tâches sans avoir à vérifier manuellement l'arrivée de la mise à jour.

## Paramètres des règles

Il n'existe pas de règles spécifiques. Pour les paramètres courants, veuillez vous référer à [Règles et notifications](../../regles-et-notifications.md).

## Détails du fonctionnement du système

- **Remise à zéro de la minuterie.** L'alerte "Rapport de localisation sur demande" est assortie d'un délai de réinitialisation d'une minute, ce qui signifie que l'événement d'alerte ne se produira pas plus d'une fois toutes les 1 minutes. Si ce type d'événement se produit pendant que la règle attend la réinitialisation, cet événement sera omis par la plate-forme, y compris les rapports.
- **Plusieurs appareils.** Dans ce type de règle, les utilisateurs ont la possibilité de sélectionner plusieurs suiveurs dont ils souhaitent recevoir des notifications. La seule condition est que les suiveurs sélectionnés prennent en charge les événements de localisation à la demande et que la fonction soit intégrée à la plateforme pour les suiveurs en question. Cela signifie que les utilisateurs peuvent choisir plusieurs suiveurs compatibles pour recevoir des notifications, ce qui leur permet de surveiller les événements de conduite dangereuse sur plusieurs véhicules ou appareils de manière pratique.