# Règles et notifications

Utilisation **Règles et notifications** Dans Navixy, vous pouvez détecter divers événements et en être informé. Ces fonctionnalités aident les utilisateurs à surveiller et à gérer plus efficacement leur flotte, leurs actifs et leurs employés sur le terrain. Les événements peuvent aller de la simple violation d'une géofence à des scénarios complexes tels que les alertes antivol ou la prévention des vols de carburant. Voir les [exemples](broken-reference) pour plus de détails.

## Types d'événements détectés

Navixy propose un ensemble complet d'événements structurés en différentes catégories pour vous aider à surveiller et à gérer efficacement votre flotte, vos actifs et vos employés sur le terrain. Vous trouverez ci-dessous les catégories d'événements :

* [**Puissance de l'appareil**](../../guide-de-litilizateur/regles-et-notifications/regles-et-notifications/puissance-de-lappareil.md) - Contrôler l'état de l'alimentation de l'appareil, y compris la batterie et les connexions externes
* [**Connexion des appareils**](../../guide-de-litilizateur/regles-et-notifications/regles-et-notifications/connexion-des-appareils.md) - Suivi de la connectivité de l'appareil au réseau cellulaire ou à la plate-forme
* [**Positionnement de l'appareil**](../../guide-de-litilizateur/regles-et-notifications/regles-et-notifications/positionnement-de-lappareil.md) - Contrôler les informations GPS
* [**Sécurité**](../../guide-de-litilizateur/regles-et-notifications/regles-et-notifications/securite.md) - Événements liés à la sécurité et à la manipulation des véhicules
* [**Sécurité**](../../guide-de-litilizateur/regles-et-notifications/regles-et-notifications/safety.md) - Événements liés à la sécurité des conducteurs
* [**Surveillance des mouvements**](../../guide-de-litilizateur/regles-et-notifications/regles-et-notifications/surveillance-des-mouvements.md) - Suivi des mouvements, de la vitesse et de l'itinéraire des véhicules
* [**Planification et répartition**](../../guide-de-litilizateur/regles-et-notifications/regles-et-notifications/planification-et-repartition.md) - Gérer la planification des véhicules et du personnel
* [**Efficacité des véhicules**](../../guide-de-litilizateur/regles-et-notifications/regles-et-notifications/efficacite-des-vehicules.md) - Contrôler la consommation de carburant et l'efficacité
* [**Entrées et sorties**](../../guide-de-litilizateur/regles-et-notifications/regles-et-notifications/entrees-et-sorties.md) - Suivi de l'état des capteurs et des équipements connectés

### Où les événements sont calculés

Dans les systèmes IdO, les événements peuvent être détectés soit du côté de l'appareil, soit du côté du serveur :

* **Événements détectés du côté de l'appareil**: Déclenchés par les capteurs ou les entrées du dispositif de suivi GPS installé dans le véhicule ou le bien. Ces événements se produisent en raison d'actions ou de conditions physiques, telles que l'appui sur un bouton d'urgence, la détection d'un accident de voiture ou l'enregistrement d'un comportement de conduite difficile. Les événements spécifiques détectés dépendent des capacités du dispositif utilisé.
* **Événements détectés du côté du serveur**: Générés par l'analyse des données reçues de l'appareil en fonction de règles et de conditions prédéfinies par l'utilisateur. Ces événements sont identifiés par la logique du serveur, comme la détection de violations de la géofence, de déviations d'itinéraires, d'alertes de maintenance programmée ou de variations inhabituelles du niveau de carburant. Le serveur traite les données et déclenche des alertes en fonction des critères configurés.

## Gérer les règles

Dans Navixy, les règles sont des conditions prédéfinies qui déclenchent des événements lorsqu'elles sont remplies. Pour configurer, modifier ou supprimer les règles que vous souhaitez surveiller et dont vous voulez être informé, cliquez sur **Alertes** dans le menu principal.

![](https://squaregps.atlassian.net/wiki/images/icons/grey_arrow_down.png)

En savoir plus

Pour accéder à la configuration des règles de notification dans Navixy, allez dans le menu de gauche et choisissez **Alertes**. Le panneau de notification s'ouvre. Cliquez sur **Fixer des règles**L'interface des règles d'alerte s'affiche.

![image-20240805-214736.png](../../guide-de-litilizateur/regles-et-notifications/attachments/image-20240805-214736.png)

Dans l'interface des règles d'alerte, vous pouvez

* **Voir les règles existantes**: L'interface affiche une liste de toutes les règles d'alerte existantes.
* **Sélectionner ou créer de nouvelles règles**: Vous pouvez sélectionner des règles existantes à modifier ou créer de nouvelles règles en cliquant sur le bouton "+".
* **Paramètres des règles**: Pour chaque règle, vous pouvez configurer les paramètres suivants :
  * **Nom et type**: Définir le nom et la description de la règle.
  * **Paramètres**: Définir les conditions et les paramètres spécifiques de la règle.
  * **Notifications**: Configurez comment et à qui les notifications seront envoyées.
  * **Calendrier**: Définir l'horaire auquel la règle sera active.

### Lier des règles à des objets

Une règle peut être liée à un ou plusieurs objets, tels que des véhicules individuels ou des groupes de véhicules en fonction de l'alerte. Cette flexibilité vous permet d'appliquer la même règle à différents actifs, garantissant ainsi une surveillance et des notifications cohérentes.

![](https://squaregps.atlassian.net/wiki/images/icons/grey_arrow_down.png)

Étapes pour lier une règle à des objets

1. **Ouvrir les paramètres de la règle**: Naviguez jusqu'à l'écran **Alertes** dans le menu principal et sélectionnez la règle que vous souhaitez configurer.
2. **Sélectionner des objets**: Dans le **Paramètres des règles** vous verrez une liste d'objets disponibles sur le côté gauche. Ces objets peuvent être des véhicules individuels ou des groupes de véhicules organisés par département.
3. **Choisir des objets**: Cochez les cases en regard des objets ou des groupes auxquels vous souhaitez lier la règle. Par exemple, vous pouvez sélectionner des véhicules individuels comme "Oliver (Chevrolet)" et "Marisol (Nissan)", ou des groupes entiers comme "Département des ventes".

### Nom et type

Dans le cadre de la **Nom et type** de la boîte de dialogue, vous pouvez spécifier les détails suivants pour votre règle de notification :

* **Type de règle**: Sélectionnez l'un des nombreux types d'événements qui peuvent être surveillés par la plate-forme.
* **Étiquette de la règle**: Donnez un nom à la règle pour l'identifier facilement. Exemple : "Le véhicule est sorti du dépôt ABC".
* **Rule description**: Ajoutez une brève description de la règle pour expliquer son objectif ou tout autre détail supplémentaire. Exemple : "Cette règle déclenche une alerte lorsqu'un véhicule sort de la zone ABC du dépôt désigné, ce qui permet de surveiller les mouvements non autorisés."

L'utilisation de l'étiquette et de la description vous permet d'organiser et de gérer efficacement de nombreuses règles.

### Notifications

Vous pouvez recevoir des notifications par différents canaux afin d'être rapidement informé des événements importants. Ces canaux sont les suivants

* **SMS notifications**: Alertes immédiates envoyées sur le téléphone portable de l'utilisateur.
* **Notifications par courrier électronique**: Notifications détaillées envoyées à l'adresse électronique de l'utilisateur.
* **Notifications push**: Alertes instantanées via l'application mobile X-GPS.
* **Notifications In-App**: Alertes affichées dans l'interface web de Navixy.

Le texte de la notification permet d'identifier précisément l'alerte qui a été déclenchée. Le message de notification sera celui qui apparaîtra lorsque l'alerte sera déclenchée.

### Calendrier

Dans le cadre de la **Calendrier** vous pouvez définir quand vos règles de notification sont actives ou inactives. Cela permet de contrôler avec précision le moment où les alertes doivent être déclenchées, en fonction de vos besoins opérationnels spécifiques.

![](https://squaregps.atlassian.net/wiki/images/icons/grey_arrow_down.png)

Configuration de l'horaire

Voici comment vous pouvez configurer le calendrier :

* **Modèle**: Sélectionnez un modèle de programmation prédéfini, le cas échéant, pour appliquer rapidement des modèles de programmation courants, tels que les week-ends, les jours de la semaine et tous les jours.
* **Périodes actives**: Les blocs bleus représentent les moments où la règle est active et déclenche des notifications. Vous pouvez définir ces blocs pour des heures spécifiques de la journée et des jours de la semaine.
* **Périodes d'inactivité**: Les blocs gris indiquent les moments où la règle est inactive et ne déclenche pas de notifications. Cela permet d'éviter les alertes inutiles pendant les heures non opérationnelles.

Pour personnaliser le calendrier, il suffit de cliquer sur les blocs horaires souhaités pour passer de l'état actif à l'état inactif. Cette flexibilité garantit que vous ne recevrez des notifications qu'aux moments opportuns, ce qui réduit le risque de lassitude à l'égard des alertes et améliore l'efficacité de vos efforts de surveillance.

![image-20240805-221914.png](../../guide-de-litilizateur/regles-et-notifications/attachments/image-20240805-221914.png)

## Consulter l'historique des notifications

L'historique des notifications peut être consulté sur différentes plateformes, ce qui permet aux utilisateurs de revoir les événements et les alertes passés.

* **Web app**: Accédez à l'historique des notifications via la section "Événements" de l'interface web de Navixy. Filtrez par date, type d'événement et autres critères.
* **Application mobile**: Voir les notifications récentes et l'historique dans l'application mobile Navixy.
* **Rapports**: Générer des rapports détaillés sur les événements passés et les notifications à des fins d'analyse et d'archivage.

## Suspendre et reprendre les règles

Les utilisateurs peuvent suspendre temporairement les règles et les reprendre si nécessaire. Cette fonction est utile pendant les périodes où les actions des règles ne sont pas nécessaires, par exemple en cas de maintenance ou d'inactivité saisonnière.

![](https://squaregps.atlassian.net/wiki/images/icons/grey_arrow_down.png)

Comment suspendre une règle existante

1. **Naviguer vers les alertes**: Aller à la page **Alertes** dans le menu principal.
2. **Sélectionner la règle**: Recherchez la règle que vous souhaitez suspendre dans la liste des règles d'alerte.
3. **Suspendre la règle**: Cliquez sur l'icône de pause à côté du nom de la règle pour la suspendre.

Pour reprendre la règle, il suffit de cliquer sur l'icône de lecture de la règle. Cela réactivera les actions de la règle.

## Exemples

Voici quelques exemples de la manière dont les notifications d'événements peuvent être utilisées dans divers scénarios :

### Alertes de géofence

Les alertes de géofence sont une fonction puissante de Navixy qui aide les utilisateurs à surveiller les mouvements de leurs véhicules et de leurs biens à l'intérieur de limites géographiques prédéfinies, connues sous le nom de géofences. Cette fonctionnalité est essentielle pour garantir l'efficacité opérationnelle, la sécurité et le respect des politiques de l'organisation.

![](https://squaregps.atlassian.net/wiki/images/icons/grey_arrow_down.png)

En savoir plus

**QU'EST-CE QU'UNE GÉOFENCE ?**

Une géofence est un périmètre virtuel défini sur une carte autour d'une zone géographique spécifique. Cette zone peut être de n'importe quelle forme et de n'importe quelle taille, comme un rayon circulaire autour d'un point ou un polygone plus complexe qui délimite une région spécifique.

**COMMENT FONCTIONNENT LES ALERTES DE GÉOFENCE ?**

Lorsqu'un véhicule ou un bien équipé d'un dispositif de suivi GPS franchit la limite d'une géofence, un événement est déclenché. Le système enregistre alors cet événement et envoie des notifications à l'utilisateur selon les paramètres prédéfinis.

**MISE EN PLACE D'ALERTES DE GÉOFENCE**

1. **Définir la zone de géofence**:

* **Géofence circulaire**: Définir un rayon autour d'un point central, tel qu'un entrepôt ou un bureau.
* **Géofence polygonale**: Dessinez une forme complexe sur la carte pour couvrir des zones telles que les chantiers de construction, les zones de livraison ou les quartiers d'une ville.
* **Route geofence :** Créez une géofence étroite et allongée qui suit un itinéraire ou un chemin spécifique, tel qu'une autoroute, une voie ferrée ou un pipeline, afin de surveiller les mouvements le long de cet itinéraire et de détecter les déviations.

2. **Configurer les conditions d'alerte**:

* **Alertes à la saisie**: Notifier l'entrée d'un véhicule ou d'un bien dans la géofence.
* **Alertes de sortie**: Notifier lorsqu'un véhicule ou un bien quitte le périmètre.

3. **Définir les préférences de notification**:

* Choisissez les canaux par lesquels les notifications seront envoyées, tels que les SMS, les courriels, les notifications push ou les alertes in-app.
* Personnalisez le contenu du message pour y inclure des détails pertinents tels que l'identification du véhicule, le lieu, l'heure de l'événement, etc.

**UTILISATIONS PRATIQUES DES ALERTES DE GEOFENCE**

* **Gestion du parc automobile**: S'assurer que les véhicules respectent les itinéraires prédéfinis et détecter les déplacements non autorisés ou les écarts par rapport aux itinéraires assignés.
* **Sécurité des actifs**: Surveillez l'emplacement des biens de valeur et recevez des alertes immédiates s'ils sont déplacés en dehors d'une zone sécurisée.
* **Gestion des employés**: Suivre les employés sur le terrain et s'assurer qu'ils se trouvent dans les zones de travail désignées pendant leurs quarts de travail.
* **Efficacité opérationnelle**: Optimiser la logistique en contrôlant les heures d'entrée et de sortie aux endroits clés tels que les entrepôts et les points de livraison.

**EXEMPLE DE SCÉNARIO**

Une société de livraison met en place une géofence autour de son entrepôt principal. Lorsqu'un camion de livraison pénètre dans cette géofence, une alerte d'entrée est déclenchée et le responsable de l'entrepôt en est informé par notification push. Ce dernier peut ainsi se préparer à décharger le camion. Si le camion quitte la géofence, une alerte de sortie est envoyée à l'équipe de sécurité, indiquant une utilisation non autorisée ou un vol potentiel.

En utilisant les alertes de géofence, les organisations peuvent renforcer leur contrôle opérationnel, améliorer la sécurité et assurer la conformité avec les réglementations internes et externes.

### Alertes antivol pour les voitures

Les alertes antivol sont une fonction essentielle de Navixy, conçue pour renforcer la sécurité des véhicules en détectant les mouvements non autorisés ou les manipulations. Cette fonctionnalité apporte une tranquillité d'esprit aux propriétaires de véhicules et aux gestionnaires de flottes en garantissant une action immédiate en cas d'activités suspectes.

![](https://squaregps.atlassian.net/wiki/images/icons/grey_arrow_down.png)

En savoir plus

**COMMENT FONCTIONNENT LES ALERTES ANTIVOL DANS LES VOITURES ?**

Les alertes antivol pour voitures sont déclenchées lorsque des conditions spécifiques indiquant une utilisation non autorisée ou une manipulation sont réunies. Ces conditions peuvent être personnalisées en fonction des exigences de l'utilisateur et des besoins de sécurité du véhicule.

**MISE EN PLACE D'ALERTES ANTIVOL POUR LES VOITURES**

1. **Définir les critères de mouvement non autorisé**:

* **Détection de l'allumage**: Surveille l'état de l'allumage du véhicule pour détecter si le véhicule est démarré.
* **Détection des mouvements**: Utilisez le suivi GPS pour identifier les déplacements inattendus d'un véhicule par rapport à son emplacement de stationnement.
* **Restrictions temporelles**: Définir des alertes pour les mouvements de véhicules en dehors des heures de travail ou en dehors des heures d'ouverture prévues.

2. **Détection de la falsification**:

* **Détecteurs pour portes et fenêtres**: Installez des capteurs pour détecter si les portes ou les fenêtres sont ouvertes de force ou sans autorisation.
* **Déconnexion de la batterie**: Définir des alertes pour les cas où la batterie du véhicule est déconnectée, ce qui est une méthode couramment utilisée par les voleurs pour désactiver les systèmes de suivi.
* **Interférence du signal GPS**: Surveille le brouillage ou l'interférence avec le signal GPS, ce qui indique une éventuelle falsification.

3. **Configurer les notifications d'alerte**:

* **Instant notifications**: Configurez des SMS, des courriels, des notifications push ou des alertes in-app pour qu'ils soient envoyés immédiatement lorsqu'une activité non autorisée est détectée.
* **Destinataires de l'alerte**: Désigner des personnes ou des équipes spécifiques (par exemple, le personnel de sécurité, les gestionnaires de flotte) pour recevoir ces alertes.
* **Personnalisation du contenu des alertes**: Inclure des détails essentiels dans la notification, tels que l'emplacement actuel du véhicule, l'heure de l'événement et le type d'activité non autorisée détectée.

**UTILISATIONS PRATIQUES DES ALERTES ANTIVOL POUR LES VOITURES**

* **Sécurité des véhicules privés**: Les propriétaires de véhicules privés peuvent utiliser les alertes antivol pour protéger leur voiture contre le vol ou l'utilisation non autorisée, en particulier dans les zones à haut risque.
* **Gestion du parc automobile**: Les gestionnaires de flotte peuvent assurer la sécurité de leurs véhicules, en empêchant l'utilisation non autorisée par les employés ou le vol dans les parkings et les dépôts.
* **Services de location**: Les sociétés de location de voitures peuvent surveiller leurs véhicules afin de détecter les mouvements non autorisés ou les manipulations et d'y réagir, protégeant ainsi leurs actifs.
* **Logistique et livraison**: Les entreprises de logistique et de livraison peuvent protéger leurs véhicules et les marchandises de valeur qu'ils transportent contre le vol ou l'accès non autorisé.

**EXEMPLE DE SCÉNARIO**

Une entreprise de logistique a mis en place des alertes de sécurité spécifiques pour ses camions de livraison. Un soir, après les heures de bureau, le système détecte que le contact de l'un des camions a été mis. Une alerte instantanée est envoyée au gestionnaire de la flotte par notification push, SMS et courriel, indiquant que le contact a été mis sans autorisation.

Simultanément, le suivi GPS montre que le camion s'éloigne de son emplacement de stationnement. Le gestionnaire de flotte contacte immédiatement les autorités locales et leur communique la localisation en temps réel du camion. Grâce à cette alerte rapide, les autorités interceptent le véhicule, empêchant ainsi le vol et sécurisant les actifs de l'entreprise.

En utilisant les alertes antivol, les entreprises peuvent renforcer considérablement la sécurité de leurs véhicules, réagir rapidement en cas de vol potentiel et minimiser le risque de perte d'actifs.

### Alertes sur le contrôle de la température

Les alertes de contrôle de la température sont une fonction utile de Navixy, conçue pour garantir que les marchandises sensibles sont transportées dans des conditions optimales. Cette fonctionnalité est cruciale pour les industries telles que les produits pharmaceutiques, les aliments et les boissons, et d'autres secteurs où le maintien d'une plage de température spécifique est essentiel à la préservation de la qualité et de la sécurité des produits.

![](https://squaregps.atlassian.net/wiki/images/icons/grey_arrow_down.png)

En savoir plus

**COMMENT FONCTIONNENT LES ALERTES DE CONTRÔLE DE LA TEMPÉRATURE ?**

Les alertes de contrôle de la température surveillent la température des marchandises en temps réel à l'aide de capteurs installés dans le véhicule de transport. Lorsque la température dépasse ou tombe en dessous des limites prédéfinies, une alerte est déclenchée. Cela permet de prendre des mesures immédiates pour rectifier la situation et éviter d'endommager la cargaison.

**MISE EN PLACE D'ALERTES DE CONTRÔLE DE LA TEMPÉRATURE**

1. **Installer des capteurs de température**:

* **Placement du capteur**: Placer des capteurs de température à des endroits stratégiques de la zone de chargement pour assurer un contrôle précis et complet.
* **Étalonnage du capteur**: S'assurer que les capteurs sont calibrés correctement pour fournir des relevés de température précis.

2. **Définir les limites de température**:

* **Seuils supérieurs et inférieurs**: Définir les limites maximales et minimales de température en fonction des exigences de la cargaison spécifique.
* **Plages de température**: Définir les plages de température acceptables pour répondre aux différents types de cargaison dont les exigences peuvent varier.

3. **Configurer les conditions d'alerte**:

* **Contrôle en temps réel**: Surveille en permanence la température et déclenche des alertes si elle s'écarte des limites fixées.
* **Alertes basées sur la durée**: Définir des alertes à déclencher si la température reste en dehors de la plage acceptable pendant une durée spécifiée, ce qui indique un problème persistant.
* **Seuils multiples**: Définir plusieurs seuils pour différents niveaux d'alerte (par exemple, avertissement, critique) en fonction de la gravité de l'écart de température.

4. **Définir les préférences de notification**:

* **Canaux de notification**: Choisissez les canaux par lesquels les alertes seront envoyées, tels que les SMS, les courriels, les notifications push ou les alertes in-app.
* **Destinataires de l'alerte**: Préciser les personnes ou les équipes chargées de répondre aux alertes de température (par exemple, contrôle de la qualité, responsables de la logistique).
* **Personnalisation du contenu des alertes**: Inclure des détails essentiels dans les notifications, tels que l'étiquette de l'objet, la température actuelle, l'emplacement, l'heure de l'alerte et les actions recommandées.

**UTILISATION PRATIQUE DES ALERTES DE CONTRÔLE DE LA TEMPÉRATURE**

* **Industrie pharmaceutique**: Veiller à ce que les vaccins, les médicaments et les autres produits pharmaceutiques sensibles à la température soient transportés dans la plage de température requise pour préserver leur efficacité et leur sécurité.
* **Industrie alimentaire et des boissons**: Prévenir la détérioration et garantir la sécurité alimentaire en maintenant la température correcte pour les denrées périssables telles que les produits laitiers, la viande et les fruits et légumes pendant le transport.
* **Industrie chimique**: Protéger les produits chimiques sensibles à la température contre la dégradation ou les réactions dangereuses en surveillant et en contrôlant les conditions de transport.
* **Logistique de la chaîne du froid**: Optimiser le processus de la chaîne du froid en veillant à ce que tous les maillons de la chaîne d'approvisionnement maintiennent les conditions de température requises, de la production à la livraison.

**EXEMPLE DE SCÉNARIO**

Une société pharmaceutique utilise les alertes de contrôle de température de Navixy pour surveiller le transport de vaccins. Ces vaccins doivent être conservés entre 2°C et 8°C pour rester efficaces. L'entreprise installe des capteurs de température dans ses camions frigorifiques et règle les seuils de température inférieurs et supérieurs en conséquence.

Au cours d'une livraison, l'un des camions rencontre un dysfonctionnement dans son unité de réfrigération, entraînant une hausse de la température au-delà de la limite de 8°C. Le système déclenche immédiatement une alerte, envoyant des notifications à l'équipe de contrôle de la qualité par SMS, courriel et notifications push.

La notification comprend des détails tels que la température actuelle (10°C), la localisation du camion et l'heure de l'alerte. L'équipe chargée du contrôle de la qualité contacte le conducteur et lui demande de prendre des mesures correctives, par exemple de s'arrêter dans l'installation la plus proche proposant des services de réparation des systèmes de réfrigération.

En outre, l'équipe met en place un autre véhicule pour poursuivre la livraison, en veillant à ce que les vaccins restent dans la plage de température de sécurité. Cette réaction rapide permet d'éviter une éventuelle détérioration des vaccins, ce qui évite à l'entreprise une perte financière importante et préserve l'intégrité de ses produits.

En utilisant les alertes de contrôle de la température, les organisations peuvent garantir un transport sûr et efficace des marchandises sensibles, minimiser le risque de détérioration ou de dommage et se conformer aux réglementations sectorielles.

### Alertes pour la prévention du vol de carburant

Les alertes de prévention de vol de carburant sont une fonctionnalité essentielle de Navixy, conçue pour protéger les véhicules contre le siphonnage de carburant non autorisé et pour garantir une utilisation efficace du carburant. Cette fonctionnalité aide les gestionnaires de flotte et les propriétaires de véhicules à surveiller les niveaux de carburant en temps réel et à recevoir des alertes immédiates en cas de baisse suspecte des niveaux de carburant, ce qui permet d'intervenir rapidement et d'atténuer les pertes.

![](https://squaregps.atlassian.net/wiki/images/icons/grey_arrow_down.png)

Alertes pour la prévention du vol de carburant

**COMMENT FONCTIONNENT LES ALERTES DE PRÉVENTION DES VOLS DE CARBURANT**

Les alertes de prévention de vol de carburant sont déclenchées lorsque le niveau de carburant dans le réservoir d'un véhicule baisse de manière inattendue, indiquant un éventuel vol ou une utilisation non autorisée. Le système utilise les données des capteurs de niveau de carburant installés dans le véhicule pour surveiller et analyser en permanence les niveaux de carburant.

**LA MISE EN PLACE D'ALERTES POUR LA PRÉVENTION DU VOL DE CARBURANT**

1. **Installer les capteurs de niveau de carburant**:

* **Placement du capteur**: Installer des capteurs dans le réservoir de carburant afin d'obtenir une lecture précise du niveau de carburant.
* **Étalonnage du capteur**: Veillez à ce que les capteurs soient correctement calibrés pour refléter des niveaux de carburant précis, en tenant compte de la forme et de la taille du réservoir.

2. **Définir les conditions d'alerte**:

* **Baisses inattendues**: Définir des conditions pour détecter les baisses significatives du niveau de carburant qui se produisent en dehors des schémas d'utilisation normaux, par exemple lorsque le véhicule est garé ou n'est pas utilisé.
* **Limites de seuil**: Établir des seuils spécifiques pour les baisses de carburant (par exemple, plus de 10 litres sur une courte période) afin de déclencher des alertes.
* **Alertes temporelles**: Configurez les alertes pour qu'elles soient plus sensibles pendant les périodes où le véhicule ne devrait pas être utilisé, par exemple en dehors des heures de bureau ou pendant les week-ends.

3. **Configurer les paramètres de notification**:

* **Canaux de notification**: Choisissez les canaux de réception des alertes, tels que les SMS, les courriels, les notifications push ou les alertes in-app.
* **Destinataires de l'alerte**: Désigner des personnes ou des équipes (gestionnaires de flotte, personnel de sécurité, etc.) chargées de répondre aux alertes de vol de carburant.
* **Personnalisation des alertes**: Inclure des informations détaillées dans les alertes, telles que l'identification du véhicule, la localisation actuelle, l'heure de la chute de carburant et la quantité de carburant perdue.

**UTILISATIONS PRATIQUES DES ALERTES DE PRÉVENTION DES VOLS DE CARBURANT**

* **Gestion du parc automobile**: Protéger les véhicules de la flotte contre le vol de carburant, réduire les coûts d'exploitation et garantir l'exactitude des relevés de consommation de carburant.
* **Équipement fixe :** Protéger les équipements stationnaires tels que les générateurs électriques diesel contre le siphonnage de carburant non autorisé, en assurant un fonctionnement régulier et en évitant les pertes de carburant coûteuses.

**EXEMPLE DE SCÉNARIO**

Une entreprise de logistique utilise les alertes de prévention de vol de carburant de Navixy pour surveiller ses camions de livraison. Elle a installé des capteurs de niveau de carburant dans tous ses véhicules et configuré le système pour qu'il détecte les baisses inattendues de niveau de carburant, en particulier en dehors des heures de travail.

Un soir, alors que toutes les livraisons sont terminées et que les camions sont garés au dépôt de l'entreprise, le système détecte une baisse soudaine de 15 litres du niveau de carburant de l'un des camions. Cette baisse inattendue déclenche une alerte immédiate, envoyant des notifications au gestionnaire de la flotte par SMS, courriel et notifications push.

L'alerte comprend l'identification du camion, sa localisation dans le dépôt, l'heure de la chute de carburant et la quantité de carburant perdue. Le gestionnaire du parc automobile contacte rapidement l'équipe de sécurité du site pour enquêter sur la situation. L'équipe de sécurité trouve des preuves de la manipulation du réservoir de carburant et parvient à appréhender le suspect, ce qui permet d'éviter d'autres vols de carburant.

En utilisant les alertes de prévention du vol de carburant, l'entreprise de logistique peut surveiller et protéger efficacement ses actifs en carburant, en réduisant les pertes dues au vol et en assurant une gestion efficace du carburant. Cette approche proactive permet non seulement de réduire les coûts, mais aussi de préserver l'intégrité des opérations.

## Règles créées automatiquement

Lorsque vous [activer](../../guide-de-litilizateur/guide-de-lutilisateur/demarrage-rapide/activer-le-dispositif-gps.md) un nouvel appareil sur la plateforme Navixy, le système crée automatiquement des règles basées sur les capacités de l'appareil, telles que la règle "Appuyer sur le bouton SOS" pour un traceur GPS personnel doté d'un bouton d'urgence. Cette automatisation vous permet de gagner du temps en configurant les fonctions de surveillance essentielles dès le départ, ce qui garantit que votre appareil est prêt à être utilisé immédiatement.

Ces règles préconfigurées sont entièrement personnalisables : vous pouvez facilement ajouter des notifications, ajuster les paramètres ou suspendre une règle si elle n'est pas nécessaire. Cette approche rationalisée améliore la sécurité et l'expérience des utilisateurs, vous permettant de vous concentrer sur ce qui compte le plus sans les tracas d'une configuration manuelle.

## Personnalisation des notifications dans le navigateur

Vous pouvez personnaliser les notifications d'événements dans le navigateur en cliquant sur l'icône de l'engrenage dans la liste des événements. Pour accéder aux paramètres de notification et les personnaliser, cliquez sur "Alertes" dans le menu de gauche pour ouvrir Notifications, puis cliquez sur l'icône en forme de roue dentée.

![image-20240814-041437.png](../../guide-de-litilizateur/regles-et-notifications/attachments/image-20240814-041437.png)

* **Notifications du navigateur :** Activez cette option pour recevoir des alertes d'événements directement dans le centre de notification de votre système d'exploitation (par exemple, le Centre d'action Windows). Votre navigateur vous demandera d'autoriser ces notifications.
* **Afficher les notifications :** Les nouveaux événements apparaîtront sous forme de notifications contextuelles dans le coin supérieur droit de la page de la plateforme de surveillance.
* **Notification audio :** Chaque nouvel événement déclenche une alerte sonore dans le navigateur.
* **Volume :** Réglez le volume des notifications sonores de votre navigateur en fonction de vos préférences.
