# Version 2.0 - Questions dynamiques depuis JSON

**Date :** 18 juin 2026  
**Équipe :** Produit Odyssey

---

## 🎉 Changements majeurs

### Architecture refactorée

**Avant (v1.3) :**
- Questions en dur dans le HTML
- Difficile d'ajouter/modifier des questions
- Code HTML très long et répétitif
- 2 questions exemples seulement

**Après (v2.0) :**
- ✅ Questions dans un fichier JSON séparé
- ✅ HTML génère dynamiquement les questions au chargement
- ✅ Facile d'ajouter/modifier des questions
- ✅ **11 questions complètes Business intégrées**
- ✅ Traduction FR/EN automatique depuis le JSON
- ✅ Code HTML plus court et maintenable

---

## 📊 Questions intégrées (11 questions)

### 👥 Programme Fidélité (4 questions)

#### Q1 : Surclassement automatique
- Niveau surclassement (N+1 vs multiple)
- Moment vérification disponibilité
- Gestion N+2 pour Platinum
- Chambres communicantes

#### Q2 : Late Check-out tarification
- Tarif 14h Silver/Turquoise
- Tarifs 16h par niveau
- Existence late 18h
- Gestion non-disponibilité

#### Q3 : Early Check-in
- Définition early check-in
- Qui décide disponibilité
- Tarif Turquoise
- Déjeuner inclus

#### Q4 : Politique Annulation
- Définition J-7
- Heure limite
- Annulation partielle groupe
- No-show facturation

### 📅 Gestion Overbooking (2 questions)

#### Q5 : Seuils acceptables
- Overbooking volontaire autorisé
- Seuil alerte
- Qui résout
- Compensation standard

#### Q6 : Ordre priorité
- Ordre détaillé
- Choix entre plusieurs Turquoise
- Compensation par statut
- Transport autre resort

### 🧹 Housekeeping (2 questions)

#### Q7 : Cycle Clean → Dirty → Clean
- Quand passage Dirty
- Validation Inspected → Clean
- Délai nettoyage
- Conflit fidélité vs timing

#### Q8 : Maintenance
- Qui peut bloquer
- Préavis minimum
- Gestion résa existante
- Système CMMS

### 🏢 Groupes (1 question)

#### Q9 : Gestion groupes
- Définition nombre chambres
- Remise automatique
- Proximité géographique
- Check-in processus
- Annulation partielle

### 📬 Notifications (2 questions)

#### Q10 : Emails clients
- Confirmation contenu
- Rappel J-7 heure
- Rappel J-1 contenu
- Remerciement post-séjour
- Email upgrade timing

#### Q11 : Notifications internes
- Arrivée Platinum destinataires
- Format notifications
- No-show alerte
- Chambre pas Clean alerte

---

## 🏗️ Architecture technique

### Fichiers

```
outil-collaboratif-experts/
├── questions-business-only.json        # Données questions (11 questions)
├── odyssey-questionnaire-experts.html  # Chargement dynamique
└── odyssey-expert-admin-dashboard.html # Visualisation réponses
```

### Structure JSON

```json
{
  "metadata": {
    "version": "1.0",
    "totalQuestions": 11,
    "audience": "Experts opérationnels Club Med"
  },
  "sections": [
    {
      "id": "loyalty",
      "icon": "👥",
      "title": {"fr": "...", "en": "..."},
      "questions": [
        {
          "id": "q1_1",
          "number": "Q1",
          "title": {"fr": "...", "en": "..."},
          "context": {"fr": "...", "en": "..."},
          "items": [
            {
              "id": "q1_1_1",
              "type": "radio|select|checkbox|number|textarea",
              "label": {"fr": "...", "en": "..."},
              "required": true|false,
              "options": [...]
            }
          ]
        }
      ]
    }
  ]
}
```

### Types de questions supportés

