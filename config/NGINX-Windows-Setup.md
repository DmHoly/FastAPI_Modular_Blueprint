# 🚀 Installation et Configuration de Nginx sous Windows

## 📋 **Introduction**
Nginx est un serveur web rapide et performant qui peut être utilisé comme **reverse proxy** pour gérer les requêtes vers **FastAPI (Backend) et un Frontend (Dash, Streamlit, React...)**.

Ce guide explique comment **installer, configurer et lancer** Nginx sur **Windows**.

---

## 📜 **1️⃣ Télécharger et Installer Nginx sous Windows**
### 🔹 **Étape 1 : Télécharger Nginx**
1. Accédez au site officiel de **Nginx** :  
   👉 [https://nginx.org/en/download.html](https://nginx.org/en/download.html)  
2. **Téléchargez la version Windows** (`nginx/Windows` en `.zip`).  
3. **Décompressez le fichier ZIP** dans un dossier, par exemple :  

## 🛠️ **2️⃣ Configurer Nginx pour le Reverse Proxy**  

### **🔹 Étape 1 : Modifier le fichier de configuration (`nginx.conf`)**
1. **Accédez au fichier de configuration** :  

C:\nginx\conf\nginx.conf
2. **Ouvrez-le avec un éditeur de texte** (`Notepad++`, `VS Code`, etc.).
3. **Remplacez le contenu du fichier par la configuration suivante :**  

```nginx
worker_processes  1;

events {
 worker_connections  1024;
}

http {
 include       mime.types;
 default_type  application/octet-stream;

 sendfile        on;
 keepalive_timeout  65;

 server {
     listen 80;  # 📌 Écoute sur le port 80 (HTTP)
     server_name localhost;  # 📌 Nom du serveur

     # 📡 Proxy pour FastAPI (Backend)
     location /api/ {
         proxy_pass http://127.0.0.1:8000/;  # 📌 Redirige les requêtes API vers FastAPI
         proxy_set_header Host $host;
         proxy_set_header X-Real-IP $remote_addr;
         proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
         proxy_set_header X-Forwarded-Proto $scheme;
     }

     # 🌐 Proxy pour le frontend (Dash, Streamlit, React, etc.)
     location / {
         proxy_pass http://127.0.0.1:8050/;  # 📌 Redirige vers l'interface frontend
         proxy_set_header Host $host;
         proxy_set_header X-Real-IP $remote_addr;
         proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
         proxy_set_header X-Forwarded-Proto $scheme;
     }

     # 📌 Gestion des erreurs
     error_page 500 502 503 504 /50x.html;
     location = /50x.html {
         root html;
     }
 }
}
```
# 🚀 **3️⃣ Lancer et Utiliser Nginx sur Windows**  

Après avoir installé et configuré **Nginx**, nous allons maintenant le **démarrer**, le **vérifier** et le **configurer pour qu’il démarre automatiquement** sous Windows.  

---

## 🛠 **🔹 Méthode 1 : Démarrer Nginx Manuellement**
1️⃣ **Ouvrir une invite de commande (`cmd`) en mode administrateur**  
- Tapez `cmd` dans la barre de recherche Windows.  
- Faites un **clic droit** → **Exécuter en tant qu'administrateur**.  

2️⃣ **Accéder au dossier Nginx**  
Dans l’invite de commande, exécutez :  

```sh
cd C:\nginx
```

## 🔄 🔹 Méthode 2 : Vérifier et Redémarrer Nginx

Vérifier la configuration
Avant de redémarrer Nginx, testez si la configuration est correcte

```sh
nginx -t
```

✅ Si tout est bon, vous devriez voir :
```sh
nginx: configuration file C:/nginx/conf/nginx.conf test is successful
```

### Arrêter Nginx
Pour arrêter complètement Nginx :

```sh
nginx -s stop
```

## 🔄 🔹 Méthode 3 : Lancer Nginx Automatiquement au Démarrage de Windows

Si vous voulez que Nginx démarre automatiquement à chaque démarrage de Windows, suivez ces étapes :

1️⃣ Créer un script start_nginx.bat
Ouvrez le Bloc-notes et collez le code suivant :

```sh
@echo off
cd C:\nginx
start nginx
exit
```
Enregistrez le fichier sous : **C:\nginx\start_nginx.bat**





