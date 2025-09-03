# Rapport sur les heures de fonctionnement du moteur

Le **Heures de fonctionnement du moteur** dans Navixy fournit des informations détaillées sur la durée pendant laquelle le moteur de votre véhicule a fonctionné, à la fois en mouvement et pendant les périodes de ralenti. Ce rapport est essentiel pour les gestionnaires de flotte qui doivent surveiller l'utilisation du moteur, optimiser l'efficacité opérationnelle et planifier les programmes d'entretien. Vous trouverez ci-dessous un guide complet sur le fonctionnement de ce rapport, les paramètres impliqués et la manière d'interpréter les données.

## Vue d'ensemble

Le rapport sur les heures de fonctionnement du moteur est conçu pour vous indiquer le temps total pendant lequel le moteur de votre véhicule a fonctionné, divisé en périodes de mouvement et de ralenti. Ce rapport comprend plusieurs aides visuelles essentielles, telles qu'un graphique d'activité par période et un graphique à barres de l'activité quotidienne, pour vous aider à comprendre et à analyser rapidement les données.

## Comment cela fonctionne-t-il ?

Le rapport calcule les heures de fonctionnement du moteur sur la base des points de données reçus par la plate-forme Navixy. Pour des calculs précis, les configurations et conditions suivantes doivent être respectées :

1. **Configuration du capteur d'allumage :**

* Le capteur d'allumage doit être correctement connecté à l'appareil et enregistrer avec précision l'état de l'allumage. Il peut s'agir d'un capteur d'allumage discret ou d'un capteur virtuel basé sur l'allumage sur la plate-forme.

2. **Durée d'allumage :**

* Le contact doit être mis pendant au moins 60 secondes pour que l'heure soit enregistrée dans le rapport.

3. **Détection de stationnement :**

* La plateforme utilise les paramètres de détection de stationnement pour différencier les heures de moteur passées en mouvement et au ralenti. Par exemple, si la vitesse de détection du stationnement est inférieure à 3 km/h et que le véhicule reste à cette vitesse ou à une vitesse inférieure pendant plus de 5 minutes, ce temps sera enregistré comme de la marche au ralenti et non comme du mouvement.

4. **Fréquence des points de données :**

* La fréquence à laquelle votre appareil envoie des points de données influe sur la précision du rapport. Les retards dans la transmission des données peuvent entraîner des inexactitudes, en particulier si l'état de l'allumage change mais n'est pas immédiatement signalé.

### Exemple de calcul

| Point | L'heure  | État d'allumage | Heures de fonctionnement du moteur                  |
| ----- | -------- | --------------- | --------------------------------------------------- |
| 1     | 16:00:00 | Arrêt           | 0 minute                                            |
| 2     | 16:01:00 | Sur             | 0 minute (l'allumage était éteint au dernier point) |
| 3     | 16:01:32 | Sur             | 0 minute (moins de 60 secondes)                     |
| 4     | 16:05:32 | Arrêt           | 4 minutes et 32 secondes                            |

## Paramètres du rapport

Le rapport sur les heures de fonctionnement du moteur comprend plusieurs paramètres configurables qui vous permettent d'adapter le résultat à vos besoins spécifiques :

* **Détails de l'exposition :** Fournit des informations détaillées sur l'endroit précis et l'heure à laquelle le moteur était allumé.
* **Résumé de l'affichage :** Affiche une vue d'ensemble de tous les appareils. Vous pouvez activer ou désactiver cette fonction selon que vous avez besoin ou non d'une page de synthèse.
* **Afficher uniquement le résumé :** Regroupe les données de plusieurs suiveurs en un seul résumé. Cette option nécessite au moins deux appareils.
* **Utilisez un filtre intelligent :** Exclut les trajets courts du rapport. Un trajet est considéré comme court s'il couvre moins de 300 mètres et que l'appareil transmet moins de quatre points de données.

## Visualisations

![image-20240815-010415.png](../../../guide-de-litilizateur/rapports/details-specifiques-du-rapport/attachments/image-20240815-010415.png)

### Diagramme d'activité global

* Ce diagramme donne une vue d'ensemble de la durée totale pendant laquelle le moteur a fonctionné au cours de la période sélectionnée. Il fait la distinction entre le temps d'arrêt du moteur, le temps passé en mouvement et le temps passé au ralenti.

### Histogramme de l'activité quotidienne

* L'histogramme décompose les heures de fonctionnement du moteur en segments quotidiens, en indiquant les temps de mouvement et d'inactivité. En survolant chaque jour, on obtient une vue plus détaillée de l'activité du moteur au cours de cette journée.

### Tableau des heures de fonctionnement du moteur

* Le tableau présente des données quotidiennes détaillées, notamment
  * **Date :** Le jour spécifique pour lequel les données sont calculées.
  * **Heures de fonctionnement du moteur :** Nombre total d'heures de fonctionnement du moteur pour la journée.
  * **En mouvement :** Temps passé en mouvement et pourcentage du nombre total d'heures de fonctionnement du moteur.
  * **La marche au ralenti :** Temps passé au ralenti et pourcentage du nombre total d'heures de fonctionnement du moteur.
  * **Intervalle moyen :** Durée moyenne pendant laquelle le moteur a fonctionné après chaque événement d'allumage.
  * **Kilométrage :** Distance parcourue lorsque le moteur est en marche.
  * **Vitesse moyenne :** La vitesse moyenne pour la journée.
  * **Intervalles :** Nombre d'intervalles pendant lesquels le moteur a été allumé au cours de la journée.

> \[!INFO] Si vous constatez une différence entre le kilométrage indiqué dans le rapport de voyage et le rapport sur les heures de fonctionnement du moteur, vérifiez deux choses :
>
> 1. Veillez à ce que les paramètres du filtre intelligent soient appliqués de manière cohérente dans tous les rapports. Des incohérences dans son utilisation peuvent entraîner des divergences.
> 2. Vérifiez que l'allumage a été détecté pendant tous les déplacements du véhicule en comparant les heures de début et de fin de voyage avec les données relatives aux heures de fonctionnement du moteur.

## Interprétation du rapport

Pour utiliser efficacement le rapport sur les heures de fonctionnement du moteur, il convient de tenir compte des éléments suivants :

* **Divergences :** Si vous constatez une différence entre le kilométrage indiqué dans le rapport de voyage et les heures de fonctionnement du moteur, vérifiez si le filtre intelligent est appliqué de manière cohérente dans tous les rapports et si l'allumage a été correctement détecté pendant le mouvement.
* **Analyse des données :** Le rapport vous permet d'analyser l'utilisation des moteurs par les employés, d'évaluer l'efficacité des véhicules, d'estimer les délais de remplacement, de calculer les coûts de dépréciation et de reconfigurer les coûts de carburant et de lubrifiant en fonction du temps d'inactivité.
