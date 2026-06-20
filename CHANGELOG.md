# 📝 Changelog - Questionnaire Experts Odyssey

## Version 2.0 - 19 juin 2026 🌓📱

### ✨ Nouveautés majeures

#### 🌓 Dark Mode
- ✅ Détection automatique du mode système (`prefers-color-scheme: dark`)
- ✅ Variables CSS pour thématisation complète
- ✅ Support manuel avec classe `.dark-mode` (optionnel)
- ✅ Compatible tous OS (Windows, macOS, Linux, iOS, Android)
- ✅ Transitions douces entre modes

#### 📱 Responsive Design
- ✅ **Mobile** (320px - 768px) : Layout vertical, boutons pleine largeur
- ✅ **Tablet** (769px - 1024px) : Grilles adaptatives
- ✅ **Desktop** (1025px+) : Affichage optimal multi-colonnes
- ✅ Touch-friendly : boutons 44px min, inputs 16px (anti-zoom iOS)

#### 🎨 CSS Moderne
- ✅ Typographie fluide : `clamp(20px, 5vw, 28px)`
- ✅ Fichier externe `responsive-dark-mode.css`
- ✅ Media queries optimisées
- ✅ Transitions et animations douces

#### 🚀 GitHub Pages
- ✅ Fichier `index.html` avec redirection automatique
- ✅ Page d'accueil stylée avec spinner
- ✅ URL publique : `https://tiphaine-mtch.github.io/odyssey_questionnaire/`
- ✅ Partage facilité avec les experts

### 📦 Fichiers modifiés

#### Questionnaire (`odyssey-questionnaire-experts-STANDALONE.html`)
- Import du nouveau `responsive-dark-mode.css`
- Variables CSS pour light/dark modes
- Header responsive avec `clamp()`
- Language switcher adaptatif (centré sur mobile)

#### Dashboard Admin (`odyssey-expert-admin-dashboard.html`)
- Variables CSS dark mode intégrées
- Dashboard grid responsive (1 colonne mobile)
- Expert list adaptative (colonnes masquées sur mobile)
- Badges avec variantes dark mode
- Filtres empilés verticalement sur mobile
- Boutons pleine largeur sur petit écran

#### Documentation
- `README.md` mis à jour avec sections dark mode et responsive
- `CHANGELOG.md` restructuré avec émojis et clarté

### 🎨 Design System

#### Variables CSS créées
```css
/* Light mode */
--bg-primary: #ffffff
--text-primary: #000000
--border-color: #e0e0e0

/* Dark mode */
--bg-primary: #1a1a1a
--text-primary: #ffffff
--border-color: #404040
```

#### Breakpoints standards
- Mobile: `max-width: 768px`
- Tablet: `769px - 1024px`
- Desktop: `min-width: 1025px`

### 🐛 Corrections
- Fix header cassé sur mobile (flex-wrap)
- Fix language switcher hors cadre (position static mobile)
- Fix grilles non adaptatives (grid: 1fr mobile)
- Fix zoom iOS sur inputs (font-size 16px)
- Fix boutons export trop étroits (width: 100% mobile)

---

## Version 1.1 - 18 juin 2026

### ✨ Améliorations apportées

#### 1. **Simplification des rôles**
- ✅ Remplacé les 8 rôles par 4 postes standards :
  - Room Division Manager
  - Planning Manager
  - Produits & Services Manager
  - Other (avec champ texte libre obligatoire)

#### 2. **Suppression du champ email**
- ✅ Email professionnel retiré du formulaire d'identification
- Seul le nom complet est demandé
- Simplifie la collecte de données
- Plus conforme RGPD

#### 3. **Resort obligatoire pour experts resort**
- ✅ Champ "Nom du Resort" désormais **obligatoire** si localisation = Resort
- Validation ajoutée avant de démarrer le questionnaire
- Permet une meilleure traçabilité des réponses

#### 4. **Amélioration affichage Dashboard Admin**

##### a) Fonctionnalité de suppression
- ✅ Bouton "🗑️" ajouté sur chaque ligne expert
- Confirmation avant suppression
- Mise à jour automatique des statistiques après suppression
- Suppression définitive du localStorage

##### b) Affichage des réponses humanisé
- ✅ **Labels de questions** : `q1_1_1` → "Niveau de surclassement"
- ✅ **Labels de rôles** : `room_division_manager` → "Room Division Manager"
- ✅ **Formatage des réponses** :
  - Radio buttons : `n_plus_1` → "Toujours N+1"
  - Prix : `30` → "30 €"
  - Dates : `j_7` → "J-7 (7 jours avant)"
- ✅ **Localisation formatée** : Affichage direct du nom du resort au lieu de "Resort: ARPC"

##### c) Modal expert détaillé
- ✅ Card avec fond coloré pour les infos principales
- ✅ Questions organisées en cards distinctes
- ✅ Réponses avec barre latérale jaune pour meilleure lisibilité
- ✅ Commentaires affichés en italique sous les réponses

