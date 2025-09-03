# Entrée ou sortie de la géofence

## Vue d'ensemble

Une géofence est une zone désignée sur une carte qui agit comme une frontière virtuelle. Cette règle permet de suivre l'entrée et la sortie des traceurs dans la zone de géofence spécifiée. Les utilisateurs recevront des notifications lorsque leurs objets franchiront les limites de la géofence. Par exemple, si un engin de chantier quitte la zone désignée, un employé de l'entreprise peut en être informé par l'intermédiaire de l'interface utilisateur, d'un courrier électronique ou d'un SMS, si cela est configuré dans la règle.

![image-20240805-231934.png](../../../guide-de-litilizateur/regles-et-notifications/surveillance-des-mouvements/attachments/image-20240805-231934.png)

Cette fonctionnalité permet d'obtenir des informations précieuses et de contrôler les mouvements d'objets, en garantissant le respect de limites prédéfinies. Elle renforce la sécurité en alertant les utilisateurs de tout mouvement non autorisé ou de tout vol potentiel en dehors de la zone de géofence spécifiée. En outre, elle permet une gestion efficace des actifs en permettant aux utilisateurs de suivre et d'optimiser l'utilisation de leur équipement dans les zones désignées.

## Paramètres des règles

#### Les géofences

Spécifiez les géofences qui déclencheront des notifications lorsqu'elles seront franchies. Vous pouvez répertorier plusieurs géofences dans une même règle.

Pour les réglages courants, veuillez vous référer à [Règles et notifications](../../../guide-de-litilizateur/regles-et-notifications.md).

## Détails du fonctionnement du système

* L'alerte "Entrée ou sortie de géofence" est assortie d'un délai de réinitialisation de 60 secondes, ce qui signifie que l'alerte ne se déclenchera pas plus d'une fois par minute. Si un événement se produit pendant que la règle attend la réinitialisation, la plate-forme ne tiendra pas compte de l'événement, y compris dans les rapports.
* Cette règle est traitée dans le nuage et n'est pas liée à un matériel spécifique, ce qui permet de l'appliquer à plusieurs suiveurs simultanément. Cette flexibilité vous permet de gérer plusieurs suiveurs dans le cadre d'une seule règle.
* Veuillez noter que le système peut générer une alerte d'entrée/sortie même en cas de dérive GPS. Bien que les coordonnées GPS non valides soient filtrées, de petites dérives GPS peuvent encore apparaître dans la trace. Diverses méthodes sont disponibles pour empêcher les dérives GPS, selon les fonctionnalités du modèle de traceur. Pour plus de détails sur la prévention des dérives GPS, reportez-vous au manuel de l'appareil.
