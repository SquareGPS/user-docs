# Conduite difficile

## Vue d'ensemble

La règle "conduite difficile" est conçue pour aider les entreprises à surveiller et à améliorer le comportement des conducteurs, afin de garantir une utilisation plus sûre des véhicules et de réduire le risque d'accident. Cette règle est particulièrement utile pour les flottes, les sociétés de location de voitures et les opérations logistiques, où la qualité de la conduite a un impact direct sur les coûts d'entretien des véhicules, la sécurité et la satisfaction des clients. En détectant les incidents de conduite difficiles et en y réagissant, les entreprises peuvent mieux gérer leurs véhicules, réduire l'usure et maintenir un niveau de service élevé.

Cette règle utilise l'accéléromètre intégré de l'appareil pour surveiller les accélérations soudaines, les freinages brusques et les virages serrés. Lorsque l'appareil GPS détecte l'un de ces événements, il envoie les données à la plateforme, qui génère alors des alertes et enregistre les incidents pour examen. Pour utiliser cette règle, assurez-vous que la fonction de détection de la conduite difficile est correctement configurée dans le fichier Paramètres de l'appareil ou le configurateur de traceur.

## Paramètres des règles

Veillez à ce que la fonction de conduite difficile soit configurée dans le module Appareils et paramètres Les utilisateurs peuvent créer des règles à partir du menu de la plateforme, en particulier dans le widget "Conduite difficile", ou par l'intermédiaire de l'outil de configuration de l'appareil. Une fois la règle configurée, les utilisateurs peuvent la créer et la gérer à partir de la plateforme.

Aucun autre paramètre spécifique n'est requis pour cette règle. Pour les paramètres courants, veuillez vous référer à [Règles et notifications](../).

## Détails du fonctionnement du système

* **Remise à zéro de la minuterie :** L'alerte "Conduite difficile" est assortie d'un délai de réinitialisation de 10 secondes, ce qui signifie que l'alerte ne se déclenchera pas plus d'une fois toutes les 10 secondes. Si un événement se produit pendant la période de réinitialisation, la plateforme supprimera l'alerte afin que les notifications et les rapports restent précis et gérables.
* **Plusieurs appareils :** Les utilisateurs peuvent appliquer cette règle à plusieurs traqueurs, à condition qu'ils prennent en charge la détection de la conduite dangereuse et que cette fonction soit intégrée à la plateforme. Cela permet aux utilisateurs de surveiller efficacement les incidents liés à la conduite en état d'ébriété sur plusieurs véhicules ou appareils.
* **Traitement des événements indépendant du GPS :** La plateforme traite et affiche les événements de conduite difficiles même si le paquet de données ne contient pas de coordonnées GPS valides. Ces événements sont enregistrés, qu'ils se produisent à l'intérieur ou à l'extérieur d'un périmètre géographique donné. Dans ce cas, les paramètres de géofencing intérieur/extérieur sont contournés afin de garantir qu'aucun événement critique n'est manqué.
