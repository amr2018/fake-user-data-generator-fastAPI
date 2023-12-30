
from faker import Faker
from fastapi import FastAPI

app = FastAPI()
fake = Faker()

# create home route
@app.get('/')
def home():
    return {'msg': 'hello world'}

# create fake user info generator route
@app.get('/fake-user-data')
def fake_user():
    return {
        'first name': fake.first_name(),
        'last name': fake.last_name(),
        'username': fake.user_name(),
        'email': fake.email(),
        'password': fake.password(),
        'website': fake.url()
    }
