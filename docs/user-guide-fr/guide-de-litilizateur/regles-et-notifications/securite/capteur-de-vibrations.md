# Capteur de vibrations

## Vue d'ensemble

Un capteur de vibrations, également appelé capteur de secousses, s'appuie sur l'accéléromètre intégré d'un appareil pour détecter des vibrations ou des mouvements continus, généralement lorsqu'un véhicule est garé. Cette règle est conçue pour déclencher des alertes ou des notifications lorsque des vibrations inhabituelles ou continues sont détectées, signalant ainsi une activité non autorisée ou des perturbations potentielles. Les paramètres de sensibilité du capteur peuvent être ajustés en fonction des besoins de l'utilisateur, selon la configuration de l'appareil.

Cette règle est particulièrement utile dans diverses applications, telles que la protection des véhicules stationnés par les entreprises de construction. Des vibrations continues peuvent indiquer un accès non autorisé ou une tentative de vol. Les alertes générées par cette règle permettent aux entreprises de réagir rapidement, réduisant ainsi le risque de vol de véhicules, minimisant les dommages potentiels et limitant les pertes.

Il est important de noter que l'efficacité de cette règle dépend du matériel et de la configuration du traceur GPS. Tous les scénarios liés à la détection des vibrations doivent être configurés dans l'environnement du traceur. Par exemple, certains traceurs offrent des options de configuration, telles que l'état d'allumage ou le délai d'attente pour les mouvements.

## Paramètres des règles

Cette règle dépend entièrement des capacités et de la configuration matérielle de l'appareil. Il n'y a pas de paramètres spécifiques à configurer dans la règle elle-même.

Pour les réglages courants, veuillez vous référer à [Règles et notifications](../../regles-et-notifications.md).

## Détails du fonctionnement du système

- **Remise à zéro de la minuterie :** L'alerte "Capteur de vibrations" est assortie d'un délai de réinitialisation d'une minute, ce qui signifie que l'alerte ne se déclenchera pas plus d'une fois par minute. Si un événement se produit pendant que la règle attend la réinitialisation, la plate-forme ne tient pas compte de l'événement, y compris dans les rapports.
- **Plusieurs appareils :** Les utilisateurs peuvent sélectionner plusieurs suiveurs pour recevoir des notifications de cette règle, à condition que les suiveurs prennent en charge les événements liés aux capteurs de vibrations et que la fonction soit intégrée à la plateforme.
- **Alerte d'événement indépendante du GPS :** Si la plate-forme reçoit un événement vibratoire d'un traceur sans coordonnées GPS valides, l'événement est toujours considéré comme valide et affiché, qu'il se soit produit à l'intérieur ou à l'extérieur d'une géofence. La logique des boutons radio Intérieur/Extérieur est ignorée dans ce cas, car il est préférable d'afficher un événement potentiellement critique que de l'omettre.