# Conduite écologique

Le **Rapport sur l'éco-conduite** Navixy est un outil puissant conçu pour analyser et améliorer le comportement des conducteurs de votre flotte. En attribuant un score entre 0 et 100 à chaque conducteur, le système fournit une mesure claire de la performance de conduite basée sur les points de pénalité accumulés à la suite de diverses infractions de conduite. Ces infractions sont évaluées en fonction de leur fréquence et de leur gravité tous les 100 kilomètres parcourus, ce qui garantit une évaluation complète des habitudes de chaque conducteur.

Pour accéder au rapport sur l'écoconduite, naviguez jusqu'à la page d'accueil du site web de la Commission européenne. **Fleet Management app** et sélectionnez l'option **Onglet "Eco-Driving".**

![image-20240814-183737.png](../../guide-de-litilizateur/gestion-du-parc-automobile/attachments/image-20240814-183737.png)

## Comprendre les points de pénalité

Les points de pénalité sont un élément clé du rapport sur la conduite écologique, qui vous permet d'évaluer l'impact des différents types d'infractions sur les performances du conducteur. Le système suit trois catégories principales d'infractions au code de la route : les excès de vitesse, la conduite brusque et la marche au ralenti excessive. Chaque type d'infraction contribue au score global, les scores les plus bas indiquant des infractions plus fréquentes ou plus graves.

## Personnalisation du rapport

Le rapport sur l'écoconduite peut être adapté à vos besoins spécifiques, ce qui vous permet de définir vos propres critères pour déterminer ce qui constitue une infraction et sa gravité. Vous pouvez attribuer différents points de pénalité à diverses infractions, ce qui vous permet de donner la priorité à certains aspects du comportement au volant en fonction des normes de votre organisation.

![image-20240814-183612.png](../../guide-de-litilizateur/gestion-du-parc-automobile/attachments/image-20240814-183612.png)

**Caractéristiques principales**

* **Excès de vitesse :** Contrôler les cas où les conducteurs dépassent les limites de vitesse fixées, les sanctions étant adaptées en fonction de l'ampleur et de la durée de l'excès de vitesse.
* **Conduite difficile :** Suivez les manœuvres agressives telles que les freinages brusques, les accélérations ou les virages serrés, avec des seuils personnalisables en fonction des appareils de votre flotte.
* **Marche au ralenti excessive :** Identifier et sanctionner les conducteurs qui laissent tourner le moteur au ralenti pendant de longues périodes, ce qui peut entraîner un gaspillage de carburant et réduire l'efficacité du véhicule.

![](https://squaregps.atlassian.net/wiki/images/icons/grey_arrow_down.png)

Calculs dans le rapport Eco Driving

Le rapport Eco Driving de Navixy est conçu pour évaluer et noter le comportement de conduite des employés sur la base d'un ensemble de critères. Le score de chaque conducteur varie de 0 à 100 et est influencé par les points de pénalité attribués pour diverses infractions.

Vous trouverez ci-dessous des explications détaillées sur la manière dont ces points de pénalité sont calculés et comment ils affectent le score global du conducteur. Ces calculs et rapports détaillés permettent aux gestionnaires de flotte d'évaluer le comportement de conduite de manière exhaustive, afin de promouvoir des pratiques de conduite plus sûres et plus efficaces dans l'ensemble de leur flotte.

### Excès de vitesse

Les excès de vitesse sont sanctionnés en fonction de l'ampleur et de la durée du dépassement de la limite de vitesse. Vous pouvez soit fixer une limite de vitesse universelle, soit utiliser des limites de vitesse spécifiques à chaque véhicule.

**Calcul des pénalités pour excès de vitesse :**

Les points de pénalité pour excès de vitesse sont calculés selon la formule suivante :

`Time Factor × Penalty Points = Total Penalty Points`

Par exemple, si un véhicule dépasse la limite de vitesse de 21 km/h pendant une durée de 1 minute et 37 secondes, le système exclura la première minute (non pénalisée) et calculera la pénalité pour les 37 secondes restantes. Si la pénalité pour un dépassement de 20 à 30 km/h de la limite de vitesse est fixée à 10 points, la formule sera la suivante :

`0.616 × 10 = 6.16 penalty points`

### Infractions sévères au code de la route

Les événements de conduite difficiles, tels que les accélérations rapides, les freinages brusques et les virages serrés, sont enregistrés par des traceurs GPS équipés de capteurs d'accélération. La gravité de chaque événement de conduite difficile peut être personnalisée et des points de pénalité sont attribués en conséquence.

**Calcul des sanctions pour conduite en état d'ivresse**

Chaque épisode de conduite difficile entraîne automatiquement un nombre prédéfini de points de pénalité. Ces points sont déduits du score global du conducteur en fonction de la fréquence de ces événements.

### Infractions liées à la marche au ralenti excessive

La marche au ralenti excessive est contrôlée lorsqu'un véhicule reste à l'arrêt avec le moteur en marche pendant une période prolongée. Des points de pénalité sont attribués en fonction de la durée de la marche au ralenti au-delà d'un seuil prédéfini.

**Calcul des pénalités pour la marche au ralenti**

Par exemple, si un véhicule tourne au ralenti pendant 8 minutes et 14 secondes et que le seuil est fixé à 5 minutes, le calcul de la pénalité exclura les 5 premières minutes et ne pénalisera que les 3 minutes et 14 secondes restantes. Si la pénalité pour la marche au ralenti est fixée à 5 points par minute, le calcul sera le suivant :

`3.23 × 5 = 16.17 penalty points`

### Total pour la période page

La section "Total pour la période" fournit une vue d'ensemble de toutes les sanctions et notes pour chaque conducteur ou véhicule au cours de la période sélectionnée. Elle comprend une représentation graphique et des tableaux détaillés.

**Graphique du montant de la pénalité**

Ce graphique affiche les points de pénalité cumulés, classés par couleur selon le type d'infraction (rouge pour les excès de vitesse, bleu pour la conduite en état d'ivresse et vert pour la marche au ralenti).

