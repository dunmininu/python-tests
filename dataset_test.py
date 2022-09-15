import pandas as pd
import uuid
import random
from faker import Faker
import datetime

num_users = 100000

features = [
    "id",
    "gender",
    "subscriber",
    "name",
    "email",
    "last_login",
    "dob",
    "education",
    "bio",
    "rating",
]

df = pd.DataFrame(columns=features)

df["id"] = [uuid.uuid4().hex for i in range(num_users)]

print(df["id"].nunique() == num_users)
