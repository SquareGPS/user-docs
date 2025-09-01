# Déplacement non autorisé

## Vue d'ensemble

La règle "Mouvement non autorisé" est conçue pour renforcer la sécurité des véhicules en alertant les utilisateurs lorsqu'un véhicule à l'arrêt commence à se déplacer sans autorisation. Cette règle est particulièrement utile dans les situations où le véhicule est censé rester immobile, par exemple lorsqu'il est éteint, mais qu'il se met inopinément en mouvement. Elle permet d'identifier rapidement un vol potentiel ou une utilisation non autorisée, ce qui permet aux utilisateurs d'agir rapidement.

**Applications typiques :**

- **Prévention des vols :** Alertes immédiates si un véhicule est déplacé sans autorisation.
- **Sécurité du parking :** Surveiller les véhicules dans les aires de stationnement désignées afin de détecter tout mouvement non autorisé.
- **Protection des actifs :** Veiller à ce que les véhicules ou équipements stationnaires restent en sécurité en dehors des heures de travail.

La règle fonctionne en utilisant l'accéléromètre intégré de l'appareil GPS et d'autres paramètres de configuration pour détecter tout mouvement non autorisé. La précision de cette règle dépend de l'installation et de la configuration correctes de l'appareil, qui varient selon le modèle. Lorsque la plateforme reçoit le paquet de données indiquant un mouvement non autorisé, elle traite et affiche l'événement, fournissant aux utilisateurs des alertes en temps réel.

## Paramètres des règles

Cette règle dépend entièrement des capacités du dispositif et de la configuration matérielle. En règle générale, le dispositif doit être capable de détecter si le véhicule n'est pas utilisé, par exemple en contrôlant l'état de l'allumage.

Il n'y a pas de paramètres spécifiques à configurer dans la règle elle-même. Pour les paramètres courants, veuillez vous référer à [Règles et notifications](../../regles-et-notifications.md).

## Détails du fonctionnement du système

- **Remise à zéro de la minuterie :** L'alerte "Mouvement non autorisé" est assortie d'un délai de réinitialisation de 5 minutes, ce qui signifie que l'alerte ne se déclenchera pas plus d'une fois toutes les 5 minutes. Si un événement se produit pendant la période de réinitialisation de la règle, la plate-forme supprime l'alerte, ce qui garantit que les notifications et les rapports restent clairs et gérables.
- **Plusieurs appareils :** Cette règle peut être appliquée à plusieurs traceurs, à condition qu'ils prennent en charge les événements de "mouvement non autorisé" et que cette fonction soit intégrée à la plateforme. Cela permet aux utilisateurs de surveiller les mouvements non autorisés de plusieurs véhicules, assurant ainsi une couverture de sécurité complète.
- **Traitement des événements indépendant du GPS :** La plateforme traite et affiche les mouvements non autorisés même si le paquet de données ne contient pas de coordonnées GPS valides. Ces événements sont enregistrés, qu'ils se produisent à l'intérieur ou à l'extérieur d'une géofence désignée. Les paramètres de géofence intérieur/extérieur sont contournés dans ce cas, ce qui garantit qu'aucun événement critique n'est manqué.