# Capteurs pour véhicules

Les **Capteurs et boutons** widget dans Navixy vous permet de gérer et de configurer divers capteurs connectés à vos appareils GPS depuis la plateforme. Cette fonction est essentielle pour surveiller divers paramètres du véhicule, tels que les niveaux de carburant, la température et les diagnostics du moteur, directement à partir de la plateforme.

## Vue d'ensemble

Le **Capteurs et boutons** se trouve dans la section **Appareils et paramètres** à laquelle vous pouvez accéder en cliquant sur l'élément correspondant dans le menu principal de l'interface web.

Le widget donne un aperçu du nombre de capteurs déjà connectés à l'appareil sélectionné. Le développement du panneau vous permet d'ajouter de nouveaux capteurs ou de modifier les capteurs existants.

![](../../../guide-de-litilizateur/appareils-et-parametres/attachments/image-20240815-205217.png)

Le nombre et le type de capteurs que vous pouvez connecter dépendent du modèle de l'appareil GPS. Par exemple, certains appareils permettent de configurer les paramètres des données transmises via le bus CAN ou le connecteur de diagnostic OBDII.

## Ajout et modification de capteurs

Pour gérer vos capteurs, vous pouvez utiliser les boutons suivants :

* **Ajouter**: Permet d'ajouter un nouveau capteur.
* **Editer**: Permet de modifier les paramètres d'un capteur existant.
* **Supprimer**: Supprime le capteur sélectionné du système.

### Types de capteurs

Navixy prend en charge différents types de capteurs, notamment :

*
* [**Capteurs de mesure**](measurement-sensors/): Ces capteurs mesurent et transmettent des valeurs continues telles que la température, le niveau de carburant ou le régime du moteur.
* [**Capteurs d'agrégation**](capteurs-dagregation.md): Combiner des données provenant de sources multiples en une seule valeur à déclarer.
* [**Capteurs virtuels**](capteurs-virtuels/): Dérivé de données calculées ou de valeurs combinées de capteurs.

### Copie des réglages du capteur

Pour rationaliser la configuration, vous pouvez copier les paramètres des capteurs d'un appareil à l'autre, à condition que les appareils soient du même modèle. Cette fonction est particulièrement utile pour la gestion de grandes flottes de véhicules de types similaires.

**Etapes pour copier les paramètres du capteur :**

1. Cliquez sur le bouton de copie (📋).
2. Sélectionnez les appareils auxquels vous souhaitez appliquer les paramètres copiés.
3. Cliquez sur **Appliquer**.

**Remarque :** La copie des paramètres du capteur écrase les paramètres actuels des appareils sélectionnés. Veillez à ne sélectionner que les appareils que vous souhaitez mettre à jour.
