from github import Github
import os

# Remplacez par votre token d'accès personnel
GITHUB_TOKEN = 'your_personal_access_token'
REPO_NAME = 'test-repo'
FILE_NAME = 'README.md'
COMMIT_MESSAGE = 'Initial commit'

# Authentification
g = Github(GITHUB_TOKEN)

# Créer un nouveau dépôt
user = g.get_user()
repo = user.create_repo(REPO_NAME)

# Contenu du fichier
content = "# Test Repo\n\nThis is a test repository."

# Créer un fichier et faire un commit
repo.create_file(FILE_NAME, COMMIT_MESSAGE, content, branch="main")

print(f"Repository '{REPO_NAME}' created with initial commit.")