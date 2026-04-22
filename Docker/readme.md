# Guide de l'Écosystème Docker : Conteneurisation et Persistance

Ce document offre une vue d'ensemble sur l'utilisation de Docker, de la gestion du stockage à l'orchestration simplifiée avec Compose.

---

## 🏗️ Fondamentaux : Pourquoi Docker ?

Traditionnellement, le déploiement d'applications s'appuie sur le **Cloud Computing** (ressources distantes via Internet). Docker optimise ce processus grâce aux **conteneurs**.

### Conteneur vs Machine Virtuelle
À l'inverse d'une VM qui simule un matériel complet, Docker s'appuie sur le **noyau du système hôte**. Cela rend les conteneurs :
* **Performance :** Démarrage quasi instantané.
* **Légèreté :** Consommation minimale de ressources.
* **Portabilité :** Environnement identique du développement à la production.

---

## 📦 Automatisation avec le Dockerfile

Le **Dockerfile** est le plan de fabrication d'une image. Il permet d'automatiser l'installation des dépendances et la configuration logicielle.

**Instructions clés :**
- `FROM` : Définit l'image parente (ex: Alpine, Ubuntu, Node).
- `WORKDIR` : Spécifie le répertoire d'exécution des commandes.
- `COPY` / `ADD` : Transfère les fichiers locaux vers l'image.
- `RUN` : Exécute des commandes lors de la construction.
- `EXPOSE` : Indique les ports de communication.
- `CMD` : Définit l'action par défaut au lancement du conteneur.

---

## 💾 Gestion de la Persistance (Stockage)

Par nature, un conteneur est **éphémère** : toute donnée créée à l'intérieur est supprimée avec lui. Pour pallier cela, trois méthodes existent :

1.  **Volumes (Préconisé) :** Gérés par Docker, ils sont isolés du système de fichiers hôte classique et parfaits pour la production.
2.  **Bind Mounts :** Créent un lien direct entre un dossier spécifique de votre PC et le conteneur. Idéal pour voir ses modifications de code en direct.
3.  **Tmpfs Mount :** Stockage ultra-rapide résidant uniquement en mémoire vive (RAM). Les données disparaissent à l'arrêt du service.



---

## 🚀 Orchestration avec Docker Compose

Dès qu'une architecture devient complexe (ex: une application Web + une base de données), l'utilisation de **Docker Compose** devient indispensable. 

Il permet de piloter plusieurs services via un unique fichier `docker-compose.yml`, évitant ainsi de taper de longues lignes de commande `docker run`.

### Avantages majeurs :
- Centralisation de la configuration.
- Création automatique de réseaux isolés entre les services.
- Gestion des dépendances (ex: attendre que la DB soit prête avant de lancer le site).

---

## 🛠️ Exemples Pratiques

### 1. Lancement rapide d'un service (CLI)
Déploiement d'une instance MySQL avec persistance des données :

```bash
# Création d'un espace de stockage nommé
docker volume create db_persist

# Lancement du conteneur
docker run -d \
  --name database_app \
  -e MYSQL_ROOT_PASSWORD=mon_password \
  -v db_persist:/var/lib/mysql \
  -p 3306:3306 \
  mysql:8