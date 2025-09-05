# Changement de conducteur

## Vue d'ensemble

La règle "Changement de conducteur" aide les gestionnaires de flotte à savoir quel conducteur conduit un véhicule, en particulier lorsque plusieurs conducteurs partagent le même véhicule. Cette fonction fonctionne avec des technologies d'identification du conducteur telles que les iButton, les lecteurs RFID ou les clés matérielles BLE.

## Paramètres des règles

Pour utiliser cette règle, commencez par ajouter tous vos pilotes au fichier **Gestion du parc automobile** → **Section conducteurs**. Attribuez à chaque conducteur une clé matérielle unique, telle qu'un iButton ou une étiquette RFID. Lorsqu'un changement de conducteur est détecté, la plateforme associe l'événement au bon conducteur, ce qui garantit la précision des rapports et des alertes.

Aucun autre réglage spécifique de la règle n'est nécessaire. Pour les paramètres courants, veuillez vous référer à [Règles et notifications](../).

## Détails du fonctionnement du système

* **Détection de changement de conducteur :** La plate-forme identifie un changement de conducteur en vérifiant si les dernières données de clé matérielle reçues du traceur diffèrent des données précédentes. Si la clé a changé, elle l'enregistre comme un événement de changement de conducteur. Cet événement diffère de l'événement [Identification du conducteur](identification-du-conducteur.md) où l'alerte est déclenchée directement par le matériel en cas d'authentification réussie du conducteur, et où la plateforme se contente d'afficher l'événement.
* **Les dérogations manuelles :** Les modifications manuelles apportées au conducteur par l'intermédiaire de l'interface utilisateur (c'est-à-dire dans les widgets) ne déclenchent pas d'événement de modification du conducteur. Ces changements ne sont pas non plus inclus dans le "Rapport sur tous les événements". Cependant, tous les changements manuels et automatiques de conducteur peuvent être examinés en détail dans le rapport "Changement d'équipe de conducteur".
* **Minuterie de réinitialisation de l'alerte :** L'alerte "Changement de conducteur" est assortie d'un délai de réinitialisation de 10 secondes, ce qui l'empêche de se déclencher plus d'une fois toutes les 10 secondes. Si un changement de conducteur se produit pendant cette période, la plate-forme supprime l'alerte, ce qui permet de conserver des notifications et des rapports précis et concis.
* **Prise en charge de plusieurs appareils :** Cette règle peut être appliquée à plusieurs systèmes de suivi, ce qui permet aux gestionnaires de flotte de surveiller les changements de conducteur sur plusieurs véhicules. Les systèmes de suivi doivent être compatibles avec l'événement "Changement de conducteur" et intégrer cette fonction dans la plateforme.
* **Traitement des événements indépendant du GPS :** La plateforme traite les événements de changement de conducteur même si les données GPS sont manquantes ou invalides. Ces événements seront toujours enregistrés et affichés, qu'ils se soient produits à l'intérieur ou à l'extérieur d'un périmètre géographique. Cela permet de s'assurer que tous les événements critiques de changement de conducteur sont capturés et rapportés avec précision.

## Voir aussi

* [**Règle d'identification des conducteurs**](identification-du-conducteur.md) - la règle utilisée pour vérifier et autoriser le conducteur avant ou pendant la conduite du véhicule, fournir des alertes immédiates et s'assurer que seuls les conducteurs autorisés peuvent conduire le véhicule.
