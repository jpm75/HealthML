{\rtf1\ansi\ansicpg1252\cocoartf1404\cocoasubrtf470
{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
\paperw11900\paperh16840\margl1440\margr1440\vieww10800\viewh8400\viewkind0
\pard\tx566\tx1133\tx1700\tx2267\tx2834\tx3401\tx3968\tx4535\tx5102\tx5669\tx6236\tx6803\pardirnatural\partightenfactor0

\f0\fs24 \cf0 import pandas as pd\
from sklearn.model_selection import train_test_split\
from sklearn.ensemble import RandomForestClassifier\
\
# Load the microbiome and disease dataset\
data = pd.read_csv("microbiome_data.csv")\
\
# Split the data into training and test sets\
X_train, X_test, y_train, y_test = train_test_split(data.iloc[:,:-1], data.iloc[:, -1], test_size=0.2, random_state=42)\
\
# Train a random forest classifier on the training data\
rfc = RandomForestClassifier(n_estimators=100, random_state=42)\
rfc.fit(X_train, y_train)\
\
# Evaluate the model on the test set\
accuracy = rfc.score(X_test, y_test)\
print("Accuracy: \{:.2f\}%".format(accuracy*100))\
\
# Use the trained model to predict the disease for a new sample\
new_sample = pd.DataFrame(\{"colony1": [0.1], "colony2": [0.2], "colony3": [0.3], "colony4": [0.4], "colony5": [0.5]\})\
prediction = rfc.predict(new_sample)\
print("Predicted disease for the new sample:", prediction[0])\
}