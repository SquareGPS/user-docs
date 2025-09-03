# Comptoir des passagers (Galileosky)

[Dispositifs Galileosky](https://www.navixy.com/devices/galileosky/)Lorsqu'ils sont intégrés aux capteurs de flux de passagers PP-01, ils constituent une solution robuste pour le comptage du nombre de passagers entrant et sortant des véhicules de transport public. Cette intégration s'appuie sur la technologie Easy Logic de Galileosky, permettant une collecte et une analyse avancées des données, qui peuvent être contrôlées par le biais de la plateforme Navixy.

#### Exemple de cas d'utilisation

Imaginez un opérateur de bus urbain qui a besoin de suivre le nombre de passagers pour optimiser les itinéraires et améliorer l'efficacité du service. En intégrant les appareils Galileosky aux capteurs PP-01 et en utilisant la plateforme Navixy, l'opérateur peut suivre avec précision le flux de passagers, analyser les tendances et prendre des décisions éclairées sur l'ajustement des itinéraires et l'amélioration des services.

## Principales caractéristiques et avantages

* **Comptage des passagers :** Le capteur PP-01 connecté au dispositif Galileosky permet un comptage précis des passagers entrant et sortant du véhicule.
* **Enregistrement des données sur la base d'événements :** Les données peuvent être enregistrées en fonction d'événements spécifiques tels que l'ouverture ou la fermeture des portes, ce qui garantit que les données relatives aux passagers ne sont enregistrées qu'aux moments opportuns.
* **Enregistrement des données cumulées :** Le système peut également être configuré pour enregistrer les données cumulées des passagers, ce qui permet d'obtenir le total des passagers tout au long du voyage.

## Les étapes de l'intégration

1. **Connecter le capteur PP-01 :**

* Le capteur PP-01 se connecte à l'appareil Galileosky via l'interface RS485. Veillez à ce que la connexion soit correcte en suivant les instructions de câblage fournies.
* Configurez l'interface RS485 avec les paramètres suivants :
  * Vitesse : 19200 bits/s
  * Bits de données : 8
  * Bit d'arrêt : 1

2. **Configurer le capteur PP-01 :**

* Connectez le capteur PP-01 à un PC à l'aide d'un adaptateur RS485-USB.
* Utilisez l'utilitaire de configuration PP-01 pour configurer le capteur. Ajustez l'adresse du capteur selon vos besoins, en la choisissant dans la gamme de 1 à 8.
* Utilisez le Configurateur Galileosky pour charger le script Easy Logic approprié en fonction du mode choisi (enregistrement par événement ou cumulatif).
* Assurez-vous que le script est bien téléchargé et configuré sur l'appareil Galileosky.

3. **Intégration avec Navixy :**

* Dans la plateforme Navixy, naviguez vers la section "Devices and Settings" et allez à "Sensors and Buttons".
* Créez un nouveau capteur de mesure et sélectionnez l'entrée correspondant à l'étiquette de l'utilisateur à partir du dispositif Galileosky.
* Cartographier les données du capteur PP-01 sur la plate-forme Navixy, en assurant une correspondance correcte entre les données du capteur et l'interface Navixy.

## Suivi et rapports

* **Vue en temps réel.** Une fois intégrées, les données relatives aux passagers peuvent être contrôlées en temps réel à l'aide du widget "Sensor readings" (relevés des capteurs) dans l'interface utilisateur. [Widgets d'information sur les appareils](../../../../../../../wiki/pages/createpage.action).
* **Rapports.** Vous pouvez également générer des [Rapports](../../../../rapports/details-specifiques-du-rapport/rapport-sur-les-capteurs-de-mesure.md) qui comprennent des données sur le nombre de passagers, ce qui permet une analyse complète et une meilleure compréhension des flux de passagers.