| Type | Description | Exemple |
|------|-------------|---------|
| **radio** | Choix unique | N+1 vs multiple levels |
| **select** | Dropdown | J-7, J-3, J-1, check-in |
| **checkbox** | Choix multiples | Destinataires notification |
| **number** | Valeur numérique | Tarif en €, délai en minutes |
| **textarea** | Texte libre long | Description processus |

### Chargement dynamique

```javascript
// 1. Chargement JSON au démarrage
await loadQuestions();

// 2. Génération HTML
renderQuestions();

// 3. Attachement event listeners
attachAutoSaveListeners();

// 4. Changement de langue → re-render
setLanguage('en');
```

---

## ✨ Fonctionnalités

### 1. Questions chargées depuis JSON ✅
- Fichier `questions-business-only.json`
- 11 questions complètes
- Traduction FR/EN intégrée

### 2. Génération dynamique HTML ✅
- Fonction `renderQuestions()`
- Génère sections, questions, items
- Support tous types de champs

### 3. Traduction à la volée ✅
- Changement langue → re-render questions
- Sauvegarde réponses avant re-render
- Restaure réponses après

### 4. Sauvegarde automatique ✅
- Auto-save à chaque changement
- Support checkboxes (tableaux)
- LocalStorage persistant

### 5. Progression dynamique ✅
- Calcul basé sur questions JSON
- Exclusion champs commentaires
- Visual feedback (cards vertes)

---

## 🎯 Avantages

### Pour l'équipe produit

✅ **Ajout question facile**
```json
// Ajouter dans questions-business-only.json
{
  "id": "q5_3",
  "number": "Q12",
  "title": {"fr": "Nouvelle question", "en": "New question"},
  "items": [...]
}
```

✅ **Modification rapide**
- Changer un label : modifier JSON
- Pas besoin toucher HTML
- Déploiement immédiat

✅ **Traduction centralisée**
- FR et EN dans le même fichier
- Pas de duplication
- Cohérence garantie

### Pour les experts

✅ **11 questions complètes**
- Toutes les questions Business
- Bien organisées par section
- Contexte clair pour chaque question

✅ **Interface bilingue**
- FR/EN à la demande
- Questions traduites
- Placeholders traduits

✅ **Progression claire**
- Barre de progression
- Compteur réponses
- Visual feedback

---

## 📋 Scope des questions

### ✅ Inclus : Questions Business (11)
Adressées aux **experts opérationnels** :
- Room Division Manager
- Planning Manager  
- Produits & Services Manager

Sujets :
- Programme fidélité
- Overbooking
- Housekeeping
- Groupes
- Notifications

### ❌ Exclus : Questions Design (14)
À adresser à l'**équipe Design** :
- Composants PMS Figma
- Échelle typographique
- Bibliothèque icônes
- Shadows & elevation
- Animations
- Dark mode
- Responsive
- Accessibilité WCAG

### ❌ Exclus : Questions Tech (13)
À adresser à l'**équipe Tech** :
- Stack backend/frontend
- Architecture temps réel
- Intégrations API (CRS, Stripe, SendGrid...)
- Sécurité & Auth
- Infrastructure cloud
- Tests & qualité

**Raison :** Les experts opérationnels ne peuvent pas répondre aux questions techniques ou design.

---

## 🚀 Déploiement

### Prérequis
- Serveur web pour servir le JSON (CORS)
- Ou hébergement static (GitHub Pages, Netlify, etc.)

### Test local

```bash
# Serveur Python simple
cd outil-collaboratif-experts
python3 -m http.server 8000

# Ouvrir
http://localhost:8000/odyssey-questionnaire-experts.html
```

### Production

1. **Upload fichiers** :
   - `odyssey-questionnaire-experts.html`
   - `questions-business-only.json`
   - `club-med-trident-design-tokens.css`

2. **Partager URL** aux experts

3. **Dashboard admin** :
   - `odyssey-expert-admin-dashboard.html`
   - Consulter réponses
   - Export JSON/CSV/Markdown

---

## 🔧 Maintenance

### Ajouter une question

1. Ouvrir `questions-business-only.json`
2. Ajouter dans la section appropriée :

