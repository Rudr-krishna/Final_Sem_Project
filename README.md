# Final_Sem_Project

This project focuses on comparing different models for stock price prediction using time series and LSTM-based approaches. The objective is to evaluate and identify the most effective model for forecasting future stock prices across multiple major companies.

**Companies Covered**
- Apple Inc. (AAPL)
- Microsoft Corp. (MSFT)
- Tesla Inc. (TSLA)
- Amazon Inc. (AMZN)
- NVIDIA Corp. (NVDA)

## Project Highlights

1. **Stock Price Prediction:**
    - Predict future closing prices using three models:
        - LSTM (Long Short-Term Memory Neural Network)
        - ARIMA (AutoRegressive Integrated Moving Average)
        - ARIMAX (ARIMA with Exogenous Variables)
    - Model performance is evaluated using:
        - **MAE** (Mean Absolute Error)
        - **RMSE** (Root Mean Squared Error)
        - **R² Score** (Coefficient of Determination)

2. **Model Evaluation**:
    - Each model is trained and tested on one year of historical stock data for each company.
    - Performance metrics are compared to analyze which model performs best.
    - Evaluation includes error metrics tables and actual vs predicted graph visualizations.

## Technology Stack

- **Language**: Python
- **Libraries**: NumPy, Pandas, Scikit-learn, Keras, Statsmodels, Matplotlib, Seaborn
- **Model Used**: LSTM, ARIMA, ARIMAX
- **Data Source**: Yahoo Finance API 

## Getting Started

Follow these steps to clone the repository and run the code:

### 1. Clone the Repository

```bash
git clone https://github.com/Rudr-krishna/Final_Sem_Project.git
cd your-repo-name
```


### 2. Install Required Dependencies

It is recommended to use a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # For Windows: venv\Scripts\activate
```

Then install the dependencies:

```bash
pip install -r requirements.txt
```

---

## File Structure

- `Model_prediction.ipynb` – Main notebook to run the model predictions
- `Generalized_EDA.ipynb` – Notebook for the EDA of all companies stocks data.
- `Generalized_models_and_Evaluation.ipynb` – Main notebook for model training and testing with evaluation of all companies.
- `Data_extraction.py` – Python script to download the stocks data.
- `Models/` – Folder containing saved `.pkl` models
- `Stocks_Data/` – Folder for storing raw or preprocessed stock data
- `requirements.txt` – All required Python packages

---

## How to Use

After installing the requirements, open the Jupyter Notebook:

```bash
jupyter notebook
```

Then run:

```
Model_prediction.ipynb
```

This notebook:
- Loads pre-trained models (`ARIMA`, `ARIMAX`, `LSTM`)
- Uses company-wise data to make **30-day predictions**
- Visualizes the predicted stock prices of the next 30 days.

---

## Note

- Models are already trained and saved in `.pkl` format.
- Ensure you have a stable internet connection for downloading data using `yfinance`.