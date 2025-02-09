"""
📌 Backend - Génération de Graphiques Matplotlib

en realité il faut bien séparer les responsabilités,
ici on a un service qui génère un graphique fictif basé sur le type de données

dans un cas plus concret il faut :
1) services de recuperation des données à partir de la base de données (id, type de données)
2) services de traitement des données (calculs, transformations)
3) services de génération de graphiques (graphiques basés sur les données traitées)


"""

import matplotlib.pyplot as plt

def generate_graph(user_id: int, data_type: str):
    """📈 Génère un graphique fictif basé sur le type de données."""
    fig, ax = plt.subplots()
    ax.plot([1, 2, 3], [user_id * 10, user_id * 15, user_id * 20], marker='o')
    ax.set_title(f"Graphique pour {data_type} - Utilisateur {user_id}")

    return fig, ax
