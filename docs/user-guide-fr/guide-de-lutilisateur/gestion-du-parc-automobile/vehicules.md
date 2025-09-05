# Véhicules

Les véhicules dans Navixy sont essentiels pour le suivi et la gestion de votre flotte. Ils vous permettent de surveiller divers aspects tels que l'emplacement, la consommation de carburant, les calendriers d'entretien et la performance globale de la flotte, ce qui permet des opérations efficaces et une meilleure prise de décision.

## Onglet Véhicules

L'onglet "Véhicules" présente un aperçu détaillé de tous les véhicules de votre flotte. Les informations sont organisées sous forme de tableau, complété par un menu visuel sur le côté droit de l'écran. Ici, vous pouvez facilement ajouter ou modifier les détails des véhicules, les associer à des dépôts spécifiques et les lier à des trackers qui ont été activés sur la plateforme.

### Ajout d'un nouveau véhicule

Pour ajouter un nouveau véhicule, il suffit d'appuyer sur la touche **+** bouton. Vous avez également la possibilité de télécharger une image du véhicule pour faciliter son identification.

* **Onglet principal :** Saisir les informations essentielles sur le véhicule, y compris les étiquettes et toute note pertinente.
* **Onglet de spécification :** Fournir des spécifications détaillées, telles que les dimensions du véhicule, la taille de l'empattement, le nombre de roues, la vitesse autorisée, la disponibilité de la remorque et l'année de fabrication.
* **Tableau des carburants :** Enregistrez les informations relatives au carburant, notamment le type de carburant, la capacité du réservoir et le taux de consommation par 100 km (ou miles). Ces données sont essentielles pour établir des rapports précis sur la consommation de carburant.
* **Onglet assurance :** Saisissez les détails de l'assurance du véhicule, y compris le numéro de police et la date d'expiration.

<details>

<summary>Consommation de carburant dans le profil du véhicule et son rôle dans les rapports sur les carburants</summary>

Dans Navixy, la configuration du **Consommation de carburant** dans le profil du véhicule est une étape essentielle pour suivre et rendre compte de la consommation de carburant de votre flotte en fonction du kilométrage parcouru, sans avoir recours aux données OBDII ou à des capteurs de carburant spécialisés.

Ce paramètre est généralement défini en termes de litres par 100 kilomètres (L/100 km) ou de miles par gallon (MPG), selon les préférences régionales.

#### Comment la consommation de carburant est utilisée dans les rapports sur les carburants

1. **Estimation de la consommation de carburant :**\
   La valeur de la consommation de carburant saisie dans le profil du véhicule sert de référence pour estimer la consommation de carburant d'un véhicule sur une distance donnée. Par exemple, si un véhicule est réglé pour consommer 10 L/100 km, le système estimera qu'il consomme 10 litres de carburant pour 100 kilomètres parcourus.
2. **Calcul des coûts de carburant prévus :**\
   Navixy utilise le taux de consommation de carburant défini ainsi que le kilométrage enregistré pour calculer les frais de carburant prévus. En entrant le prix du litre ou du gallon dans les paramètres, le système peut générer des rapports qui estiment le montant que vous devriez dépenser en carburant, ce qui facilite l'établissement du budget et la planification financière.
3. **Comparaison avec les données réelles sur les carburants :**\
   Combiné aux données des capteurs de niveau de carburant, Navixy peut comparer la consommation de carburant estimée avec la consommation réelle. Cette comparaison permet d'identifier les écarts, tels que le vol de carburant, les inefficacités dans le comportement de conduite ou les problèmes liés au moteur du véhicule qui pourraient entraîner une consommation de carburant plus élevée que prévu.

</details>

### Importation de véhicules

Si vous avez une flotte importante et que vous devez créer des profils pour plusieurs véhicules, il est plus efficace d'importer toutes les informations en une seule fois à l'aide d'un fichier unique, plutôt que de créer des profils de véhicules un par un. Les données doivent être au format XLS, XLSX ou CSV.

Pour importer des profils de véhicules :

1. Ouvrez l'application "Gestion du parc automobile", cliquez sur "Ajouter un véhicule" et sélectionnez "Importer à partir d'un fichier Excel".
2. Dans la fenêtre d'importation, vous trouverez un exemple de fichier Excel que vous pouvez utiliser comme modèle.
3. Assurez-vous que les colonnes de votre fichier correspondent aux champs corrects du système de suivi en saisissant les champs d'en-tête appropriés. Cette opération peut être effectuée soit avant l'importation, soit pendant le processus.
4. Dans le fichier chargé, vous devrez spécifier des informations clés telles que
   1. Nom
   2. Plaque d'immatriculation
   3. Type\
      \
      Après avoir rempli le formulaire, enregistrez le fichier sur votre ordinateur.

Pour télécharger le fichier dans le système :

1. Cliquez sur le bouton "Sélectionner", recherchez votre fichier et cliquez sur "Suivant".
2. Vous serez invité à vérifier les champs de l'en-tête. Si tout est correct, cliquez à nouveau sur "Suivant".
3. Si l'un des champs est incorrect, le système vous demandera de le corriger. Si un champ obligatoire est vide, l'information ne sera pas importée.
4. Une fois que les informations sont correctes, l'importation est terminée avec succès et les nouveaux profils de véhicules apparaissent dans l'application "Gestion du parc automobile".
