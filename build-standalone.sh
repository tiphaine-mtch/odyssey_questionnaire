#!/bin/bash
# Script pour créer une version standalone avec JSON embarqué

echo "🔨 Construction version standalone..."

# Lire le JSON
JSON_CONTENT=$(cat questions-business-only.json)

# Créer le HTML avec JSON embarqué
cat odyssey-questionnaire-experts.html | \
  sed "s|const QUESTIONS_DATA_EMBEDDED = null;|const QUESTIONS_DATA_EMBEDDED = ${JSON_CONTENT};|" | \
  sed "s|questionsData = await response.json();|questionsData = QUESTIONS_DATA_EMBEDDED || await response.json();|" \
  > odyssey-questionnaire-experts-standalone.html

echo "✅ Fichier créé: odyssey-questionnaire-experts-standalone.html"
echo "👉 Tu peux maintenant double-cliquer dessus pour l'ouvrir"
