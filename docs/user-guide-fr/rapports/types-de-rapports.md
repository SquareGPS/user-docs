# Types de rapports

Navixy fournit une série complète de rapports qui vous permettent de contrôler divers aspects des opérations de votre flotte. Ces rapports sont organisés en catégories, ce qui facilite la recherche et la génération des données dont vous avez besoin. Vous trouverez ci-dessous un aperçu des catégories de rapports disponibles et des rapports spécifiques qu'elles contiennent.

## Rapports d'activité

Les rapports d'activité fournissent des informations détaillées sur les mouvements et les arrêts de vos véhicules, ce qui vous permet de suivre l'historique des trajets et d'identifier les schémas d'utilisation des véhicules.

- **Voyages**  
Ce rapport offre un historique détaillé des trajets, y compris la longueur, le temps de trajet, la durée des arrêts et la vitesse. Il fournit également un aperçu de la consommation de carburant pour les véhicules dépourvus de capteurs de carburant.
- **Arrêts**  
Le rapport Arrêts présente les détails des arrêts et des stationnements, y compris le lieu, la durée et le temps d'inactivité (temps passé avec le moteur allumé pendant le stationnement).
- **Déplacements et arrêts par équipe**  
Un rapport combiné qui vous permet de visualiser les données relatives aux déplacements et aux arrêts, segmentées par équipes, vous aidant ainsi à analyser l'utilisation des véhicules pendant des intervalles de temps spécifiques.

## Rapports sur les points de repère

Les rapports sur les points de repère vous aident à suivre les visites dans des zones géographiques prédéfinies, telles que les géofences et les points d'intérêt (POI).

- **Visites de la géofence**  
Permet de suivre le nombre de visites dans des zones géo-censurées au cours d'une période donnée, en fournissant des détails sur les entrées, les sorties et la durée des séjours.
- **Visites de POI**  
Semblable au rapport de géofence, ce rapport permet de suivre les visites de points d'intérêt, en détaillant la date et l'heure de chaque visite.

## Rapports sur la sécurité et la sûreté

Ces rapports se concentrent sur les événements liés à la sécurité et les alertes générées par le système, vous aidant ainsi à assurer la sécurité de vos véhicules et de vos conducteurs.

- **Sécurité des voitures**  
Fournit des détails sur les alarmes de voitures, les évacuations, les accidents et d'autres événements liés à la sécurité.
- **Bouton d'urgence (SOS)**  
Capture les événements déclenchés par le bouton SOS sur les appareils GPS équipés d'un bouton de panique.
- **Détection des chutes**  
Suivi des événements de chute détectés par des appareils équipés de capteurs de chute, couramment utilisés dans les trackers personnels.
- **Détachement du traceur**  
Signale les cas où un dispositif de repérage a été retiré de l'objet qui lui était assigné, souvent utilisé pour le repérage des cargaisons.
- **Rapport de sécurité global**  
Un rapport complet qui regroupe tous les événements liés à la sûreté et à la sécurité.

## Rapports sur l'utilisation des véhicules

Les rapports d'utilisation des transports vous permettent de contrôler l'utilisation de vos véhicules et de leurs ressources, y compris la consommation de carburant et l'utilisation du moteur.

- **Heures de fonctionnement du moteur**  
Affiche des informations détaillées sur les heures de fonctionnement du moteur, qu'il soit en marche ou au ralenti, ainsi que des diagrammes d'activité et des histogrammes. En savoir plus :
  - [Rapport sur les heures de fonctionnement du moteur](details-specifiques-du-rapport/rapport-sur-les-heures-de-fonctionnement-du-moteur.md)
