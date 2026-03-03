"""
config.py
=========
Configurazione centralizzata per il Competitive Analyzer.

Contiene:
  - BRAND_CONFIGS  : URL, selettori CSS e categorie target per ogni brand
  - CATEGORY_RULES : regole di classificazione automatica dei prodotti
"""

from selenium.webdriver.common.by import By
from typing import Dict, List, Tuple


# ---------------------------------------------------------------------------
# BRAND CONFIGURATIONS
# ---------------------------------------------------------------------------

BRAND_CONFIGS: Dict[str, Dict] = {

    "Diadora": {
        "base_url": "https://www.diadora.com/it/it/",
        "cookie_selectors": [
            (By.ID,    "onetrust-accept-btn-handler"),
            (By.XPATH, "//button[contains(text(), 'Accetta')]"),
            (By.XPATH, "//button[contains(text(), 'Accept')]"),
        ],
        "product_container": [
            ("div", r"product-grid__item"),
            ("div", r"product-tile"),
            ("li",  r"product-item"),
        ],
        "name_selectors": [
            ("class", r"product-tile__name"),
            ("class", r"product-name"),
        ],
        "price_selectors": [
            ("class", r"product-price__sale"),
            ("class", r"price"),
        ],
        "color_selectors": [
            ("class", r"color-swatches"),
            ("class", r"swatch"),
        ],
        "size_selectors": [
            ("class", r"size-selector"),
            ("class", r"sizes"),
        ],
        "category_url_map": {
            "Sneakers": "https://www.diadora.com/it/it/calzature/sneakers/",
            "Running":  "https://www.diadora.com/it/it/calzature/running/",
            "Calcio":   "https://www.diadora.com/it/it/calzature/calcio/",
            "Sandali":  "https://www.diadora.com/it/it/calzature/sandali/",
            "Stivali":  "https://www.diadora.com/it/it/calzature/stivali/",
        },
        "pagination_selector": (By.XPATH, "//a[@class='pagination__next']"),
    },

    "Nike": {
        "base_url": "https://www.nike.com/it/",
        "cookie_selectors": [
            (By.XPATH, "//button[contains(text(), 'Accetta')]"),
            (By.XPATH, "//button[@id='hf-cookie-accept-btn']"),
        ],
        "product_container": [
            ("div", r"product-card"),
            ("div", r"product-card__body"),
        ],
        "name_selectors": [
            ("class", r"product-card__title"),
            ("class", r"product-card__subtitle"),
        ],
        "price_selectors": [
            ("class", r"product-price"),
        ],
        "color_selectors": [
            ("class", r"product-card__product-count"),
        ],
        "size_selectors": [],
        "category_url_map": {
            "Sneakers": "https://www.nike.com/it/w/sneakers-5e1x6",
            "Running":  "https://www.nike.com/it/w/running-37v7j",
            "Calcio":   "https://www.nike.com/it/w/scarpe-da-calcio-1gdj0",
            "Sandali":  "https://www.nike.com/it/w/sandali-2po3y",
            "Training": "https://www.nike.com/it/w/training-5e1x6",
        },
        "pagination_selector": (By.XPATH, "//button[@data-qa='load-more-button']"),
    },

    "Adidas": {
        "base_url": "https://www.adidas.it/",
        "cookie_selectors": [
            (By.XPATH, "//button[contains(@data-auto-id, 'gdpr-consent-accept')]"),
            (By.XPATH, "//button[contains(text(), 'Accetta')]"),
        ],
        "product_container": [
            ("div", r"product-card"),
            ("div", r"\bgl-product-card\b"),
        ],
        "name_selectors": [
            ("class", r"product-card__title"),
            ("class", r"gl-product-card__name"),
        ],
        "price_selectors": [
            ("class", r"product-card__pricing"),
            ("class", r"gl-product-card__price"),
        ],
        "color_selectors": [
            ("class", r"product-card__color"),
        ],
        "size_selectors": [],
        "category_url_map": {
            "Sneakers": "https://www.adidas.it/scarpe-lifestyle",
            "Running":  "https://www.adidas.it/scarpe-running",
            "Calcio":   "https://www.adidas.it/scarpe-calcio",
            "Sandali":  "https://www.adidas.it/sandali",
            "Training": "https://www.adidas.it/scarpe-training",
            "Tennis":   "https://www.adidas.it/scarpe-tennis",
        },
        "pagination_selector": (By.XPATH, "//button[contains(@class, 'pagination__btn--next')]"),
    },

    "Puma": {
        "base_url": "https://eu.puma.com/it/it/",
        "cookie_selectors": [
            (By.XPATH, "//button[contains(@class, 'accept')]"),
            (By.XPATH, "//button[contains(text(), 'Accetta')]"),
        ],
        "product_container": [
            ("div",     r"product-tile"),
            ("article", r"product"),
        ],
        "name_selectors": [
            ("class", r"product-tile__name"),
            ("class", r"product-name"),
        ],
        "price_selectors": [
            ("class", r"product-price"),
            ("class", r"price"),
        ],
        "color_selectors": [
            ("class", r"product-tile__color"),
        ],
        "size_selectors": [],
        "category_url_map": {
            "Sneakers": "https://eu.puma.com/it/it/sneakers",
            "Running":  "https://eu.puma.com/it/it/running",
            "Calcio":   "https://eu.puma.com/it/it/calcio/scarpe",
            "Sandali":  "https://eu.puma.com/it/it/sandali",
            "Training": "https://eu.puma.com/it/it/training",
        },
        "pagination_selector": (By.XPATH, "//button[contains(@class, 'load-more')]"),
    },

    "New Balance": {
        "base_url": "https://www.newbalance.com/it/",
        "cookie_selectors": [
            (By.XPATH, "//button[contains(text(), 'Accetta')]"),
            (By.ID,    "onetrust-accept-btn-handler"),
        ],
        "product_container": [
            ("li",  r"product-tile"),
            ("div", r"product-tile"),
        ],
        "name_selectors": [
            ("class", r"product-tile__product-name"),
        ],
        "price_selectors": [
            ("class", r"product-tile-price"),
        ],
        "color_selectors": [
            ("class", r"product-tile-colors-count"),
        ],
        "size_selectors": [],
        "category_url_map": {
            "Sneakers": "https://www.newbalance.com/it/uomo/calzature/lifestyle/",
            "Running":  "https://www.newbalance.com/it/uomo/calzature/running/",
            "Training": "https://www.newbalance.com/it/uomo/calzature/training/",
            "Tennis":   "https://www.newbalance.com/it/uomo/calzature/tennis/",
        },
        "pagination_selector": (By.XPATH, "//button[contains(@class, 'pagination')]"),
    },

    "Asics": {
        "base_url": "https://www.asics.com/it/",
        "cookie_selectors": [
            (By.XPATH, "//button[contains(text(), 'Accetta')]"),
            (By.ID,    "onetrust-accept-btn-handler"),
        ],
        "product_container": [
            ("li",  r"product-grid-item"),
            ("div", r"product-tile"),
        ],
        "name_selectors": [
            ("class", r"product-tile__title"),
        ],
        "price_selectors": [
            ("class", r"price"),
            ("class", r"product-tile__price"),
        ],
        "color_selectors": [
            ("class", r"color-swatches"),
        ],
        "size_selectors": [],
        "category_url_map": {
            "Running":  "https://www.asics.com/it/it-it/scarpe/running/",
            "Tennis":   "https://www.asics.com/it/it-it/scarpe/tennis/",
            "Training": "https://www.asics.com/it/it-it/scarpe/training/",
            "Sneakers": "https://www.asics.com/it/it-it/scarpe/lifestyle/",
        },
        "pagination_selector": (By.XPATH, "//a[contains(@class, 'next-page')]"),
    },
}


