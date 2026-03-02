import os
from dotenv import load_dotenv

# Cette ligne charge les variables du fichier .env dans le système
load_dotenv()

class Config:
    """
    Classe pour centraliser la configuration de l'API.
    C'est très propre pour un portfolio.
    """
    # Récupération du Token (on met None par défaut si pas trouvé)
    TOKEN = os.getenv("NOTION_TOKEN")
    
    # Récupération des IDs de bases de données
    DB_QUESTIONS = os.getenv("DATABASE_QUESTIONS_ID")
    DB_RECHERCHES = os.getenv("DATABASE_RECHERCHES_ID")

    @staticmethod
    def check_config():
        """Petite méthode pour vérifier que tout est bien chargé"""
        if not Config.TOKEN:
            return "❌ Erreur : TOKEN non trouvé dans le .env"
        if not Config.DB_QUESTIONS:
            return "⚠️ Attention : ID Base Questions manquant"
        return "✅ Configuration chargée avec succès !"