# Transmission des données

Le **Transmission des données** Le widget dans Navixy vous permet de transmettre des données de suivi GPS et télématiques de Navixy à d'autres serveurs et applications tierces à l'aide d'API et de services web.

## Qu'est-ce que le transfert de données ?

Le transfert de données (ou retransmission de données) est une fonction qui vous permet d'envoyer des données de suivi GPS et télématiques de Navixy vers d'autres serveurs ou applications tierces en temps réel. Les types de données qui peuvent être transmises sont les suivants :

* Données du véhicule
* GPS location
* Données des appareils IoT

La transmission des données peut se faire soit hors ligne, soit presque instantanément lorsque les données sont transmises.

### Principaux objectifs de la transmission de données

1. **Respect des réglementations gouvernementales :** Dans certains pays, les autorités exigent que les véhicules transmettent des données (telles que la localisation et la vitesse) en utilisant des protocoles spécifiques pour se conformer aux lois locales.
2. **Intégrations d'entreprises :** Les grandes entreprises, en particulier dans des secteurs comme le commerce de détail ou la logistique, demandent souvent à leurs fournisseurs d'envoyer des données GPS et télématiques à leurs systèmes afin de respecter leurs obligations contractuelles, par exemple pour assurer des livraisons dans les délais ou maintenir des conditions spécifiques (comme la température) pour les cargaisons.
3. **Consolidation des données :** L'intégration de divers composants au sein de systèmes logiciels complexes nécessite souvent une normalisation des données, en particulier lorsque ces composants sont fournis par plusieurs fournisseurs indépendants.

### Comment fonctionne le transfert de données

Les données collectées sur le véhicule sont envoyées dans un format de protocole spécifié à une adresse et à un port déterminés par l'utilisateur. Navixy propose différents protocoles de transmission de données qui peuvent être sélectionnés en fonction de vos besoins spécifiques dans l'interface utilisateur.

## Gestion de la transmission des données

Vous pouvez gérer le transfert de données via le widget correspondant dans la section "Appareils et paramètres".

Dans ce widget, vous pouvez

* Relier un ou plusieurs retranslateurs à un appareil.
* Spécifiez l'ID utilisé lors de l'envoi de données (par défaut, l'ID utilisé est le même que celui de l'appareil lui-même).
* Déconnecter les retraducteurs de l'appareil.
* Créez de nouveaux retranslateurs et modifiez les retranslateurs existants en cliquant sur le bouton "Protocoles".

### Gestion des retraducteurs

Lors de la gestion d'un retranslateur, vous pouvez configurer les paramètres suivants :

* **Nom :** Une étiquette pratique pour une identification facile.
* **Protocole de transfert de données :** Choisissez parmi les protocoles pris en charge.
* **Adresse et port du serveur de destination :** Indiquer où les données doivent être envoyées.
* **Login et mot de passe :** Pour l'autorisation sur le serveur de réception (si nécessaire).
* **Activité de retraduction :** Activez ou désactivez le retranslateur si nécessaire.

Vous pouvez créer plusieurs retraducteurs si votre plan d'abonnement le permet. Les profils des retraducteurs peuvent être modifiés, supprimés ou suspendus.

### Protocols

Voici quelques exemples de protocoles disponibles à des fins diverses :

#### Protocoles de conformité aux réglementations gouvernementales

<table><thead><tr><th width="184">Protocol</th><th>Description</th></tr></thead><tbody><tr><td><strong>Machines jaunes</strong> (🇨🇴)</td><td>Protocole basé sur SOAP obligatoire pour les machines jaunes, permettant d'envoyer des rapports aux serveurs de la police.</td></tr><tr><td><strong>Olympstroy</strong> (🇷🇺)</td><td>Protocole basé sur SOAP utilisé lors de la préparation des Jeux olympiques de 2014.</td></tr><tr><td><strong>OSINERGMIN</strong> (🇵🇪)</td><td>Protocole d'envoi d'informations télématiques au gouvernement péruvien pour la surveillance d'unités dans des industries telles que l'exploitation minière et le gaz.</td></tr><tr><td><strong>RNIS</strong> (🇷🇺)</td><td>Utilisé dans le système régional de navigation et d'information de Moscou pour le contrôle des mouvements de véhicules.</td></tr></tbody></table>

