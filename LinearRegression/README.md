## Boston House Price Prediction (Flask + Linear Regression)

This project serves a simple web app to predict median house values (MEDV) in Boston using a trained Linear Regression model.

### Features
- Predicts Boston house prices from 13 standard dataset features
- Flask web UI with a form for inputs
- Simple server-side rendering with `templates/index.html`

### Project Structure
```
Boston House Price Prediction/
  └─ LinearRegression/
       ├─ boston_housing.pkl         # Trained scikit-learn LinearRegression model
       ├─ linearRegression.py        # Flask app
       ├─ requirements.txt           # Python dependencies
       └─ templates/
            └─ index.html            # Web form and result display
```

### Requirements
- Python 3.8+
- pip

Install project dependencies:
```bash
cd "LinearRegression"
pip install -r requirements.txt
```

Note: You may see a warning about scikit-learn model version mismatch when loading `boston_housing.pkl`. The model was trained on a newer version; predictions still work, but to avoid the warning you can align scikit-learn versions or retrain the model in your current environment.

### Run the App (Development)
Using PowerShell on Windows:
```powershell
cd "LinearRegression"
python .\linearRegression.py
```

The server starts at `http://127.0.0.1:5000/` (or `http://localhost:5000/`). Open it in your browser.

### Usage
1. Open the web app.
2. Enter numeric values for each feature:
   - `CRIM`, `ZN`, `INDUS`, `CHAS`, `NOX`, `RM`, `AGE`, `DIS`, `RAD`, `TAX`, `PTRATIO`, `B`, `LSTAT`.
3. Submit to get the predicted house price.

The prediction is shown as a single numeric value. For the Boston dataset, MEDV values represent thousands of dollars. For example, 24.7 ≈ $24,700.

### API Endpoints
- `GET /` → Renders the form (`templates/index.html`).
- `POST /predict` → Accepts the 13 feature values from the form and returns a page with the prediction.

### Environment Variables (Optional)
- `FLASK_ENV=development` to enable auto-reload and debug mode (already `debug=True` in the script for local use).

### Common Issues & Troubleshooting
- "Trying to unpickle estimator LinearRegression from version X when using version Y":
  - Align scikit-learn versions (install the version used for training) or retrain the model with your current version.
- "X does not have valid feature names, but LinearRegression was fitted with feature names":
  - This is a warning from scikit-learn when passing a plain array. It does not block predictions in this app.
- Page not found / template error:
  - Ensure the `templates/index.html` file exists at `LinearRegression/templates/index.html`.
- Import or module errors:
  - Reinstall requirements: `pip install -r requirements.txt`.

### Retraining (Optional)
If you want a fresh model trained in your environment:
1. Load the Boston housing dataset from a trusted source or a local copy.
2. Train a `LinearRegression` model using the same 13 features in this order:
   `CRIM, ZN, INDUS, CHAS, NOX, RM, AGE, DIS, RAD, TAX, PTRATIO, B, LSTAT`.
3. Save with pickle:
```python
import pickle
with open("boston_housing.pkl", "wb") as f:
    pickle.dump(model, f)
```
4. Replace the `boston_housing.pkl` in `LinearRegression/`.

### License
For educational and demo purposes.


