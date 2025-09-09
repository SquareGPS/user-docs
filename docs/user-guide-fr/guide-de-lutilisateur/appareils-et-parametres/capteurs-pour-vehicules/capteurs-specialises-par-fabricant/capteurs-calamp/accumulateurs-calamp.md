# Accumulateurs CalAmp

[CalAmp devices](https://www.navixy.com/devices/calamp/) sont équipés d'accumulateurs (variables) qui stockent différents types de données, en fonction de la configuration de l'appareil par l'utilisateur.

Afin de simplifier l'intégration et l'utilisation de ces accumulateurs au sein de la plateforme Navixy, un widget dédié a été introduit. Ce widget permet aux utilisateurs de configurer et de récupérer facilement les données des accumulateurs suivants :

## Accumulateurs pris en charge

- **Tension de la carte**: Surveille le niveau de tension de la carte interne de l'appareil, ce qui est essentiel pour évaluer l'état de santé et d'alimentation de l'appareil.
- **Capteurs de température externes (1-8)**: Capture les données d'un maximum de 8 capteurs de température externes connectés à l'appareil CalAmp, ce qui permet une surveillance détaillée des conditions environnementales.
- **Kilométrage du matériel**: Il s'agit des données kilométriques calculées directement par l'appareil lui-même, ce qui donne une mesure précise de la distance parcourue, basée sur les données matérielles plutôt que sur les seules données GPS.
- **Valeurs des capteurs analogiques (1-8)**: Récupère les relevés d'un maximum de 8 capteurs analogiques connectés à l'appareil, ce qui permet de surveiller une large gamme d'entrées, telles que la pression, l'humidité ou d'autres signaux analogiques.
- **IO\_States (États d'entrée/sortie)**: Affiche l'état des canaux d'entrée et de sortie de l'appareil, ce qui est essentiel pour comprendre l'interaction en temps réel entre l'appareil et les périphériques connectés.
- **ID iButton (parties basse et haute)**: Capture l'identifiant unique des dispositifs iButton en deux parties (basse et haute), qui est généralement utilisé pour l'identification du conducteur ou le contrôle d'accès dans les applications de gestion de flotte.

## Configuration des accumulateurs CalAmp dans Navixy

Pour configurer et surveiller ces accumulateurs sur la plateforme Navixy, suivez les étapes suivantes :

1. Accéder à la section "Appareils et paramètres
2. Sélectionner l'appareil CalAmp souhaité
3. Ouvrez le widget Accumulateurs. Vous pouvez sélectionner les accumulateurs que vous souhaitez surveiller. En fonction de vos besoins, vous pouvez activer la surveillance de la tension de la carte, des capteurs de température externes, du kilométrage matériel, des valeurs des capteurs analogiques, des états des E/S et des éléments d'identification des iButton.
4. Sauvegardez votre configuration.

## Suivi des données de l'accumulateur

Une fois configuré, vous pouvez visualiser les données en temps réel des accumulateurs sélectionnés directement dans la plateforme Navixy. Ces données peuvent être utilisées à diverses fins de surveillance et de reporting, en fonction de vos besoins opérationnels.

## Applications pratiques

- **Gestion du parc automobile**: Contrôle du kilométrage du matériel pour un suivi précis de la distance et une programmation de l'entretien.
- **Surveillance de l'environnement**: Utilisez des capteurs de température externes pour suivre les conditions environnementales à l'intérieur des cargaisons ou autour des véhicules.
- **Identification du conducteur**: Mettez en place un système de contrôle d'identité iButton pour vous assurer que seul le personnel autorisé utilise vos véhicules.
- **Surveillance des entrées analogiques**: Suivre diverses entrées analogiques pour des applications spécialisées, telles que la surveillance des niveaux de fluides ou de la pression dans les réservoirs.