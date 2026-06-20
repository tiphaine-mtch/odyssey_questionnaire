# 🎯 Logique d'identification selon le rôle

**Version :** 1.2  
**Date :** 18 juin 2026

---

## 📋 Principe

Le formulaire d'identification s'adapte **automatiquement** selon le rôle sélectionné, car chaque rôle implique une localisation spécifique.

---

## 🔄 Logique par rôle

### 1. **Room Division Manager** 🏨
**Localisation automatique :** Resort

**Champs demandés :**
- ✅ Nom complet
- ✅ Rôle : Room Division Manager (sélectionné)
- ✅ **Dans quel resort travaillez-vous ?** (champ texte libre)

**Exemple :**
```
Nom: Marie Dupont
Rôle: Room Division Manager
Resort: Les Arcs Panorama (ARPC)
```

**Données sauvegardées :**
```json
{
  "name": "Marie Dupont",
  "role": "room_division_manager",
  "location": "resort",
  "resort": "Les Arcs Panorama (ARPC)",
  "businessUnit": null
}
```

---

### 2. **Planning Manager** 📅
**Localisation automatique :** Resort

**Champs demandés :**
- ✅ Nom complet
- ✅ Rôle : Planning Manager (sélectionné)
- ✅ **Dans quel resort travaillez-vous ?** (champ texte libre)

**Exemple :**
```
Nom: Jean Martin
Rôle: Planning Manager
Resort: Phuket (PHUC)
```

**Données sauvegardées :**
```json
{
  "name": "Jean Martin",
  "role": "planning_manager",
  "location": "resort",
  "resort": "Phuket (PHUC)",
  "businessUnit": null
}
```

---

### 3. **Produits & Services Manager** 🌍
**Localisation automatique :** Business Unit

**Champs demandés :**
- ✅ Nom complet
- ✅ Rôle : Produits & Services Manager (sélectionné)
- ✅ **Dans quelle Business Unit travaillez-vous ?** (dropdown)
  - EMEA (Europe, Middle East, Africa)
  - ESAP (East & South Asia Pacific)
  - NAM (North America)
  - SAM (South America)

**Exemple :**
```
Nom: Sophie Leclerc
Rôle: Produits & Services Manager
Business Unit: EMEA
```

**Données sauvegardées :**
```json
{
  "name": "Sophie Leclerc",
  "role": "produits_services_manager",
  "location": "business_unit",
  "resort": null,
  "businessUnit": "EMEA"
}
```

---

### 4. **Other** ❓
**Localisation :** À définir par l'utilisateur

**Champs demandés :**
- ✅ Nom complet
- ✅ Rôle : Other (sélectionné)
- ✅ **Précisez votre rôle** (champ texte libre obligatoire)
- ✅ **Localisation** (dropdown)
  - Siège Social
  - Business Unit
  - Resort / Village

**Si localisation = Resort :**
- ✅ **Nom du Resort** (champ texte libre obligatoire)

**Si localisation = Business Unit :**
- ✅ **Business Unit** (champ texte libre obligatoire)

**Exemple 1 - Other en Resort :**
```
Nom: Ahmed Ben Ali
Rôle: Revenue Manager (précisé)
Localisation: Resort
Resort: Cefalù (CFAC)
```

**Données sauvegardées :**
```json
{
  "name": "Ahmed Ben Ali",
  "role": "Revenue Manager",
  "location": "resort",
  "resort": "Cefalù (CFAC)",
  "businessUnit": null
}
```

**Exemple 2 - Other au Siège :**
```
Nom: Laura Fernandez
Rôle: Responsable Programme Fidélité (précisé)
Localisation: Siège Social
```

**Données sauvegardées :**
```json
{
  "name": "Laura Fernandez",
  "role": "Responsable Programme Fidélité",
  "location": "siege",
  "resort": null,
  "businessUnit": null
}
```

---

## 🎨 Affichage dynamique des champs

### État initial (aucun rôle sélectionné)
```
[Nom complet]         [requis]
[Rôle / Fonction]     [requis] (dropdown)
```

