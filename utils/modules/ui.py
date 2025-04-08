# modules/ui.py
import streamlit as st

def saisir_profil():
    st.subheader("👤 Ajouter un membre de l'équipe")

    with st.form("form_profil"):
        nom = st.text_input("Nom complet")
        signe = st.selectbox("Signe astrologique", [
            "Bélier", "Taureau", "Gémeaux", "Cancer", "Lion", "Vierge",
            "Balance", "Scorpion", "Sagittaire", "Capricorne", "Verseau", "Poissons"
        ])
        competences = st.multiselect(
            "Compétences", ["Python", "SQL", "Design", "Communication", "Analyse", "Gestion", "IA", "Déploiement"]
        )
        submit = st.form_submit_button("✅ Enregistrer")

    if submit:
        if nom and signe and competences:
            return {"nom": nom, "signe": signe, "competences": ", ".join(competences)}
        else:
            st.warning("Veuillez remplir tous les champs.")
    return None