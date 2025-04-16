# save_model.py
import pickle
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
import pandas as pd
from sklearn.model_selection import train_test_split

df=pd.read_csv("Houseprice/Housing.csv")

yn_cols=["mainroad", "guestroom", "basement", "hotwaterheating", "airconditioning", "prefarea"]
df[yn_cols]=df[yn_cols].replace({"yes": 1, "no": 0})
df["furnishingstatus"]=df["furnishingstatus"].replace({"furnished": 1, "unfurnished": 0, "semi-furnished": 2})
X=df.drop("price",axis=1)
y=df["price"]
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

with open("app/housemodel.pkl", "wb") as f:
    pickle.dump(model, f)