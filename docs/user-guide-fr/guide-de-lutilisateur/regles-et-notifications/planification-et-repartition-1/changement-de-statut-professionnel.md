# Changement de statut professionnel

## Vue d'ensemble

La règle "Changement de statut de travail" est conçue pour surveiller et suivre les activités en temps réel des employés mobiles qui utilisent l'application X-GPS Tracker. Cette règle alerte les employés qui mettent à jour leur statut actuel, en indiquant par exemple qu'ils sont disponibles pour une nouvelle tâche ou qu'ils ont commencé une nouvelle activité.

Lorsque la règle "Statut de travail" est active, tout changement dans le statut d'un employé déclenche des notifications immédiates par SMS, par courriel ou par des alertes contextuelles dans l'interface utilisateur. Cette fonctionnalité permet aux superviseurs et aux dispatchers de rester informés des activités et de la disponibilité de leur équipe, ce qui améliore la coordination et la gestion des tâches.

## Paramètres des règles

#### Statuts de travail

Définissez les statuts de travail spécifiques qui déclencheront des notifications lorsqu'ils seront sélectionnés par les employés. Les utilisateurs peuvent choisir les statuts à surveiller, ce qui garantit que le système n'émet des alertes que pour les mises à jour de statut les plus pertinentes. Ces statuts sont créés et attribués par le biais du widget "Statuts de travail" dans le menu Dispositifs et paramètres.

Pour les réglages courants, veuillez vous référer à [Règles et notifications](../../../guide-de-litilizateur/regles-et-notifications.md).

## Détails du fonctionnement du système

* Cette règle est spécifiquement conçue pour être utilisée avec les appareils compatibles avec le système de suivi X-GPS, ce qui signifie que seuls ces appareils peuvent être sélectionnés comme sources pour le suivi des changements d'état du travail.
* La liste des statuts de travail qui déclenchent cette règle peut varier en fonction des listes personnalisées attribuées aux différents suiveurs. Si vous modifiez la liste des périphériques liés à la règle et que cela modifie la liste des états de travail associés, la règle inclura à la fois les anciens et les nouveaux états. Cependant, les nouveaux statuts ajoutés dans la liste mise à jour ne seront pas sélectionnés par défaut. Vous pouvez modifier la règle pour inclure ces nouveaux états.
* Contrairement à de nombreuses autres règles, la règle "Statut de travail" n'est pas assortie d'un délai de remise à zéro, ce qui permet de notifier immédiatement tout changement de statut.

Cette configuration aide les organisations à maintenir une communication claire et une gestion efficace des tâches en tenant l'équipe informée de l'état d'avancement du travail de chaque membre.