- **Volume de carburant**  
Fournit des données sur la consommation de carburant, les remplissages et les vidanges, ainsi que les volumes de carburant initiaux et finaux. En savoir plus :
  - [Rapport sur la consommation de carburant](details-specifiques-du-rapport/rapport-sur-le-volume-de-carburant.md)
  - [Gestion du carburant dans Navixy](https://squaregps.atlassian.net/wiki/spaces/SC/pages/2380890113/Fuel+control+in+Navixy)
- **Débitmètre**  
Se concentre sur les données de consommation de carburant recueillies à partir de débitmètres, sans indiquer les niveaux de carburant à des moments précis.
- **Capteurs pour véhicules**  
Affiche les données reçues des capteurs du véhicule via CAN-bus ou OBDII, y compris le kilométrage, le régime, la vitesse et la température du liquide de refroidissement. En savoir plus :
  - [Rapport sur les relevés CAN / OBDII du véhicule](https://squaregps.atlassian.net/wiki/spaces/UDOCFR/pages/3027438928/Types+de+rapports)

## Rapports sur la qualité de la conduite

Ces rapports sont essentiels pour surveiller le comportement des conducteurs, notamment en ce qui concerne les excès de vitesse et d'autres actions potentiellement dangereuses.

- **Infraction à la vitesse**  
Détaille les cas où le véhicule a dépassé la limite de vitesse, y compris la date, le lieu et la vitesse réelle. Voir aussi :
  - [Conduite sévère dans les règles et les notifications](../regles-et-notifications/safety/conduite-difficile.md)
  - [L'éco-conduite dans la gestion du parc automobile](../gestion-du-parc-automobile/conduite-ecologique.md)

### Rapports sur l'état des appareils

Les rapports sur l'état des dispositifs fournissent des informations sur l'état opérationnel de vos dispositifs de suivi, vous aidant ainsi à assurer une surveillance ininterrompue.

- **Activation/désactivation de l'appareil**  
Trace les cas où le dispositif GPS a été activé ou désactivé manuellement. Voir aussi :
  - [Dispositif activé/désactivé dans Règles et notifications](../regles-et-notifications/puissance-de-lappareil/dispositif-activedesactive.md)
- **Perte de la connexion GSM**  
Signale les périodes pendant lesquelles le dispositif GPS a perdu sa connexion GSM, ce qui indique un manque de communication avec le serveur de surveillance. Voir aussi :
  - [Perte de connexion de l'appareil dans les règles et les notifications](../regles-et-notifications/connexion-des-appareils/lappareil-a-perdu-la-connexion.md)

## Rapports sur les dispositifs connectés

Ces rapports se concentrent sur les capteurs et les équipements connectés à vos dispositifs de suivi, fournissant des données opérationnelles détaillées.

- **Capteurs de mesure**  
Fournit un historique détaillé des relevés des capteurs, tels que la température, les niveaux de carburant et la tension.
- **Temps de fonctionnement de l'équipement**  
Permet de suivre l'activité et le temps d'inactivité des équipements connectés au dispositif de suivi via des entrées numériques. En savoir plus :
  - [Rapport sur les heures de travail de l'équipement](details-specifiques-du-rapport/rapport-sur-le-temps-de-travail-des-equipements.md)

## Rapports d'activité

Les rapports d'activité sont conçus pour vous aider à contrôler les tâches opérationnelles et les performances de votre personnel sur le terrain.

- **Rapport d'activité**  
Résume l'état des tâches assignées aux employés, ce qui vous aide à suivre leur progression et leur achèvement.
- **Valeurs du formulaire des tâches**  
Affiche les données des formulaires soumis par les employés lorsqu'ils accomplissent des tâches via l'application X-GPS Tracker.
- **Rapport sur les états de travail**  
Enregistre les modifications apportées aux statuts de travail, qu'elles soient le fait d'employés ou d'opérateurs.
- **Enregistrements**  
Liste tous les enregistrements effectués par les employés sur la carte à l'aide de l'application X-GPS Tracker.
- **Changement de poste du conducteur**  
Suivi des changements de conducteur, ce qui vous permet de savoir quel conducteur conduisait un véhicule à un moment donné.
- **Voyages par état**  
Un rapport de voyage spécialisé qui regroupe les données par région ou par pays.

## Autres rapports

Ces rapports couvrent une variété d'événements et d'activités supplémentaires, offrant ainsi un large aperçu des opérations de votre flotte.

- **Tous les événements**  
Un rapport complet qui regroupe tous les types d'événements pris en charge par la plateforme, regroupés par catégorie d'événements.
- **Entrée/sortie de la géofence**  
Il suit les événements d'entrée et de sortie des zones géo-censurées, fournissant des données détaillées sur les mouvements à l'intérieur et à l'extérieur de ces régions.
- **Rapport de localisation par SMS**  
Liste les demandes de localisation envoyées par SMS lorsque l'appareil GPS ne dispose pas d'une connexion Internet.
- **Rapport sur les points**  
Montre le déplacement de l'appareil dans le temps par points, y compris les coordonnées et les liens vers des cartes.