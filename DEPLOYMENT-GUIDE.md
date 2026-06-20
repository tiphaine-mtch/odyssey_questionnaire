# 🚀 Guide de déploiement - Questionnaire Experts Odyssey

## ✅ Modifications terminées (v2.0)

### 🌓 Dark Mode
- ✅ Variables CSS pour light/dark modes
- ✅ Détection automatique OS avec `prefers-color-scheme`
- ✅ Support manuel avec classe `.dark-mode`
- ✅ Tous les composants compatibles (badges, cards, boutons, inputs)

### 📱 Responsive Design
- ✅ Mobile (320px - 768px) : layout vertical optimisé
- ✅ Tablet (769px - 1024px) : grilles adaptatives
- ✅ Desktop (1025px+) : affichage multi-colonnes
- ✅ Typographie fluide avec `clamp()`
- ✅ Touch-friendly (44px min, font-size 16px)

### 📦 Fichiers prêts
- ✅ `index.html` - Page d'accueil avec redirection
- ✅ `odyssey-questionnaire-experts-STANDALONE.html` - Questionnaire (117K)
- ✅ `odyssey-expert-admin-dashboard.html` - Dashboard admin (43K)
- ✅ `responsive-dark-mode.css` - Styles responsive + dark mode (11K)
- ✅ `questions-business-only.json` - 11 questions métiers (36K)
- ✅ `README.md` - Documentation complète (13K)
- ✅ `CHANGELOG.md` - Historique des versions (8.3K)

---

## 🌐 Déploiement GitHub Pages

### Étape 1 : Vérifier les fichiers

Dans le dossier `outil-collaboratif-experts/`, vous devez avoir :

```
✅ index.html
✅ odyssey-questionnaire-experts-STANDALONE.html
✅ odyssey-expert-admin-dashboard.html
✅ responsive-dark-mode.css
✅ club-med-trident-design-tokens.css
✅ questions-business-only.json
✅ README.md
✅ CHANGELOG.md
```

### Étape 2 : Commit et push vers GitHub

```bash
cd "/mnt/c/Users/metchti/Planning calendar/outil-collaboratif-experts"

# Ajouter tous les fichiers modifiés
git add index.html
git add odyssey-questionnaire-experts-STANDALONE.html
git add odyssey-expert-admin-dashboard.html
git add responsive-dark-mode.css
git add README.md
git add CHANGELOG.md

# Créer un commit
git commit -m "v2.0: Add dark mode and responsive design

- Dark mode with automatic OS detection
- Responsive layout for mobile, tablet, desktop
- New landing page (index.html)
- Updated CSS with modern variables
- Enhanced admin dashboard
- Updated documentation"

# Pousser vers GitHub
git push origin main
```

### Étape 3 : Activer GitHub Pages (si pas déjà fait)

1. Aller sur `https://github.com/tiphaine-mtch/odyssey_questionnaire`
2. Cliquer sur **Settings** (⚙️)
3. Dans le menu de gauche : **Pages**
4. **Source** : sélectionner `main` branch
5. Cliquer **Save**
6. Attendre 1-2 minutes

### Étape 4 : Vérifier le déploiement

**URL principale** : `https://tiphaine-mtch.github.io/odyssey_questionnaire/`

Cette URL redirige automatiquement vers le questionnaire.

**URLs directes** :
- Questionnaire : `https://tiphaine-mtch.github.io/odyssey_questionnaire/odyssey-questionnaire-experts-STANDALONE.html`
- Dashboard Admin : `https://tiphaine-mtch.github.io/odyssey_questionnaire/odyssey-expert-admin-dashboard.html`

---

## 🧪 Tests à faire après déploiement

### Test 1 : Dark Mode
- [ ] Ouvrir le questionnaire sur desktop
- [ ] Vérifier que le dark mode s'active si OS en mode sombre
- [ ] Changer le mode OS → vérifier transition automatique
- [ ] Tous les composants doivent être lisibles (pas de texte blanc sur fond blanc)

### Test 2 : Responsive Mobile
- [ ] Ouvrir sur smartphone (ou DevTools responsive mode)
- [ ] Header doit s'empiler verticalement
- [ ] Language switcher centré sous le titre
- [ ] Boutons pleine largeur
- [ ] Inputs ne doivent PAS zoomer automatiquement (iOS)
- [ ] Cards empilées verticalement
- [ ] Progress bar visible

### Test 3 : Responsive Tablet
- [ ] Ouvrir sur tablette (768px - 1024px)
- [ ] Dashboard grid : 2 colonnes
- [ ] Expert list : 3-4 colonnes visibles
- [ ] Pas de scroll horizontal

