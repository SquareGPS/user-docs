# Widget de données brutes

L'outil d'exportation de données brutes dans Navixy vous permet de télécharger des données analysées et décodées à partir de n'importe quel tracker GPS sur la plateforme au format CSV. Cette fonctionnalité est essentielle pour le diagnostic des appareils, l'analyse des données et l'intégration des données avec des programmes d'IA / ML.

[![Raw data export tool](https://www.navixy.com/wp-content/uploads/2023/12/browser_a0qszuge3l.png)

](https://www.navixy.com/wp-content/uploads/2023/12/browser_a0qszuge3l.png)

## Vue d'ensemble

Grâce à l'outil d'exportation des données brutes, vous pouvez :

- **Télécharger les données analysées** à partir de n'importe quel traceur GPS sur la plateforme.
- **Sélectionner des paramètres spécifiques** à inclure dans votre fichier CSV, avec une fonction de recherche facile à utiliser.
- **Accès aux données historiques** sans qu'il soit nécessaire d'activer l'enregistrement des données à l'avance.
- **Ajuster les horodatages** à votre fuseau horaire préféré, ce qui facilite la gestion des données dans différentes régions.

La sortie des données brutes se compose de toutes les informations décodées à partir des protocoles propriétaires du modèle d'appareil. Une fois décodées, les données sont stockées dans un format universel, y compris les détails clés tels que l'emplacement et les relevés des capteurs. Les données sont fournies dans un format de fichier CSV pour faciliter l'accès et l'intégration.

## Comment utiliser l'exportation de données brutes

Commencez par vous rendre dans la section "Appareils et paramètres" et localisez l'appareil. Cliquez ensuite sur le bouton "Exporter les données" dans le portlet "Données brutes".

[![Raw data export tool file configuration window](https://www.navixy.com/wp-content/uploads/2023/12/browser_ybwmnfdh8h.png)

](https://www.navixy.com/wp-content/uploads/2023/12/browser_ybwmnfdh8h.png)

L'outil "Exportation de données brutes" s'ouvre alors. Choisissez la plage de dates, le fuseau horaire et les paramètres qui doivent être inclus dans un fichier csv.

Pour éviter les fermetures accidentelles de fenêtres, l'outil "Exportation de données brutes" ne peut être fermé qu'en cliquant sur le "X" dans le coin supérieur droit. En outre, si vous n'avez pas changé d'appareil ou actualisé la page, l'outil se souviendra des paramètres précédemment sélectionnés. Cette fonction permet de revoir facilement les paramètres du traceur GPS ou du capteur, de revenir et de continuer à travailler.

### Sélection d'une plage de dates

Vous pouvez sélectionner les 30 derniers jours ou plus, en fonction de votre plan. Les dates peuvent être choisies en cliquant sur le calendrier ou en les saisissant manuellement. Des heures spécifiques peuvent également être définies. Voici quelques options de sélection rapide :

- Hier
- La semaine dernière
- 30 derniers jours

En cliquant sur ces derniers, la plage de dates appropriée est automatiquement définie.

Pour simplifier le processus, un compteur indique le nombre de jours que vous avez sélectionnés. Si vous tentez de sélectionner une date antérieure de plus de 30 jours, vous recevrez un message et le bouton de sélection sera désactivé.

### Choisir un fuseau horaire

Le fuseau horaire est par défaut celui du compte de l'utilisateur, mais il peut être modifié :

- Choix dans une liste de fuseaux horaires disponibles.
- Saisir le nom du fuseau horaire.
- Introduction du décalage du fuseau horaire (par exemple, -8, +2).

### Sélection des paramètres

Les paramètres disponibles varient selon le modèle d'appareil et comprennent tous les paramètres intégrés dans la plate-forme pour chaque modèle. Il est possible de sélectionner jusqu'à 1000 paramètres par fichier.

Les options de sélection des paramètres sont les suivantes :

- **Sélectionner tout**: Cliquez sur la case à cocher pour sélectionner tous les paramètres.
- **Sélectionner des paramètres spécifiques**: Utilisez les cases à cocher en regard de chaque paramètre.
- **Recherche**: Rechercher des paramètres spécifiques en tapant leur nom ou une partie de leur nom.

En cas d'entrées multiples du même type, le système donne la priorité à l'entrée dont le numéro d'index est le plus élevé. Vous pouvez spécifier les indices à inclure en saisissant des nombres séparés par des virgules ou en définissant une plage à l'aide d'un tiret (par exemple, "1-2, 4, 7").

Un décompte des paramètres sélectionnés s'affiche, et chaque paramètre choisi ajoute une colonne au fichier CSV.

[![Raw data export tool file configuration window with chosen parameters](https://www.navixy.com/wp-content/uploads/2023/12/browser_imbnj05cft.png)

](https://www.navixy.com/wp-content/uploads/2023/12/browser_imbnj05cft.png)

## Comment lire le fichier de données brutes

Après avoir sélectionné les paramètres nécessaires, cliquez sur "Télécharger CSV" pour télécharger le fichier.

- Le fichier peut être ouvert avec n'importe quel éditeur de texte ou visualiseur de tableau compatible avec le format CSV. Les colonnes sont séparées par des virgules.
- Le nom du fichier comprend l'identifiant de l'appareil, l'étiquette du traceur, ainsi que la date et l'intervalle de temps spécifiés.
- Chaque ligne (à partir de la deuxième) représente un message envoyé par l'appareil à la plate-forme. La première ligne contient l'heure du message dans le fuseau horaire choisi, suivie des paramètres sélectionnés.

[![Raw data file columns example](https://www.navixy.com/wp-content/uploads/2023/12/nvidia_share_xbgmryofhf.png)

](https://www.navixy.com/wp-content/uploads/2023/12/nvidia_share_xbgmryofhf.png)

Cet outil est essentiel pour le diagnostic et l'analyse, car il fournit des informations détaillées sur les données de votre appareil.