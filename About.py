import streamlit as st

st.title("🧩 모델 설명 (AV-HSI 구성)")

st.markdown("""
## 📌 AV–HSI란?  
AV-HSI(Air–Vibration Hybrid Safety Index)는  
**공연장 환경 + 관람객 인원 + 장르 특성 + 계절 요소**를 반영한  
공연장 **통합 안전·환경지수**입니다.

---

## 📚 사용한 데이터
- 한국체육산업개발 KSPC 공연장 정보
- 스포츠센터 공기질/CO₂ 인원 증가량 연구값
- 서울시 미세먼지/계절 요인 데이터
- 관람객·장르별 위험 가중치

---

## 🤖 사용된 모델 : XGBoost Regressor
- OneHotEncoder + ColumnTransformer 전처리
- 관람 인원 / 장르 / 공연장 / MONTH 을 입력
- 위험도(0~100)을 출력

---

## 🧮 위험등급 산정 기준
| 위험도 | 등급 |
|--------|------|
| 81~100 | 🚨 매우 위험 |
| 61~80 | ⚠️ 경계 |
| 41~60 | 주의 |
| 21~40 | 양호 |
| 0~20 | 안전 |

""")
