# Absence du conducteur

## Vue d'ensemble

L'événement "Absence du conducteur" est conçu pour contrôler et garantir la présence du conducteur sur le siège du véhicule. Cette fonction est particulièrement importante pour éviter que le véhicule ne soit laissé sans surveillance dans des situations où il pourrait présenter un risque pour la sécurité ou enfreindre les politiques de l'entreprise.

### Comment cela fonctionne-t-il ?

Cette fonction repose généralement sur des systèmes vidéo embarqués équipés d'IA et de capteurs pour surveiller en permanence le siège du conducteur. Ces systèmes utilisent une combinaison de reconnaissance visuelle (via des caméras) et de données de capteurs pour détecter la présence ou l'absence d'un conducteur. Si le système détecte que le siège du conducteur est inoccupé lorsque le véhicule est en marche ou lorsqu'il devrait être occupé, il déclenche un événement "Absence du conducteur".

Cet événement est ensuite communiqué à la plateforme télématique Navixy, qui peut générer des alertes, enregistrer l'événement et avertir le personnel approprié. Une alerte peut être déclenchée, par exemple, si le véhicule est en mouvement et que le système détecte qu'il n'y a pas de conducteur sur le siège, ou si le conducteur quitte le siège sans avoir correctement sécurisé le véhicule.

### Applications

- **Sécurité des flottes :** Veiller à ce que les véhicules ne soient pas utilisés sans conducteur, afin de prévenir les accidents et l'utilisation non autorisée.
- **La sécurité :** Alerter les gestionnaires de flotte si un véhicule est laissé sans surveillance dans une zone potentiellement dangereuse ou à haut risque.
- **Conformité :** Aider les flottes à se conformer aux réglementations en matière de sécurité qui exigent la présence d'un conducteur pendant le fonctionnement du véhicule.
- **Assurance :** Fournir des preuves en cas d'incidents où l'absence du conducteur pourrait être un facteur, ce qui peut être nécessaire pour les réclamations d'assurance ou à des fins juridiques.

L'événement "Absence du conducteur" est un élément essentiel de l'amélioration de la sécurité et de la sûreté des flottes. Il fournit aux gestionnaires de flottes les outils nécessaires pour surveiller les situations où la présence du conducteur est requise et pour y répondre.

## Paramètres des règles

Aucun paramètre spécifique n'est requis pour cette règle.

Pour les réglages courants, veuillez vous référer à [Règles et notifications](../../regles-et-notifications.md).

## Détails du fonctionnement du système

- **Remise à zéro de la minuterie :** L'alerte "Absence du conducteur" est assortie d'un délai de réinitialisation de 10 secondes, ce qui signifie que l'alerte ne se déclenchera pas plus d'une fois toutes les 10 secondes. Si un événement se produit pendant la période de réinitialisation de la règle, la plate-forme supprime l'alerte, ce qui permet de conserver des notifications et des rapports clairs et faciles à gérer.

- **Plusieurs appareils :** Cette règle peut être appliquée à plusieurs systèmes de suivi, à condition qu'ils prennent en charge les événements "Absence du conducteur" et que cette fonction soit intégrée à la plateforme. Cela permet aux utilisateurs de surveiller ces événements sur plusieurs véhicules ou appareils de manière pratique.

- **Traitement des événements indépendant du GPS :** La plateforme traite et affiche les événements liés à l'absence du conducteur, même si le paquet de données ne contient pas de coordonnées GPS valides. Ces événements sont enregistrés, qu'ils se produisent à l'intérieur ou à l'extérieur d'une géofence désignée. Les paramètres de géofence intérieur/extérieur sont contournés dans ce cas, ce qui garantit qu'aucun événement critique n'est manqué.