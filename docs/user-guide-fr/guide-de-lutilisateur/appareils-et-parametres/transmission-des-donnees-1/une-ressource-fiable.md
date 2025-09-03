# Une ressource fiable

# Recurso Confiable-GPS tracking/data forwarding pour les entreprises

Recurso Confiable est un logiciel de sécurité et de logistique qui surveille, donne de la visibilité et génère de la prévisibilité sur les opérations de transport. Navixy a créé le protocole de transfert de données de Recurso Confiable pour être utilisé par d'autres entreprises qui travaillent également avec Recurso Confiable dans de multiples secteurs au Mexique, en Colombie, aux États-Unis et en Amérique centrale.

*Catégorie de protocole : Protocole d'entreprise*

### Table des matières

1. [Qu'est-ce que Recurso Confiable ?](#what-is-rc)
2. [Informations techniques sur Recurso Confiable](#tech-info-rc)
3. [Recurso Confiable Configuration](#rc-config)
  1. [Mise en place](#setting-up)
  2. [Gestion](#managing)
  3. [Dépannage](#troubleshooting)

## Qu'est-ce que Recurso Confiable ?

Avec le protocole Recurso Confiable, les partenaires de l'entreprise peuvent transférer les données de suivi GPS de manière sûre et fiable en un seul endroit afin d'optimiser les processus de gestion de la flotte. Cela permet au client de travailler et de communiquer avec d'autres partenaires de Recurso Confiable.

Lors du développement de ce protocole, Navixy a pris en compte les besoins des grandes entreprises de logistique et de vente au détail. Les entreprises peuvent rationaliser les données et les fonctionnalités importantes de la plateforme de gestion de flotte et de suivi GPS, telles que les systèmes de contrôle, la planification des trajets, le suivi en temps réel, les rapports de modélisation prédictive, la mise en œuvre et la modification de la géofence, l'optimisation des itinéraires, et bien plus encore. Les entreprises qui étaient auparavant déconnectées les unes des autres sur le réseau de Recurso Confiable sont désormais en mesure de communiquer efficacement et rapidement.

## Recurso Confiable informations techniques générales

Le protocole Recurso Confiable utilise SOAP pour envoyer des données XML toutes les 5 minutes via HTTP à Recurso Confiable.

Données envoyées à Recurso Confiable :

- Code de l'événement AVL
- Plaque d'immatriculation
- ID de l'envoi
- Date
- Direction
- Latitude
- Longitude
- Altitude
- Vitesse
- Cours
- Allumage
- Compteur kilométrique
- Identifiant du client
- Nom du client
- ID de l'appareil

## Recurso Confiable Configuration

### Mise en place

Paramètres requis

- Recurso Confiable Login et mot de passe
- ID externe
- Adresse du serveur de destination
  - [http://gps.rcontrol.com.mx/Tracking/wcf/RCService.svc](http://gps.rcontrol.com.mx/Tracking/wcf/RCService.svc)
- Port du serveur de destination
  - 80

Pour configurer la transmission des données dans le protocole Recurso Confiable, ouvrez les paramètres de l'appareil à partir du menu principal en appuyant sur l'icône "Engrenage" en bas à gauche de l'écran.

Cliquez ensuite sur le widget "Transfert de données".

Cliquez sur "Protocoles".

Une fenêtre s'ouvre alors, dans laquelle vous pouvez saisir les paramètres requis en appuyant sur le bouton +.

Pour le protocole Recurso Confiable, saisissez les informations suivantes :

| Paramètre | Explication | --- | --- | Nom | Entrez un nom pour rendre ce retranslateur facilement identifiable | | Protocole et Login | Sélectionnez le protocole Recurso Confiable dans la liste déroulante;<br><br>Utiliser Recurso Confiable Login et Mot de passe | | Adresse et port du serveur de destination | Adresse : [http://gps.rcontrol.com.mx/Tracking/wcf/RCService.svc](http://gps.rcontrol.com.mx/Tracking/wcf/RCService.svc) | Port : 80 |

L'écran de gestion de la retraduction devrait ressembler à ce qui suit, avec le login et le mot de passe de Recurso Confiable. Assurez-vous que le bouton "Activé" est coché et cliquez sur le bouton "Enregistrer" pour terminer le processus.

![Recurso Confiable](https://www.navixy.com/wp-content/uploads/2022/10/pasted-image-0-1-1-600x120.png)

Ensuite, le retranslateur devra être lié à l'appareil du côté de Recurso Confiable. Pour ce faire, sélectionnez l'option "Link" ![link image](https://www.navixy.com/wp-content/uploads/2022/08/image-3.png)

dans le widget de transfert de données. Sélectionnez le retraducteur à connecter et cliquez sur "Lien" ci-dessous.

Ensuite, ajoutez les informations nécessaires à l'identification du dispositif sur Recurso Confiable dans le champ ID externe, soit en cliquant sur l'icône crayon, soit en cliquant sur le champ ID externe lui-même. Cette valeur devrait inclure les éléments suivants du côté de Recurso Confiable, où seule la plaque d'immatriculation est obligatoire :

Plaque d'immatriculation

ID de l'itinéraire

Numéro d'identification de l'entreprise

Nom de l'entreprise

Le format du champ ID externe sera séparé par un trait de plume. Par exemple :

ABC123|1|123|John

Si seule la plaque d'immatriculation est disponible, l'identifiant externe peut être saisi seul :

ABC123

Si d'autres informations sont manquantes, veillez à inclure les tuyaux, par exemple :

ABC123||123|

Sélectionnez "Enregistrer" une fois que vous avez terminé.

### Gestion

Pour modifier ou arrêter la transmission des données, veuillez suivre les étapes suivantes :

Sélectionnez l'icône "Crayon" ou cliquez dans la case associée pour modifier l'identifiant externe utilisé pour pointer vers l'appareil sur le système tiers.

Pour arrêter le transfert de données, cliquez sur le bouton "Corbeille".

Ensuite, accusez réception de la modification sur la fenêtre contextuelle.

Pour modifier les paramètres du retranslateur, tels que le nom, les informations de connexion ou l'activation, cliquez sur "Gestion des retranslateurs".

La fenêtre de gestion du retranslateur s'ouvre alors. Sélectionnez la ligne à modifier et cliquez sur le crayon en haut à gauche, ou double-cliquez sur la ligne en question pour autoriser la modification. Enregistrez les modifications.

![Recurso Confiable](https://www.navixy.com/wp-content/uploads/2022/10/pasted-image-0-3-600x107.png)

### Dépannage

Si les données ne s'affichent pas sur le système tiers de Recurso Confiable, veuillez vérifier :

- Le nom d'utilisateur et le mot de passe pour Recurso Confiable sont correctement saisis
- L'URL a été saisie correctement
- Retranslator est activé
- L'identifiant externe correspond à l'information Recurso Confiable correspondante