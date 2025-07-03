import re
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline

class PiiDetector:
    PII_PATTERNS = {
        'email': r'[\w\.-]+@[\w\.-]+',
        'phone': r'\b\d{3}[-.\s]?\d{3}[-.\s]?\d{4}\b',
        'credit_card': r'\b(?:\d[ -]*?){13,16}\b',
        'bank_account': r'\b\d{8,20}\b',
        'social_login': r'(facebook|google|twitter|linkedin)',
        'place_of_birth': r'(Springfield|Metropolis|Gotham|Lorem|Ipsum)',
        'age': r'\b\d{1,3} (years old|yrs old|y/o|age)\b',
        'salary': r'\$?\d{1,3}(,\d{3})*(\.\d{2})? (USD|EUR|PLN|dollars|euros|zloty|salary)'
    }

    def __init__(self, train_data=None):
        if train_data is None:
            train_data = [
                ("Lorem ipsum dolor sit amet, 123-456-7890 consectetur.", 'phone'),
                ("Contact me at lorem.ipsum@email.com for more info.", 'email'),
                ("My credit card is 4111 1111 1111 1111.", 'credit_card'),
                ("Bank account: 1234567890123456.", 'bank_account'),
                ("I was born in Lorem.", 'place_of_birth'),
                ("My age is 42 years old.", 'age'),
                ("My salary is $100,000 USD.", 'salary'),
                ("Login with Google or Facebook.", 'social_login'),
                ("Just some random Lorem Ipsum text.", 'none'),
                ("No PII here, just Ipsum.", 'none')
            ]
        self.X_train = [x[0] for x in train_data]
        self.y_train = [x[1] for x in train_data]
        self.model = Pipeline([
            ('vect', CountVectorizer()),
            ('clf', MultinomialNB())
        ])
        self.train()

    def train(self):
        self.model.fit(self.X_train, self.y_train)

    def predict(self, text):
        for label, pattern in self.PII_PATTERNS.items():
            if re.search(pattern, text, re.IGNORECASE):
                return label
        return self.model.predict([text])[0]

if __name__ == "__main__":
    detector = PiiDetector()
    test_texts = [
        "Contact: 555-123-4567",
        "My email is test@example.com",
        "My salary is 50000 euros.",
        "I was born in Ipsum.",
        "This is just a test sentence."
    ]
    for t in test_texts:
        print(f"Text: {t}\nPrediction: {detector.predict(t)}\n") 