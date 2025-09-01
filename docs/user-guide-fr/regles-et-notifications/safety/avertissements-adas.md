# Avertissements ADAS

## Vue d'ensemble

Les systèmes avancés d'aide à la conduite (ADAS) sont conçus pour améliorer la sécurité du conducteur en lui fournissant des alertes et une surveillance en temps réel pendant qu'il est sur la route. Les systèmes ADAS utilisent des algorithmes avancés et des technologies de vision artificielle, alimentés par l'IA, pour analyser les données des caméras vidéo et des capteurs lidar. Cela permet au système de détecter avec précision les dangers potentiels et les comportements de conduite dangereux, garantissant une approche proactive de la sécurité routière en accord avec les dernières avancées en matière de télématique automobile.

La plate-forme Navixy enregistre les événements suivants et peut en alerter les utilisateurs :

| **Événement** | **Description** |
| --- | --- |
| **Alerte de franchissement de ligne (LDW)** | Alerte le conducteur lorsque le véhicule dérive involontairement de sa voie, ce qui permet d'éviter les collisions potentielles dues à l'inattention du conducteur. |
| **Avertisseur de collision avant (FCW)** | Avertit le conducteur de l'imminence d'une collision avec un véhicule ou un objet situé devant lui, ce qui lui permet de freiner à temps ou de prendre des mesures d'évitement pour éviter l'accident. |
| **Avertissement de surveillance de la voie de circulation (HMW)** | Surveille la distance par rapport au véhicule qui précède et alerte le conducteur si la distance de suivi devient dangereuse, ce qui favorise des habitudes de conduite plus sûres. |
| **Pedestrian in Danger Zone (PDZ)** | Détecte si un piéton se trouve à proximité du véhicule, en particulier dans les angles morts, afin d'éviter les accidents et d'améliorer la sécurité routière. |
| **Avertissement de collision avec un piéton (PCW)** | Il émet un avertissement lorsqu'il détecte un risque de collision avec un piéton, ce qui donne au conducteur le temps de réagir et d'éviter l'incident. |
| **Reconnaissance des panneaux de signalisation (TSR)** | Identifie et signale au conducteur les panneaux de signalisation importants, tels que les limitations de vitesse ou les panneaux d'arrêt, afin de garantir le respect du code de la route. |

Le suivi de ces événements permet d'améliorer la sensibilisation des conducteurs, de réduire le risque d'accident et de garantir le respect du code de la route. Cela permet d'améliorer les performances des conducteurs, d'atténuer les responsabilités et d'éviter des amendes ou des réparations coûteuses.

## Paramètres des règles

### Sélection d'un événement

Les événements ADAS étant traités au niveau de l'appareil télématique Video et non dans le nuage, aucun réglage supplémentaire n'est nécessaire. Il vous suffit de sélectionner les événements que vous souhaitez surveiller pour assurer un suivi complet du comportement du conducteur.

Pour les réglages courants, veuillez vous référer à [Règles et notifications](../../regles-et-notifications.md).

## Détails du fonctionnement du système

- **Pas de minuterie de remise à zéro :** L'alerte "ADAS" n'est pas assortie d'un délai de remise à zéro, ce qui signifie qu'une alerte sera déclenchée chaque fois qu'un événement ADAS sera détecté.
- **Plusieurs appareils :** Les utilisateurs peuvent sélectionner plusieurs suiveurs pour recevoir des notifications ADAS. La seule condition est que les traceurs choisis prennent en charge les événements ADAS et que cette fonction soit intégrée dans la plateforme. Cela permet un suivi efficace des comportements de conduite dans une flotte de véhicules.
- **Alerte d'événement indépendant du GPS :** La plateforme reconnaîtra et affichera les événements ADAS même si le paquet de données provenant du traceur ne contient pas de coordonnées GPS valides. Dans ce cas, les paramètres de géofence intérieure/extérieure sont ignorés, ce qui permet de ne pas manquer des événements critiques.