#### Conformité des entreprises

<table><thead><tr><th width="184">Protocol</th><th>Description</th></tr></thead><tbody><tr><td><strong>Altotrack Chep Mexique</strong></td><td>Transfère les positions des véhicules de la plate-forme Chep vers le HUB Altotrack.</td></tr><tr><td><strong>ArmCargo</strong></td><td>Envoie les données aux services de gestion des risques liés aux actifs pour l'évaluation des risques.</td></tr><tr><td><strong>Cargo en ligne</strong></td><td>Transmet les données au service CargoOnline.</td></tr><tr><td><a href="ilsp.md"><strong>ILSP</strong></a></td><td>Permet au logiciel de l'ILSP de partager des données sur les véhicules à travers les réseaux au Mexique.</td></tr><tr><td><strong>Trouvez-vous</strong></td><td>Transmet les données au projet logistique de Localizar-t, Forza.</td></tr><tr><td><strong>Solutions ReC</strong></td><td>Envoie des données aux serveurs de ReC Servicios Consultores.</td></tr><tr><td><a href="une-ressource-fiable.md"><strong>Recurso Confiable</strong></a></td><td>Utilisé pour la transmission de données avec le logiciel de Recurso Confiable dans diverses industries au Mexique et au-delà.</td></tr><tr><td><strong>SafetyNet pulsian</strong></td><td>Transmet les alarmes SOS à un serveur CAD SafetyNet pour l'assistance d'urgence.</td></tr><tr><td><a href="simpliroute.md"><strong>SimpliRoute</strong></a></td><td>Protocole de transmission des données de suivi des véhicules à SimpliRoute.</td></tr><tr><td><strong>TraceReports</strong></td><td>Envoie des données au système TraceReports.</td></tr><tr><td><a href="unigis.md"><strong>Unigis</strong></a></td><td>Permet le partage de données avec la plateforme TMS d'Unigis, souvent utilisée par les services logistiques.</td></tr><tr><td><strong>Wirtrack</strong></td><td>Transmet les données aux services Wirsolut.</td></tr></tbody></table>

#### Consolidation des données

<table><thead><tr><th width="184">Protocol</th><th>Description</th></tr></thead><tbody><tr><td><strong>Contrôle AVL</strong></td><td>Envoie des données aux serveurs AVL Control pour la gestion de la sécurité et les statistiques.</td></tr><tr><td><strong>Granit3</strong></td><td>Transmet les données aux serveurs de navigation de Santel.</td></tr><tr><td><strong>Startrack</strong></td><td>Protocole basé sur SOAP pour l'envoi de données au système logistique de Startrack.</td></tr><tr><td><strong>Lacak.io</strong></td><td>Protocole de transfert de données pour Lacak.io.</td></tr><tr><td><a href="navixy-ws.md"><strong>Navixy Web Service</strong></a></td><td>Protocole basé sur SOAP pour la transmission de données sur les flottes à des systèmes tiers.</td></tr><tr><td><strong>SA-RM</strong></td><td>Protocole général d'acheminement des données.</td></tr><tr><td><strong>Transnavigation</strong></td><td>Transmet les données aux serveurs de Transnavigation.</td></tr><tr><td><a href="wialon-ips.md"><strong>Wialon IPS</strong></a></td><td>Protocole public de Gurtam pour la retransmission des données des traceurs GPS et GLONASS.</td></tr><tr><td><strong>Wisetrack</strong></td><td>Transmet les données aux serveurs de Wisetrack.</td></tr></tbody></table>

Ces options fournissent un cadre solide pour le partage des données, vous aidant à répondre aux exigences réglementaires, à vous intégrer aux systèmes d'entreprise et à consolider les données pour une analyse complète.
