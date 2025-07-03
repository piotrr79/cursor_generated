# Dummy ML PII Detection Model

This project provides a basic machine learning model to analyze text data for the presence of personal details (PII), such as:
- Email
- Phone number
- Place of birth
- Age
- Salary
- Credit card number
- Bank account number
- Social logins (Google, Facebook, etc.)

## Approach
- Uses regular expressions for direct pattern matching.
- Falls back to a simple Naive Bayes classifier trained on Lorem Ipsum examples.

## Files
- `model.py` — Main model and prediction logic
- `requirements.txt` — Python dependencies
- `test_model.py` — Unit tests for the model

## Usage
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Run the model on example texts:
   ```bash
   python model.py
   ```
3. Run tests:
   ```bash
   pytest test_model.py
   ```

## Notes
- This is a demonstration model and not suitable for production PII detection.
- For real-world use, expand the training data and regex patterns. 