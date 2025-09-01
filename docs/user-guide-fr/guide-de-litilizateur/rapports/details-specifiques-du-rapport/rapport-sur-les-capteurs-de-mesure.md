# Rapport sur les capteurs de mesure

Le **Rapport sur les capteurs de mesure** dans Navixy est conçu pour fournir des données détaillées à partir de capteurs de mesure configurés ou de capteurs virtuels avec une méthode de calcul de la valeur à la source sur une période sélectionnée.

Ce rapport permet aux utilisateurs de visualiser des informations graphiques et statistiques provenant des capteurs de leurs appareils, ce qui facilite le contrôle et la prise de décision.

## Exigences pour la génération du rapport

Pour réussir à générer le **Rapport sur les capteurs de mesure**les conditions suivantes doivent être remplies :

- **Compatibilité des appareils :** Assurez-vous que l'appareil prend en charge la lecture du capteur requis sur la plate-forme. Vous pouvez le vérifier en consultant la liste des entrées prises en charge pour le modèle spécifique.
- **Transmission active des données :** L'appareil et ses capteurs doivent être configurés correctement et transmettre activement des données.
- **Capteurs virtuels :** [Capteurs virtuels](../../appareils-et-parametres/capteurs-pour-vehicules/capteurs-virtuels.md) doit disposer d'une méthode de calcul de la valeur de la source et fournir des valeurs numériques à la plateforme.
- **Configuration du capteur :** Les capteurs de mesure doivent être correctement configurés sur la plate-forme.

## Paramètres du rapport

Le rapport utilise plusieurs paramètres pour adapter le résultat à vos besoins :

- **Détails plage de temps :** Affiche les relevés reçus par incréments de 5, 30 minutes, 1, 3 ou 6 heures dans le tableau des données détaillées.
- **Axe des X sur le graphique :** Choisissez d'afficher les informations en fonction de la durée ou du kilométrage.
- **Données lisses :** Appliquer un lissage au graphique pour filtrer les valeurs maximales et établir une moyenne des données en cas de variance importante.
- **Afficher l'adresse :** Affiche l'adresse reçue par la plate-forme avec les données du capteur. L'adresse affichée correspond à la première lecture dans le segment détaillé.
- **Utilisez un filtre intelligent :** Exclure les données des trajets courts, définis comme des trajets de moins de 300 mètres avec moins de 4 points de données envoyés par l'appareil.

Pour chaque appareil, vous devez sélectionner le capteur pour lequel le rapport doit être généré. Seuls les appareils dont le capteur est configuré [mesure](../../appareils-et-parametres/capteurs-pour-vehicules/measurement-sensors.md) ou [virtuel](../../appareils-et-parametres/capteurs-pour-vehicules/capteurs-virtuels.md) seront disponibles dans la liste. Si vous sélectionnez un capteur virtuel d'un type incorrect, le rapport indiquera "Ceci n'est pas un capteur de mesure".

## Visualisations

### Graphique avec les relevés des capteurs

Le graphique du rapport affiche les mesures ou les relevés des capteurs virtuels sous forme de graphique, ce qui permet de visualiser les tendances des données dans le temps ou sur une certaine distance.

- **Survoler les points :** Lorsque vous survolez un point du graphique, vous pouvez voir l'heure exacte à laquelle il a été enregistré et la valeur du capteur. Si l'axe des X est réglé sur le kilométrage, vous verrez également la distance à laquelle le relevé a été effectué.

### Tableau des données statistiques

Le rapport comprend un tableau de données statistiques qui fournit des résumés quotidiens des relevés des capteurs.

**Colonnes du tableau de données statistiques :**

- **Date :** La date spécifique pour les données enregistrées.
- **Minimum (unités de mesure) :** La valeur la plus basse enregistrée par le capteur à cette date.
- **Maximum (unités de mesure) :** La valeur la plus élevée enregistrée par le capteur à cette date.
- **Valeur moyenne (unités de mesure) :** La moyenne de tous les relevés de capteurs pour cette date.

Note : Les unités de mesure varient en fonction des réglages du capteur.

### Tableau de ventilation des données

Le **tableau de ventilation des données** présente les relevés des capteurs sur des intervalles de temps spécifiques, par exemple toutes les 30 minutes, à partir d'une heure donnée. Il fournit une vue détaillée des données du capteur, ce qui permet d'identifier les tendances ou les problèmes au cours de périodes spécifiques.

- **Interprétation du tableau :** Si le message "Aucune donnée" apparaît, cela signifie qu'aucune lecture n'a été reçue pendant cette période. Cela peut être dû au fait que l'appareil ne transmet pas de données, qu'il est éteint ou que le capteur est déconnecté.