##### d) Exports améliorés
- ✅ **CSV** : Colonnes humanisées (plus d'email, labels lisibles)
- ✅ **Markdown** : Questions et réponses formatées avec labels
- ✅ **Rapport synthèse** : Questions groupées avec labels complets

---

## Exemples de formatage

### Avant (v1.0)
```
Question: q1_1_1
Réponse: n_plus_1
Expert: marie.dupont@clubmed.com
Rôle: chef_reception
```

### Après (v1.1)
```
Question: Niveau de surclassement
Réponse: Toujours N+1
Expert: Marie Dupont
Rôle: Room Division Manager
Localisation: Les Arcs Panorama (ARPC)
```

---

## Structure grid mise à jour

### Liste experts (Dashboard)
```
Colonne 1: Infos expert (avatar + nom + rôle badge)
Colonne 2: Localisation (badge)
Colonne 3: Progression (barre + pourcentage)
Colonne 4: Taux complétion (%)
Colonne 5: Bouton "Voir détails"
Colonne 6: Bouton "🗑️" suppression
```

---

## Mapping des labels

### Questions
| Code technique | Label humanisé |
|----------------|----------------|
| `q1_1` | Surclassement automatique |
| `q1_2` | Late Check-out tarification |
| `q1_1_1` | Niveau de surclassement |
| `q1_1_2` | Moment de vérification disponibilité |
| `q1_1_3` | Surclassement N+2 pour Platinum |
| `q1_2_1` | Tarif late checkout 14h (Silver/Turquoise) |
| `q1_2_2_gold` | Tarif late checkout 16h Gold |
| `q1_2_2_silver` | Tarif late checkout 16h Silver |
| `q1_2_2_turquoise` | Tarif late checkout 16h Turquoise |

### Rôles
| Code technique | Label humanisé |
|----------------|----------------|
| `room_division_manager` | Room Division Manager |
| `planning_manager` | Planning Manager |
| `produits_services_manager` | Produits & Services Manager |
| `other` | Autre |

### Réponses radio
| Code technique | Label humanisé |
|----------------|----------------|
| `n_plus_1` | Toujours N+1 |
| `multiple` | Peut sauter plusieurs niveaux |
| `depends` | Dépend du statut |
| `j_7` | J-7 (7 jours avant) |
| `j_3` | J-3 (3 jours avant) |
| `j_1` | J-1 (veille) |
| `checkin` | Au moment du check-in |
| `auto_n2` | Surclassement automatique N+2 |
| `proposition` | Proposition avec validation |
| `manual` | Validation manuelle uniquement |
| `yes` | Oui |
| `no` | Non |

---

## Fonctions JavaScript ajoutées

### Dashboard Admin

```javascript
// Conversion des codes en labels lisibles
getRoleLabel(role)           // "room_division_manager" → "Room Division Manager"
getQuestionLabel(key)        // "q1_1_1" → "Niveau de surclassement"
formatAnswer(key, value)     // "n_plus_1" → "Toujours N+1" ou "30" → "30 €"

// Suppression de réponse
deleteSubmission(submissionId)  // Supprime + refresh + confirmation
```

---

## Tests à effectuer

### ✅ Questionnaire Expert
- [ ] Sélectionner "Room Division Manager" → Pas de champ "Autre"
- [ ] Sélectionner "Other" → Champ texte obligatoire apparaît
- [ ] Sélectionner "Resort" sans remplir nom → Validation bloque
- [ ] Soumettre formulaire complet → Données sauvegardées sans email

### ✅ Dashboard Admin
- [ ] Voir liste experts → Rôles affichés en badge lisible
- [ ] Cliquer "Voir détails" → Modal avec questions formatées
- [ ] Cliquer "🗑️" → Confirmation puis suppression
- [ ] Exporter CSV → Colonnes humanisées
- [ ] Exporter Markdown → Questions et réponses lisibles
- [ ] Exporter Rapport synthèse → Labels complets

---

## Migration données existantes

Si des données V1.0 existent dans localStorage :

```javascript
// Les données restent compatibles
// L'email sera simplement ignoré dans les exports
// Les anciens codes role seront convertis automatiquement via getRoleLabel()
```

Aucune migration nécessaire ! 🎉

---

## Prochaines étapes possibles

### Features en attente
- [ ] Filtres avancés (par resort, par rôle)
- [ ] Recherche dans les réponses
- [ ] Comparaison de 2 experts côte à côte
- [ ] Statistiques par question (consensus, divergences)
- [ ] Export PDF avec graphiques
- [ ] API backend pour sync multi-utilisateurs
- [ ] Notifications email aux experts
- [ ] Dashboard temps réel avec WebSocket

---

**Version :** 1.1  
**Date :** 18 juin 2026  
**Auteur :** Équipe Produit Odyssey
