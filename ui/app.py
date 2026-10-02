
import streamlit as st
import pandas as pd
import joblib

model = joblib.load('models/final_model.pkl')

st.title('Heart Disease Prediction App')
age = st.number_input('Age', value=50)
sex = st.selectbox('Sex (1 = Male, 0 = Female)', [0, 1])
cp = st.selectbox('Chest Pain Type', [0, 1, 2, 3])
trestbps = st.number_input('Resting Blood Pressure', value=120)
chol = st.number_input('Cholesterol', value=200)
fbs = st.selectbox('Fasting Blood Sugar > 120', [0, 1])
restecg = st.selectbox('Resting ECG', [0, 1, 2])
thalach = st.number_input('Max Heart Rate', value=150)
exang = st.selectbox('Exercise Induced Angina', [0, 1])
oldpeak = st.number_input('Oldpeak', value=1.0)
slope = st.selectbox('Slope', [0, 1, 2])
ca = st.selectbox('CA', [0, 1, 2, 3])
thal = st.selectbox('Thal', [1, 2, 3])

if st.button('Predict'):
    input_data = pd.DataFrame([[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]],
                              columns=['age', 'sex', 'cp', 'trestbps', 'chol', 'fbs', 'restecg', 'thalach', 'exang', 'oldpeak', 'slope', 'ca', 'thal'])
    pred = model.predict(input_data)
    if pred[0] == 1:
        st.error('تحذير: يوجد احتمال الإصابة بمرض القلب!')
    else:
        st.success('النتيجة: سليمة (لا يوجد خطر ظاهر).')
