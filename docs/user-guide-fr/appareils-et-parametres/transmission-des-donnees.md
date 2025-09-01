# Transmission des données

Le **Transmission des données** Le widget dans Navixy vous permet de transmettre des données de suivi GPS et télématiques de Navixy à d'autres serveurs et applications tierces à l'aide d'API et de services web.

## Qu'est-ce que le transfert de données ?

Le transfert de données (ou retransmission de données) est une fonction qui vous permet d'envoyer des données de suivi GPS et télématiques de Navixy vers d'autres serveurs ou applications tierces en temps réel. Les types de données qui peuvent être transmises sont les suivants :

- Données du véhicule
- GPS location
- Données des appareils IoT

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

- Relier un ou plusieurs retranslateurs à un appareil.
- Spécifiez l'ID utilisé lors de l'envoi de données (par défaut, l'ID utilisé est le même que celui de l'appareil lui-même).
- Déconnecter les retraducteurs de l'appareil.
- Créez de nouveaux retranslateurs et modifiez les retranslateurs existants en cliquant sur le bouton "Protocoles".

### Gestion des retraducteurs

Lors de la gestion d'un retranslateur, vous pouvez configurer les paramètres suivants :

- **Nom :** Une étiquette pratique pour une identification facile.
- **Protocole de transfert de données :** Choisissez parmi les protocoles pris en charge.
- **Adresse et port du serveur de destination :** Indiquer où les données doivent être envoyées.
- **Login et mot de passe :** Pour l'autorisation sur le serveur de réception (si nécessaire).
- **Activité de retraduction :** Activez ou désactivez le retranslateur si nécessaire.

Vous pouvez créer plusieurs retraducteurs si votre plan d'abonnement le permet. Les profils des retraducteurs peuvent être modifiés, supprimés ou suspendus.

### Protocols

Voici quelques exemples de protocoles disponibles à des fins diverses :

#### Protocoles de conformité aux réglementations gouvernementales

| Protocol | Description |
| --- | --- |
| **Machines jaunes** (🇨🇴) | Protocole basé sur SOAP obligatoire pour les machines jaunes, permettant d'envoyer des rapports aux serveurs de la police. |
| **Olympstroy** (🇷🇺) | Protocole basé sur SOAP utilisé lors de la préparation des Jeux olympiques de 2014. |
| **OSINERGMIN** (🇵🇪) | Protocole d'envoi d'informations télématiques au gouvernement péruvien pour la surveillance d'unités dans des industries telles que l'exploitation minière et le gaz. |
| **RNIS** (🇷🇺) | Utilisé dans le système régional de navigation et d'information de Moscou pour le contrôle des mouvements de véhicules. |

#### Conformité des entreprises

| Protocol | Description |
| --- | --- |
| **Altotrack Chep Mexique** | Transfère les positions des véhicules de la plate-forme Chep vers le HUB Altotrack. |
| **ArmCargo** | Envoie les données aux services de gestion des risques liés aux actifs pour l'évaluation des risques. |
| **Cargo en ligne** | Transmet les données au service CargoOnline. |
| [**ILSP**](transmission-des-donnees/ilsp.md) | Permet au logiciel de l'ILSP de partager des données sur les véhicules à travers les réseaux au Mexique. |
| **Trouvez-vous** | Transmet les données au projet logistique de Localizar-t, Forza. |
| **Solutions ReC** | Envoie des données aux serveurs de ReC Servicios Consultores. |
| [**Une ressource fiable**](transmission-des-donnees/une-ressource-fiable.md) | Utilisé pour la transmission de données avec le logiciel de Recurso Confiable dans diverses industries au Mexique et au-delà. |
| **SafetyNet pulsian** | Transmet les alarmes SOS à un serveur CAD SafetyNet pour l'assistance d'urgence. |
| [**SimpliRoute**](transmission-des-donnees/simpliroute.md) | Protocole de transmission des données de suivi des véhicules à SimpliRoute. |
| **TraceReports** | Envoie des données au système TraceReports. |
| [**Unigis**](transmission-des-donnees/unigis.md) | Permet le partage de données avec la plateforme TMS d'Unigis, souvent utilisée par les services logistiques. |
| **Wirtrack** | Transmet les données aux services Wirsolut. |

#### Consolidation des données

| Protocol | Description |
| --- | --- |
| **Contrôle AVL** | Envoie des données aux serveurs AVL Control pour la gestion de la sécurité et les statistiques. |
| **Granit3** | Transmet les données aux serveurs de navigation de Santel. |
| **Startrack** | Protocole basé sur SOAP pour l'envoi de données au système logistique de Startrack. |
| **Lacak.io** | Protocole de transfert de données pour Lacak.io. |
| [**Navixy Web Service**](transmission-des-donnees/navixy-ws.md) | Protocole basé sur SOAP pour la transmission de données sur les flottes à des systèmes tiers. |
| **SA-RM** | Protocole général d'acheminement des données. |
| **Transnavigation** | Transmet les données aux serveurs de Transnavigation. |
| [**Wialon IPS**](transmission-des-donnees/wialon-ips.md) | Protocole public de Gurtam pour la retransmission des données des traceurs GPS et GLONASS. |
| **Wisetrack** | Transmet les données aux serveurs de Wisetrack. |

Ces options fournissent un cadre solide pour le partage des données, vous aidant à répondre aux exigences réglementaires, à vous intégrer aux systèmes d'entreprise et à consolider les données pour une analyse complète.