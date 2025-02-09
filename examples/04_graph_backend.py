from app.backend import generate_graph
import matplotlib.pyplot as plt

if __name__ == "__main__":
    # Générer un graphique
    fig, ax = generate_graph(1, "weight")
    plt.show()