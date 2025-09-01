# Détection des chutes

## Vue d'ensemble

La règle sur la "détection des chutes" vise à garantir la sécurité et le bien-être des personnes en détectant et en avertissant les utilisateurs des risques de chutes ou d'accidents.

Cette règle utilise des capteurs et des algorithmes avancés pour surveiller les mouvements et l'orientation des appareils GPS personnels. Si le système détecte un changement soudain et important de position ou d'accélération, il l'identifie comme une chute potentielle et déclenche une notification.

Cette fonctionnalité est particulièrement précieuse pour la surveillance des personnes âgées, des travailleurs isolés ou d'autres personnes vulnérables aux chutes. En fournissant des alertes en temps réel, le système permet une réponse et une assistance immédiates, améliorant ainsi la sécurité générale et offrant une tranquillité d'esprit aux soignants et aux proches.

## Paramètres des règles

La fonctionnalité de cette règle dépend des capacités et de la configuration de l'appareil, de sorte qu'aucune configuration spécifique n'est requise.

Pour les réglages courants, veuillez vous référer à [Règles et notifications](../../regles-et-notifications.md).

## Détails du fonctionnement du système

- **Remise à zéro de la minuterie :** L'alerte "Détection de chute" est assortie d'un délai de réinitialisation de 30 secondes, ce qui signifie que l'alerte ne se déclenchera pas plus d'une fois toutes les 30 secondes. Si un événement se produit pendant la période de réinitialisation de la règle, la plate-forme supprime l'alerte, ce qui garantit que les notifications et les rapports restent clairs et gérables.
- **Plusieurs appareils :** Cette règle peut être appliquée à plusieurs traceurs GPS personnels, à condition qu'ils prennent en charge les événements de "détection de chute" et que cette fonction soit intégrée à la plateforme. Cela permet aux utilisateurs de surveiller les événements de détection de chute sur plusieurs appareils, assurant ainsi une couverture complète.
- **Traitement des événements indépendant du GPS :** La plate-forme traite et affiche les événements de détection de chute même si le paquet de données ne contient pas de coordonnées GPS valides. Ces événements sont enregistrés, qu'ils se produisent à l'intérieur ou à l'extérieur d'une géofence désignée. Les paramètres de géofence intérieur/extérieur sont contournés dans ce cas, ce qui garantit qu'aucun événement critique n'est manqué.