# Cas d'intrusion

## Vue d'ensemble

La règle "Intrusion dans le boîtier" est conçue pour les appareils GPS qui émettent une alerte lorsque le boîtier de l'appareil est manipulé ou ouvert, ce qui vous permet d'être immédiatement informé de tout accès non autorisé à vos appareils.

Cette règle est essentielle pour renforcer la sécurité et la protection des marchandises de valeur pendant le transport ou le stockage. En utilisant des trackers équipés de la règle "Case Intrusion", vous pouvez ajouter une couche supplémentaire de sécurité pour protéger vos biens.

## Paramètres des règles

Cette règle dépend entièrement des capacités et de la configuration matérielle de l'appareil. Il n'y a pas de paramètres spécifiques à configurer dans la règle elle-même.

Pour les réglages courants, veuillez vous référer à [Règles et notifications](../../regles-et-notifications.md).

## Détails du fonctionnement du système

- **Chronomètre de repos.** L'alerte "Cas d'intrusion" est assortie d'un délai de réinitialisation d'une minute, ce qui signifie que l'alerte ne se déclenchera pas plus d'une fois par minute. Si un événement se produit pendant la période de réinitialisation, il sera omis de la plate-forme, y compris dans les rapports.
- **Plusieurs appareils.** Vous pouvez sélectionner plusieurs traceurs GPS qui déclencheront des notifications lorsqu'un événement de sabotage se produira. La seule condition est que les traceurs sélectionnés prennent en charge les événements de détection de sabotage et que cette fonction soit intégrée à la plateforme.

- **Alerte d'événement indépendante du GPS.** Cette règle fonctionne indépendamment des coordonnées GPS. Si la plate-forme reçoit un événement de sabotage d'un traceur sans données GPS valides, l'événement est toujours considéré comme valide et affiché, qu'il se soit produit à l'intérieur ou à l'extérieur d'une géofence. Dans ce cas, les paramètres des boutons radio Intérieur/Extérieur des géofences sont ignorés afin de garantir que des événements potentiellement critiques ne soient pas manqués.