### Après sélection "Room Division Manager"
```
[Nom complet]                        [requis]
[Rôle / Fonction]                    [requis] ✓ Room Division Manager
[Dans quel resort travaillez-vous ?] [requis] (ex: Les Arcs Panorama)
```

### Après sélection "Planning Manager"
```
[Nom complet]                        [requis]
[Rôle / Fonction]                    [requis] ✓ Planning Manager
[Dans quel resort travaillez-vous ?] [requis] (ex: Phuket)
```

### Après sélection "Produits & Services Manager"
```
[Nom complet]                              [requis]
[Rôle / Fonction]                          [requis] ✓ Produits & Services Manager
[Dans quelle Business Unit travaillez-vous ?] [requis] (dropdown: EMEA/ESAP/NAM/SAM)
```

### Après sélection "Other"
```
[Nom complet]            [requis]
[Rôle / Fonction]        [requis] ✓ Other
[Précisez votre rôle]    [requis] (ex: Revenue Manager)
[Localisation]           [requis] (dropdown: Siège/BU/Resort)

// Si Resort sélectionné
  [Nom du Resort]        [requis] (ex: Les Arcs Panorama)

// Si Business Unit sélectionné
  [Business Unit]        [requis] (ex: Europe Alpes)
```

---

## 🔍 Validation des données

### Règles de validation

| Rôle | Champs obligatoires | Validation |
|------|---------------------|------------|
| **Room Division Manager** | Nom + Resort | Resort non vide |
| **Planning Manager** | Nom + Resort | Resort non vide |
| **Produits & Services Manager** | Nom + BU | BU sélectionnée dans dropdown |
| **Other** | Nom + Rôle précisé + Localisation | Rôle non vide + Localisation sélectionnée |
| **Other (Resort)** | + Resort | Resort non vide |
| **Other (BU)** | + BU | BU non vide |

### Messages d'erreur

```javascript
// Pas de rôle sélectionné
"Veuillez remplir tous les champs obligatoires."

// Room Division ou Planning Manager sans resort
"Veuillez préciser dans quel resort vous travaillez."

// Produits & Services Manager sans BU
"Veuillez sélectionner votre Business Unit."

// Other sans rôle précisé
"Veuillez préciser votre rôle."

// Other sans localisation
"Veuillez sélectionner votre localisation."

// Other (Resort) sans resort
"Veuillez préciser le nom de votre resort."

// Other (BU) sans BU
"Veuillez préciser votre Business Unit."
```

---

## 📊 Mapping automatique

### Tableau de correspondance

| Rôle sélectionné | Location auto | Champ additionnel |
|------------------|---------------|-------------------|
| Room Division Manager | `resort` | `resort` (texte libre) |
| Planning Manager | `resort` | `resort` (texte libre) |
| Produits & Services Manager | `business_unit` | `businessUnit` (dropdown EMEA/ESAP/NAM/SAM) |
| Other | **manuel** | `location` (dropdown) + resort/BU selon choix |

---

## 🎯 Affichage Dashboard Admin

### Badge localisation

**Room Division Manager :**
```html
<span class="badge badge-resort">Les Arcs Panorama (ARPC)</span>
```

**Planning Manager :**
```html
<span class="badge badge-resort">Phuket (PHUC)</span>
```

**Produits & Services Manager :**
```html
<span class="badge badge-bu">EMEA</span>
```

**Other (Siège) :**
```html
<span class="badge badge-siege">Siège Social</span>
```

### Détail expert (modal)

**Room Division Manager - Les Arcs :**
```
Rôle: Room Division Manager
Localisation: Les Arcs Panorama (ARPC)
Date soumission: 18/06/2026 14:30
```

**Produits & Services Manager - EMEA :**
```
Rôle: Produits & Services Manager
Localisation: EMEA
Date soumission: 18/06/2026 15:45
```

---

## 🧪 Scénarios de test

