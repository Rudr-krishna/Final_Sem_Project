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
    - Visual results for one representative company are shown in the report, with results for 
      the remaining companies included in the appendix.

## Technology Stack

- **Language**: Python
- **Libraries**: NumPy, Pandas, Scikit-learn, Keras, Statsmodels, Matplotlib, Seaborn
- **Model Used**: LSTM, ARIMA, ARIMAX
- **Data Source**: Yahoo Finance API 
