# GPT-2 Inference with Docker

Ce projet permet d'effectuer une inférence sur le modèle GPT-2 en utilisant Docker. Il utilise Hugging Face Transformers pour le modèle GPT-2 et une interface graphique pour l'inférence.

## Prérequis

- Docker et Docker Compose installés sur votre machine.
- NVIDIA Container Toolkit si vous souhaitez utiliser le GPU pour l'inférence.

## Installation

### 1. Cloner le dépôt

Commencez par cloner ce dépôt sur votre machine locale :

```bash
git clone https://github.com/ImDeveloperz/model_gpt2.git
cd model_gpt2
```
### 2. Construire et démarrer les conteneurs Docker
   
```bash
docker-compose up --build
```

### 3. Utilisation

Après avoir démarré les conteneurs, vous pouvez accéder à l'interface graphique pour l'inférence en ouvrant votre navigateur et en naviguant vers http://localhost:5000.
Exemple de requête d'inférence

```bash
curl -X POST "http://localhost:5000/generate" -H "Content-Type: application/json" -d '{"text": "Voici un exemple de texte à compléter par GPT-2."}'
```

