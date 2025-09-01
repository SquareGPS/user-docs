# L'appareil a perdu la connexion

## Vue d'ensemble

La règle "Perte de connexion de l'appareil" est conçue pour surveiller et notifier les utilisateurs lorsqu'un appareil GPS perd sa connexion avec la plate-forme. Cette perte de connexion peut être due à plusieurs raisons, telles que des problèmes matériels (décharge de la batterie, déconnexion de l'alimentation, défaillance du matériel, problèmes de câblage) ou des problèmes de communication (problèmes de réseau GSM, mauvaise couverture, fonds insuffisants ou pannes du fournisseur).

Cette règle permet aux utilisateurs de rester informés de l'état de fonctionnement de leurs dispositifs de localisation et de réagir rapidement aux problèmes potentiels, tels que les dysfonctionnements de l'équipement, le brouillage GSM ou le vol de véhicules. Elle permet également de collecter des données précieuses pour optimiser les opérations, par exemple en identifiant les zones mal couvertes ou en détectant les défaillances de l'équipement ou du fournisseur de services.

> [!INFO]
> Pour la surveillance en temps réel de l'état de l'alimentation de l'appareil, il est recommandé d'utiliser la fonction ["Fonction d'autodéclaration "interrupteur de l'appareil ON/OFF](/wiki/pages/createpage.action?spaceKey=USERDOCSOLD&title=Device%20switched%20ON%20%2F%20OFF)si elle est prise en charge par votre appareil GPS.

## Paramètres des règles

#### Temps hors ligne plus de

Le paramètre "Temps de déconnexion supérieur à" permet aux utilisateurs de définir un minuteur personnalisé qui commence à décompter après que le traceur est passé dans un état rouge (indiquant une perte de connexion). La période totale de déconnexion est calculée comme suit :

- **Délai d'attente par défaut (10 minutes)**: Il s'agit de la période standard après laquelle un traceur est considéré comme ayant perdu la connexion si aucune donnée n'est reçue de l'appareil.
- **Votre délai d'attente hors ligne personnalisé**: Le temps supplémentaire spécifié par l'utilisateur dans le champ "Temps hors ligne supérieur à".

Par exemple, si un appareil perd la connexion à 10h10, après le délai par défaut de 10 minutes, il sera marqué d'un état rouge à 10h20. Si l'utilisateur fixe le délai de déconnexion personnalisé à 7 minutes, la notification sera déclenchée à 10h27.

Pour le paramétrage des règles communes, veuillez vous référer à [Règles et notifications](../../regles-et-notifications.md).

## Détails du fonctionnement du système

- L'alerte "Perte de connexion de l'appareil" est assortie d'un délai de réinitialisation de 10 secondes, ce qui signifie que l'alerte ne se déclenchera pas plus d'une fois toutes les 10 secondes. Si un événement se produit pendant que la règle attend la réinitialisation, il sera omis par la plateforme, y compris dans les rapports.
- Cette règle est traitée dans le nuage et n'est pas liée à un matériel spécifique, ce qui la rend applicable à plusieurs suiveurs simultanément. Cette flexibilité vous permet de gérer plusieurs trackers dans le cadre d'une seule règle.
- Les délais d'attente au niveau du transport varient selon les modèles d'appareils. Si vous incluez plusieurs modèles de traceurs dans la même règle, les périodes de notification peuvent différer en fonction des paramètres de délai d'attente spécifiques de l'appareil. Cette variation est due au fait que la notification est déclenchée par une combinaison du délai d'attente par défaut du traceur et du délai d'attente hors ligne personnalisé spécifié dans la configuration de la règle.

En utilisant cette règle, les utilisateurs peuvent s'assurer qu'ils sont rapidement informés de toute perturbation de la connectivité des traceurs, ce qui leur permet de prendre des mesures rapides pour résoudre les problèmes potentiels.