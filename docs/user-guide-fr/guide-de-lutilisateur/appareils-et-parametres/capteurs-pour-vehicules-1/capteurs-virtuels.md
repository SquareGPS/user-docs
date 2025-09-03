# Capteurs virtuels

# Capteurs virtuels

Les capteurs virtuels vous permettent de traiter plus efficacement les données télémétriques. En cartographiant la tension de la carte, ils peuvent vous aider à calculer les heures de fonctionnement du moteur en fonction de conditions et de valeurs définies. En outre, ils vous permettent de convertir plusieurs points de données provenant de différents capteurs connectés à un appareil en indicateurs plus faciles à comprendre tels que "chaud", "froid", "ouvert" et "fermé", quel que soit le fabricant ou le modèle de l'appareil. Cela ouvre de nouvelles possibilités de surveillance, de suivi et de prévision des performances de technologies complexes.

[![Virtual sensor interface](https://www.navixy.com/wp-content/uploads/2024/03/browser_clvf66ikbi.png)

](https://www.navixy.com/wp-content/uploads/2024/03/browser_clvf66ikbi.png)

Interface de capteur virtuel

## Comment créer un capteur virtuel

Les capteurs virtuels peuvent être créés via le portlet "Sensors and Buttons" situé dans l'onglet Devices and settings :

1. Entrez dans la section des appareils et des paramètres.
2. Sélectionnez un traceur GPS.
3. Cliquez sur "+".
4. Sélectionnez l'option "Capteur virtuel".

Chaque appareil peut avoir jusqu'à 100 capteurs virtuels.

[![Virtual sensor adding in sensors and buttons portlet](https://www.navixy.com/wp-content/uploads/2024/03/browser_73sv6rayqh.png)

](https://www.navixy.com/wp-content/uploads/2024/03/browser_73sv6rayqh.png)

Ajout d'un capteur virtuel dans le portlet des capteurs et des boutons

Les étapes suivantes dépendent du cas d'utilisation qui doit être résolu par le capteur virtuel. Vous trouverez ci-dessous des exemples et des instructions pour différentes méthodes de calcul.

## Méthodes de calcul

Les capteurs virtuels ont trois types de calcul différents :

- Valeur dans l'intervalle.
- Valeur de la source.
- Index des bits.

Toutes les valeurs des capteurs virtuels doivent correspondre à la forme sous laquelle elles sont reçues de l'appareil. Tous les états sont vos définitions de ces valeurs.

Nous décrivons ici le fonctionnement des différentes méthodes de calcul. Cliquez sur le nom de la méthode de calcul pour la développer.

#### [Valeur dans la fourchette](#1679329407451-09b70c96-6385)

Ce type de capteur virtuel aide nos clients à maintenir des paramètres importants tels que l'allumage virtuel, la température, l'humidité et le niveau de carburant dans une plage spécifiée.

Voici comment cela fonctionne :

- si la valeur du capteur se situe à l'intérieur des limites spécifiées, elle est de 1 pour la plate-forme. Et 1 est égal à votre valeur A.
- si la valeur du capteur est en dehors de ces cadres, la valeur du capteur virtuel est 0 pour la plate-forme. Et 0 est égal à votre valeur B.

### Exemple d'allumage virtuel

Si vous ne disposez pas d'une entrée d'allumage ou si votre appareil fonctionne déjà à pleine capacité, vous pouvez utiliser un outil d'allumage virtuel pour détecter l'état de l'allumage. La tension de bord de la voiture augmente considérablement lorsque le moteur est allumé, ce qui permet d'utiliser le seuil de tension comme indicateur du fait que le moteur tourne ou non. En règle générale, la tension de bord doit dépasser 13,2 V pour indiquer que le moteur fonctionne.

Pour créer ce capteur :

1. Commencez par lui donner un nom.
2. Réglez l'entrée sur la tension de la carte, ou tout autre capteur si nécessaire.
3. Activer l'option "Considérer comme état d'allumage" dans les paramètres.
4. Choisissez "Valeur dans l'intervalle" comme méthode de calcul.
5. Spécifiez une valeur minimale, par exemple 13,2 V. La valeur maximale n'est pas nécessaire puisque la tension de la carte peut varier lorsque l'allumage est activé.
6. Enfin, définissez la signification des états 0 et 1 - en général, il s'agit respectivement de On et Off.

[![Example configuration for virtual ignition](https://www.navixy.com/wp-content/uploads/2024/03/browser_7qx9prhhxc.png)

](https://www.navixy.com/wp-content/uploads/2024/03/browser_7qx9prhhxc.png)

Exemple de configuration pour l'allumage virtuel

Une fois que vous avez défini votre plage de seuil de tension, si la valeur embarquée entrante se situe dans cette plage, la plate-forme commutera l'état d'allumage sur "on". À l'inverse, si elle se situe en dehors de cette fourchette, elle passera à l'état "éteint". L'allumage virtuel créé à l'aide de cette méthode sera également pris en compte dans les rapports et les notifications basés sur son état ; par exemple, vous pouvez l'utiliser pour générer des rapports sur les heures de fonctionnement du moteur ou des alertes en cas de marche au ralenti excessive.

En outre, cet allumage sera utilisé pour la détection des déplacements et du stationnement en tenant compte de l'allumage.

### Exemple avec un capteur analogique

Cet exemple est similaire au précédent, mais au lieu de contrôler l'allumage du véhicule, il contrôle la température.

Supposons que vous disposiez d'un capteur analogique qui collecte des données de température - disons qu'il émet 1020 pour -10°C et 1900 = 0°C. Les données provenant des capteurs analogiques ne sont pas calibrées et doivent donc être spécifiées sous cette forme pour le capteur virtuel.

Nous pouvons définir notre fourchette : tout ce qui se situe entre 1020 et 1900 sera considéré comme "froid" (1) et tout ce qui est supérieur à 1900 sera considéré comme "chaud" (0).

[![Example configuration for reading temperature from analog sensor](https://www.navixy.com/wp-content/uploads/2024/03/browser_kgzvrsdzb1.png)

](https://www.navixy.com/wp-content/uploads/2024/03/browser_kgzvrsdzb1.png)

Exemple de configuration pour la lecture de la température à partir d'un capteur analogique

#### [Valeur de la source](#1679329407460-fa411058-510d)

Avec les capteurs virtuels, vous pouvez attribuer votre définition à n'importe quelle valeur reçue. Cette méthode fonctionne avec des ensembles prédéfinis de valeurs et de chaînes, ce qui permet de travailler facilement avec des valeurs statiques sans avoir à spécifier différentes plages. En outre, elle peut fonctionner avec toutes les données dont vous avez besoin. En outre, elle peut fonctionner avec toutes les données dont vous avez besoin :

- 0/1,
- vrai/faux,
- marche/arrêt,
- ouvrir/fermer,
- armé/désarmé,
- État 1/État 2/État 3,
- touche 1/clé 2/clé 3, etc.

Le mode fonctionne comme suit :

- lorsque la valeur 1 arrive, c'est la valeur A ;
- lorsque la valeur 2 arrive, c'est la valeur B ;
- et lorsque la valeur 3 arrive, c'est votre valeur C et ainsi de suite.

Illustrons ce type de fonctionnalité par des exemples concrets.

### Exemple avec les relevés CAN d'une voiture

Certains capteurs CAN peuvent fournir différentes valeurs numériques à une plate-forme. Par exemple, nous avons un camion équipé d'un capteur CAN d'état de la prise de force qui ne peut fournir que les valeurs suivantes :

- 0 - Désactivé
- 1 - Maintien
- 2 - Maintien à distance
- 3 - Veille
- 4 - Mise en veille à distance
- 5 - Ensemble
- 6 - Décélération
- 7 - Curriculum vitae
- 8 - Accélérer

Pour configurer un tel capteur :

1. Spécifiez son nom.
2. Choisissez l'entrée.
3. Considérer que l'allumage doit être coupé.
4. Sélectionnez "Valeur source" comme méthode de calcul.
5. Remplissez le tableau avec vos propres valeurs sur le côté gauche et les valeurs respectives des capteurs sur le côté droit. Ajoutez des lignes en cliquant sur le signe "+" et supprimez-les en utilisant le bouton "poubelle".

[![Configuration example for source value calculation method](https://www.navixy.com/wp-content/uploads/2024/03/browser_xlxdl1ak9e.png)

](https://www.navixy.com/wp-content/uploads/2024/03/browser_xlxdl1ak9e.png)

Exemple de configuration de la méthode de calcul de la valeur de la source

### Les clés matérielles pour les conducteurs, l'équipement et les remorques

Certains appareils peuvent être capables de lire les conducteurs et leurs iButtons, les clés RFID ou les équipements connectés à l'appareil via des capteurs Bluetooth. La plateforme peut détecter l'équipement ou le conducteur le plus proche de l'appareil, et le capteur virtuel est capable d'afficher ces noms.

La méthode d'identification la plus simple est celle des étiquettes : chaque unité connectée à un équipement lourd possède son propre capteur auquel est attachée une étiquette, reconnue par la plate-forme comme une clé matérielle. Lorsqu'elle est connectée à la machine, cette clé est envoyée à la plate-forme et le nom qui lui est associé peut être affiché de manière compréhensible - de la même manière que les valeurs de la prise de force ont été nommées.

[![Configuration example for source value calculation method for hardware key or state field sensor reading](https://www.navixy.com/wp-content/uploads/2024/03/browser_vw7hkgdl0n.png)

](https://www.navixy.com/wp-content/uploads/2024/03/browser_vw7hkgdl0n.png)

Exemple de configuration de la méthode de calcul de la valeur source pour la lecture d'une clé matérielle ou d'un capteur de champ d'état

#### [Index des bits](#1679330119395-5e95e66b-c1e9)

Certains appareils peuvent fournir des données avancées dans leurs paquets, parfois en fusionnant plusieurs paramètres [en une seule valeur](https://www.navixy.com/blog/sensor-parameters-avl/). L'outil Capteurs virtuels vous permet de travailler avec des parties de valeurs télématiques, en décodant les données transmises par le matériel GPS.

Par exemple, disons que la valeur 011 est transmise - nous devons d'abord lire cette information en little endian conformément au protocole :

- 1 - Indique l'état de la ceinture du conducteur : 0 - attachée, 1 - non attachée. Bit 0
- 1 - Affiche l'état de la porte du conducteur : 0 - fermée, 1 - ouverte. Bit 1
- 0 - Indique l'état de la hotte : 0 - fermée, 1 - ouverte. Bit 2

Chaque position du paramètre affiche la valeur de différents systèmes du véhicule. Pour les configurer et les afficher, vous devez créer un capteur séparément pour chaque paramètre.

Pour un capteur qui indique l'état du capot de la voiture dans notre exemple, vous devez

1. Définir le nom du capteur.
2. Choisissez l'entrée conformément à la documentation de l'appareil.
3. Sélectionner "Bit Index" comme méthode de calcul
4. Choisissez le bit 2 pour ce champ.

Voici un exemple de capteur qui indique l'état du capot de la voiture.

[![Configuration example for Bit index calculation sensor](https://www.navixy.com/wp-content/uploads/2024/03/browser_2qcam8zclk.png)

](https://www.navixy.com/wp-content/uploads/2024/03/browser_2qcam8zclk.png)

Exemple de configuration du capteur de calcul de l'indice de bits

Une fois qu'un capteur virtuel est configuré et que le capteur de l'appareil qui lui est associé a fourni des données, celles-ci peuvent être consultées dans le widget "Lectures du capteur" de l'onglet "Informations" de l'appareil. Les capteurs de votre appareil peuvent désormais parler dans votre langue.