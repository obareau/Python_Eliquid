
# Documentation : **EliquidCalculator**

## Version : 1.0

---

## **Introduction**
Le programme **EliquidCalculator** est une application graphique permettant de calculer les proportions nécessaires pour fabriquer un e-liquide pour cigarette électronique. Il inclut des fonctionnalités pour gérer des bases neutres ou nicotinées, des boosters, et des arômes. Il permet également de sauvegarder, charger et exporter les recettes sous divers formats (JSON, PDF, CSV).

---

## **Fonctionnalités**
### 1. **Calcul des proportions**
- Prise en charge des bases neutres et bases déjà nicotinées.
- Calcul du volume des arômes, boosters, et bases nécessaires pour atteindre :
  - Un volume total défini.
  - Un taux de nicotine souhaité.

### 2. **Personnalisation**
- Configuration du taux de PG/VG pour la base, les boosters, et les arômes.
- Prise en compte des volumes et proportions d'arômes.

### 3. **Export et sauvegarde**
- Export des recettes en :
  - **JSON** : Chargement et modification ultérieure.
  - **PDF** : Recette formatée pour impression.
  - **CSV** : Fichier tabulaire pour gestion ou partage.
- Génération de résultats détaillés affichés dans l'interface.

### 4. **Comparaison**
- Comparaison graphique (camemberts) de deux recettes en termes de proportions des ingrédients.

---

## **Installation**
### Prérequis
- Python 3.7 ou supérieur.
- Bibliothèques nécessaires :
  ```bash
  pip install tkinter matplotlib fpdf pillow
  ```

---

## **Interface Graphique**
### Section **Nom de la Recette**
- Permet de nommer votre recette. Le nom sera utilisé pour l’affichage et les fichiers exportés.

### Section **Volume Total**
- **Volume Total (ml)** : Volume final souhaité pour le e-liquide.

### Section **Arômes**
- **Proportion d'Arôme (%)** : Pourcentage d’arôme dans le mélange.
- **PG / VG de l'Arôme (%)** : Composition de l’arôme.

### Section **Nicotine**
- **Taux de Nicotine voulu (mg/ml)** : Objectif de nicotine pour le mélange final.
- **PG / VG de la Base et des Boosters (%)** : Composition respective de la base neutre et des boosters.

### Section **Base Nicotinée**
- **Activer/Désactiver Base Nicotinée** : Active ou désactive l’utilisation d’une base pré-nicotinée.
- **Taux de Nicotine de la Base (mg/ml)** : Taux de nicotine dans la base.
- **Volume Base Nicotinée (ml)** : Volume de la base nicotinée.

### Résultats
- Résultats détaillés affichés dans une zone dédiée :
  - Volumes nécessaires pour chaque ingrédient.
  - Nombre exact de boosters requis.
  - Taux final de nicotine.

---

## **Fonctionnalités Avancées**
### Export PDF
- Export de la recette au format PDF, avec les informations suivantes :
  - Nom de la recette.
  - Volumes et proportions.
  - Composition PG/VG des ingrédients.
  - Nombre de boosters.
  - Taux final de nicotine.

### Export CSV
- Fichier tabulaire avec toutes les informations de la recette.

### Chargement et Sauvegarde
- **JSON** :
  - Sauvegarde des recettes pour modification ultérieure.
  - Chargement des recettes depuis un fichier.

### Comparaison
- Sélectionnez deux fichiers JSON pour comparer les proportions d’ingrédients :
  - Graphiques camemberts générés automatiquement.

---

## **Utilisation**
### 1. **Création d'une Recette**
1. Entrez un nom pour la recette.
2. Configurez le volume total et les proportions d’arômes.
3. Définissez le taux de nicotine souhaité et les compositions PG/VG des ingrédients.
4. Activez la base nicotinée si nécessaire et remplissez les détails correspondants.
5. Cliquez sur **Calculer** pour afficher les résultats.

### 2. **Sauvegarde**
- Cliquez sur **Sauvegarder Recette** pour enregistrer au format JSON.

### 3. **Export**
- Cliquez sur **Exporter en PDF** ou **Exporter en CSV** pour sauvegarder dans le format choisi.

### 4. **Chargement**
- Cliquez sur **Charger Recette** pour ouvrir une recette JSON existante.

### 5. **Comparaison**
1. Cliquez sur **Comparer Recettes**.
2. Sélectionnez deux fichiers JSON.
3. Consultez les graphiques camemberts générés.

---

## **Exemples d’Utilisation**
### Création d'une Recette Standard
1. Nom de la recette : **"Fruité Mentholé"**.
2. Volume Total : **100 ml**.
3. Proportion d’Arôme : **12%**.
4. Taux de Nicotine souhaité : **6 mg/ml**.
5. Composition PG/VG :
   - Base : **50/50**.
   - Booster : **50/50**.
6. Résultats :
   - **12 ml d’arôme**.
   - **30 ml de boosters** (3 boosters de 10 ml).
   - **58 ml de base neutre**.

---

## **Structure des Fichiers**
### JSON (Sauvegarde)
```json
{
  "nom": "Fruité Mentholé",
  "volume_total": 100,
  "arome_proportion": 12,
  "nicotine_target": 6,
  "final_nicotine": 6,
  "num_boosters": 3,
  "base_pg": 50,
  "base_vg": 50,
  "booster_pg": 50,
  "booster_vg": 50,
  "arome_pg": 100,
  "arome_vg": 0
}
```

### CSV (Export)
| Clé                     | Valeur        |
|--------------------------|---------------|
| Nom de la recette        | Fruité Mentholé |
| Volume total (ml)        | 100           |
| Proportion d'arôme (%)   | 12            |
| Taux de nicotine (mg/ml) | 6             |
| Nombre de boosters       | 3             |
| Taux PG/VG de la base    | 50% / 50%     |
| Taux PG/VG des boosters  | 50% / 50%     |

---

## **Limitations Connues**
1. Le programme ne vérifie pas la cohérence des compositions PG/VG lorsque plusieurs arômes sont utilisés.
2. La comparaison se limite aux proportions d’ingrédients et ne traite pas les compositions PG/VG.

---

## **Prochaines Améliorations**
1. Gestion de plusieurs arômes avec des compositions PG/VG différentes.
2. Calcul des coûts totaux par recette (bases, boosters, arômes).
3. Prise en charge d’unités personnalisées (autres volumes de boosters ou bases).

---

## **Support et Contribution**
- Si vous rencontrez des problèmes ou souhaitez contribuer :
  - Contactez le développeur ou ouvrez une issue sur le dépôt GitHub.