**Graphique de classement**

Ce graphique montre les scores de chaque conducteur ou appareil, calculés pour 100 kilomètres parcourus. Les scores sont ajustés en fonction des pénalités, ce qui permet de comprendre clairement les performances de chaque conducteur.

### Tableaux contenant des informations détaillées

Chaque type d'infraction est subdivisé en tableaux détaillés, offrant un aperçu d'événements spécifiques tels que les excès de vitesse, la conduite en état d'ivresse et la marche au ralenti.

#### Tableau des excès de vitesse

Ce tableau répertorie tous les excès de vitesse, avec des points de pénalité attribués en fonction de la vitesse la plus élevée dépassée au cours de l'événement.

#### Table de conduite sévère

Les événements enregistrés dans une fenêtre de 5 minutes sont regroupés et les pénalités sont calculées pour chaque groupe.

#### Tableau des intervalles de repos

Ce tableau fournit des détails sur chaque cas de marche au ralenti avec le moteur en marche, y compris la durée et les points de pénalité correspondants.

## Analyse des résultats

Le rapport sur l'écoconduite fournit des données graphiques et tabulaires, ce qui permet de voir d'un coup d'œil quels conducteurs sont performants et lesquels pourraient avoir besoin d'une formation plus poussée. L'interface graphique utilise un code couleur pour distinguer les différents types d'infractions, tandis que les tableaux offrent une ventilation détaillée des pénalités par conducteur ou par appareil.

### Paramètres et personnalisation

Vous pouvez affiner le rapport Eco Driving pour vous concentrer sur des périodes spécifiques, des jours de la semaine ou des heures de la journée qui sont les plus pertinents pour votre entreprise. En outre, le système vous permet de choisir de générer des rapports basés sur des conducteurs individuels ou sur les véhicules qu'ils utilisent, ce qui offre une certaine flexibilité en fonction de vos préférences en matière de suivi.

### Programmation du rapport d'écoconduite

Le rapport Eco Driving de Navixy peut être programmé pour s'exécuter automatiquement à des intervalles spécifiques, ce qui vous permet de surveiller et d'évaluer régulièrement le comportement de conduite sans intervention manuelle. Cette fonction vous permet de recevoir des informations cohérentes et opportunes sur les performances de votre flotte, ce qui vous aide à identifier les tendances et à traiter les problèmes de manière proactive.

Pour programmer le rapport, accédez à l'onglet "Programmation" dans la section Eco Driving, définissez la fréquence souhaitée et indiquez les destinataires. Le système générera le rapport selon vos paramètres et le livrera directement dans votre boîte de réception ou le mettra à disposition pour téléchargement sur la plateforme.

### Applications pratiques

Le rapport Eco Driving est particulièrement utile pour les entreprises qui doivent surveiller de près le comportement des conducteurs, comme les entreprises de transport de passagers, de transport de matières dangereuses ou les services d'urgence. En analysant ce rapport, les entreprises peuvent prolonger la durée de vie des véhicules, réduire la probabilité d'accidents et s'assurer que les véhicules sont utilisés de manière efficace et responsable.

Dans l'ensemble, le rapport sur la conduite écologique est une fonction essentielle pour tout gestionnaire de flotte qui cherche à maintenir des normes élevées en matière de sécurité des conducteurs, d'efficacité et de conformité aux réglementations.
