# database/db.py
import psycopg2
import os

def connect():
    return psycopg2.connect(
        host=os.getenv("DB_HOST", "localhost"),
        database=os.getenv("DB_NAME", "astro_db"),
        user=os.getenv("DB_USER", "postgres"),
        password=os.getenv("DB_PASSWORD", "")
    )


    def save_profil(nom, signe, competences):
    # Nettoyage des champs
        nom = nom.strip().title()
        signe = signe.strip().title()

        # Traitement des compétences (séparation, suppression des espaces, doublons, format propre)
        competences_list = list({comp.strip().capitalize() for comp in competences.split(",") if comp.strip()})
        competences_clean = ", ".join(sorted(competences_list))

        # Connexion et insertion dans PostgreSQL
        conn = connect()
        cur = conn.cursor()
        cur.execute("""
            INSERT INTO profils (nom, signe_zodiaque, competences)
            VALUES (%s, %s, %s)
        """, (nom, signe, competences_clean))
        conn.commit()
        cur.close()
        conn.close()

def get_all_profils():
    conn = connect()
    cur = conn.cursor()
    cur.execute("SELECT nom, signe_zodiaque, competences FROM profils")
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return [
        {"nom": r[0], "zodiac": r[1], "competences": r[2]} for r in rows
    ]
    
