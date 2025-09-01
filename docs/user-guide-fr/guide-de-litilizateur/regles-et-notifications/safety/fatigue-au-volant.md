# Fatigue au volant

## Vue d'ensemble

La règle de conduite en cas de fatigue est une fonction essentielle de la plateforme télématique, conçue pour améliorer la sécurité routière en détectant et en alertant les équipes de dispatching lorsque des signes de fatigue du conducteur sont identifiés. Utilisant des caméras de suivi avancées, le système surveille en permanence les conducteurs pour détecter les indicateurs de somnolence ou de fatigue, qui sont des facteurs clés des accidents de la route.

Lorsque la fatigue est détectée, une alerte immédiate est envoyée au dispatching, ce qui permet d'intervenir rapidement, par exemple en organisant des pauses ou en apportant le soutien nécessaire. La mise en œuvre de cette règle permet non seulement de prévenir les accidents et de réduire les pertes opérationnelles, mais aussi de donner la priorité au bien-être des conducteurs et de promouvoir des pratiques de conduite sûres.

## Paramètres des règles

Comme cette règle dépend du matériel, la configuration est minimale au sein de la plateforme elle-même. L'exigence principale est de s'assurer que les suiveurs sélectionnés sont équipés pour prendre en charge et détecter les événements de conduite en état de fatigue.

Pour les réglages courants, veuillez vous référer à [Règles et notifications](../../regles-et-notifications.md).

## Détails du fonctionnement du système

- **Remise à zéro de la minuterie :** L'alerte "Fatigue au volant" est régie par un délai de réinitialisation de 5 secondes, ce qui garantit que les alertes ne se déclenchent pas plus d'une fois toutes les 5 secondes. Si un événement de fatigue est détecté pendant cette période de réinitialisation, il sera omis de la plateforme et des rapports.

- **Plusieurs appareils :** Cette règle permet de sélectionner plusieurs dispositifs à surveiller. Les appareils sélectionnés doivent prendre en charge les événements liés à la conduite en état de fatigue et cette fonction doit être intégrée à la plateforme. Cela permet un suivi complet sur plusieurs véhicules ou appareils, garantissant un suivi et une gestion cohérents de la fatigue du conducteur.

- **Alerte d'événement indépendante du GPS :** La plateforme enregistrera et affichera les événements de fatigue au volant même si le paquet de données ne contient pas de coordonnées GPS valides. Dans ce cas, les paramètres de géofence intérieur/extérieur sont ignorés, car le système donne la priorité à l'affichage des événements critiques, en veillant à ce qu'aucune information cruciale ne soit négligée.