# Antenne GPS déconnectée

## Vue d'ensemble

La règle de l'"antenne GPS déconnectée" est conçue pour les appareils GPS qui utilisent une antenne externe, généralement connectée par un câble et une prise. Lorsque l'antenne est déconnectée (ou coupée), la réception du signal satellite peut être perturbée, ce qui peut entraîner des problèmes de suivi. Cette règle vous alerte immédiatement lorsqu'une telle déconnexion se produit, ce qui vous permet de résoudre rapidement le problème et de maintenir un suivi continu de vos actifs.

Par exemple, si vous gérez une flotte de véhicules de livraison équipés de traceurs et d'antennes GPS externes, cette règle vous aide à contrôler l'intégrité de vos connexions GPS. Si une antenne est déconnectée en raison de facteurs environnementaux ou d'une manipulation, vous en serez immédiatement informé. Cela vous permet de prendre des mesures correctives, telles que l'envoi d'un technicien pour rétablir la connexion, afin d'éviter des retards potentiels et de maintenir des opérations efficaces.

{% hint style="info" %}
La plupart des appareils GPS modernes sont équipés d'antennes intégrées à haute sensibilité, ce qui rend les antennes externes obsolètes.
{% endhint %}

## Paramètres des règles

Cette règle dépend entièrement des capacités et de la configuration matérielle de l'appareil. Il n'y a pas de paramètres spécifiques à configurer dans la règle elle-même.

Pour les réglages courants, veuillez vous référer à [Règles et notifications](../).

## Détails du fonctionnement du système

* **Remise à zéro de la minuterie :** L'alerte "antenne GPS déconnectée" est assortie d'un délai de réinitialisation de 5 minutes, ce qui signifie que l'alerte ne se déclenchera pas plus d'une fois toutes les 5 minutes. Si un événement se produit pendant la période de réinitialisation, il sera omis par la plateforme et ne sera pas inclus dans les rapports.
* **Plusieurs appareils :** Vous pouvez surveiller plusieurs traceurs avec cette règle, à condition que les traceurs sélectionnés prennent en charge les événements de déconnexion de l'antenne GPS et que la fonction soit intégrée à la plateforme. Cela permet une surveillance complète de plusieurs véhicules ou appareils.
* **Gestion des événements sans coordonnées :** La plate-forme enregistrera et affichera l'événement même s'il est reçu dans un paquet sans coordonnées GPS valides. Vous êtes ainsi informé de l'événement de déconnexion, quelles que soient les données de localisation. Les paramètres des boutons radio Intérieur/Extérieur pour les géofences sont ignorés dans ces cas, ce qui donne la priorité à l'affichage des événements potentiellement critiques.
