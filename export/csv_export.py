# export/csv_export.py
import pandas as pd
from io import StringIO

def export_to_csv(groupes):
    data = []
    for num, equipe in groupes.items():
        for membre in equipe:
            data.append({
                "Équipe": f"Équipe {num+1}",
                "Nom": membre["nom"],
                "Signe Zodiaque": membre["zodiac"],
                "Élément": membre["element"]
            })
    df = pd.DataFrame(data)
    buffer = StringIO()
    df.to_csv(buffer, index=False)
    return buffer.getvalue()
