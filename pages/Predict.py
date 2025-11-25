import streamlit as st
import pandas as pd
import pickle

st.title("🔮 공연 위험도 예측")

# Load model
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

hall = st.selectbox(
    "공연장",
    ['KSPO DOME', '핸드볼경기장', '올림픽홀', '우리금융아트홀']
)

genre = st.selectbox(
    "장르",
    ['아이돌/댄스/대중가요','갈라','뮤지컬/클래식/오케스트라','팝/밴드/재즈',
     '트로트','이벤트/기타','발라드','전자음악/힙합','인디/어쿠스틱']
)

audience = st.slider(
    "관람인원", 1000, 90000, 20000, step=500
)

month = st.selectbox("월", list(range(1, 13)))

if st.button("예측하기"):
    new_data = pd.DataFrame([{
        "공연장": hall,
        "장르": genre,
        "관람인원": audience,
        "MONTH": month
    }])

    pred = model.predict(new_data)[0]

    # 위험 등급
    if pred >= 81: label = "🚨 5단계 (위험)"
    elif pred >= 61: label = "⚠️ 4단계 (경계)"
    elif pred >= 41: label = "3단계 (주의)"
    elif pred >= 21: label = "2단계 (양호)"
    else: label = "1단계 (안전)"

    st.subheader("📌 예측 결과")
    st.write(f"**AV-HSI 예측치:** {pred:.2f}")
    st.write(f"**위험 등급:** {label}")
