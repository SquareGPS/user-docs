# Dépannage de l'activation du dispositif GPS

L'activation des dispositifs de localisation GPS sur la plateforme Navixy est généralement simple grâce à [activation automatique du dispositif](../../guide-de-lutilisateur/demarrage-rapide/activer-le-dispositif-gps.md). Toutefois, si vous rencontrez des problèmes, ce guide vous aidera à dépanner et à résoudre les problèmes courants d'activation de l'appareil.

### **Les paramètres du fuseau horaire de l'appareil diffèrent de UTC+0h**

Veillez à ce que les dispositifs de suivi GPS soient réglés sur UTC+0h pour éviter que le serveur Navixy n'interprète mal les données. Reconfigurez tous les dispositifs réglés manuellement ou précédemment connectés à UTC+0h avant l'activation sur Navixy.

![](https://squaregps.atlassian.net/wiki/images/icons/grey_arrow_down.png)

En savoir plus

**Enjeu :**\
Lorsque le logiciel serveur Navixy reçoit des données d'un dispositif de suivi GPS, ces données sont accompagnées d'un horodatage. Le serveur traite ces données en fonction des préférences de l'utilisateur en matière de fuseau horaire, ce qui garantit l'exactitude des détails de la trace et des rapports sur différents fuseaux horaires. Toutefois, le serveur s'attend à ce que toutes les données relatives aux appareils soient exprimées en UTC+0h. Les appareils configurés manuellement ou les appareils précédemment connectés à une autre plateforme peuvent avoir un fuseau horaire différent, ce qui entraîne une mauvaise interprétation de l'horodatage par Navixy, et peut marquer les données comme étant obsolètes ou défectueuses.

**Solution :**\
Pour un traitement et un affichage précis des données, tous les dispositifs de suivi GPS doivent être configurés sur UTC+0h. Si l'appareil n'est pas configuré sur UTC+0h, le serveur Navixy peut interpréter les données de manière incorrecte, ce qui affecte la fiabilité des détails de la trace et des rapports.

**Recommandations pour le dépannage :**

1. Assurez-vous que l'appareil est réglé sur UTC+0h avant de l'activer sur Navixy.
2. Évitez de régler le fuseau horaire local sur l'appareil.

### L'appareil est éteint ou n'a pas de connexion GSM

Assurez-vous que l'appareil est allumé et connecté au réseau GSM. Pour ce faire, vérifiez l'état de l'alimentation de l'appareil et vérifiez qu'il est enregistré sur le réseau GSM. Si possible, envoyez un SMS test pour confirmer que l'appareil reçoit correctement les messages.

![](https://squaregps.atlassian.net/wiki/images/icons/grey_arrow_down.png)

En savoir plus

**Enjeu :**

Lorsque le serveur Navixy tente de communiquer avec un dispositif de suivi GPS, celui-ci doit être allumé et connecté au réseau GSM. Si l'appareil est éteint ou n'est pas connecté au réseau GSM, les commandes d'activation ne peuvent pas être transmises, ce qui fait que l'appareil semble hors ligne ou ne répond pas.

**Solution :**

Pour assurer une communication correcte entre le serveur Navixy et le dispositif de suivi GPS, vérifiez que le dispositif est sous tension et qu'il dispose d'une connexion GSM stable. Cela permet au serveur de recevoir et de traiter correctement les données.

**Recommandations pour le dépannage :**

* Si vous avez un accès physique à l'appareil, vérifiez ses indicateurs LED pour confirmer qu'il est allumé et connecté au réseau GSM.
* Envoyer un SMS à l'appareil avec confirmation de livraison pour vérifier l'enregistrement sur le réseau GSM. Si l'envoi du SMS échoue, l'appareil n'est pas enregistré sur le réseau GSM. Il se peut que vous deviez envoyer un SMS à l'appareil via le portail SIM pour vérifier.

### Le solde de la carte SIM est faible ou il n'y a pas de service Internet

Assurez-vous que le solde de la carte SIM est suffisant et que le service internet est activé pour que l'appareil puisse se connecter à la plateforme. Vérifiez le solde de la carte SIM et assurez-vous qu'il est suffisant pour permettre l'utilisation des données Internet. En outre, confirmez que le plan de données de la carte SIM comprend un trafic Internet suffisant pour maintenir une connexion stable avec la plate-forme.

![](https://squaregps.atlassian.net/wiki/images/icons/grey_arrow_down.png)

En savoir plus

**Enjeu :**\
Au cours du processus d'activation de l'appareil, un dispositif de localisation tente de se connecter à la plateforme Navixy et de transmettre ses données de localisation sur Internet. Si le solde de la carte SIM du dispositif est insuffisant ou si les limites du trafic Internet sont dépassées, le dispositif ne peut pas se connecter à la plateforme. Les données de localisation et d'autres informations essentielles ne peuvent alors pas être envoyées, ce qui rend le dispositif de repérage non fonctionnel.

**Solution :**\
Pour garantir une connectivité et une transmission de données ininterrompues, vérifiez que la carte SIM utilisée dans le dispositif de repérage dispose d'un solde et d'un trafic GPRS suffisants. Surveillez et rechargez régulièrement le solde de la carte SIM pour éviter les problèmes de connectivité.

**Recommandations pour le dépannage :**

* Vérifiez que le solde de la carte SIM est suffisant pour permettre l'accès à Internet. Vérifiez que le plan de la carte SIM comprend suffisamment de données Internet pour répondre aux besoins de communication de l'appareil.
* Assurez-vous que les paramètres APN sont correctement configurés sur votre appareil. Obtenez les paramètres APN corrects auprès de votre fournisseur de réseau cellulaire, qui comprennent généralement le nom APN, le nom d'utilisateur et le mot de passe. Vous trouverez généralement ces informations sur le site web de l'opérateur ou en contactant son service clientèle.
* Si les problèmes de connectivité persistent, contactez votre fournisseur de carte SIM pour confirmer qu'il n'y a pas de problèmes liés au réseau qui affectent le trafic Internet.

### IMEI ou numéro de téléphone saisi de manière incorrecte

Vérifiez l'exactitude de l'IMEI et du numéro de téléphone saisis lors de l'activation. Vérifiez chaque chiffre de l'IMEI et du numéro de téléphone par rapport à la documentation ou à l'étiquette de l'appareil pour vous assurer qu'il n'y a pas d'erreur. Corrigez toute anomalie afin d'éviter les problèmes d'activation et de garantir une communication réussie avec la plateforme.

![](https://squaregps.atlassian.net/wiki/images/icons/grey_arrow_down.png)

En savoir plus

**Enjeu :**

Lors de l'activation d'un appareil sur la plateforme Navixy, un numéro IMEI ou un numéro de téléphone incorrect peut faire échouer l'activation. Cette erreur est généralement due à une faute de frappe ou à une mauvaise saisie des données de l'appareil, ce qui entraîne l'échec de la communication entre l'appareil et le serveur.

**Solution :**

Pour garantir la réussite de l'activation, vérifiez à nouveau l'IMEI et le numéro de téléphone saisis pour l'appareil. Assurez-vous que tous les chiffres sont corrects et correspondent aux informations de l'appareil.

**Recommandations pour le dépannage :**

* Vérifiez l'IMEI et le numéro de téléphone en consultant la documentation ou l'étiquette de l'appareil.
* Si l'activation échoue, supprimez l'appareil et recommencez l'activation en saisissant à nouveau l'IMEI et le numéro de téléphone afin de corriger toute erreur éventuelle.

### La configuration est protégée par un mot de passe ou un numéro maître

Si l'appareil possède des paramètres personnalisés tels que des mots de passe ou des numéros de téléphone maîtres, il peut empêcher la configuration automatique par Navixy, ce qui entraîne des échecs d'activation. Supprimez tout mot de passe ou numéro maître personnalisé avant de tenter une activation automatique.

![](https://squaregps.atlassian.net/wiki/images/icons/grey_arrow_down.png)

En savoir plus

**Enjeu :**\
Lors de l'activation de l'appareil, la plateforme Navixy envoie des commandes SMS de configuration à l'appareil à partir du numéro de téléphone de service. Si l'appareil a été précédemment configuré pour recevoir des commandes de configuration à partir d'un numéro principal dédié ou si un mot de passe personnalisé a été défini, ces commandes peuvent échouer, entraînant une activation infructueuse.

**Solution :**\
Pour permettre l'activation automatique, supprimez tous les mots de passe personnalisés ou les numéros maîtres de l'appareil. Sinon, configurez manuellement l'appareil à l'aide des commandes d'activation appropriées.

**Recommandations pour le dépannage :**

* Supprimez tout mot de passe personnalisé ou numéro maître de l'appareil avant de procéder à l'activation automatique.
* Si l'activation automatique échoue, [configurer manuellement](https://squaregps.atlassian.net/wiki/spaces/USERDOCSOLD/pages/2909016770/Manual+device+activation) l'appareil à l'aide des commandes d'activation fournies.

### Dispositif non pris en charge ou modification du dispositif

Assurez-vous que votre appareil figure dans la liste des appareils suivants [soutenu par Navixy](https://navixy.com/devices/). Si vous n'êtes pas sûr du fabricant et/ou du modèle, veuillez consulter le fournisseur de votre appareil. Il est également recommandé de mettre à jour le micrologiciel de l'appareil.

![](https://squaregps.atlassian.net/wiki/images/icons/grey_arrow_down.png)

En savoir plus

**Enjeu :**\
Lors de l'activation d'un dispositif de localisation GPS sur la plateforme Navixy, il est important que le modèle du dispositif soit correctement identifié et indiqué lors de l'activation. Si l'appareil n'est pas correctement identifié, les données envoyées par l'appareil peuvent ne pas être analysées correctement ou être mal interprétées. En outre, la version du micrologiciel pour le même modèle peut être obsolète ou être une version personnalisée, ce qui entraîne des problèmes de compatibilité.

**Solution :**\
Pour résoudre ces problèmes, vérifiez que votre appareil figure sur la liste des appareils pris en charge et qu'il dispose de la dernière version du micrologiciel. Si votre appareil ne figure pas dans la liste des modèles pris en charge ou s'il est doté d'une version personnalisée du micrologiciel, veuillez contacter votre fournisseur de services pour obtenir de l'aide.

**Recommandations pour le dépannage :**

* Consultez la liste des appareils pris en charge.
* Mettre à jour le micrologiciel de l'appareil avec la dernière version.
* Si l'appareil n'est pas pris en charge ou utilise une version personnalisée du micrologiciel, veuillez contacter l'équipe d'assistance technique de votre fournisseur. [fournisseur de services.](../../guide-de-lutilisateur/demarrage-rapide/fournisseur-de-services.md)

### Teltonika et Ruptela, leaders dans le domaine de l'espace avec activation automatique

Veillez à configurer correctement les appareils Teltonika et Ruptela afin d'éviter les problèmes liés aux espaces en tête des commandes SMS. Configurer les appareils [manuellement](https://squaregps.atlassian.net/wiki/spaces/USERDOCSOLD/pages/2909016770/Manual+device+activation) ou vérifiez auprès de votre fournisseur de services s'il est possible d'utiliser une autre passerelle SMS optimisée pour les communications M2M.

![](https://squaregps.atlassian.net/wiki/images/icons/grey_arrow_down.png)

Click here to expand...

**Enjeu :**\
Lors de l'activation automatique des dispositifs Teltonika et Ruptela, les utilisateurs peuvent rencontrer des problèmes dus au fait que certaines passerelles SMS suppriment les espaces en tête. Ces dispositifs attendent qu'un utilisateur et un mot de passe précèdent la commande, comme par exemple `<login> <password> command`. Lorsque l'identifiant et le mot de passe ne sont pas définis (ce qui est recommandé), cela se traduit par des espaces doubles en début de ligne `command`. Certaines passerelles SMS, non optimisées pour la communication M2M, rognent ces espaces, ce qui fait que les commandes ne sont pas reconnues par les appareils.

**Solution :**\
Pour résoudre ce problème, vous pouvez soit contacter votre fournisseur de services pour remplacer la passerelle SMS, soit configurer manuellement ces appareils via le logiciel de configuration Teltonika ou Ruptela en utilisant l'adresse IP et le port du serveur Navixy.

**Recommandations pour le dépannage :**

* [Configurer manuellement les appareils](https://squaregps.atlassian.net/wiki/spaces/USERDOCSOLD/pages/2909016770/Manual+device+activation) à l'aide du logiciel de configuration.
* Contactez votre fournisseur de services pour utiliser une passerelle SMS optimisée pour la communication M2M qui préserve les espaces de premier plan.

### La carte SIM n'a pas de numéro de téléphone

[Processus d'activation automatique du dispositif](../../guide-de-lutilisateur/demarrage-rapide/activer-le-dispositif-gps.md) nécessite la saisie du numéro de téléphone d'une carte SIM, mais les cartes SIM pour les communications M2M peuvent ne pas en avoir. Dans ce cas, [configurer manuellement l'appareil](https://squaregps.atlassian.net/wiki/spaces/USERDOCSOLD/pages/2909016770/Manual+device+activation) et saisissez l'IMEI de l'appareil (ou un ensemble arbitraire de chiffres) comme numéro de téléphone dans la boîte de dialogue d'activation. Vous pouvez également contacter votre fournisseur de services pour demander l'intégration avec la plateforme MVNO afin de permettre la communication à l'aide de l'ICCID.

![](https://squaregps.atlassian.net/wiki/images/icons/grey_arrow_down.png)

En savoir plus

**Enjeu :**

Les cartes SIM M2M des fournisseurs MVNO ne sont souvent pas associées à un numéro de téléphone. Au lieu de cela, ces cartes SIM sont identifiées par d'autres identifiants, le plus souvent ICCID. Par conséquent, les commandes de configuration ne peuvent pas être envoyées via une passerelle SMS commune comme c'est le cas avec les cartes SIM normales. Cela pose des problèmes d'activation et de communication des appareils.

**Solution :**

Pour résoudre ce problème, vous avez deux possibilités : [configurer manuellement l'appareil](https://squaregps.atlassian.net/wiki/spaces/USERDOCSOLD/pages/2909016770/Manual+device+activation) et indiquer l'IMEI de l'appareil (ou toute autre série de chiffres arbitraire) comme numéro de téléphone dans la boîte de dialogue d'activation, ou contacter votre [fournisseur de services](../../guide-de-lutilisateur/demarrage-rapide/fournisseur-de-services.md) pour demander l'intégration avec la plateforme MVNO, permettant une communication bidirectionnelle par SMS en utilisant l'ICCID au lieu d'un numéro de téléphone.

**Recommandations pour le dépannage :**

* [Configurer manuellement l'appareil](https://squaregps.atlassian.net/wiki/spaces/USERDOCSOLD/pages/2909016770/Manual+device+activation) et saisissez l'IMEI de l'appareil comme numéro de téléphone dans la boîte de dialogue d'activation.
* [Contactez votre fournisseur de serveur](../../guide-de-lutilisateur/demarrage-rapide/fournisseur-de-services.md) pour demander l'intégration avec la plateforme MVNO afin de permettre la communication à l'aide de l'ICCID.

## Voir aussi

* [Guide d'activation du dispositif MQTT](https://squaregps.atlassian.net/wiki/spaces/SC/pages/2732589133/Activate+Your+MQTT+Device+on+Navixy)