### Test 4 : Dashboard Admin
- [ ] Ouvrir le dashboard
- [ ] Vérifier que les KPIs s'affichent
- [ ] Onglets fonctionnels
- [ ] Liste des experts responsive
- [ ] Bouton delete fonctionne
- [ ] Export JSON/CSV/Markdown fonctionnent

### Test 5 : Fonctionnalités questionnaire
- [ ] Remplir formulaire identité
- [ ] Répondre à quelques questions
- [ ] Vérifier sauvegarde auto (rafraîchir page)
- [ ] Soumettre questionnaire
- [ ] Vérifier dans dashboard admin

---

## 📱 Tester sur vrais appareils

### iPhone / iPad
1. Safari : `https://tiphaine-mtch.github.io/odyssey_questionnaire/`
2. Activer dark mode iOS : Réglages > Luminosité > Mode sombre
3. Vérifier que le questionnaire passe en dark
4. Taper dans un input → ne doit PAS zoomer
5. Tous les boutons tactiles doivent être facilement cliquables

### Android
1. Chrome : `https://tiphaine-mtch.github.io/odyssey_questionnaire/`
2. Activer dark mode : Paramètres > Affichage > Thème sombre
3. Vérifier transition automatique
4. Navigation fluide, pas de scroll horizontal

### Desktop
1. **Chrome** : DevTools > Toggle device toolbar (Ctrl+Shift+M)
   - Tester iPhone SE, iPad, Desktop
2. **Firefox** : DevTools > Responsive Design Mode (Ctrl+Shift+M)
3. **Edge** : DevTools > Device emulation
4. **Safari** (Mac uniquement) : Développement > Responsive Design Mode

---

## 🔧 Si quelque chose ne marche pas

### Problème : Dark mode ne fonctionne pas
**Solution** :
1. Vérifier que `responsive-dark-mode.css` est bien présent sur GitHub
2. Ouvrir DevTools (F12) > Console > vérifier s'il y a une erreur CSS
3. Vérifier que le lien `<link rel="stylesheet" href="responsive-dark-mode.css">` est présent dans les HTML

### Problème : Responsive ne marche pas sur mobile
**Solution** :
1. Vérifier présence de `<meta name="viewport" content="width=device-width, initial-scale=1.0">` dans `<head>`
2. Vider cache navigateur mobile : Safari > Réglages > Safari > Effacer historique
3. Force refresh : Ctrl+Shift+R (desktop) ou mode navigation privée (mobile)

### Problème : GitHub Pages ne se met pas à jour
**Solution** :
1. Attendre 5 minutes (GitHub Actions peut être lent)
2. Vérifier Actions : `https://github.com/tiphaine-mtch/odyssey_questionnaire/actions`
3. Vider cache navigateur : Ctrl+Shift+R
4. Essayer en navigation privée

### Problème : Les questions ne s'affichent pas
**Solution** :
1. Vérifier que `questions-business-only.json` est bien sur GitHub
2. Ouvrir DevTools Console (F12) > rechercher erreurs JavaScript
3. La version STANDALONE doit avoir le JSON embarqué → pas de dépendance réseau

---

## 📊 Monitoring post-déploiement

### Semaine 1
- Recueillir feedback des premiers experts
- Monitorer les soumissions dans le dashboard admin
- Noter les bugs/améliorations demandées

### Analytics (optionnel)
Si tu veux suivre l'utilisation :
1. Créer compte Google Analytics
2. Ajouter tracking code dans `<head>` de index.html
3. Suivre : pages vues, temps passé, taux complétion

---

## 🎯 Prochaines étapes suggérées

### Court terme
- [ ] Partager URL avec premiers beta-testeurs
- [ ] Collecter feedback UX
- [ ] Ajuster si besoin

### Moyen terme (v2.1)
- [ ] Ajouter graphiques dans dashboard (Chart.js)
- [ ] Export PDF avec mise en page
- [ ] Service Worker pour mode offline complet

### Long terme (v3.0)
- [ ] Backend Firebase/Supabase pour vraie collaboration
- [ ] Authentification experts
- [ ] Notifications temps réel
- [ ] Versioning des réponses

---

## 📞 Support

**Repository** : `https://github.com/tiphaine-mtch/odyssey_questionnaire`  
**Issues** : `https://github.com/tiphaine-mtch/odyssey_questionnaire/issues`

Pour toute question technique, créer une issue sur GitHub.

---

**Version** : 2.0  
**Date** : 19 juin 2026  
**Status** : ✅ Prêt à déployer
