import streamlit as st
import random

st.set_page_config(page_title="プログラミング演習 試験対策", layout="centered")

questions = [
    {
        "type": "ox",
        "question": "Webサイトから自動的に情報を取得する技術をスクレイピングという。",
        "answer": "○",
        "explain": "HTMLなどを自動取得する技術。"
    },
    {
        "type": "choice",
        "question": "Kaggleはどのようなプラットフォームか？",
        "choices": ["GitHub", "Kaggle", "Docker", "Flask"],
        "answer": "Kaggle",
        "explain": "データ分析コンペとデータ共有の場。"
    },
    {
        "type": "fill",
        "question": "平均を0、分散を1に揃える処理を（　）という。",
        "answer": "標準化",
        "explain": "Zスコア化とも呼ばれる。"
    },
    {
        "type": "choice",
        "question": "時系列予測ライブラリ Prophet を開発した企業は？",
        "choices": ["Google", "Meta", "Microsoft", "Amazon"],
        "answer": "Meta",
        "explain": "旧Facebook。"
    },
    {
        "type": "ox",
        "question": "k-means法は教師あり学習である。",
        "answer": "×",
        "explain": "教師なし学習。"
    }
]

if "index" not in st.session_state:
    random.shuffle(questions)
    st.session_state.index = 0
    st.session_state.score = 0
    st.session_state.finished = False

st.title("📘 プログラミング演習 試験対策クイズ")

if st.session_state.finished:
    st.success(f"終了！ 正解数：{st.session_state.score} / {len(questions)}")
    st.write(f"正答率：{st.session_state.score / len(questions) * 100:.1f}%")

    if st.button("もう一度"):
        st.session_state.index = 0
        st.session_state.score = 0
        st.session_state.finished = False
        random.shuffle(questions)
    st.stop()

q = questions[st.session_state.index]
st.write(f"### Q{st.session_state.index + 1}")
st.write(q["question"])

answer = None
if q["type"] == "ox":
    answer = st.radio("答え", ["○", "×"])
elif q["type"] == "choice":
    answer = st.radio("答え", q["choices"])
elif q["type"] == "fill":
    answer = st.text_input("答えを入力")

if st.button("回答する"):
    if answer == "":
        st.warning("答えを入力してください")
    else:
        if answer == q["answer"]:
            st.success("⭕ 正解")
            st.session_state.score += 1
        else:
            st.error(f"❌ 不正解（正解：{q['answer']}）")

        st.info(f"💡 解説：{q['explain']}")

        if st.button("次の問題へ"):
            st.session_state.index += 1
            if st.session_state.index >= len(questions):
                st.session_state.finished = True
            st.experimental_rerun()
