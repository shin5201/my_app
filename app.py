import streamlit as st

st.title("平均値計算アプリ")

numbers = st.text_input("数値を入力してください (カンマ区切り)")

if numbers:
    num_list = list(map(int, numbers.split(",")))
    avg = sum(num_list) / len(num_list)
    st.write("平均値: ", avg)
else:
    st.write("数値を入力してください")
