# app.py
import streamlit as st
from database.db import save_profil, connect, get_all_profils
from logic.team_generator import generate_teams
from export.csv_export import export_to_csv
from export.pdf_export import generate_pdf
from utils.zodiac import sign_elements
# Page Configuration
st.set_page_config(page_title="AstroTeam IA", layout="centered")
st.title("🔮 Générateur d'équipes compatibles astrologiquement")


# Affichage du logo
st.markdown(
    """
    <div style='text-align: center;'>
        <img src='assets/banner_astro.png' width='600'/>
    </div>
    """,
    unsafe_allow_html=True
)

# Formulaire pour l'ajout de profil
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

 #Génération des équipes compatibles
if st.button("🚀 Former les équipes compatibles"):
    profils = get_all_profils()
    groupes = generate_teams(profils)

    for idx, groupe in groupes.items():
        st.subheader(f"Équipe {idx + 1}")
        for membre in groupe:
            st.markdown(f"- {membre['nom']} ({membre['zodiac']} – {membre['element']})")

    # Export CSV
    csv_data = export_to_csv(groupes)
    st.download_button("📥 Télécharger CSV", csv_data, "equipes.csv", "text/csv")
    
     # Export PDF
    pdf_data = generate_pdf(groupes)
    st.download_button("📄 Télécharger PDF", pdf_data, "equipes.pdf", "application/pdf")