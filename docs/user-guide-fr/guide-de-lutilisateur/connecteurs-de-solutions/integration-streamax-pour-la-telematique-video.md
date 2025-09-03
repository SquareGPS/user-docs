# Streamax

Streamax est un fabricant leader de MDVR, bien établi sur le marché mondial. Avec leurs appareils, vous pouvez activer l'enregistrement vidéo 24h/24 et 7j/7 depuis vos véhicules, collecter des données télématiques, accéder à distance aux séquences vidéo et surveiller la sécurité de conduite en utilisant les technologies ADAS (Systèmes d'Assistance Avancée au Conducteur) et DSM (Surveillance de l'État du Conducteur).

En intégrant Streamax avec Navixy, vous obtenez une surveillance vidéo complète combinée à une gestion de flotte avancée dans une interface unique. Examinons de plus près comment mettre en œuvre cette combinaison puissante et intégrer le tableau de bord Streamax dans l'interface Navixy.

## 1. Établissement de l'intégration

Pour établir l'intégration, vous devrez obtenir les identifiants API de votre compte Streamax et demander la configuration de l'intégration à notre équipe de support.

### Obtenir les identifiants API de Streamax

1. **Obtenez la clé API et le secret** : Suivez le processus d'authentification tel que décrit dans la [documentation d'authentification de signature Streamax](https://ftcloud.streamax.com:20002/DOC/Sign%20Authentication) pour obtenir votre clé API et votre secret.
2. **Contactez Navixy** : Une fois que vous avez vos identifiants API, contactez votre Responsable de Réussite Client ou utilisez [ce formulaire](https://www.navixy.com/contact/). Envoyez une demande pour intégrer Streamax avec votre compte Navixy, contenant les informations suivantes :

* Votre clé API
* Votre secret API
* Les détails de votre compte Navixy
* Demande d'activation de l'intégration Streamax

3. **Attendez la confirmation** : Nos spécialistes configureront l'intégration en 1 à 3 jours de notre côté et confirmeront quand elle sera prête à être utilisée.

> \[!TIP] Après avoir reçu la confirmation de notre support, votre compte Streamax est prêt pour l'intégration !

## 2. Ajout d'un appareil Streamax à Navixy

Après avoir reçu la confirmation de notre équipe de support que l'intégration est prête, vous pouvez ajouter votre appareil Streamax à la plateforme. Pour ce faire, suivez la procédure habituelle d'activation d'appareil :

1. Allez à **Activation d'appareil**.
2. Sélectionnez votre appareil Streamax dans la liste.
3. Sélectionnez l'option **Carte SIM achetée séparément** et passez à l'étape suivante.
4. Saisissez un **ID d'appareil** correct (IMEI de l'appareil)
5. Complétez la configuration de l'appareil

Pour des instructions détaillées sur comment activer un appareil dans Navixy, consultez [Activer le dispositif GPS](https://squaregps.atlassian.net/wiki/spaces/UDOCFR/pages/3027435597/Activer+le+dispositif+GPS?atlOrigin=eyJpIjoiZDQxMzQ3MjhiN2JkNDg1YzljNzUzYjA4NjNiMzc5MzEiLCJwIjoiYyJ9).

> \[!TIP] Votre appareil et votre compte Navixy sont prêts pour l'intégration !

## 3. Intégration de Streamax dans l'interface utilisateur Navixy

À cette étape, nous effectuons l'intégration réelle en intégrant le tableau de bord Streamax dans votre interface Navixy.\
Navixy offre une fonctionnalité [Applications utilisateur](https://squaregps.atlassian.net/wiki/spaces/UDOCFR/pages/3027436264/Applications+utilisateur?atlOrigin=eyJpIjoiOTI2NjAzNzgzYWYxNGUwM2IzNmFhOTY3YzkwOWQxNGMiLCJwIjoiYyJ9) qui permet d'intégrer des applications tierces directement dans l'interface de la plateforme. Nous l'utiliserons pour intégrer Mettax.

> \[!NOTE] **Navigation** La section **Applications utilisateur** est accessible aux **Propriétaires** de compte dans la section **Paramètres du compte**. Pour la trouver :
>
> 1. Cliquez sur l'icône de profil dans le coin supérieur gauche de l'écran pour ouvrir les paramètres de votre compte
> 2. Dans la barre latérale des paramètres, sélectionnez **Applications utilisateur**

1. Créez une nouvelle application\
   Commencez par cliquer sur le bouton ![image-20250725-080704.png](../../guide-de-litilizateur/connecteurs-de-solutions/attachments/image-20250725-080704.png) dans la liste **Applications utilisateur**.
2. Configurez la nouvelle application
3. Mettez le lien vers votre compte Streamax dans le champ **URL de l'application**, par exemple : `https://{votre_instance}.ifleetvision.com/ftv/ft/dashboard#`.
4. Saisissez un **Libellé** pour l'application (par exemple, Tableau de bord Streamax).
5. Sélectionnez **Intégré** dans le champ **Afficher comme** pour afficher la fonctionnalité Streamax dans Navixy.
6. Cliquez sur **Enregistrer** pour terminer la configuration.

> \[!TIP] Votre nouvelle application apparaît automatiquement dans la barre latérale gauche de Navixy. Ouvrez-la et connectez-vous avec vos identifiants Streamax pour accéder à votre tableau de bord télématique vidéo complet avec surveillance à 360°, détection d'événements alimentée par IA et flux vidéo multi-canaux - le tout intégré avec vos outils de gestion de flotte Navixy existants. ![ad2ef31528184f07816d99b67b1e4374.png](../../guide-de-litilizateur/connecteurs-de-solutions/attachments/ad2ef31528184f07816d99b67b1e4374.png)
