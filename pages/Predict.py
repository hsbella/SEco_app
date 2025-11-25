import streamlit as st
import pandas as pd
import pickle

st.title("🔮 공연 위험도 예측")

# 모델 로드
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

# 학습 데이터 기반 실제 카테고리 값
hall_list = ['KSPO DOME', '핸드볼경기장', '우리금융아트홀', '올림픽홀']

genre_list = [
    '아이돌/댄스/대중가요',
    '갈라',
    '뮤지컬/클래식/오케스트라',
    '팝/밴드/재즈',
    '트로트',
    '록/밴드/인디',
    '이벤트/기타',
    '발라드',
    '전자음악/힙합',
    '인디/어쿠스틱'
]

# 입력 UI
hall = st.selectbox("공연장", hall_list)
genre = st.selectbox("장르", genre_list)
audience = st.slider("관람인원", 100, 100000, 100, step=100)
month = st.selectbox("월", list(range(1,13)))


# 예측 버튼
if st.button("예측하기"):

    # 컬럼 순서를 학습 순서와 정확히 맞춤
    new_data = pd.DataFrame(
        [[hall, genre, audience, month]],
        columns=['공연장', '장르', '관람인원', 'MONTH']
    )

    # 예측
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


