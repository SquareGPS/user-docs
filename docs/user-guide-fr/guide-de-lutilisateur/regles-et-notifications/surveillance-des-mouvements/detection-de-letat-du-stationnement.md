# Détection de l'état du stationnement

## Vue d'ensemble

Cette règle permet aux utilisateurs de recevoir des notifications lorsqu'un appareil commence ou termine son stationnement. Par exemple, les organisations qui souhaitent contrôler le temps de conduite de leurs véhicules peuvent utiliser cette règle pour s'assurer que les véhicules ne sont pas utilisés en dehors des heures de travail. Cette règle fournit des notifications à l'interface utilisateur, à l'adresse électronique ou au numéro de téléphone concernant les états de stationnement des objets sélectionnés.

La mise en place de cette règle permet aux utilisateurs de rester informés du début et de la fin de leurs déplacements, ainsi que des changements dans l'état de stationnement de leurs véhicules. Le contrôle, la sécurité et l'efficacité des opérations de gestion de flotte s'en trouvent renforcés.

## Paramètres des règles

**Configurations de détection de stationnement**

Les paramètres d'une règle de détection de stationnement sont gérés exclusivement dans le widget Détection de stationnement. Pour des informations détaillées sur la configuration de la détection de stationnement, veuillez vous référer à l'article Détection de stationnement.

Pour les réglages courants, veuillez vous référer à [Règles et notifications](../).

## Détails du fonctionnement du système

* L'alerte "Détection de l'état de stationnement" est assortie d'un délai de réinitialisation de 10 secondes, ce qui signifie que l'événement d'alerte ne se produira pas plus d'une fois toutes les 10 secondes. Si un événement se produit pendant que la règle attend la réinitialisation, la plate-forme ne tiendra pas compte de l'événement, y compris dans les rapports.
* Cette règle est détectée du côté du serveur et n'est pas liée à un matériel spécifique, ce qui permet de l'appliquer à plusieurs trackers simultanément. Cette flexibilité vous permet de gérer plusieurs trackers au sein d'une seule règle.
