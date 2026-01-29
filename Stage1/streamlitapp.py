import streamlit as st
import os
def giaithua(x):
    if x != int(x):
        return "nhap so nguyen di"
    x = int(x)
    if x < 0:
        return "nhap so lon hon 0 di"
    ans = 1
    for i in range(1,x+1):
        ans *= i
    return ans

def load_user():
    path = r"C:\HocML\Stage1\user.txt"
    try:
        if os.path.exists(path):
            with open(path,"r",encoding = "utf-8") as f:
                user = [line.strip() for line in f.readlines() if line.strip()]
                return user
        else:
            st.error("file user khong ton tai")
    except Exception as e:
        st.error(f"loi khi doc file user: {e}")
        return []
def login_page():
    st.title("Dang nhap")

    username = st.text_input("nhap ten nguoi dung:")

    if st.button("Dang nhap"):
        if username:
            user = load_user()
            if username in user:
                st.session_state.login = True
                st.session_state.username = username
                st.rerun()
            else:
                st.session_state.greeting = True
                st.session_state.username = username
                st.rerun()
        else:
            st.warning("co dinh nhap ten nguoi dung khom?")
def factorial_calculator():
    st.title("chao mung vuot duoc ai user")

    st.write(f"xin chao, {st.session_state.username}")

    if st.button("dang xuat"):
        st.session_state.login = False
        st.session_state.username = ""
        st.rerun()
    # co divi nma k bt de lam gi
    st.divider()

    number = st.number_input("hi")

    if st.button("tinh giai thua"):
        res = giaithua(number)
        st.write(f"giai thua cua {number} la {res}")

def greating_page():
    st.title("ni hao")
    st.write(f"ni hao ma {st.session_state.username}")
    st.write("rat tiec rat tiec")

    if st.button("Quay la dang nhap di onichan"):
        st.session_state.greeting = False
        st.session_state.unsername = ""
        st.rerun()
def main():
    if 'login' not in st.session_state:
        st.session_state.login = False
    if "username" not in st.session_state:
        st.session_state.username = ""
    if "greeting" not in st.session_state:
        st.session_state.greeting = False
    
    if st.session_state.login:
        factorial_calculator()
    elif st.session_state.greeting:
        greating_page()
    else:
        login_page()
# them 1 ci kho hieu
main()

