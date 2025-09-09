# Déclenchement de la sortie

## Vue d'ensemble

Les dispositifs GPS pour véhicules sont souvent équipés de sorties configurables qui permettent aux utilisateurs de contrôler diverses fonctions du véhicule, telles que l'immobilisation du moteur, l'activation de l'alarme, etc. Ces sorties peuvent être gérées directement à partir du tableau de bord de votre plateforme télématique. En configurant une règle pour les changements d'état des sorties, vous pouvez recevoir des notifications via l'interface utilisateur, l'application mobile, un SMS ou un e-mail dès que l'état de la sortie est modifié.

Cette fonction vous permet de rester informé de toute modification apportée à l'équipement connecté à votre appareil GPS. Que vous activiez ou désactiviez des fonctions spécifiques, cette règle constitue un moyen fiable de surveiller et de gérer l'état des sorties de votre véhicule.

Par exemple, dans le cadre de la gestion d'un parc automobile, cette règle est particulièrement utile pour surveiller l'état d'un bloc moteur ou d'un système de coupure de l'alimentation en carburant. Si un dispositif GPS est configuré pour contrôler ces sorties, la règle peut générer des alertes chaque fois que le bloc moteur est activé ou désactivé. Les gestionnaires de flotte peuvent ainsi s'assurer que les mesures de sécurité sont correctement appliquées et que l'utilisation non autorisée des véhicules est évitée.

## Paramètres des règles

#### Sortie

Spécifiez la sortie matérielle que vous souhaitez surveiller en sélectionnant le numéro de sortie approprié. Reportez-vous à la documentation du fabricant du traceur pour déterminer quelle sortie contrôle quelle fonctionnalité.

## Détails du fonctionnement du système

- **Alerte en cas d'événement indépendant du GPS :** Si la plate-forme détecte un événement de changement de sortie (tel que le passage de 1 à 0 ou vice versa) à partir d'un paquet de données de suivi sans coordonnées valides, l'événement sera tout de même considéré comme valide et affiché. Cela s'applique indépendamment du fait que l'événement se soit produit à l'intérieur ou à l'extérieur d'une géofence, car la logique de géofence intérieur/extérieur est ignorée afin de s'assurer que des événements potentiellement importants ne sont pas négligés.
- **Alertes sélectives :** Si vous souhaitez recevoir des alertes uniquement pour des changements de sortie spécifiques, par exemple de "OFF à ON" et non de "ON à OFF", vous pouvez y parvenir en supprimant le texte de notification pour l'état de sortie indésirable dans les paramètres.
- **Remise à zéro de la minuterie :** L'alerte "Outputs Triggering" est assortie d'un délai de réinitialisation de 10 secondes, ce qui signifie qu'elle ne se déclenchera pas plus d'une fois toutes les 10 secondes. Si un autre événement se produit pendant la période de réinitialisation, il sera omis de la plate-forme, y compris dans les rapports.
- **Plusieurs appareils :** Vous pouvez assigner plusieurs suiveurs à cette règle, chaque suiveur utilisant le même numéro de sortie spécifié dans les paramètres de la règle. Par exemple, si vous sélectionnez la sortie n°2, la règle vous notifiera chaque fois qu'un des traqueurs sélectionnés signalera un changement dans sa sortie n°2.