```json
{
  "id": "q6_1",
  "number": "Q12",
  "title": {
    "fr": "Titre question",
    "en": "Question title"
  },
  "context": {
    "fr": "Contexte...",
    "en": "Context..."
  },
  "items": [
    {
      "id": "q6_1_1",
      "type": "radio",
      "required": true,
      "label": {
        "fr": "Label français",
        "en": "English label"
      },
      "options": [
        {"value": "opt1", "label": {"fr": "Option 1", "en": "Option 1"}},
        {"value": "opt2", "label": {"fr": "Option 2", "en": "Option 2"}}
      ]
    }
  ]
}
```

3. Sauvegarder
4. Recharger page → Question apparaît automatiquement

### Modifier une question

1. Trouver l'ID dans `questions-business-only.json`
2. Modifier le texte FR/EN
3. Sauvegarder
4. Les experts voient la modification immédiatement

### Supprimer une question

1. Retirer du JSON
2. Sauvegarder
3. Question disparaît du questionnaire

---

## 📊 Données générées

### Format réponse (localStorage)

```json
{
  "id": "ODYSSEY-1718703600000",
  "expert": {
    "name": "Marie Dupont",
    "role": "room_division_manager",
    "location": "resort",
    "resort": "Les Arcs Panorama (ARPC)"
  },
  "answers": {
    "q1_1_1": "n_plus_1",
    "q1_1_2": "j_3",
    "q1_2_1": "30",
    "q1_2_2_gold": "50",
    "q3_2_1": ["reception", "maintenance"],
    "q5_1_1": ["booking_ref", "dates", "price"]
  },
  "submittedAt": "2026-06-18T14:30:00Z"
}
```

### Checkboxes = tableaux

```json
"q3_2_1": ["reception", "maintenance", "revenue"]
```

### Radio/Select = string

```json
"q1_1_1": "n_plus_1"
```

### Number = string

```json
"q1_2_1": "30"
```

---

## ✅ Checklist migration

### Code
- [x] Créer `questions-business-only.json` avec 11 questions
- [x] Fonction `loadQuestions()` 
- [x] Fonction `renderQuestions()`
- [x] Support tous types (radio, select, checkbox, number, textarea)
- [x] Traduction dynamique
- [x] Auto-save avec checkboxes
- [x] Progression dynamique
- [x] Restore answers après changement langue

### Questions intégrées
- [x] Q1 : Surclassement (4 items)
- [x] Q2 : Late checkout (7 items)
- [x] Q3 : Early check-in (4 items)
- [x] Q4 : Annulation (4 items)
- [x] Q5 : Overbooking seuils (4 items)
- [x] Q6 : Overbooking priorité (4 items)
- [x] Q7 : Cycle Clean (4 items)
- [x] Q8 : Maintenance (4 items)
- [x] Q9 : Groupes (5 items)
- [x] Q10 : Emails clients (5 items)
- [x] Q11 : Notifications internes (4 items)

**Total : 11 questions, 49 items**

---

## 🎓 Formation équipe

### Qui doit remplir ?

**Experts opérationnels uniquement :**
- Room Division Manager (resort)
- Planning Manager (resort)
- Produits & Services Manager (BU)

**PAS les équipes :**
- ❌ Design (questions techniques design)
- ❌ Tech (questions techniques code/infra)

### Instructions experts

1. Ouvrir le questionnaire
2. S'identifier (nom, rôle, resort/BU)
3. Répondre aux 11 questions
4. Utiliser zone commentaire si besoin clarification
5. Soumettre

**Durée estimée :** 20-30 minutes

---

## 📞 Support

**Questions technique (JSON, chargement) :**
- Slack : `#odyssey-pms-dev`
- Email : dev-odyssey@clubmed.com

**Questions contenu (ajouter/modifier questions) :**
- Slack : `#odyssey-product`
- Email : product-odyssey@clubmed.com

---

**Version :** 2.0  
**Auteur :** Équipe Produit Odyssey  
**Date :** 18 juin 2026
