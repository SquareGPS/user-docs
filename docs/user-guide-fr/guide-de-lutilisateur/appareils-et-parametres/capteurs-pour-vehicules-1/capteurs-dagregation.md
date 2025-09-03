# Capteurs d'agrégation

Les **Capteur d'agrégation** widget dans Navixy est un outil puissant qui vous permet de combiner des données provenant de plusieurs capteurs et de les traiter à l'aide d'une fonction d'agrégation. Cette fonctionnalité est particulièrement utile dans les scénarios où plusieurs capteurs sont utilisés pour surveiller des paramètres similaires, tels que les niveaux de carburant dans un véhicule.

![image-20240815-205851.png](../../../guide-de-litilizateur/appareils-et-parametres/capteurs-pour-vehicules/attachments/image-20240815-205851.png)

## Options de la fonction d'agrégation

#### Les deux fonctions d'agrégation disponibles sont **Moyenne (AVG)** et **Total (SUM)**.

* **AVG (Moyenne)**: Cette fonction calcule la valeur moyenne des capteurs sélectionnés. Elle est utile lorsque vous souhaitez lisser les relevés de plusieurs capteurs, afin d'obtenir une valeur plus stable et plus représentative.
* **SOMME**: Cette fonction additionne les valeurs des capteurs sélectionnés. Elle est idéale lorsque la valeur totale d'un paramètre doit être surveillée, comme le niveau de carburant combiné de deux réservoirs.

## Exemples pratiques : plusieurs capteurs de carburant dans un véhicule

1. **Réservoir unique avec deux capteurs de niveau de carburant**:

* **Scénario**: Vous avez un grand réservoir de carburant avec deux capteurs placés en différents points à l'intérieur du réservoir.
* **Goal**: Pour obtenir une lecture plus précise du niveau global de carburant en faisant la moyenne des lectures des deux capteurs.
* **Configuration**:
  * **Fonction d'agrégation**: Sélectionner **AVG**.
  * **Capteurs pour l'agrégation**: Choisissez les deux capteurs de niveau de carburant.
  * **Résultat**: Le système affiche le niveau moyen de carburant, fournissant une lecture équilibrée qui compense tout écart entre les deux capteurs.

2. **Deux réservoirs avec capteurs séparés**:

* **Scénario**: Vous avez deux réservoirs de carburant séparés, et chaque réservoir a son propre capteur de niveau de carburant.
* **Goal**: Pour contrôler la quantité totale de carburant disponible dans les deux réservoirs.
* **Configuration**:
  * **Fonction d'agrégation**: Sélectionner **SOMME**.
  * **Capteurs pour l'agrégation**: Choisissez les capteurs des deux réservoirs.
  * **Résultat**: Le système additionne les niveaux de carburant des deux réservoirs, ce qui vous donne le carburant total disponible.

## Configuration du capteur d'agrégation

1. **Étiquette**: Entrez un nom pour votre capteur d'agrégation qui identifie clairement son objectif.
2. **Fonction d'agrégation**: Sélectionnez l'une ou l'autre des options suivantes **AVG** (pour le calcul de la moyenne) ou **SOMME** (pour l'addition) en fonction de vos besoins.
3. **Type de capteur**: Choisissez le type de capteur (par exemple, niveau de carburant).
4. **Précision**: Spécifier la marge d'erreur acceptable. Par exemple, si la précision est fixée à 5 % et que la valeur maximale est de 100 litres, les variations de 5 litres ou moins seront ignorées.
5. **Valeur maximale**: Définir la limite supérieure de la valeur agrégée. Cela permet d'éviter que la lecture agrégée ne dépasse un certain seuil.
6. **Unités**: Spécifier l'unité de mesure (par exemple, litres).
7. **Capteurs pour l'agrégation**: Sélectionnez les capteurs individuels dont vous souhaitez agréger les données.
8. **Économiser**: Après avoir configuré le capteur, cliquez sur **Économiser** pour appliquer les paramètres.

Cette configuration vous permet de contrôler et de gérer efficacement les données provenant de sources multiples, améliorant ainsi la précision et l'utilité de vos solutions de gestion de flotte et de télématique.
