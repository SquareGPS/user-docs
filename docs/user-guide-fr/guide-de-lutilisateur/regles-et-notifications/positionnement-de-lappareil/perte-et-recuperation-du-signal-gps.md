# Perte et récupération du signal GPS

## Vue d'ensemble

La règle "Perte/rétablissement du signal GPS" surveille la disponibilité du signal GPS pour vos appareils. Cette règle déclenche des notifications lorsqu'un appareil perd son signal GPS, souvent parce qu'il se trouve à l'intérieur, sous terre ou dans une zone où la visibilité des satellites est faible, et lorsque le signal est rétabli par la suite. En recevant ces notifications, vous pouvez rester informé de l'état de la localisation de vos actifs, même dans des environnements difficiles.

Cette règle est particulièrement utile dans les environnements où la couverture du signal GPS n'est pas fiable, tels que les chantiers de construction, les entrepôts ou les installations souterraines. Pour recevoir ces alertes lorsque le signal GPS est perdu et rétabli, il est essentiel de s'assurer que votre traceur dispose d'une connexion cellulaire et d'une connexion internet.

## Paramètres des règles

Cette règle est traitée dans le nuage, ce qui signifie que le logiciel du serveur surveille le moment où le signal GPS est perdu et le moment où il est rétabli. Vous pouvez appliquer cette règle à plusieurs traceurs simultanément, à condition que les traceurs prennent en charge ce type d'événement et qu'il soit intégré à la plateforme.

Pour le paramétrage des règles communes, veuillez vous référer à la section [Règles et notifications](../).

## Détails du fonctionnement du système

* **Remise à zéro de la minuterie :** L'alerte "perte/récupération du signal GPS" est assortie d'un délai de réinitialisation de 10 secondes, ce qui signifie que l'alerte ne se déclenchera pas plus d'une fois toutes les 10 secondes. Si un événement se produit pendant la période de réinitialisation, il sera omis par la plateforme, y compris dans les rapports.
* **Plusieurs appareils :** Vous pouvez sélectionner plusieurs traceurs à surveiller dans le cadre de cette règle, à condition que les traceurs prennent en charge les événements de perte/récupération du signal GPS et que la fonction soit intégrée à la plateforme. Cela vous permet de gérer efficacement plusieurs appareils.
* **Alerte d'événement indépendante du GPS :** La plateforme enregistrera et affichera cet événement même s'il est reçu dans un message sans coordonnées valides, ce qui vous permettra d'être informé quel que soit l'emplacement de l'événement. Les paramètres intérieur/extérieur des géofences sont ignorés dans ce cas, car la plate-forme affiche en priorité les événements potentiellement critiques.
