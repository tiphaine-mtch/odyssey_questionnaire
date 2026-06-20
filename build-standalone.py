#!/usr/bin/env python3
"""
Script pour créer une version standalone du questionnaire
avec le JSON embarqué directement dans le HTML
"""

import json
import re

print("🔨 Construction version standalone...")

# Lire le JSON
with open('questions-business-only.json', 'r', encoding='utf-8') as f:
    questions_data = json.load(f)

# Lire le HTML
with open('odyssey-questionnaire-experts.html', 'r', encoding='utf-8') as f:
    html_content = f.read()

# Convertir le JSON en string JavaScript
json_str = json.dumps(questions_data, ensure_ascii=False, indent=2)

# Remplacer la ligne const QUESTIONS_DATA_EMBEDDED = null;
pattern = r'const QUESTIONS_DATA_EMBEDDED = null;'
replacement = f'const QUESTIONS_DATA_EMBEDDED = {json_str};'
html_content = re.sub(pattern, replacement, html_content)

# Modifier la fonction loadQuestions pour utiliser les données embarquées d'abord
old_load = """try {
                // Try to fetch external JSON first
                const response = await fetch('questions-business-only.json');
                if (response.ok) {
                    questionsData = await response.json();
                } else {
                    throw new Error('JSON file not found');
                }
            } catch (error) {
                console.warn('Could not load external JSON, using embedded data:', error);
                // Fallback to embedded data if fetch fails
                questionsData = QUESTIONS_DATA_EMBEDDED || getEmbeddedQuestions();
            }"""

new_load = """// Use embedded data directly (standalone version)
            questionsData = QUESTIONS_DATA_EMBEDDED;
            if (!questionsData) {
                console.error('No embedded questions data');
                alert('Erreur: Données des questions manquantes');
                return;
            }"""

html_content = html_content.replace(old_load, new_load)

# Écrire le fichier standalone
with open('odyssey-questionnaire-experts-STANDALONE.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

print("✅ Fichier créé: odyssey-questionnaire-experts-STANDALONE.html")
print("")
print("📝 Instructions:")
print("1. Double-clique sur: odyssey-questionnaire-experts-STANDALONE.html")
print("2. Il s'ouvre dans ton navigateur")
print("3. Les 11 questions s'affichent automatiquement")
print("")
print("✨ Ce fichier fonctionne sans serveur web !")
