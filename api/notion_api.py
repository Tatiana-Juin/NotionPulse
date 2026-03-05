# import customtkinter
import requests
import json
from .config_api import Config

class NotionAPI:
    # appelle de api 
    BASE_URL = "https://api.notion.com/v1"

    # headers => OBLIGATION POUR API NOTION 
    headers = {
        "Authorization": f"Bearer {Config.TOKEN}",
        "Content-Type": "application/json",
        "Notion-Version": "2022-06-28"
    }

    # VERIFICATION 
    @classmethod
    def verification(cls,question):
        # enlever les espace 
        question = question.strip()
        # Pour etre sur que l'on a inserer une question 
        if not question: 
            return False, "erreur tu dois poser une question"
        
        # rechercher si une question existe deja dans la DB 
        url = f"{cls.BASE_URL}/databases/{Config.DB_QUESTIONS}/query"

        # On filtre les question de la db equals => egale 
        payload = {
            "filter": {
                "property":"Nom",
                "title": {
                    "equals": question
                }
            }
        }
        # envoyer la requete 
        response = requests.post(url,headers=cls.headers,json=payload)
        # si la reponse retourne 200 aucune erreur avec api 
        if response.status_code==200:
            # convertie en json
            donnees = response.json()
            # verification de la taille du tableau 
            if len(donnees["results"]) > 0:
                return False,"Cette question existe deja"
            else:
                return True,"la question est nouvelle"
        else:
            return False, f"Erreur api {response.status_code}"
    
    # AJOUT DE LA QUESTION 
    @classmethod
    def ajout_question(cls,question):


        # POUR CREER UNE NOUVELLE LIGNE, POUR L'INSERTION 
        url = f"{cls.BASE_URL}/pages"

        payload = {
            "parent" : {"database_id": Config.DB_QUESTIONS},
            "properties":{
                "Nom":{
                    "title":[{"text": {"content": question}}]
                }
                # "Description":{
                #     "rich_text":[{"text": {"content":"depuis mon application"}}]
                # }
            }
        }
        try:
            response = requests.post(url,headers=cls.headers,json=payload)

            if response.status_code==200:
                return "Question ajouter"
            else:
                return f"erreur lors de l'ajout {response.status_code}"
        except Exception as e:
            return f"erreur de connection {e}"

    @classmethod
    def voir_question(cls):
        url = f"{cls.BASE_URL}/databases/{Config.DB_QUESTIONS}/query"
        response = requests.post(url,headers=cls.headers,json={})
        # si cela fonctionne 
        if response.status_code==200:
             donnees = response.json()
             pages = donnees.get("results",[])
            # tableau pour ajouter les nom des idée d'articles
             noms=[]
            
            # Pour voir que les 20 premier 
             for page in pages[:20]:
                 nom = page["properties"]["Nom"]["title"][0]["text"]["content"]
                 noms.append(nom)
             return noms;
        return []
            
