from model import PiiDetector

def test_predict_pii():
    detector = PiiDetector()
    assert detector.predict("Contact: 555-123-4567") == 'phone'
    assert detector.predict("My email is test@example.com") == 'email'
    assert detector.predict("4111 1111 1111 1111") == 'credit_card'
    assert detector.predict("Bank account: 1234567890123456.") == 'bank_account'
    assert detector.predict("I was born in Ipsum.") == 'place_of_birth'
    assert detector.predict("My age is 42 years old.") == 'age'
    assert detector.predict("My salary is $100,000 USD.") == 'salary'
    assert detector.predict("Login with Google or Facebook.") == 'social_login'
    assert detector.predict("Just some random Lorem Ipsum text.") == 'none' 