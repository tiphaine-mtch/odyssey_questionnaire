# Version 1.3 - Système de traduction FR/EN

**Date :** 18 juin 2026  
**Équipe :** Produit Odyssey

---

## ✨ Nouvelles fonctionnalités

### 🌍 Traduction français / anglais

Le questionnaire est désormais **entièrement traduit** en français et anglais avec un **sélecteur de langue** dans le header.

#### Fonctionnalités
- ✅ **Sélecteur de langue** : Boutons 🇫🇷 FR / 🇬🇧 EN dans le header
- ✅ **Traduction instantanée** : Changement de langue sans rechargement
- ✅ **Persistance** : La langue choisie est sauvegardée dans localStorage
- ✅ **Traduction complète** : Tous les textes UI sont traduits
- ✅ **Placeholders traduits** : Les champs de saisie aussi

---

## 🎯 Clarification du contexte

### Titres et sous-titres mis à jour

#### Questionnaire Expert
```
☀️ Club Med - Odyssey PMS
Questionnaire Experts - Calendrier des Chambres
Construction des règles métier pour la fonctionnalité 
de planning et gestion des réservations
```

#### Dashboard Admin
```
☀️ Odyssey - Admin Dashboard
Gestion des réponses experts - Calendrier des Chambres
```

#### Page d'identification
```
Contexte : Ce questionnaire vise à collecter votre expertise 
pour construire la fonctionnalité de calendrier des chambres 
du PMS Odyssey (gestion des réservations, check-in/out, 
programme fidélité, capacités resorts).
```

---

## 📋 Éléments traduits

### Header
| Français | English |
|----------|---------|
| Questionnaire Experts - Calendrier des Chambres | Expert Questionnaire - Room Calendar |
| Construction des règles métier pour la fonctionnalité de planning et gestion des réservations | Building business rules for the planning and reservation management feature |

### Identification
| Français | English |
|----------|---------|
| 👤 Identification | 👤 Identification |
| Nom complet | Full name |
| Rôle / Fonction | Role / Position |
| Room Division Manager | Room Division Manager |
| Planning Manager | Planning Manager |
| Produits & Services Manager | Products & Services Manager |
| Other | Other |
| Précisez votre rôle | Specify your role |
| Dans quel resort travaillez-vous ? | Which resort do you work in? |
| Dans quelle Business Unit travaillez-vous ? | Which Business Unit do you work in? |
| Localisation | Location |
| Siège Social | Headquarters |
| Business Unit | Business Unit |
| Resort / Village | Resort / Village |

### Boutons
| Français | English |
|----------|---------|
| Commencer le questionnaire → | Start questionnaire → |
| ← Retour | ← Back |
| Voir le résumé → | View summary → |
| ← Modifier mes réponses | ← Modify my answers |
| ✅ Soumettre mes réponses | ✅ Submit my answers |
| Recommencer | Start over |
| 📄 Télécharger JSON | 📄 Download JSON |
| 📊 Télécharger CSV | 📊 Download CSV |

### Progression
| Français | English |
|----------|---------|
| Progression : | Progress: |
| réponses | answers |

### Alerts & Messages
| Français | English |
|----------|---------|
| 📅 Contexte : Calendrier des Chambres | 📅 Context: Room Calendar |
| Ce questionnaire porte sur les règles métier du calendrier de planning des chambres | This questionnaire covers the business rules for the room planning calendar |
| 💡 Comment répondre ? | 💡 How to answer? |
| Répondez aux questions pour lesquelles vous avez l'expertise opérationnelle | Answer questions for which you have operational expertise |
| Laissez vide si vous ne savez pas | Leave blank if you don't know |
| Utilisez la zone "Questions/Commentaires" pour demander des clarifications | Use the "Questions/Comments" section to request clarifications |
| Vos réponses sont sauvegardées automatiquement | Your answers are saved automatically |

### Page de succès
| Français | English |
|----------|---------|
| Merci pour votre contribution ! | Thank you for your contribution! |
| Vos réponses ont été enregistrées et seront analysées par l'équipe produit Odyssey | Your answers have been saved and will be analyzed by the Odyssey product team |
| Référence : | Reference: |
| 📥 Télécharger vos réponses | 📥 Download your answers |
| Conservez une copie de vos réponses pour référence future | Keep a copy of your answers for future reference |

---

## 🔧 Implémentation technique

### Structure du système de traduction

```javascript
const translations = {
    fr: {
        'header.title': 'Questionnaire Experts - Calendrier des Chambres',
        'form.name': 'Nom complet',
        'btn.start': 'Commencer le questionnaire →',
        // ... 40+ clés
    },
    en: {
        'header.title': 'Expert Questionnaire - Room Calendar',
        'form.name': 'Full name',
        'btn.start': 'Start questionnaire →',
        // ... 40+ clés
    }
};
```

### Attributs HTML

#### Texte simple
```html
<div data-i18n="header.title">Questionnaire Experts</div>
```

#### Placeholders
```html
<input data-i18n-placeholder="form.name.placeholder" placeholder="Ex: Marie Dupont">
```

### Fonction setLanguage()

