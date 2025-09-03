# Rapport sur le volume de carburant

Le **Fuel Volume Report** in Navixy offre une vision complète de l'utilisation du carburant dans votre flotte, en fournissant des données cruciales sur les changements de volume de carburant, les événements de ravitaillement et la consommation de carburant sur une période de temps donnée.

Ce rapport est essentiel pour les gestionnaires de flotte qui souhaitent contrôler l'efficacité du carburant, détecter les vols potentiels de carburant et gérer efficacement les coûts de carburant. Vous trouverez ci-dessous un guide détaillé sur le fonctionnement de ce rapport, les paramètres impliqués et la manière d'interpréter les données.

![](../../../guide-de-litilizateur/rapports/details-specifiques-du-rapport/attachments/image-20240815-003825.png)

## Vue d'ensemble

Le rapport sur le volume de carburant se compose de plusieurs sections :

1. **Graphique de la variation du volume de carburant :** Une représentation visuelle des variations du niveau de carburant au fil du temps.
2. **Tableau des garnitures :** Une liste détaillée des opérations de ravitaillement, y compris l'heure, le volume et le lieu de chaque ravitaillement.
3. **Détails par tableau de dates :** Des résumés quotidiens des changements de volume de carburant, y compris le kilométrage, le nombre de ravitaillements et les calculs de consommation de carburant.
4. **Évaluation de la qualité des capteurs de niveau de carburantLAB:** Une fonction expérimentale qui évalue la précision et la fiabilité des données des capteurs de carburant. Voir aussi : [Améliorer la précision de la gestion des carburants grâce à l'indice de qualité des capteurs de carburant](https://www.navixy.com/blog/enhancing-fuel-management-accuracy-with-fuel-sensor-quality-index/).

## Caractéristiques principales et cas d'utilisation

Le rapport sur le volume de carburant peut être utilisé dans différents scénarios :

* **Contrôle de la consommation de carburant :** Suivre la consommation de carburant et identifier les schémas ou les anomalies qui pourraient indiquer un manque d'efficacité ou un vol potentiel de carburant.
* **Évaluation de la précision des capteurs :** Évaluer les performances des capteurs de niveau de carburant afin de garantir la fiabilité de la collecte des données.
* **Détection de la fraude sur les carburants :** Identifier les schémas ou les lieux de ravitaillement inhabituels qui peuvent indiquer une activité frauduleuse.

## Paramètres du rapport

Pour générer un rapport précis sur le volume de carburant, veillez à ce que les configurations suivantes soient correctement établies :

1. **Étalonnage du capteur de niveau de carburant :**&#x20;
   1. Pour un seul capteur de niveau de carburant, veillez à ce que le tableau d'étalonnage soit rempli conformément aux recommandations du fabricant. En outre, définissez les seuils de filtrage des émissions dans la section "Avancé" sous le tableau d'étalonnage.
   2. Pour les véhicules dotés de plusieurs réservoirs, étalonnez chaque capteur séparément et créez un capteur global dont les unités de volume sont réglées sur les litres ou les gallons. Évitez d'utiliser l'option "Custom Option" dans le réglage de l'unité de mesure du capteur.
   3. Pour les capteurs qui indiquent les niveaux de carburant en pourcentage, un étalonnage est également nécessaire, avec des volumes de carburant minimum et maximum spécifiés.
2. **Traitement des données des capteurs :** \
   La plateforme collecte des données brutes à partir de dispositifs et de capteurs de carburant, qui sont ensuite filtrées sur la base des valeurs ignorées définies dans les paramètres du capteur. La plateforme enregistre les données telles qu'elles sont reçues, sans les modifier.
3. **Génération de graphiques :** \
   La plate-forme génère un graphique des valeurs stockées sur la base des paramètres du rapport. Les réglages des capteurs de carburant, y compris les valeurs seuils, sont appliqués à ce graphique.
4. **Lissage automatisé :** \
   Le processus de lissage du graphique est entièrement automatisé, tous les paramètres de lissage et de filtrage étant appliqués automatiquement pour produire un graphique convivial et lisible.

## Sections détaillées du rapport

1. **Fuel volume change graph:**\
   Ce graphique présente les relevés du capteur de niveau de carburant au fil du temps. Si plusieurs capteurs sont utilisés, le graphique n'affiche que les données du capteur global. Les événements de ravitaillement en carburant sont numérotés et représentés aux points correspondants du graphique.
2. **Tableau des garnitures :** \
   Le tableau répertorie tous les événements de ravitaillement au cours de la période sélectionnée, y compris la date, l'heure, le volume de carburant et le lieu.
3. **Détails par tableau de dates :**\
   Fournit des résumés quotidiens des données, y compris
   1. **Date :** Le jour spécifique pour lequel les données sont calculées.
   2. **Kilométrage :** La distance parcourue ce jour-là.
   3. **Nombre de ravitaillements :** Nombre de ravitaillements.
   4. **Volume :** Volume total de carburant rempli.
   5. **Consommé :** Consommation réelle de carburant pour la journée, calculée comme suit `initial fuel level + volume of refuelings - final fuel level`.
   6. **Consommation par 100 km :** Consommation de carburant par 100 km, calculée comme suit `(initial fuel level + volume of refuelings - final fuel level) / mileage * 100`.
4. **Évaluation de la qualité de la lecture des capteurs de carburantLAB:**
   1. Cette section évalue la qualité des relevés des capteurs de carburant, en attribuant une note quantitative (de 1,0 à 10,0) et une note qualitative (faible, moyenne, élevée) en fonction du bruit et de la précision des données des capteurs.
   2. Le système peut afficher un message indiquant que les données sont insuffisantes pour l'évaluation de la qualité si le capteur a été installé récemment ou si la période de collecte des données est trop courte.

## Aperçu du rapport

Le rapport sur le volume de carburant peut révéler des informations essentielles, telles que

* **Détection de la fraude sur les carburants :** Identifier les divergences entre les ravitaillements déclarés et la consommation réelle de carburant, en particulier dans les stations-service.
* **Efficacité opérationnelle :** Analyse de la consommation de carburant par rapport au kilométrage afin d'identifier les inefficacités potentielles ou les domaines de réduction des coûts.
* **Contrôle de la performance des capteurs :** Évaluer régulièrement la précision et la fiabilité des capteurs de carburant afin de s'assurer que les données utilisées pour la prise de décision sont fiables.
