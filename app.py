import streamlit as st
import random
import time

# 앱 설정
st.set_page_config(page_title="결정해줘!", page_icon="🎲")

st.title("🎲 오늘의 결정")
st.write("고민되는 선택지들을 한 줄에 하나씩 적어주세요.")

# 1. 입력창 (여러 줄 입력 가능)
# 똑같은 걸 여러 번 적으면 그만큼 확률이 올라갑니다!
user_input = st.text_area("선택지 입력 (한 줄에 하나씩)", 
                         # 예시: 짜장면이 2배 확률
                         height=150)

# 2. 리스트 정리
options = [line.strip() for line in user_input.split('\n') if line.strip()]

# 3. 현재 주머니 상태 보여주기
if options:
    st.info(f"현재 주머니에 총 **{len(options)}개**의 제비가 들어있어요.")
    with st.expander("내용 확인하기"):
        st.write(", ".join(options))

# 4. 버튼 및 결과
st.divider()

if st.button("🚀 주머니에서 하나 뽑기"):
    if options:
        # 애니메이션 효과
        progress_bar = st.progress(0)
        status_text = st.empty()
        
        for i in range(100):
            status_text.text(f"주머니 섞는 중... {random.choice(options)}")
            progress_bar.progress(i + 1)
            time.sleep(0.01)
            
        # 최종 결과
        result = random.choice(options)
        status_text.empty()
        progress_bar.empty()
        
        st.balloons()
        st.success("결과가 나왔습니다!")
        st.markdown(f"""
            <div style="background-color: #f0f2f6; padding: 30px; border-radius: 10px; text-align: center;">
                <h1 style="color: #ff4b4b; font-size: 40px;">{result}</h1>
            </div>
        """, unsafe_allow_html=True)
    else:
        st.warning("선택지를 최소 하나는 입력해주세요!")