```javascript
function setLanguage(lang) {
    currentLanguage = lang;
    localStorage.setItem('odyssey_lang', lang);

    // Update buttons
    document.getElementById('lang-fr').classList.toggle('active', lang === 'fr');
    document.getElementById('lang-en').classList.toggle('active', lang === 'en');

    // Update text content
    document.querySelectorAll('[data-i18n]').forEach(el => {
        const key = el.getAttribute('data-i18n');
        if (translations[lang][key]) {
            el.innerHTML = translations[lang][key];
        }
    });

    // Update placeholders
    document.querySelectorAll('[data-i18n-placeholder]').forEach(el => {
        const key = el.getAttribute('data-i18n-placeholder');
        if (translations[lang][key]) {
            el.placeholder = translations[lang][key];
        }
    });
}
```

### Persistance

```javascript
// Sauvegarde de la langue choisie
localStorage.setItem('odyssey_lang', 'en');

// Chargement au démarrage
const savedLang = localStorage.getItem('odyssey_lang') || 'fr';
setLanguage(savedLang);
```

---

## 🎨 Design du sélecteur

### Position
- **Desktop** : En haut à droite du header (position absolue)
- **Mobile** : Centré sous le titre (position statique)

### Style
```css
.language-switcher {
    background: rgba(255, 255, 255, 0.1);
    padding: 4px;
    border-radius: 8px;
}

.lang-btn {
    background: transparent;
    border: 2px solid transparent;
    color: white;
    font-weight: 600;
}

.lang-btn.active {
    background: var(--color-brand-saffran-yellow);
    color: var(--color-brand-black-coal);
}
```

### Exemple visuel

```
┌─────────────────────────────────────────────────┐
│ ☀️ Club Med - Odyssey PMS        [🇫🇷 FR][🇬🇧 EN]│
│ Questionnaire Experts - Calendrier des Chambres │
└─────────────────────────────────────────────────┘
```

---

## 🧪 Tests

### Scénario 1 : Premier chargement
1. Ouvrir le questionnaire
2. ✅ Langue par défaut : Français
3. ✅ Bouton FR actif (jaune)
4. ✅ Tous les textes en français

### Scénario 2 : Changement de langue
1. Cliquer sur 🇬🇧 EN
2. ✅ Traduction instantanée (pas de rechargement)
3. ✅ Bouton EN actif
4. ✅ Tous les textes en anglais
5. ✅ Placeholders des inputs traduits

### Scénario 3 : Persistance
1. Sélectionner anglais
2. Fermer le navigateur
3. Rouvrir le questionnaire
4. ✅ Interface en anglais automatiquement

### Scénario 4 : Responsive
1. Ouvrir sur mobile
2. ✅ Sélecteur centré sous le titre
3. ✅ Fonctionnel sur petit écran

### Scénario 5 : Remplissage formulaire
1. Sélectionner anglais
2. Remplir formulaire
3. Changer en français
4. ✅ Les données saisies sont conservées
5. ✅ Les labels sont traduits

---

## 📊 Couverture de traduction

### Sections traduites ✅
- [x] Header (titre + sous-titre)
- [x] Progression bar
- [x] Page identification (titre + description)
- [x] Tous les champs du formulaire
- [x] Labels des champs
- [x] Placeholders
- [x] Options des dropdowns (rôles, localisation)
- [x] Boutons d'action
- [x] Alertes informatives
- [x] Page de succès
- [x] Messages de téléchargement

### Sections NON traduites (contenus dynamiques) ⚠️
- [ ] Questions métier (Q1.1, Q1.2, etc.) - À traduire séparément
- [ ] Commentaires des experts - Saisis en langue choisie
- [ ] Nom des resorts - Noms propres (pas de traduction)
- [ ] Business Units - Acronymes standards (EMEA, ESAP, NAM, SAM)

---

## 🔜 Prochaines étapes

### Phase 2 : Traduction des questions
- [ ] Ajouter traductions pour toutes les questions métier
- [ ] Section Programme Fidélité (Q1.1, Q1.2, etc.)
- [ ] Section Check-in/out
- [ ] Section Capacités
- [ ] Options de réponses (choix multiples)

### Phase 3 : Traduction Dashboard Admin
- [ ] Ajouter sélecteur de langue dans le dashboard
- [ ] Traduire les KPIs
- [ ] Traduire les labels de colonnes
- [ ] Traduire les filtres
- [ ] Traduire les exports

### Phase 4 : Formats d'export
- [ ] Export CSV avec headers traduits selon langue
- [ ] Export Markdown avec titres traduits
- [ ] Rapport synthèse bilingue

---

## 💡 Bonnes pratiques

### Ajouter une nouvelle traduction

1. **Ajouter la clé dans l'objet translations**
```javascript
fr: {
    'new.key': 'Texte en français'
},
en: {
    'new.key': 'Text in English'
}
```

2. **Ajouter l'attribut data-i18n dans le HTML**
```html
<div data-i18n="new.key">Texte en français</div>
```

3. **Tester les deux langues**

### Convention de nommage des clés

```
section.element.variant
```

**Exemples :**
- `header.title` → Titre principal du header
- `form.name` → Label du champ nom
- `form.name.placeholder` → Placeholder du champ nom
- `btn.start` → Bouton "Commencer"
- `alert.info.title` → Titre de l'alerte informative

---

## 🌐 Langues supportées

| Langue | Code | Flag | Statut |
|--------|------|------|--------|
| **Français** | `fr` | 🇫🇷 | ✅ Complet |
| **English** | `en` | 🇬🇧 | ✅ Complet |

---

## 📞 Support

**Questions traduction :**
- Slack : `#odyssey-product`
- Email : product-odyssey@clubmed.com

---

**Version :** 1.3  
**Auteur :** Équipe Produit Odyssey  
**Date :** 18 juin 2026
