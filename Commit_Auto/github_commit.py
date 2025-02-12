import os
import git
import schedule
import time
from datetime import datetime
import sys
import io

# If you're still running into issues with encoding, set the default encoding for the console
# This makes sure that standard output is using UTF-8
sys.stdout.reconfigure(encoding='utf-8')

# Print your message
print("\u23f3 Démarrage du script de commit automatique...")

# Paramètres du dépôt local
REPO_PATH = r"C:\Users\a.haddouti\Desktop\vs file"  # Remplace par le chemin de ton dépôt local
GITHUB_USERNAME = "Adnanehaddouti"
GITHUB_REPO = "vs-file"  # Nom du repo (ex: "mon_projet")

def auto_commit():
    try:
        # Ouvre le dépôt local
        repo = git.Repo(REPO_PATH)

        # Vérifie s'il y a des modifications
        if repo.is_dirty(untracked_files=True):
            repo.git.add(A=True)  # Ajoute tous les fichiers modifiés
            commit_message = f"Auto-commit {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
            repo.index.commit(commit_message)
            print(f"✅ Commit effectué : {commit_message}")

            # Push vers GitHub
            origin = repo.remote(name="main")
            origin.set_url(f"https://{GITHUB_USERNAME}:{GITHUB_TOKEN}@github.com/{GITHUB_USERNAME}/{GITHUB_REPO}.git")
            origin.push()
            print("🚀 Changements poussés sur GitHub avec succès !")
        else:
            print("🔄 Rien à commit, le dépôt est à jour.")

    except Exception as e:
        print(f"❌ Erreur : {e}")

# Planifier le commit chaque jour à 10h00
schedule.every().day.at("15:33").do(auto_commit)

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')


print("Démarrage du script de commit automatique...")
while True:
    schedule.run_pending()
    time.sleep(60)  # Vérifie toutes les minutes