# ---------------------------------------------------------------------------
# CATEGORY CLASSIFICATION RULES
# ---------------------------------------------------------------------------

CATEGORY_RULES: Dict[str, Dict] = {
    "Running": {
        "keywords": ["run", "running", "corsa", "jogging", "marathon", "boost", "gel"],
        "subcategories": {
            "Strada":      ["road", "strada", "urban"],
            "Trail":       ["trail", "mountain", "off-road"],
            "Racing":      ["race", "racing", "carbon", "pro"],
            "Allenamento": ["training", "everyday", "daily"],
        },
    },
    "Calcio": {
        "keywords": ["calcio", "football", "soccer", "fg", "ag", "tf", "sg", "indoor", "futsal"],
        "subcategories": {
            "Terreno Naturale": ["fg", "firm ground", "naturale"],
            "Sintetico":        ["ag", "artificial", "sintetico", "tf"],
            "Indoor":           ["indoor", "sala", "futsal"],
        },
    },
    "Tennis": {
        "keywords": ["tennis", "court", "clay", "grass", "hard court"],
        "subcategories": {
            "Terra Rossa": ["clay"],
            "Cemento":     ["hard", "all court"],
            "Erba":        ["grass"],
        },
    },
    "Sneakers": {
        "keywords": ["sneaker", "lifestyle", "casual", "retro", "classic", "street", "heritage"],
        "subcategories": {
            "Retro/Heritage": ["retro", "heritage", "classic", "og", "vintage"],
            "Contemporanee":  ["lifestyle", "casual", "contemporary"],
            "Collab/Limited": ["collab", "limited", "special edition"],
        },
    },
    "Training": {
        "keywords": ["training", "cross", "gym", "workout", "fitness", "functional"],
        "subcategories": {
            "Cross Training": ["cross", "crossfit"],
            "Gym":            ["gym", "fitness", "indoor"],
            "Functional":     ["functional", "performance"],
        },
    },
    "Sandali": {
        "keywords": ["sandal", "sandali", "slide", "flip", "ciabatta", "infradito"],
        "subcategories": {
            "Slides":        ["slide", "ciabatta"],
            "Flip Flop":     ["flip", "infradito"],
            "Sandali Bassi": ["sandal", "sandali", "flat"],
        },
    },
    "Stivali": {
        "keywords": ["stival", "boot", "ankle", "chelsea", "combat"],
        "subcategories": {
            "Chelsea":      ["chelsea"],
            "Ankle Boot":   ["ankle"],
            "Combat":       ["combat", "military"],
            "Stivali Alti": ["tall boot", "stivale alto"],
        },
    },
}
