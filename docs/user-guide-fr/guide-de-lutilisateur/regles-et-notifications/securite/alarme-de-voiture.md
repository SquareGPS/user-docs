# Alarme de voiture

## Vue d'ensemble

La règle "Alarme de voiture déclenchée" est conçue pour renforcer la sécurité de votre flotte en fournissant des notifications en temps réel lorsque le système d'alarme d'un véhicule est activé. Cette règle contribue à la protection de vos biens en alertant rapidement votre équipe en cas de vol potentiel, d'accès non autorisé ou de détérioration.

Cette règle fonctionne en contrôlant le système d'alarme du véhicule par l'intermédiaire d'un dispositif de localisation GPS connecté. En règle générale, le signal de sortie du système d'alarme est relié à l'entrée du dispositif GPS. Lorsque l'alarme est déclenchée, le dispositif GPS détecte ce signal et envoie une alerte à la plateforme.

## Paramètres des règles

Aucune règle spécifique n'est requise. Pour les paramètres courants, veuillez vous référer à [Règles et notifications](../../../guide-de-litilizateur/regles-et-notifications.md).

## Détails du fonctionnement du système

* **Remise à zéro de la minuterie :** L'alerte "Alarme de voiture déclenchée" est assortie d'un délai de réinitialisation de 5 minutes, ce qui signifie que l'alerte ne se déclenchera pas plus d'une fois toutes les 5 minutes. Si un événement se produit pendant la période de réinitialisation, la plate-forme supprime l'alerte, ce qui permet de conserver des notifications et des rapports clairs et concis.
* **Plusieurs appareils :** Cette règle peut être appliquée à plusieurs traceurs, à condition qu'ils prennent en charge les événements "Déclenchement d'une alarme de voiture" et que cette fonction soit intégrée à la plateforme. Cela vous permet de surveiller efficacement ces alertes sur plusieurs véhicules ou appareils.
* **Alerte d'événement indépendant du GPS :** La plateforme traite et affiche les événements liés aux alarmes automobiles même si le paquet de données ne contient pas de coordonnées GPS valides. Ces événements sont enregistrés, qu'ils se produisent à l'intérieur ou à l'extérieur d'un périmètre géographique donné. Dans ce cas, les paramètres de géofencing intérieur/extérieur sont contournés, ce qui permet de ne manquer aucun événement critique.
