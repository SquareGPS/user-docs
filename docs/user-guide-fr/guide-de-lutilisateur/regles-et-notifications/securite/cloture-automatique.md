# Clôture automatique

## Vue d'ensemble

La fonction "Auto geofencing", disponible sur certains dispositifs de suivi GPS, est une solution robuste conçue pour renforcer la sécurité des véhicules en empêchant le remorquage ou le vol non autorisé.

Cette fonction établit automatiquement un périmètre autour de l'emplacement actuel du véhicule lorsque le contact est coupé. Si le véhicule sort de ce périmètre prédéfini sans que le contact soit mis, le système déclenche immédiatement une alerte, offrant ainsi une protection supplémentaire. L'utilisation de la fonction Auto geofencing nécessite un traceur GPS qui prend en charge cette fonctionnalité.

## Paramètres des règles

Cette règle dépend entièrement des capacités et de la configuration matérielle de l'appareil. Il n'y a pas de paramètres spécifiques à configurer dans la règle elle-même.

Pour les réglages courants, veuillez vous référer à [Règles et notifications](../../../guide-de-litilizateur/regles-et-notifications.md).

## Détails du fonctionnement du système

* **Remise à zéro de la minuterie**: L'alerte "Auto Geofencing" a un délai de réinitialisation d'une minute, ce qui signifie qu'elle ne se déclenchera pas plus d'une fois par minute. Si un événement se produit pendant la période de réinitialisation, il sera omis des rapports.
* **Dispositifs multiples**: Vous pouvez sélectionner plusieurs trackers pour cette règle, à condition qu'ils prennent en charge les événements de géofencing automatique et que la fonction soit intégrée à la plateforme. Cette flexibilité vous permet de surveiller plusieurs véhicules ou actifs simultanément.
* **Alerte d'événement indépendante du GPS**: Si la plateforme reçoit un événement de géofencing automatique d'un traceur dont les coordonnées GPS ne sont pas valides, l'événement sera tout de même considéré comme valide et affiché. Cela permet de ne pas manquer les événements critiques, qu'ils se produisent à l'intérieur ou à l'extérieur des géofences définies.
