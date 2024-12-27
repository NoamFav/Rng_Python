import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.arima.model import ARIMA

# Data
data_dict = {
    "Pompidou": 2279,
    "Fillon": 1819,
    "Jospin": 1800,
    "Barre": 1722,
    "Debré": 1192,
    "Mauroy": 1153,
    "Philippe": 1145,
    "Raffarin": 1119,
    "Chaban-Delmas": 1111,
    "Rocard": 1100,
    "Valls": 981,
    "Chirac": 821,
    "Chirac": 782,
    "Balladur": 773,
    "Juppé": 757,
    "de Villepin": 715,
    "Messmer": 691,
    "Ayrault": 685,
    "Castex": 682,
    "Fabius": 611,
    "Borne": 603,
    "Bérégovoy": 360,
    "Couve de Murville": 345,
    "Cresson": 323,
    "Attal": 240,
    "Cazeneuve": 160,
    "Barnier": 91,
}

# Sort data by days in descending order
sorted_data = sorted(data_dict.items(), key=lambda x: x[1], reverse=True)
sorted_names, sorted_days = zip(*sorted_data)

# Time series data
time_series_data = np.array(sorted_days)

# Fit an ARIMA model
model = ARIMA(time_series_data, order=(2, 1, 0))  # ARIMA(p, d, q)
fitted_model = model.fit()

# Forecast the next 10 values
forecast_steps = 10
forecast = fitted_model.forecast(steps=forecast_steps)

# Ensure predictions are non-negative
forecast = np.maximum(forecast, 0)

# Plot the actual data and predictions
plt.figure(figsize=(10, 6))
plt.plot(sorted_names, sorted_days, marker="o", linestyle="-", label="Actual Data")
plt.plot(
    list(sorted_names) + [f"Future {i}" for i in range(1, forecast_steps + 1)],
    np.concatenate([sorted_days, forecast]),
    marker="o",
    linestyle="--",
    color="purple",
    label="Forecasted Data (ARIMA)",
)
plt.xticks(rotation=90)
plt.xlabel("Names")
plt.ylabel("Days in Office")
plt.title("Duration in Office with Forecasted Values (ARIMA Model)")
plt.legend()
plt.tight_layout()
plt.show()