### Test 1 : Room Division Manager
1. Sélectionner "Room Division Manager"
2. ✅ Champ resort apparaît
3. ✅ Champ localisation n'apparaît PAS
4. Entrer "Les Arcs Panorama (ARPC)"
5. ✅ Validation OK
6. ✅ Données : `location = "resort"`, `resort = "Les Arcs Panorama (ARPC)"`

### Test 2 : Planning Manager
1. Sélectionner "Planning Manager"
2. ✅ Champ resort apparaît
3. Laisser resort vide
4. Cliquer "Commencer"
5. ✅ Message erreur : "Veuillez préciser dans quel resort vous travaillez."

### Test 3 : Produits & Services Manager
1. Sélectionner "Produits & Services Manager"
2. ✅ Dropdown BU apparaît (EMEA/ESAP/NAM/SAM)
3. ✅ Champ localisation n'apparaît PAS
4. Sélectionner "EMEA"
5. ✅ Validation OK
6. ✅ Données : `location = "business_unit"`, `businessUnit = "EMEA"`

### Test 4 : Other → Resort
1. Sélectionner "Other"
2. ✅ Champ "Précisez votre rôle" apparaît
3. ✅ Dropdown "Localisation" apparaît
4. Entrer "Revenue Manager"
5. Sélectionner "Resort / Village"
6. ✅ Champ "Nom du Resort" apparaît
7. Entrer "Cefalù (CFAC)"
8. ✅ Validation OK
9. ✅ Données : `role = "Revenue Manager"`, `location = "resort"`, `resort = "Cefalù (CFAC)"`

### Test 5 : Other → Siège
1. Sélectionner "Other"
2. Entrer "Responsable Fidélité"
3. Sélectionner "Siège Social"
4. ✅ Aucun champ additionnel n'apparaît
5. ✅ Validation OK
6. ✅ Données : `role = "Responsable Fidélité"`, `location = "siege"`, `resort = null`, `businessUnit = null`

---

## 💡 Avantages de cette logique

### ✅ Simplification UX
- **Moins de clics** : Pas besoin de sélectionner manuellement "Resort" pour Room Division/Planning Manager
- **Moins d'erreurs** : Les champs conditionnels guident naturellement l'utilisateur
- **Plus rapide** : 3 champs au lieu de 5 pour les rôles standards

### ✅ Cohérence métier
- **Room Division et Planning Managers** sont **toujours** en resort → pas besoin de demander
- **Produits & Services Managers** sont **toujours** en BU → pas besoin de demander
- Seul "Other" nécessite de préciser la localisation

### ✅ Qualité des données
- **BU standardisées** : Dropdown avec valeurs fixes (EMEA, ESAP, NAM, SAM) au lieu de texte libre
- **Moins de typos** : Les valeurs critiques sont contraintes
- **Meilleure exploitation** : Filtres et stats par BU facilitées

---

## 📊 Statistiques dashboard par localisation

### Filtres intelligents

**Par rôle :**
- Room Division Managers → Tous en resort
- Planning Managers → Tous en resort
- Produits & Services Managers → Tous en BU
- Other → Mixte (à filtrer ensuite)

**Par BU (pour Produits & Services) :**
- EMEA : X experts
- ESAP : Y experts
- NAM : Z experts
- SAM : W experts

**Par type de localisation :**
- Resorts : Room Div + Planning + Other(resort)
- BU : Produits & Services + Other(BU)
- Siège : Other(siege) uniquement

---

## 🔄 Migration des données existantes

Les données V1.0/V1.1 restent compatibles :

```javascript
// Ancienne structure (toujours valide)
{
  "role": "room_division_manager",
  "location": "resort",
  "resort": "Les Arcs Panorama"
}

// Nouvelle structure (identique !)
{
  "role": "room_division_manager",
  "location": "resort",  // Auto-défini
  "resort": "Les Arcs Panorama"
}
```

**Aucune migration nécessaire** ✅

---

## 📞 Support

**Questions sur la logique :**
- Slack : `#odyssey-product`
- Email : product-odyssey@clubmed.com

---

**Version :** 1.2  
**Auteur :** Équipe Produit Odyssey  
**Date :** 18 juin 2026
