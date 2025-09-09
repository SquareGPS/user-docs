# Créer des liens géographiques

Pour créer un lien géographique, il suffit de cliquer sur le bouton "+", et la boîte de dialogue de création apparaît :

![](https://www.navixy.com/wp-content/uploads/2024/04/2.png)

La boîte de dialogue propose quelques options à configurer ou à remplir :

![](https://www.navixy.com/wp-content/uploads/2024/04/3.png)

{% stepper %}
{% step %}
### **Description (facultatif)**

Champ d'information qui sert à spécifier des informations personnalisées supplémentaires sur le lien. La longueur maximale est de 100 caractères.
{% endstep %}

{% step %}
### **Sélectionner des objets et des données**

La liste des objets disponibles par le lien. Chaque objet possède la liste suivante d'options à spécifier lors de l'ajout de l'objet :

_Objet_ - La balise à suivre.

_Étiquette_ - L'étiquette spécifique qui sera affichée dans l'interface de liaison géographique et qui remplacera l'étiquette actuellement définie dans l'armoire.

_Attributs_ - Les attributs du traceur à afficher dans l'interface de liaison géographique. Les attributs comprennent :

* Vitesse
* Adresse
* Statut du mouvement
* Nom du conducteur
* Numéro de téléphone
* Nom du véhicule
* Plaque d'immatriculation
* État de la connexion

Le bouton Copier permet d'appliquer la même liste d'attributs à tous les autres objets de la liaison géographique. Cette fonction peut faire gagner beaucoup de temps lors de la configuration d'attributs pour plusieurs objets.

![](https://www.navixy.com/wp-content/uploads/2024/04/4.png)
{% endstep %}

{% step %}
### **Paramètres de la carte**

_Fournisseur de cartes_ - Sélectionnez la carte que vous souhaitez que les utilisateurs finaux de votre lien géographique voient grâce au lien géographique généré. La liste des cartes est spécifiée par le fournisseur de services de la plateforme.

_Trace duration_ - La trace de suivi.

Voici à quoi pourrait ressembler une trace fixée pendant 5 minutes :

![](https://www.navixy.com/wp-content/uploads/2024/04/5.png)

_Échelles_ - Le zoom de la carte et l'ajustement automatique de la position sur le mouvement du traceur multiple.

_Géofence_ _paramètres_ - Il est possible de choisir d'afficher ou de masquer les emplacements des traqueurs en fonction de la position de la géofence. Par exemple, en sélectionnant l'option "Track outside geofence", les traceurs ne seront affichés sur la carte que lorsqu'ils se trouvent en dehors des géofences sélectionnées. Cette fonction peut être utile pour des scénarios tels que l'expédition ou la livraison, où l'utilisateur final ne doit pas voir le tracker chargé de marchandises avant le départ. En revanche, l'option "Suivre à l'intérieur des géofences" n'affichera les traceurs que lorsqu'ils se trouvent à l'intérieur des géofences sélectionnées.

![](https://www.navixy.com/wp-content/uploads/2024/04/7.png)
{% endstep %}

{% step %}
### Durée de validité limitée

Spécifiez la durée de vie du lien. Celle-ci peut être sélectionnée rapidement parmi des périodes prédéfinies ou fixée à une période de temps personnalisée. Si la durée de vie est définie pour commencer à un moment futur, le lien restera inactif jusqu'à ce que ce moment arrive. Ne sélectionnez pas l'option pour une configuration permanente de la liaison géographique.
{% endstep %}

{% step %}
### Avant-première

Vérifier à quoi ressemble la géolocalisation configurée à partir de l'interface web de la géolocalisation, du point de vue de l'utilisateur final. La fonction de prévisualisation permet de passer rapidement de l'interface utilisateur à l'interface de liaison géographique pour obtenir une représentation plus précise de la configuration de la liaison géographique.
{% endstep %}
{% endstepper %}

Après avoir appuyé sur le bouton "Créer", une fenêtre de dialogue apparaît avec le lien généré. Ce lien peut être copié et fourni aux utilisateurs finaux ou partagé via les boutons des réseaux sociaux :

![](https://www.navixy.com/wp-content/uploads/2024/04/9-1.png)
