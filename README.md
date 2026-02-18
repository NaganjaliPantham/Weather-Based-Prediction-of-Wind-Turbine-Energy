# Weather-Based Prediction of Wind Turbine Energy Output: A Next-Generation Approach to Renewable Energy Management

The project aims to predict the energy output of a wind turbine based on weather conditions. This is valuable for energy companies and grid operators to better manage and optimize energy production. By analyzing historical data of weather conditions and energy output, machine learning models can be trained to predict the energy output of a wind turbine given current weather conditions.
# Project Demo Video
# Team Details

|                 |                         |
| --------------- | ----------------------- |
| **Team ID**     | LTVIP2026TMIDS84120     |
| **Team Leader** | Pantham Naganjali       |
| **Team Member** | Gurram Teja Sri         |
| **Team Member** | Dadala Lakshman         |
| **Team Member** | Steni Desabathula       |

---

## Project Structure

```
smartinternz/
├── data/
│   └── dataset/
│       ├── train.csv                        # Training dataset (28,200 rows)
│       └── test.csv                         # Test dataset (12,087 rows)
├── Flask-Wind-Mill-Power-Prediction/
│   ├── static/
│   │   └── style.css                        # Stylesheet for the web app
│   ├── templates/
│   │   ├── intro.html                       # Landing page
│   │   └── predict.html                     # Weather API & prediction page
│   ├── .env                                 # Environment variables (API key)
│   ├── app.py                               # Flask app entry point
│   ├── windApp.py                           # Flask routes & prediction logic
│   └── power_prediction.sav                 # Saved ML model (for Flask)
├── Wind_mill_model.ipynb                    # Jupyter Notebook (full pipeline)
├── wind turbine energy prediction.py        # Standalone ML pipeline script
├── test_model.py                            # Script to test saved model
├── power_prediction.sav                     # Saved ML model
└── README.md
```

---

## Technologies Used

| Category                | Technology                  |
| ----------------------- | --------------------------- |
| **Language**            | Python                      |
| **ML Libraries**        | NumPy, Pandas, Scikit-learn |
| **Visualization**       | Matplotlib, Seaborn         |
| **Model**               | Random Forest Regressor     |
| **Web Framework**       | Flask                       |
| **API**                 | OpenWeatherMap API          |
| **Frontend**            | HTML, CSS                   |
| **Model Serialization** | Joblib                      |
| **Environment**         | Jupyter Notebook, VS Code   |

---

## Project Setup

### 1. Clone the Repository

```bash
git clone https://github.com/Sujeeth-Varma/Weather-Based-Prediction-of-Wind-Turbine-Energy-Output.git
```

### 2. Create & Activate Virtual Environment

```bash
python -m venv .venv
source .venv/bin/activate        # Linux/Mac
.venv\Scripts\activate         # Windows
```

### 3. Install Dependencies

```bash
pip install numpy pandas matplotlib seaborn scikit-learn joblib flask requests python-dotenv
```

### 4. Download Dataset

```bash
curl -L -o data/predict-the-powerkwh-produced-by-windmills.zip \
  https://www.kaggle.com/api/v1/datasets/download/emnikkhil/predict-the-powerkwh-produced-by-windmills
unzip data/predict-the-powerkwh-produced-by-windmills.zip -d data/
```

### 5. Train the Model

```bash
python "wind turbine energy prediction.py"
```

This will train the Random Forest Regressor and save it as `power_prediction.sav`.

### 6. Test the Model

```bash
python test_model.py
```

### 7. Run the Flask App

```bash
cd "Flask-Wind-Mill-Power-Prediction"
```

Add your OpenWeatherMap API key in the `.env` file:

```
OPENWEATHER_API_KEY=your_api_key_here
```

Then start the server:

```bash
python app.py
```

Open **http://127.0.0.1:5000** in your browser.
# Weather-Based-Prediction-of-Wind-Turbine-Energy
