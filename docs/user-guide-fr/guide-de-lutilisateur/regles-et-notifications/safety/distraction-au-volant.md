# Distraction au volant

## Vue d'ensemble

La fonction de distraction au volant est un élément des systèmes télématiques avancés, conçu pour détecter et alerter les utilisateurs lorsque les conducteurs se livrent à des activités distrayantes, telles que fumer ou utiliser un téléphone portable.

Cette fonction dépend de la configuration du matériel, généralement des caméras de tableau de bord ou des appareils GPS équipés de caméras, pour identifier et signaler les distractions. La plateforme traite ces événements en temps réel et envoie des notifications, ce qui permet de prendre rapidement des mesures correctives pour améliorer la sécurité routière et promouvoir un comportement de conduite responsable.

Cette règle dépend de l'appareil, c'est-à-dire qu'elle s'appuie sur la configuration du matériel (généralement des caméras de tableau de bord ou des appareils GPS dotés de fonctions de caméra) pour détecter et signaler les événements de distraction. La plateforme traite ces événements et envoie des notifications à l'utilisateur en conséquence.

## Paramètres des règles

Comme cette règle est basée sur la configuration du matériel, une configuration minimale est nécessaire au sein de la plateforme elle-même. L'essentiel est de s'assurer que les dispositifs sélectionnés sont configurés pour détecter et signaler les événements de distraction du conducteur.

Pour les réglages courants, veuillez vous référer à [Règles et notifications](../../../guide-de-litilizateur/regles-et-notifications.md).

## Détails du fonctionnement du système

* **Remise à zéro de la minuterie :** L'alerte "Distraction au volant" est gérée par une minuterie de réinitialisation de 10 secondes, ce qui garantit que les alertes ne sont pas générées plus fréquemment qu'une fois toutes les 10 secondes. Si un événement de distraction se produit pendant la période de réinitialisation, il sera omis de la plateforme et des rapports.
* **Plusieurs appareils :** Les utilisateurs peuvent configurer cette règle sur plusieurs trackers, à condition qu'ils prennent en charge les événements de "Distraction au volant" et que cette fonction soit intégrée à la plateforme. Cela permet une surveillance complète sur plusieurs véhicules ou appareils, garantissant ainsi un contrôle cohérent du comportement du conducteur.
* **Alerte d'événement indépendante du GPS :** La plateforme enregistrera et affichera les événements de "distraction au volant" même si le paquet de données ne contient pas de coordonnées GPS valides. Les paramètres de géofence intérieur/extérieur sont ignorés dans ce cas, car le système donne la priorité à l'affichage des événements potentiellement critiques afin de s'assurer qu'aucune information importante n'est manquée.
