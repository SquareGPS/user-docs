# Balises définies par l'utilisateur (Galileosky)

Les appareils Galileosky, connus pour leur polyvalence et leurs capacités avancées, se distinguent particulièrement par leur prise en charge des étiquettes définies par l'utilisateur. La plupart des appareils GPS transmettent un ensemble prédéfini de données, y compris des informations essentielles telles que les coordonnées, l'altitude, l'accélération, le kilométrage et des détails spécifiques au véhicule tels que l'état de l'allumage et la température du liquide de refroidissement. Cependant, ces données sont souvent limitées à ce que le fabricant prend en charge, ce qui restreint la surveillance de paramètres supplémentaires.

Avec [Dispositifs Galileosky](https://www.navixy.com/devices/galileosky/)Les utilisateurs peuvent surmonter ces limitations en définissant des balises personnalisées, ce qui permet la transmission d'un plus large éventail de données. Cette flexibilité permet aux utilisateurs de surveiller des paramètres supplémentaires qui ne sont généralement pas pris en charge par les appareils GPS standard.

[![Data transfer in Galileosky user tags](https://www.navixy.com/wp-content/uploads/2019/09/configurator_2019-09-28_13-28-39-600x370.png)

](https://www.navixy.com/wp-content/uploads/2019/09/configurator_2019-09-28_13-28-39.png)[![Data transfer in Galileosky user tags](https://www.navixy.com/wp-content/uploads/2019/09/chrome_2019-09-28_13-40-07-600x296.png)

](https://www.navixy.com/wp-content/uploads/2019/09/chrome_2019-09-28_13-40-07.png)

## Avantages des étiquettes définies par l'utilisateur avec les appareils Galileosky

1. **Transmission de données personnalisée**: Les utilisateurs peuvent définir des paramètres spécifiques à surveiller et à transmettre, élargissant ainsi le champ d'application au-delà de l'ensemble des données prédéfinies.
2. **Amélioration de l'analyse des données**: En utilisant Easy Logic, les utilisateurs peuvent effectuer des opérations arithmétiques sur les données avant qu'elles ne soient envoyées au serveur. Il peut s'agir d'additionner, de calculer la moyenne ou de convertir les données des capteurs en informations plus significatives.
3. **Rapports conditionnels sur les données**: Des opérations logiques peuvent être appliquées pour s'assurer que les données ne sont transmises que lorsque des conditions spécifiques sont remplies, optimisant ainsi l'utilisation et la pertinence des données.
4. **Comptage et rapport d'événements**: Les appareils Galileosky peuvent compter des événements spécifiques et les signaler en temps réel, fournissant ainsi des informations essentielles pour les applications de gestion de flotte ou de télématique.
5. **Actions automatisées**: Les appareils peuvent être programmés pour effectuer des actions spécifiques, telles que la commutation de sorties ou le déclenchement d'alertes, en fonction des conditions prédéfinies, qui sont ensuite signalées au serveur.

### Applications pratiques

Avec les appareils Galileosky et Easy Logic, vous pouvez :

- **Opérations arithmétiques**: Vous pouvez manipuler les données des capteurs avant qu'elles ne soient transmises au serveur. Il s'agit notamment d'additionner, de calculer la moyenne ou de convertir les relevés des capteurs dans des formats mieux adaptés à vos besoins d'analyse.
- **Opérations logiques**: Transmettre des données uniquement lorsque des conditions spécifiques sont remplies, en veillant à ce que les données collectées soient pertinentes et utilisées efficacement. Cela peut contribuer à optimiser la transmission des données et à réduire la charge de données inutiles.
- **Comptage d'événements**: Suivre et compter facilement des événements spécifiques sur la base de critères prédéfinis. Cette fonction est particulièrement utile pour surveiller les processus répétitifs ou cycliques.
- **Actions automatisées**: Configurez des actions, telles que la commutation de sorties, en fonction de certaines conditions et faites en sorte que ces actions soient signalées au serveur. Cette fonctionnalité est idéale pour automatiser les réponses aux entrées de données en temps réel.

## Comment configurer les balises définies par l'utilisateur de Galileo avec Navixy ?

### Configurer les appareils Galileosky

1. **Installer le configurateur Galileosky**: Commencez par télécharger et installer le logiciel Galileosky Configurator.
2. **Installation dans Easy Logic**: Utilisez Easy Logic pour définir les conditions et les opérations nécessaires pour vos balises personnalisées. Ce processus implique la création de scripts dans l'environnement Easy Logic pour configurer les données que vous souhaitez surveiller et transmettre.

### Configurer les capteurs dans Navixy

1. Naviguez jusqu'à la page *Appareils et paramètres* dans la plateforme Navixy.
2. Aller à *Capteurs et boutons* et créez un nouveau capteur de mesure.
3. Sélectionnez l'entrée (User Tag), le type de capteur et les unités appropriés.
4. Notez que dans le Configurateur Galileosky, les balises utilisateur sont numérotées de 0 à 7, alors que dans Navixy, elles sont numérotées de 1 à 8. Par conséquent, la balise 0 dans le Configurateur correspond à l'entrée 1 dans Navixy, et ainsi de suite.

Comme pour tout autre capteur, vous pouvez appliquer des paramètres supplémentaires, tels que l'étalonnage, les multiplicateurs ou les seuils, afin d'affiner la sortie des données.

Une fois configurées, ces balises définies par l'utilisateur permettent d'améliorer les capacités de surveillance et d'établissement de rapports, offrant aux utilisateurs la possibilité de capturer et d'analyser des données qui vont au-delà des limites des appareils GPS standard.

4. **Configurer le capteur dans Navixy**

- **Action**:
- Créer un nouveau capteur de mesure.
- Sélectionnez l'entrée (étiquette utilisateur), le type de capteur et les unités de mesure appropriés.
- Attention à la différence de numérotation : dans le Configurateur Galileosky, les balises utilisateur sont numérotées de 0 à 7, alors que dans Navixy, elles sont numérotées de 1 à 8. Ainsi, la balise 0 dans Galileosky correspond à l'entrée 1 dans Navixy, et ainsi de suite.
- **Objectif**: Une configuration correcte garantit que les données traitées par Easy Logic de Galileosky sont correctement interprétées et affichées sur la plate-forme Navixy.

5. **Appliquer des réglages supplémentaires du capteur**

- **Action**: Améliorez la fonctionnalité de votre capteur en établissant une table d'étalonnage, en appliquant des multiplicateurs pour ajuster les valeurs ou en établissant des seuils pour filtrer les valeurs aberrantes.
- **Objectif**: Ces paramètres supplémentaires permettent d'affiner les données afin qu'elles soient aussi précises et utiles que possible.

6. **Suivi et rapports dans Navixy**

- **Action**: Utilisez le widget des lectures de capteurs dans Navixy pour surveiller les données en temps réel. En outre, vous pouvez générer des rapports détaillés basés sur les données du capteur, fournissant des informations complètes sur vos opérations.
- **Objectif**: Cette intégration permet une surveillance continue et une analyse approfondie des données personnalisées collectées par vos appareils Galileosky.