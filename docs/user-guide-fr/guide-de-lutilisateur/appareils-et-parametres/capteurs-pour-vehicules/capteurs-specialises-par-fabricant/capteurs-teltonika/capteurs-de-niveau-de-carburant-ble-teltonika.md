# Capteurs de niveau de carburant BLE (Teltonika)

Nombreux [Appareils GPS Teltonika](https://www.navixy.com/devices/teltonika/) prennent en charge les capteurs de carburant sans fil qui se connectent via Bluetooth. Les avantages de l'utilisation de ces capteurs de carburant Bluetooth sont considérables :

* **Pas de fils**: Le capteur et le traceur ne nécessitent pas de connexion physique, ce qui simplifie l'installation.
* **Indépendance par rapport aux sources d'énergie externes**: Ces détecteurs sont équipés d'une batterie intégrée qui peut durer plusieurs années sans qu'il soit nécessaire de la recharger.
* **Données complémentaires**: Outre les niveaux de carburant, le capteur transmet également des données sur la température, l'humidité et le niveau de charge de la batterie.

## Préparation de l'appareil GPS

Pour préparer votre appareil GPS Teltonika à l'intégration d'un capteur de carburant Bluetooth, suivez les étapes suivantes.

\[![Bluetooth fuel sensors](https://www.navixy.com/wp-content/uploads/2019/09/teltonika.configurator_2019-09-28_13-56-33-600x365.png)

]\(https://www.navixy.com/wp-content/uploads/2019/09/teltonika.configurator\_2019-09-28\_13-56-33.png)

1. **Télécharger le configurateur Teltonika**: Obtenez l'application sur le site officiel de Teltonika.
2. **Mise à jour du micrologiciel**: Assurez-vous que votre appareil fonctionne avec la dernière version du micrologiciel.
3. **Lancer le configurateur**:

* Aller à la page **Système** tabulation.
* Modifier le protocole de transfert de données en **Codec 8 étendu**.

4. **Connecter le capteur de carburant**:

* Naviguez jusqu'à la page **Bluetooth** dans le configurateur.
* Connecter le capteur de carburant au traceur.

5. **Activer les paramètres nécessaires**:

* Aller à la page **E/S** tabulation.
* Assurez-vous que le paramètre correspondant au capteur de carburant est activé.

> \[!INFO] **Codec 8 étendu** est un protocole de communication propre à Teltonika qui prend en charge jusqu'à 65 535 paramètres de données (ID AVL), ce qui permet une transmission de données plus détaillée par rapport au Codec 8 standard, qui n'en prend en charge que 255.

## Installation du capteur sur la plate-forme Navixy

Une fois que le tracker est connecté et qu'il transmet des données sur le carburant, suivez les étapes suivantes pour configurer les capteurs correspondants sur la plateforme Navixy.

\[![Bluetooth fuel sensors](https://www.navixy.com/wp-content/uploads/2019/09/chrome_2019-09-28_13-59-40-600x296.png)

]\(https://www.navixy.com/wp-content/uploads/2019/09/chrome\_2019-09-28\_13-59-40.png)

1. **Créer un nouveau capteur de mesure**:

* Naviguer vers Appareils et réglages → Capteurs et boutons.
* Cliquez sur Créer un nouveau [capteur de mesure](broken-reference).

2. **Configurer le capteur**:

* Sélectionnez l'entrée intitulée "BLE : Niveau LLS".
* Régler le type de capteur et les unités. Si nécessaire, remplissez le tableau d'étalonnage et ajustez les autres paramètres.

3. **Répéter l'opération pour les autres capteurs**:

* Si vous avez plusieurs capteurs de carburant, répétez le processus de configuration pour chaque capteur, en sélectionnant l'entrée appropriée pour chacun d'entre eux.

4. **Contrôler et rendre compte**:

* Une fois configuré, vous pouvez surveiller le niveau de carburant dans le widget prévu à cet effet sur la plateforme.
* Vous pouvez également générer des rapports détaillés sur la consommation de carburant.

Cette configuration vous permet d'utiliser pleinement les capacités des capteurs de carburant Bluetooth Teltonika, en fournissant des données précises et en temps réel sur les niveaux de carburant, la température, et plus encore.
