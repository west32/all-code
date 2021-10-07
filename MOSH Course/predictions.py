import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.externals import joblib


music_data=pd.read_csv("music.csv")
X=music_data.drop(columns=["genre"])
Y=music_data["genre"]

model= DecisionTreeClassifier()
model.fit(X,Y)
joblib.dump(model, "music-recommender.joblib")