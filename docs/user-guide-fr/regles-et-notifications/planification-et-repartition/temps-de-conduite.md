# Temps de conduite

## Vue d'ensemble

La règle sur les temps de conduite est conçue pour contrôler et faire respecter les pratiques de conduite sûres en suivant les périodes de travail et de repos des conducteurs. Cette règle permet de s'assurer que les conducteurs respectent les règles en matière de temps de conduite, ce qui contribue à prévenir les incidents liés à la fatigue et à promouvoir la sécurité routière en général.

Lorsqu'un conducteur dépasse le temps de conduite continue autorisé, le système génère une notification pour alerter l'utilisateur. La règle se réinitialise automatiquement une fois que le conducteur s'est reposé pendant une période donnée, que vous pouvez configurer en fonction de vos besoins.

## Paramètres des règles

#### **Temps de conduite autorisé**

Ce paramètre définit la durée maximale pendant laquelle un conducteur peut conduire sans interruption avant qu'une notification ne soit déclenchée. Une fois cette limite atteinte, le système vous alertera pour que vous preniez les mesures nécessaires.

#### Durée minimale de stationnement pour la réinitialisation

Ce paramètre spécifie la durée minimale de stationnement requise pour réinitialiser la règle de temps de conduite. La minuterie de réinitialisation ne commence que lorsque l'appareil détecte que le véhicule est entré dans un état de stationnement.

Pour les réglages courants, veuillez vous référer à [Règles et notifications](../../regles-et-notifications.md).

## Détails du fonctionnement du système

- La règle du temps de conduite fonctionne en suivant le temps total que le conducteur passe à conduire sans interruption. Lorsque le temps de conduite maximum autorisé est dépassé, le système génère une alerte.
- La règle se réinitialise après que le véhicule a été garé pendant la durée minimale spécifiée dans les paramètres, ce qui permet au conducteur de commencer une nouvelle période de conduite.
- Cette règle est traitée dans le nuage, ce qui permet de l'appliquer simultanément à plusieurs trackers. Cette flexibilité vous permet de surveiller plusieurs conducteurs à l'aide d'une seule règle.
- Le système permet de garantir le respect des règles de conduite, de réduire la fatigue des conducteurs et de promouvoir des pratiques de conduite plus sûres, contribuant ainsi à la sécurité et à l'efficacité globales de la flotte.