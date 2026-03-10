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
    def verification(cls,question,database_id,nom_propriete ="Nom"):
        # enlever les espace 
        question = question.strip()
        # Pour etre sur que l'on a inserer une question 
        if not question: 
            return False, "erreur tu dois poser une question"
        
        # rechercher si une question existe deja dans la DB 
        url = f"{cls.BASE_URL}/databases/{database_id}/query"

        # On filtre les question de la db equals => egale 
        payload = {
            "filter": {
                "property":nom_propriete,
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
    def ajout(cls,texte,database_id):


        # POUR CREER UNE NOUVELLE LIGNE, POUR L'INSERTION 
        url = f"{cls.BASE_URL}/pages"

        payload = {
            "parent" : {"database_id": database_id},
            "properties":{
                "Nom":{
                    "title":[{"text": {"content": texte}}]
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
    def voir_question(cls,database_id,texte,cursor=None):
        url = f"{cls.BASE_URL}/databases/{database_id}/query"

        # prepare les instructions pour notion 
        payload = {
            # limite le resultat sur 10 paquet
            "page_size": 5
        }

        # si on a un cursor on dit a Notion de commencer par la 
        if cursor:
            payload["start_cursor"] = cursor

        # response = requests.post(url,headers=cls.headers,json={})
        response = requests.post(url,json=payload,headers=cls.headers)
        # si cela fonctionne 
        if response.status_code==200:
             donnees = response.json()
             pages = donnees.get("results",[])
            # tableau pour ajouter les nom des idée d'articles
             noms=[]
            
            # Pour voir que les 20 premier 
             for page in pages[:5]:
                 nom = page["properties"][texte]["title"][0]["text"]["content"]
                 noms.append(nom)

             return {
                 "questions":noms,
                 "next_cursor": donnees.get("next_cursor"),
                 "has_more":donnees.get("has_more",False)
             }
        return {
            "question":[],
            "next_cursor" : None,
            "has_more": False
        }
            
