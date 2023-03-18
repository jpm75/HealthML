{\rtf1\ansi\ansicpg1252\cocoartf1404\cocoasubrtf470
{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
\paperw11900\paperh16840\margl1440\margr1440\vieww10800\viewh8400\viewkind0
\pard\tx566\tx1133\tx1700\tx2267\tx2834\tx3401\tx3968\tx4535\tx5102\tx5669\tx6236\tx6803\pardirnatural\partightenfactor0

\f0\fs24 \cf0 import numpy as np\
from keras.models import Sequential\
from keras.layers import Dense\
\
# Define the DNN model architecture\
model = Sequential()\
model.add(Dense(64, input_dim=5, activation='relu'))\
model.add(Dense(64, activation='relu'))\
model.add(Dense(1, activation='sigmoid'))\
\
# Compile the model\
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])\
\
# Load the training data\
X_train = np.array([[0.1, 0.2, 0.3, 0.4, 0.5], [0.2, 0.3, 0.4, 0.5, 0.6]])\
y_train = np.array([0, 1])\
\
# Train the model\
model.fit(X_train, y_train, epochs=100, batch_size=32)\
\
# Use the model to make predictions\
X_test = np.array([[0.1, 0.2, 0.3, 0.4, 0.5]])\
prediction = model.predict(X_test)\
\
# Determine the drug based on the prediction\
if prediction >= 0.5:\
    drug = "Drug A"\
else:\
    drug = "Drug B"\
\
# Print the suggested drug\
print("Suggested drug for this disease: ", drug)\
}