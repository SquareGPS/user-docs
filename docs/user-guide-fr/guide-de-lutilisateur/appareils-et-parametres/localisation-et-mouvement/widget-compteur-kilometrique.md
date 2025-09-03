# Widget compteur kilométrique

Les **Widget compteur kilométrique** vous permet de contrôler le kilométrage d'un véhicule en temps réel. Les relevés kilométriques peuvent être dérivés des données reçues via un dispositif de suivi GPS ou le bus CAN. En outre, la fonction de compteur kilométrique s'intègre dans le système de gestion des véhicules de l'entreprise. [Entretien du parc automobile](../../gestion-du-parc-automobile/maintenance.md) qui vous permet de planifier les travaux d'entretien d'un véhicule et de recevoir des rappels en temps voulu.

![image-20240815-181307.png](../../../guide-de-litilizateur/appareils-et-parametres/localisation-et-mouvement/attachments/image-20240815-181307.png)

## Activation du compteur kilométrique

Pour activer le compteur kilométrique :

1. Ouvrez la section "Appareils et paramètres", sélectionnez l'objet souhaité et naviguez jusqu'au widget Odomètre.
2. Cliquez sur le bouton "Ajouter un compteur kilométrique".
3. Choisissez la source de données appropriée. Des sources supplémentaires peuvent être disponibles après la création d'un capteur de mesure du kilométrage.
4. Définir la valeur initiale du kilométrage.
5. Appuyez sur "Enregistrer".

## Correction du compteur kilométrique

* **Facteur de correction.** Vous pouvez définir un facteur de correction pour ajuster automatiquement les relevés de l'odomètre à la hausse ou à la baisse. Saisissez une valeur en pourcentage dans le champ "Correction". Une valeur positive augmentera les relevés de l'odomètre, tandis qu'une valeur négative les diminuera en fonction du capteur d'entrée.
* **Mise à jour de la valeur.** Vous pouvez également mettre à jour la valeur de l'odomètre si nécessaire. Les valeurs précédentes du compteur kilométrique peuvent être consultées en générant le "Rapport sur tous les événements" dans l'application Rapports.
* **Accès rapide dans la vue d'objet.** Pour un accès rapide, la valeur de l'odomètre peut être consultée et configurée dans le widget dédié de l'écran [Vue détaillée de l'objet](../../suivi-par-gps/liste-des-objets/vue-detaillee-de-lobjet.md).

## Modification des sources du compteur kilométrique

Les types de sources de données kilométriques que vous pouvez utiliser dépendent du modèle de votre appareil. La compréhension et l'utilisation de plusieurs sources peuvent améliorer la précision du suivi du kilométrage de votre véhicule.

Pour ajouter des sources de compteur kilométrique supplémentaires :

1. **Créer un nouveau capteur de mesure :** En fonction des capacités de votre appareil, vous pouvez créer des capteurs tels que CAN Mileage ou Hardware Mileage. Ces capteurs collectent des données directement à partir des systèmes de votre véhicule, ce qui garantit des relevés kilométriques précis.
2. **Intégration avec le widget Odomètre :** Après avoir créé le capteur, il apparaîtra comme une option dans le widget Odomètre de la plateforme Navixy. Cela vous permet de choisir la source la plus appropriée pour vos données kilométriques.

En exploitant différentes sources de données kilométriques, vous pouvez améliorer la fiabilité de votre suivi, ce qui est particulièrement utile pour la planification de l'entretien et l'établissement de rapports précis. Comprendre les différents types de sources et la manière de les intégrer dans votre système est essentiel pour optimiser votre installation télématique.
