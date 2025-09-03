# Capteur de bracelet (ou de cheville)

La règle du "capteur bracelet" (ou "capteur cheville") est spécifiquement conçue pour les applications de surveillance juridique impliquant des traceurs GPS spécialisés. Il s'agit d'un outil essentiel pour la sécurité dans des contextes tels que l'assignation à résidence ou la libération conditionnelle.

Cette règle est conçue pour avertir immédiatement le personnel de sécurité si un dispositif GPS est retiré sans autorisation. Dans ces situations, la règle déclenche une alerte instantanée auprès des autorités compétentes, ce qui permet d'agir rapidement pour empêcher tout mouvement non autorisé ou toute violation des conditions légales.

## Paramètres des règles

Cette règle dépend entièrement des capacités et de la configuration matérielle de l'appareil. Il n'y a pas de paramètres spécifiques à configurer dans la règle elle-même.

Pour les réglages courants, veuillez vous référer à [Règles et notifications](../).

## Détails du fonctionnement du système

* **Remise à zéro de la minuterie.** L'alerte "Capteur de bracelet" est assortie d'un délai de réinitialisation de 3 minutes, ce qui signifie que l'événement d'alerte ne se produira pas plus d'une fois toutes les 3 minutes. Si ce type d'événement se produit alors que la règle attend la réinitialisation, cet événement sera omis par la plateforme, y compris dans les rapports.
* **Plusieurs appareils :** Avec cette règle, vous avez la possibilité de sélectionner plusieurs suiveurs pour recevoir des notifications. La seule condition est que les suiveurs sélectionnés prennent en charge les événements du capteur Bracelet et que cette fonction soit intégrée à la plateforme. Cela vous permet de surveiller simultanément plusieurs traceurs compatibles, en vous assurant de recevoir des notifications pour les événements pertinents dans différents véhicules ou appareils de manière efficace.
* **Alerte d'événement indépendante du GPS :** Lorsque la plate-forme détecte ce type d'événement matériel à partir de données de suivi dont les coordonnées ne sont pas valides, elle enregistre et affiche l'événement comme étant valide. Cela s'applique indépendamment du fait que l'événement ait eu lieu à l'intérieur ou à l'extérieur des géofences désignées. Dans ce cas, la plate-forme ne tient pas compte de la logique de géofence intérieur/extérieur pour s'assurer que l'événement est capturé et signalé.
