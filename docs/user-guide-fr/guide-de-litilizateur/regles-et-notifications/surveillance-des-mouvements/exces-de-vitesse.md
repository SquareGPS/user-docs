# Excès de vitesse

## Vue d'ensemble

L'objectif de la règle de détection des excès de vitesse est d'aider les entreprises à améliorer leurs mesures de sécurité globales en contrôlant et en traitant les excès de vitesse. Cela permet d'assurer le respect des limitations de vitesse, de promouvoir un comportement de conduite responsable parmi les employés et de réduire le risque d'accident. La plateforme propose deux méthodes de détection des excès de vitesse :

### Méthode I. Excès de vitesse détecté par la plate-forme

Cette méthode s'appuie sur les données de vitesse fournies par les traceurs GPS pour identifier les excès de vitesse. La plateforme analyse les données de vitesse des paquets de données GPS pour vérifier si la limite de vitesse spécifiée a été dépassée. Bien que cette méthode soit moins précise que les excès de vitesse détectés par l'appareil, elle peut être utilisée avec n'importe quel traceur GPS qui signale la vitesse. Il s'agit d'une option appropriée pour les appareils qui ne peuvent pas détecter les excès de vitesse de manière native.

### Méthode II. Excès de vitesse détecté par le matériel

Cette méthode utilise le matériel du traceur GPS pour détecter les excès de vitesse. L'appareil lui-même calcule le moment où un excès de vitesse se produit à l'aide de commandes à distance ou d'un logiciel de configuration de l'appareil. La plateforme reçoit ensuite des notifications de l'appareil sur la base de ces calculs. Cette méthode est très précise et fonctionne avec la plupart des traceurs modernes qui peuvent envoyer les excès de vitesse directement à la plateforme.

## Paramètres des règles

#### Limitation de vitesse, excès de vitesse détectés par la plate-forme

La limite de vitesse définit le seuil à partir duquel la règle est déclenchée. Lorsque la plate-forme reçoit des données de vitesse de l'appareil, elle compare cette valeur à la limite spécifiée. Si la vitesse dépasse la limite, la plate-forme génère une alerte d'excès de vitesse.

#### Limitation de vitesse, excès de vitesse détectés par le matériel

Pour les excès de vitesse détectés par l'appareil, il n'y a pas de paramètre spécifique dans les règles et les notifications. Utilisez plutôt le widget Paramètres de l'appareil pour configurer à distance la limite de vitesse du côté de l'appareil.

Pour les réglages courants, veuillez vous référer à [Règles et notifications](../../regles-et-notifications.md).

## Détails du fonctionnement du système

- **Exigences matérielles et traitement des événements**
  - **Plate-forme de détection des excès de vitesse**: Cette règle peut être appliquée à la plupart des traceurs qui envoient des données sur la vitesse dans leurs paquets. La règle est traitée dans le nuage, où la plateforme utilise les données de vitesse des paquets de l'appareil pour déterminer si la limite de vitesse a été dépassée. L'alerte est assortie d'un délai de réinitialisation de 15 minutes, ce qui signifie qu'elle ne se déclenchera pas plus d'une fois toutes les 15 minutes. Si un événement se produit pendant que la règle attend la réinitialisation, la plateforme omettra l'événement, y compris dans les rapports.
  - **Excès de vitesse Excès de vitesse détecté par le matériel**: Cette règle ne s'applique qu'aux suiveurs qui prennent en charge l'envoi d'événements d'excès de vitesse basés sur le matériel. Le dispositif lui-même traite la règle et la plateforme génère des notifications basées sur les calculs effectués par le matériel. L'alerte a un délai de réinitialisation d'une minute, ce qui signifie que l'alerte ne se déclenchera pas plus d'une fois par minute. Si un événement se produit pendant que la règle attend la réinitialisation, la plate-forme ne tient pas compte de l'événement, y compris dans les rapports.

- **Traqueurs multiples**: La règle permet de sélectionner plusieurs traceurs au sein d'une même règle, ce qui permet une surveillance complète de plusieurs véhicules ou dispositifs.
- **Dérive du GPS**: Le système peut générer une alerte d'excès de vitesse même en cas de dérive GPS. Bien que les coordonnées GPS non valides soient filtrées, de petites dérives GPS peuvent encore apparaître dans la trace. Cependant, la plateforme propose diverses méthodes pour minimiser ces dérives, selon les fonctionnalités du modèle de traceur. Pour des informations détaillées sur la prévention des dérives GPS, veuillez vous référer au manuel de l'appareil. Cela garantit une détection plus précise et plus fiable des événements, améliorant ainsi l'efficacité globale de la surveillance.