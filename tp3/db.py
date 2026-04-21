import mysql.connector
from mysql.connector import Error 
from config import DB_CONFIG

def get_connection(): 
    """
    crée et retourne une nouvelle connexion MySQL. 
    Lève uen exception si la connexion échoue . 
    """
    try: 
        connection = mysql.connector.connect(**DB_CONFIG)
        return connection 
    except Error as e : 
        print(f"Erreur connexion MySQL :{e} ")
        raise 
        