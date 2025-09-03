# Déviation de l'itinéraire

## Vue d'ensemble

La règle de déviation d'itinéraire permet de surveiller les déviations par rapport à un itinéraire prédéfini. Cette règle garantit que les véhicules ou les objets respectent les itinéraires prévus, ce qui améliore l'efficacité et la sécurité en identifiant et en corrigeant rapidement tout écart. Les utilisateurs reçoivent des notifications chaque fois qu'un véhicule ou un objet s'écarte de l'itinéraire spécifié, ce qui permet de maintenir la conformité et d'optimiser les opérations.

## Paramètres des règles

#### Tracer des géofences autour des chemins

Pour utiliser la règle de déviation d'itinéraire, vous devez d'abord créer une ou plusieurs géofences d'itinéraire dans la plate-forme. Suivez les étapes suivantes pour configurer la règle :

1. **Créer des géofences d'itinéraires**: Avant de configurer la règle, assurez-vous que vous avez créé des géofences d'itinéraire catégorisées comme "itinéraire".
2. **Sélectionner les géofences**: Choisissez les géofences d'itinéraire dont vous souhaitez surveiller les écarts. Seules les géofences classées comme "route" peuvent être utilisées à cette fin.

Pour les réglages courants, veuillez vous référer à [Règles et notifications](../../../guide-de-litilizateur/regles-et-notifications.md).

## Détails du fonctionnement du système

* L'alerte "Écart par rapport à l'itinéraire" est assortie d'un délai de réinitialisation de 10 secondes, ce qui signifie que l'événement d'alerte ne se produira pas plus d'une fois toutes les 10 secondes. Si un événement se produit pendant que la règle attend la réinitialisation, la plate-forme ne tiendra pas compte de l'événement, y compris dans les rapports.
* Cette règle est traitée dans le nuage et n'est pas liée à un matériel spécifique, ce qui permet de l'appliquer à plusieurs suiveurs simultanément. Cette flexibilité vous permet de sélectionner plusieurs suiveurs au sein d'une même règle.
