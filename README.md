# Montage Uitgaven Voorspeller 📊

Deze app voorspelt de montage-uitgaven op basis van jaar, maand en tijdindex, gebruikmakend van een getraind Random Forest-model.

## 🔧 Functies

- Input: Jaar, Maand, TijdIndex
- Model: Random Forest (geladen via Joblib)
- Output: Geschatte montage-uitgaven in euro's

## 🚀 Gebruikslocaties

### ▶️ Lokaal draaien

1. Installeer vereisten:

```bash
pip install -r requirements.txt
```

2. Start de app:

```bash
streamlit run app.py
```

### ☁️ Online via Streamlit Cloud

1. Upload deze bestanden naar GitHub
2. Ga naar [https://streamlit.io/cloud](https://streamlit.io/cloud)
3. Selecteer deze repo, kies `app.py` als entry point
4. Klik op **Deploy**

## 📂 Bestanden

- `app.py` — hoofdapplicatie
- `random_forest_montage_model.pkl` — getraind model (Joblib)
- `requirements.txt` — afhankelijkheden
