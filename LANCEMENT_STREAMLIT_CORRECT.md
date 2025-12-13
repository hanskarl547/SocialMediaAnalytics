# 🚀 Comment Lancer Correctement votre Application Streamlit

## ❌ Problème Actuel

Vous lancez l'application Streamlit avec :
```bash
python app.py
```

Mais Streamlit doit être lancé avec :
```bash
streamlit run app.py
```

---

## ✅ Solution

### 1. Dans le Terminal PowerShell

Assurez-vous d'être dans le bon dossier :
```powershell
cd C:\Users\HP\Documents\SocialMediaAnalytics
```

### 2. Lancez avec Streamlit

```bash
streamlit run app.py
```

---

## 🔧 Si le Port 8501 est Occupé

### Option 1 : Libérer le port

```powershell
# Trouver le processus
netstat -ano | findstr :8501

# Tuer le processus (remplacez PID par le numéro trouvé)
taskkill /PID <PID> /F
```

### Option 2 : Utiliser un autre port

```bash
streamlit run app.py --server.port 8502
```

---

## 🐛 Correction de l'Erreur Session State

L'erreur indique que `st.session_state.show_landing` n'est pas initialisé. Il faut initialiser les variables de session au début du script.

### Solution : Initialiser session_state

Dans votre `app.py` (Streamlit), ajoutez au début de la fonction `main()` :

```python
# Initialiser session_state si nécessaire
if 'show_landing' not in st.session_state:
    st.session_state.show_landing = True
    
if 'user' not in st.session_state:
    st.session_state.user = None
```

---

## 📋 Commandes Complètes

### Pour lancer Streamlit normalement :
```bash
cd C:\Users\HP\Documents\SocialMediaAnalytics
streamlit run app.py
```

### Pour lancer sur un autre port :
```bash
streamlit run app.py --server.port 8502
```

### Pour lancer avec options :
```bash
streamlit run app.py --server.port 8502 --server.headless true
```

---

## ✅ Résumé

- ❌ Ne pas utiliser : `python app.py` pour Streamlit
- ✅ Utiliser : `streamlit run app.py`
- 🔧 Si port occupé : changez le port ou tuez le processus

---

## 🎯 Après le Lancement

L'application Streamlit s'ouvrira automatiquement dans votre navigateur à :
```
http://localhost:8501
```
