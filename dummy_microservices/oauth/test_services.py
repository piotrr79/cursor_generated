import pytest
from datetime import datetime, timedelta
from dummy_microservices.oauth.models import Database
from dummy_microservices.oauth.services import UserService, TokenService

@pytest.fixture
def db():
    # Use an in-memory SQLite DB for testing
    db = Database(":memory:")
    return db

@pytest.fixture
def user_service(db):
    return UserService(db)

@pytest.fixture
def token_service(db):
    return TokenService(db)

def test_register_and_authenticate(user_service):
    assert user_service.register("alice", "password123")
    user_id = user_service.authenticate("alice", "password123")
    assert user_id is not None
    # Wrong password
    assert user_service.authenticate("alice", "wrong") is None
    # Duplicate registration
    assert not user_service.register("alice", "password123")

def test_token_creation_and_verification(user_service, token_service):
    user_service.register("bob", "pw")
    user_id = user_service.authenticate("bob", "pw")
    token = token_service.create_token(user_id)
    assert token_service.verify_token(token) == user_id
    # Expired token
    # (simulate by creating a token with past expiration)
    from jose import jwt
    from dummy_microservices.oauth.services import SECRET_KEY, ALGORITHM
    expired_token = jwt.encode({"sub": str(user_id), "exp": datetime.utcnow() - timedelta(minutes=1)}, SECRET_KEY, algorithm=ALGORITHM)
    assert token_service.verify_token(expired_token) is None 