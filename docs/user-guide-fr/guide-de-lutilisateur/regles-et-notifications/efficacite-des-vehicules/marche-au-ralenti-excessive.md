# Marche au ralenti excessive

## Vue d'ensemble

La marche au ralenti excessive est un événement important à surveiller dans la gestion de flotte, car elle a un impact direct sur la consommation de carburant, l'usure des véhicules et l'efficacité opérationnelle globale. Navixy propose deux méthodes pour détecter la marche au ralenti excessive : celle liée au matériel et celle liée à la plateforme. Chaque méthode a ses propres avantages et est adaptée aux différents types de besoins des flottes.

**La règle relative à la plate-forme** est gérée par la plateforme et utilise des paramètres définis par l'utilisateur, tels que la durée de la marche au ralenti et la détection du stationnement. Cette règle est idéale pour ceux qui ont besoin d'une solution flexible et personnalisable qui fonctionne avec n'importe quel traceur qui rapporte des données de base comme l'état de l'allumage et la localisation GPS.

**Règle relative au matériel,** quant à lui, s'appuie sur la capacité intégrée du traceur GPS à détecter les événements de marche au ralenti. Le matériel génère et transmet l'événement de marche au ralenti directement à la plateforme. Cette méthode est avantageuse pour les traceurs dotés de fonctions avancées de détection de la marche au ralenti, car elle offre potentiellement une plus grande précision et des fonctionnalités supplémentaires.

## Paramètres des règles

### Plateforme

* **Durée de la marche au ralenti :** Définir la durée après laquelle la marche au ralenti sera considérée comme excessive. La règle s'applique lorsqu'un véhicule est garé (selon les paramètres de détection de stationnement) et que le contact est mis. Si le véhicule reste dans cet état au-delà de la durée spécifiée, une notification est déclenchée.

Pour les réglages courants, veuillez vous référer à [Règles et notifications](../).

### Matériel informatique

* **Paramètres spécifiques à l'appareil :** Cette règle repose sur la configuration du matériel pour la détection de la marche au ralenti. Vous devez vous référer à la documentation de votre appareil pour configurer la détection de la marche au ralenti sur le traceur. La plateforme recevra et affichera alors les événements liés à la marche au ralenti en fonction de la sortie du dispositif.

Pour les réglages courants, veuillez vous référer à [Règles et notifications](../).

## Détails du fonctionnement du système

* **Détection de la marche au ralenti liée à la plate-forme :** La plate-forme surveille en permanence l'état de l'allumage et du stationnement du véhicule. Lorsque le véhicule est garé avec le contact mis, la plateforme commence à compter la durée de la marche au ralenti. Si la durée de marche au ralenti dépasse le seuil défini par l'utilisateur, le système envoie une alerte. Cette méthode fonctionne avec une large gamme de traceurs et offre une grande souplesse dans la définition de seuils de marche au ralenti personnalisés.
* **Détection de la marche au ralenti liée au matériel :** Le tracker lui-même surveille la marche au ralenti et envoie un événement à la plateforme lorsque la marche au ralenti dépasse le seuil prédéfini dans l'appareil. La plateforme transmet simplement cet événement à l'utilisateur. Cette méthode peut offrir une plus grande précision et des fonctions avancées en fonction des capacités du traceur.
* **Notifications :** Quelle que soit la méthode de détection, vous recevrez des notifications par l'intermédiaire de l'interface utilisateur, d'un courrier électronique ou d'un SMS. Ces notifications aident les gestionnaires de flotte à prendre des mesures immédiates pour réduire la marche au ralenti inutile, ce qui permet d'économiser du carburant et de réduire l'usure des véhicules.
* **Rapports :** Vous pouvez générer des rapports sur la marche au ralenti excessive afin d'analyser les tendances et de prendre des décisions fondées sur des données pour améliorer l'efficacité de la flotte. Ces rapports peuvent être particulièrement utiles pour identifier la marche au ralenti habituelle ou pour évaluer l'impact de la marche au ralenti sur les coûts de carburant et l'entretien des véhicules.
