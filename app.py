# app.py
import streamlit as st
from database.db import save_profil, connect, get_all_profils
from logic.team_generator import generate_teams
from export.csv_export import export_to_csv
from export.pdf_export import generate_pdf
from utils.zodiac import sign_elements

st.set_page_config(page_title="AstroTeam IA", layout="centered")
st.image("assets/demarcheursITLogo.png", use_column_width=True)
st.title("🔮 Générateur d'équipes compatibles astrologiquement")

with st.form("formulaire"):
    nom = st.text_input("Nom complet")
    signe = st.selectbox("Signe zodiaque", list(sign_elements.keys()))
    competences = st.text_area("Compétences principales (séparées par virgule)")
    submit = st.form_submit_button("Ajouter le profil")

    if submit:
        if nom.strip() and competences.strip():
            result = save_profil(nom, signe, competences)
            if result == "exists":
                st.warning("⚠️ Ce profil existe déjà dans la base.")
            else:
                st.success("✅ Profil ajouté avec succès !")
        else:
            st.warning("❗ Veuillez remplir tous les champs avant de valider.")

st.divider()

if st.button("🚀 Former les équipes compatibles"):
    profils = get_all_profils()
    groupes = generate_teams(profils)

    for idx, groupe in groupes.items():
        st.subheader(f"Équipe {idx + 1}")
        for membre in groupe:
            st.markdown(f"- {membre['nom']} ({membre['zodiac']} – {membre['element']})")

    csv_data = export_to_csv(groupes)
    st.download_button("📥 Télécharger CSV", csv_data, "equipes.csv", "text/csv")

    pdf_data = generate_pdf(groupes)
    st.download_button("📄 Télécharger PDF", pdf_data, "equipes.pdf", "application/pdf")