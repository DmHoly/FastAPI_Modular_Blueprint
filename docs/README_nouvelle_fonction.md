# 📌 Documentation - Nouvelle Fonctionnalité

## 🎯 Objectif 

L'objectif de cette documentation est de présenter comment ajouter une nouvelle fonctionnalité à l'application.

## 🚀 Procédure

✔ **Facilite l’intégration par d’autres développeurs.**  

---

# ✅ **Résumé de la CheckList**
| 🔹 **Étape**                                 | 📌 **Action**                                                          |
|----------------------------------------------|------------------------------------------------------------------------|
| **1️⃣ Définir la fonctionnalité**            | Objectif, inputs, outputs                                              |
| **2️⃣ Créer le service backend**             | Implémenter la logique dans `/backend/services/mon_service.py`         |
| **3️⃣ Exposer dans `__init__.py`**           | Ajouter dans `/backend/services/__init__.py` et `/backend/__init__.py` |
| **4️⃣ Ajouter un endpoint API**              | Créer `/api/endpoints/mon_endpoint.py` <br/>                           |
| **4️bis** Exposer le endpoint dans l'init ** | Ajouter dans `/api/endpoints/__init__.py` <br/>                    |
| **5️⃣ Ajouter la route API**                 | Modifier `/api/routes.py` pour inclure la route                        |
| **6️⃣ Exposer l’API dans `__init__.py`**     | Ajouter `from .routes import router` dans `/api/__init__.py`           |
| **7️⃣ Tester l’API avec `curl` et `requests`** | Vérifier que l’API répond bien                                         |
| **8️⃣ Ajouter un test **                     | Créer `/examples/test_mon_service.py`                                  |
| **9️⃣ Ajouter la documentation**             | Ajouter `/docs/README_nouvelle_fonction.md`                            |

optionnel : ajouter aussi dans le app/api/api_client.py le cas d'utilisation de la nouvelle fonctionnalité

---

🚀 **Maintenant, chaque nouvelle fonctionnalité est bien intégrée, testée et documentée !**  
Besoin d’ajustements ? 😊

