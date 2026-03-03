# Data Dictionary — Diadora Competitive Analysis

| Colonna | Tipo | Descrizione | Esempio |
|---|---|---|---|
| Brand | string | Nome del brand analizzato | Diadora, Nike |
| Modello | string | Nome del modello di scarpa | Diadora B.Elite |
| Categoria URL | string | Categoria come da URL del sito ufficiale | Sneakers |
| Categoria | string | Categoria classificata automaticamente dallo scraper | Sneakers |
| Sottocategoria | string | Sottocategoria rilevata da keyword matching | Retro/Heritage |
| Prezzo (€) | float | Prezzo di listino in euro | 89.95 |
| N. Colori | int | Numero di varianti colore disponibili | 3 |
| Taglie | string | Taglie disponibili separate da virgola | 40, 41, 42, 43 |
| N. Taglie | int | Numero di taglie disponibili | 8 |
| URL Prodotto | string | Link diretto alla pagina prodotto | https://... |
| Data Rilevazione | datetime | Data e ora dell'esecuzione dello scraping | 2024-11-15 14:32 |
```

---

### 📄 `requirements.txt` (nella root)
```
selenium==4.18.1
webdriver-manager==4.0.1
beautifulsoup4==4.12.3
pandas==2.2.1
openpyxl==3.1.2
jupyter==1.0.0
lxml==5.1.0
```

---

### 📄 `.gitignore` (nella root)
```
# Python
__pycache__/
*.pyc
*.pyo
.env

# Jupyter
.ipynb_checkpoints/
*.html

# Output scraping (file grandi e dati grezzi)
data/Diadora_Competitive_Analysis.xlsx
*.log
chromedriver
chromedriver.exe

# OS
.DS_Store
Thumbs.db
