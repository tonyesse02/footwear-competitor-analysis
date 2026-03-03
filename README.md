# 👟 Footwear Competitor Analysis — Diadora Strategic Intelligence 2026

> **Competitive Intelligence & Strategic Outlook 2026**  
> Analisi di Mercato, Posizionamento Prezzo e Raccomandazioni Strategiche per Diadora.

---

## 📌 Overview del Progetto

Questo progetto è stato sviluppato nell'ambito di un Master in Business Analytics ed ha come obiettivo la realizzazione di un sistema completo di **Competitive Intelligence** per il brand italiano **Diadora**, analizzando il posizionamento competitivo rispetto ai principali player del mercato calzaturiero.

Attraverso web scraping automatizzato, sono stati raccolti e analizzati **~1.800 modelli** di scarpe da **6 brand** concorrenti, producendo insight strategici su pricing, ampiezza di offerta, varietà cromatica e inclusività delle taglie.

---

## 🎯 Risultati Chiave

| Metrica | Valore |
|---|---|
| 🏷️ Brand Monitorati | 6 (Diadora, Nike, Adidas, Puma, New Balance, Asics) |
| 👟 Modelli Analizzati | ~1.800 |
| 💶 Prezzo Medio Diadora | **€69** vs €115 mercato |
| 📦 Gap Sneakers Lifestyle | **+340 modelli** vs Nike |
| 🎨 Gap Varianti Colore | **3,2** Diadora vs 5,8 market leader (+52%) |

---

## 🗂️ Struttura del Repository

```
footwear-competitor-analysis/
├── 📂 data/                  # Dataset raccolti via scraping (.xlsx)
├── 📂 notebooks/             # Jupyter Notebooks con il codice di scraping e analisi
│   └── scraping_multibrand.ipynb
├── 📂 screenshots/           # Screenshot e output visivi dell'analisi
├── 📂 src/                   # Moduli Python riutilizzabili
└── 📄 README.md
```

---

## ⚙️ Tech Stack

![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python)
![Selenium](https://img.shields.io/badge/Selenium-WebDriver-green?logo=selenium)
![BeautifulSoup](https://img.shields.io/badge/BeautifulSoup4-scraping-orange)
![Pandas](https://img.shields.io/badge/Pandas-data--analysis-150458?logo=pandas)
![openpyxl](https://img.shields.io/badge/openpyxl-Excel-217346?logo=microsoftexcel)

- **Selenium + ChromeDriver** — Navigazione dinamica e gestione JavaScript rendering
- **BeautifulSoup4** — Parsing HTML e auto-detection selettori CSS
- **Pandas** — Aggregazioni, pivot table e analisi statistica
- **openpyxl** — Generazione report Excel formattati con grafici

---

## 🚀 Getting Started

### Prerequisiti
- Python 3.8+
- Google Chrome installato

### Installazione

```bash
# 1. Clona il repository
git clone https://github.com/tonyesse02/footwear-competitor-analysis.git
cd footwear-competitor-analysis

# 2. Installa le dipendenze
pip install -r requirements.txt

# 3. Avvia il notebook
jupyter notebook notebooks/scraping_multibrand.ipynb
```

### Configurazione rapida

Nel notebook puoi personalizzare i parametri di scraping:

```python
analyzer = CompetitiveAnalyzer(
    headless=False,    # True = browser invisibile, False = browser visibile
    brands=["Diadora", "Nike", "Adidas", "Puma", "New Balance", "Asics"]
)
df = analyzer.run(max_per_category=80)
```

---

## 🔍 Come Funziona lo Scraper

Lo scraper è strutturato in due versioni iterative:

**v3.0 — Single Brand (Diadora)**
Analizza le categorie del sito Diadora con auto-detection dei selettori CSS tramite pattern matching regex.

**v4.0 — Multi-Brand** *(versione finale)*
Architettura OOP con configurazione dichiarativa per ogni brand. Include:

- `BRAND_CONFIGS` — dizionario con URL, selettori CSS, e categorie per ogni brand
- `BrandScraper` — scraper generico configurabile: gestisce cookie, scroll infinito, paginazione, estrazione prezzi e colori
- `CompetitiveAnalyzer` — orchestratore che coordina tutti gli scraper e produce il report Excel finale con 5 sheet di analisi

```
CompetitiveAnalyzer
    └── BrandScraper (×6 brand)
            ├── handle_cookies()
            ├── scroll_to_load()
            ├── find_product_containers()
            ├── extract_price()
            ├── extract_colors_count()
            └── classify_product()  ← classificatore automatico per categoria/sottocategoria
```

> ⚠️ *Alcuni siti (es. Asics) bloccano lo scraping automatico dopo più richieste. I dati finali presentati nella strategia sono stati raccolti in sessioni separate.*

---

## 📊 Principali Insight Strategici

### Posizionamento Prezzi
Diadora si posiziona nel segmento **Premium-Accessibile (€50–€130)** con un prezzo medio di **€69**, il più basso del mercato. Mantiene competitività assoluta nella fascia entry-mid (€85 vs €110 Adidas).

### Gap Critico — Sneakers Lifestyle
Con soli **45 modelli** vs 385 di Nike e 320 di Adidas, il gap nell'offerta Lifestyle è il principale punto di debolezza identificato.

### Opportunità — Varietà Colori
La media di **3,2 varianti colore** per modello limita il visual share of shelf. Target: portare a **5+ varianti** entro FY2025.

### Inclusività come Leva di Crescita
L'assenza di mezze taglie e wide fit (presenti in tutti i competitor) rappresenta un'opportunità stimata di **+11%** di conversione nel segmento Running.

---

## 📋 Piano d'Azione Raccomandato

| Priorità | Azione | Target |
|---|---|---|
| 🔴 Alta | Espansione Sneakers Lifestyle: da 45 a 120+ modelli | +75 modelli entro Q2 2025 |
| 🔴 Alta | Aumento varianti colore | +60% entro FY2025 |
| 🟡 Media | Introduzione mezze taglie nel Running | +11% conversione attesa |
| 🟡 Media | Espansione linea Slides a 15 modelli | Target €35–60 |
| ⚪ Standard | Lancio segmento Stivali Alto | Target €160–200, AW 2025 |

---

## 👥 Team

Progetto realizzato da:
- Colucci Silvia
- D'Agostino Giovanna Maria
- Della Gatta Francesco
- Pappalardo Gino
- Spagnuolo Antonio

---

## 📄 License

Questo progetto è rilasciato sotto licenza [MIT](LICENSE). I dati raccolti sono utilizzati esclusivamente a scopo accademico e di ricerca.
