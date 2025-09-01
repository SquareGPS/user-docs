# Activer le dispositif GPS

Activer un appareil signifie simplement ajouter un nouvel appareil à votre compte utilisateur. Vous pouvez activer n'importe quel [dispositif de localisation GPS pris en charge](https://navixy.com/devices/). Si votre modèle n'est pas encore pris en charge, veuillez contacter votre [fournisseur de services](prestataire-de-services.md) afin d'intégrer cet appareil à Navixy ou de trouver un autre appareil avec des fonctionnalités similaires. Nous vous suggérons également de contacter votre [fournisseur de services](prestataire-de-services.md) avant de poursuivre, car ils peuvent avoir leurs propres recommandations.

Il existe deux méthodes pour activer un dispositif de localisation GPS :

1. [**Activer automatiquement le dispositif GPS (recommandé)**](https://squaregps.atlassian.net/wiki/spaces/UDOCFR/pages/3027435597/Activer+le+dispositif+GPS#Activate-GPS-device-automatically) - simplifie l'installation de l'appareil en le configurant automatiquement sans aucune intervention manuelle. Cette méthode est recommandée dans la plupart des cas, sauf [Lorsque l'activation manuelle est nécessaire ou préférable](https://squaregps.atlassian.net/wiki/spaces/UDOCFR/pages/edit-v2/3027435597#When-manual-activation-is-required-or-preferred).
2. [**Activer manuellement le dispositif GPS**](https://squaregps.atlassian.net/wiki/spaces/UDOCFR/pages/edit-v2/3027435597#Activate-GPS-device-manually) - exige que vous entriez physiquement les paramètres de configuration dans l'appareil à l'aide de son configurateur, ou plus directement par SMS. Cette option est utile si la configuration automatique n'est pas possible en raison de contraintes techniques ou régionales spécifiques.

## Activation automatique de l'appareil GPS

Navixy offre l'avantage unique d'une activation entièrement automatique des appareils, ce qui, dans la plupart des cas, libère les utilisateurs de la nécessité de configurer manuellement leurs appareils. Le processus comprend l'envoi de commandes de configuration initiales à un appareil que vous connectez par message texte (SMS). Toutefois, si l'activation automatique ne convient pas dans votre cas, vous pouvez toujours [Configurer l'appareil manuellement](https://squaregps.atlassian.net/wiki/spaces/UDOCFR/pages/edit-v2/3027435597#Activate-GPS-device-manually).

### Étapes d'activation automatique

Une fois que vous vous êtes connecté à votre compte d'utilisateur, cliquez sur Activation de l'appareil dans le menu de gauche. L'assistant d'activation est alors lancé.

1. **Nom de l'objet :** Choisissez le nom que vous préférez (par exemple, "Véhicule ABC").
2. **Modèle et fabricant de l'appareil :** Recherchez et sélectionnez dans une liste triée par ordre alphabétique et regroupée par fabricants.
3. **Saisir le numéro de téléphone de la carte SIM :** Entrez le numéro de téléphone de la carte SIM installée dans l'appareil.
  1. La plateforme Navixy tentera de déterminer les paramètres APN appropriés en fonction du numéro de téléphone que vous avez fourni. Si les paramètres APN ne sont pas trouvés, vous devrez les saisir manuellement.
4. **Saisir l'ID d'usine/IMEI de l'appareil :**
  1. La longueur de cette valeur peut varier en fonction du modèle. Si vous avez des questions, veuillez consulter votre [fournisseur de services](prestataire-de-services.md).
5. **Code d'activation (facultatif) :**
  1. Si votre fournisseur de services l'exige, il peut être tenu de vous fournir un code d'activation avant que vous puissiez enregistrer un appareil.
6. **Activer :** Après avoir saisi les informations nécessaires, cliquez sur "Étape suivante". Des messages SMS contenant des commandes de configuration seront ensuite envoyés à l'appareil. Veuillez vous assurer que l'appareil est sous tension et capable de recevoir ces messages.

Dans un délai d'environ 15 minutes, l'appareil devrait être mis en ligne et prêt à l'emploi, en fonction des paramètres de rapport par défaut de l'appareil.

![](https://squaregps.atlassian.net/wiki/images/icons/grey_arrow_down.png)

Détails sur la configuration automatique

Grâce à l'activation automatique, la configuration de votre appareil est simple et conviviale, sans qu'il soit nécessaire d'utiliser des câbles USB, des pilotes ou des utilitaires de configuration. Le processus est rapide et permet à l'appareil d'être opérationnel en quelques minutes. Les paramètres de configuration, tels que les paramètres APN et les détails du serveur, sont envoyés automatiquement par SMS du serveur à l'appareil. Une fois connecté, l'appareil reçoit des mises à jour automatiques, telles que les paramètres du mode de suivi, principalement via le canal IP.

## Activer manuellement le dispositif GPS

Alors que Navixy offre [activation automatique de l'appareil GPS](https://squaregps.atlassian.net/wiki/spaces/UDOCFR/pages/edit-v2/3027435597#Activate-GPS-device-automatically) qui simplifie le processus de configuration, il est parfois nécessaire ou préférable de procéder à une configuration manuelle. Cette section décrit les étapes de la configuration manuelle des appareils et les cas d'utilisation particuliers pour lesquels cette méthode est préférable.

### Étapes de l'activation manuelle

Pour activer manuellement votre appareil, vous devez soit envoyer manuellement les commandes d'activation par SMS, soit vous connecter physiquement au configurateur de votre appareil avec votre PC. Les informations requises pour l'une ou l'autre option sont les suivantes :

1. **Informations d'identification APN** \- Vous pouvez obtenir ces informations auprès de votre fournisseur SIM. Les appareils requièrent généralement : le nom APN et/ou l'utilisateur APN, le mot de passe APN si nécessaire.
2. **Adresse du serveur** - Choisissez l'adresse du serveur en fonction de vos préférences en matière de résidence des données et/ou des recommandations de votre fournisseur de services :
  - Plate-forme de l'UE : `tracker.navixy.com` (recommandé) ou `52.57.1.136`
  - Plate-forme américaine : `tracker.us.navixy.com` (recommandé) ou `13.52.37.2`
3. **Port du serveur** - Ce paramètre dépend de la marque et du modèle de votre appareil et se trouve dans la section [Section des dispositifs](https://navixy.com/devices/) de notre site web. Par exemple, pour [Queclink GV65](https://www.navixy.com/devices/queclink/queclink-gv65/) le port du serveur serait 47764.

Veuillez mettre à jour ces champs dans le configurateur de votre appareil pour commencer à vous connecter à notre plateforme.

Pour l'activation par SMS, veuillez consulter le manuel de l'appareil ou l'équipe d'assistance pour connaître les commandes SMS utilisées pour activer votre appareil spécifique.

> [!INFO]
> Remarque : l'activation des SMS dépend fortement de la capacité de votre fournisseur de services SIM. D'après notre expérience, les commandes SMS provenant d'un téléphone classique ne parviennent pas à atteindre l'appareil. Dans ce cas, vous devez utiliser le portail de votre fournisseur SIM pour envoyer les messages.

### Lorsque l'activation manuelle est nécessaire ou préférable

![](https://squaregps.atlassian.net/wiki/images/icons/grey_arrow_down.png)

Appareils cellulaires présentant des problèmes de délivrabilité des SMS

Bien que Navixy et ses partenaires utilisent des passerelles SMS avec une grande capacité de livraison et une couverture mondiale, certains pays ont des réglementations locales et des problèmes techniques qui peuvent entraver la livraison des commandes M2M envoyées par SMS. Ces problèmes sont notamment les suivants

- **Réglementation anti-spam**: Restrictions locales sur les noms des expéditeurs de messages, la longueur du texte et les textes binaires.
- **Questions techniques**: Les symboles spéciaux tels que $, # et % qui sont utilisés dans les commandes de configuration peuvent ne pas passer avec succès par tous les nœuds du réseau dans la chaîne de transmission des SMS.

Si la configuration automatique échoue en raison de ces problèmes, vous pouvez configurer manuellement les paramètres de base, tels que les informations d'identification APN, l'adresse du serveur et le port. Le port du serveur et l'adresse IP pour un modèle d'appareil spécifique peuvent être trouvés dans la section Appareils de notre site web. Pour des instructions de configuration détaillées, veuillez vous référer au manuel de l'appareil ou consulter l'assistance technique de votre fournisseur d'accès Internet. [fournisseur de services](prestataire-de-services.md).

![](https://squaregps.atlassian.net/wiki/images/icons/grey_arrow_down.png)

Appareils connectés via le protocole MQTT

Les dispositifs MQTT, qui utilisent le modèle éditeur/abonné pour la communication, nécessitent un processus d'installation unique. Ces appareils doivent être configurés manuellement car ils ne suivent pas le modèle client-serveur traditionnel. Vous devez

1. Configurez l'appareil avec les paramètres appropriés du courtier MQTT.
2. Configurer manuellement les paramètres de connexion de l'appareil, tels que l'adresse et le port du courtier MQTT.
3. Veillez à ce que les rubriques et les informations d'identification correctes soient configurées.

Veuillez vous référer à la[Activez votre appareil MQTT sur Navixy](https://squaregps.atlassian.net/wiki/spaces/SC/pages/2732589133/Activate+Your+MQTT+Device+on+Navixy) section de notre [Centre d'expertise](https://squaregps.atlassian.net/wiki/spaces/SC) pour plus de détails.

![](https://squaregps.atlassian.net/wiki/images/icons/grey_arrow_down.png)

Appareils connectés via le réseau LoRa

Les réseaux LoRa (longue portée), qui sont couramment utilisés pour les applications IoT en raison de leur faible consommation et de leurs capacités de longue portée, nécessitent également une configuration manuelle. En effet, les réseaux LoRa fonctionnent différemment des réseaux cellulaires standard utilisant des passerelles LoRaWAN et ont des exigences spécifiques :

- Saisir manuellement les informations d'identification LoRaWAN de l'appareil
- Configurer l'adresse du serveur et les paramètres du réseau pour qu'ils correspondent aux spécifications du réseau LoRa.

Cette configuration est quelque peu unique pour chaque intégration. Par conséquent, veuillez consulter le support technique de votre [fournisseur de services](prestataire-de-services.md) sur la façon d'intégrer vos appareils LoRa et votre passerelle LoRaWAN avec Navixy.

![](https://squaregps.atlassian.net/wiki/images/icons/grey_arrow_down.png)

Appareils connectés via le réseau satellite

Les appareils utilisant des réseaux satellitaires tels qu'Iridium, Globalstar ou Starlink nécessitent une configuration manuelle en raison de la nature distincte de la communication par satellite, qui diffère considérablement des réseaux terrestres.

Les appareils qui utilisent une liaison satellite et la plate-forme Navixy communiquent par l'intermédiaire d'une passerelle fournie par l'opérateur satellite. Cette passerelle sert de pont entre le réseau satellitaire et l'internet, assurant ainsi une transmission de données sans faille.

Pour configurer un dispositif satellite afin qu'il soit surveillé sur Navixy, vous devez :

1. Orientez votre appareil vers le réseau satellite
2. Du côté du réseau satellitaire, il faut que le système pointe ses données vers la plate-forme Navixy.
3. Vérifiez que l'appareil est correctement enregistré et qu'il peut communiquer avec le réseau satellitaire.

Chaque intégration étant unique, veuillez consulter le support technique de votre fournisseur. [fournisseur de services](prestataire-de-services.md) pour obtenir des conseils sur l'intégration de vos appareils et de votre passerelle à Navixy.

![](https://squaregps.atlassian.net/wiki/images/icons/grey_arrow_down.png)

Appareils connectés via d'autres systèmes télématiques ou passerelles

Dans certains cas, les appareils sont déjà connectés à d'autres systèmes télématiques, tels que les plates-formes télématiques des équipementiers ou d'autres serveurs GPS, et vous avez besoin de les surveiller à la fois sur cette plate-forme et sur Navixy.

Pour surveiller des appareils qui font partie d'autres systèmes télématiques avec Navixy, vous devez.. :

- Configurer la transmission des données :  
Configurez l'autre plateforme pour qu'elle envoie des données à Navixy en utilisant l'un des protocoles pris en charge par Navixy.
- Ajouter un appareil virtuel :  
Créer un appareil virtuel sur la plateforme Navixy qui s'associe à la source de données à l'aide d'un identifiant d'appareil unique.

Pour plus de détails, veuillez lire comment [Intégrer les données IoT des serveurs et des passerelles](https://squaregps.atlassian.net/wiki/spaces/SC/pages/2732621933/Integrate+IoT+Data+from+Servers+and+Gateways).

## FAQ et dépannage

Si vous rencontrez des problèmes lors de l'activation de vos appareils, veuillez consulter notre site web. [F.A.Q. et guide de dépannage](../faq/depannage-de-lactivation-du-dispositif-gps.md) ou contacter votre [Prestataire de services](prestataire-de-services.md) pour obtenir de l'aide.