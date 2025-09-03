# Batterie faible (Batterie de secours faible)

## Vue d'ensemble

Un appareil GPS émet une alerte de batterie faible lorsque le niveau de charge de sa batterie interne tombe en dessous d'un seuil prédéterminé. Cette alerte est déclenchée pour avertir les utilisateurs que la puissance de l'appareil est faible et que la batterie doit être rechargée ou remplacée rapidement.

Dans le cas des traceurs portables, cette alerte signale que la source d'énergie principale est en train de s'épuiser, tandis que pour les traceurs montés sur véhicule, elle peut indiquer que la batterie de secours est faible, ce qui risque de compromettre la capacité de l'appareil à poursuivre le suivi en cas de perte de l'alimentation principale.

<details>

<summary>Rôle des batteries internes dans les appareils GPS</summary>

La batterie interne d'un appareil GPS est une source d'énergie intégrée qui joue un rôle crucial dans le fonctionnement de l'appareil. En fonction de l'utilisation du traceur GPS, cette batterie interne peut jouer différents rôles.

* **Dans les traceurs GPS portables,** la batterie interne est généralement la principale source d'énergie. Ces batteries sont essentielles pour suivre les biens, les personnes ou les véhicules dans des scénarios où l'alimentation externe n'est pas disponible.
* **Pour les traceurs GPS montés sur des véhicules,** la batterie interne sert généralement de source d'alimentation de secours. Cette batterie de secours intervient lorsque l'alimentation principale du véhicule est interrompue, que ce soit en raison d'une déconnexion, d'une manipulation ou d'une défaillance de la batterie du véhicule. La batterie de secours garantit la continuité du suivi et de la transmission des données, offrant ainsi un niveau supplémentaire de sécurité et de fiabilité, en particulier dans les applications critiques de gestion de flotte ou de lutte contre le vol.

</details>

## Deux règles de surveillance de la batterie

Dans Navixy, il existe deux règles distinctes conçues pour surveiller l'état de la batterie de vos appareils GPS : la règle "Batterie faible" et la règle "Batterie de secours faible".

* **La règle de la "pile faible** s'applique à la source d'énergie principale de l'appareil, généralement utilisée dans les traceurs portables ou les appareils qui dépendent uniquement de batteries internes.
* **Règle "Batterie de secours faible** surveille spécifiquement le niveau de charge des batteries secondaires ou de secours, que l'on trouve généralement dans les suiveurs montés sur des véhicules.

Il s'agit de règles basées sur le matériel, ce qui signifie que l'appareil lui-même ou sa configuration détermine le seuil de déclenchement de l'alerte de batterie faible. Lorsque la charge de la batterie tombe en dessous de ce seuil, l'appareil le signale et le système envoie une notification, ce qui permet aux utilisateurs de prendre des mesures proactives pour recharger l'appareil et éviter les temps d'arrêt.

## Paramètres des règles

Cette règle dépend entièrement des capacités et de la configuration matérielle de l'appareil. Il n'y a pas de paramètres spécifiques à configurer dans la règle elle-même.

Pour les réglages courants, veuillez vous référer à [Règles et notifications](../).

## Spécificités de la plate-forme

Les alertes "Batterie faible" et "Batterie de secours faible" présentent plusieurs similitudes au niveau du fonctionnement, mais il existe une différence au niveau des délais de réinitialisation.

* **Remise à zéro des minuteries**: L'alerte "Batterie de secours faible" a un délai de réinitialisation d'une minute, ce qui signifie que l'alerte ne se déclenchera pas plus souvent qu'une fois par minute. En revanche, l'alerte "Batterie faible" a un délai de réinitialisation plus long de 30 minutes, ce qui signifie qu'elle ne se déclenchera pas plus d'une fois toutes les 30 minutes. Si un événement se produit pendant la période de réinitialisation de l'une ou l'autre règle, il sera omis de la plate-forme, y compris des rapports.
* **Sélection du traceur**: Les deux règles permettent aux utilisateurs de surveiller plusieurs traceurs, à condition que les traceurs prennent en charge les événements respectifs et que la fonction soit intégrée à la plateforme. Cette capacité permet de contrôler efficacement les niveaux de batterie de plusieurs véhicules ou appareils.
* **Inscription à l'événement**: Pour les deux règles, la plateforme enregistrera et affichera l'événement même s'il est reçu dans un paquet sans coordonnées valides. Les utilisateurs sont ainsi informés de l'événement quel que soit son emplacement, ce qui permet de maintenir une surveillance cohérente de leurs actifs.
