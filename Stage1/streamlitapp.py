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
    BASE_DIR = os.path.dirname(__file__)
    user_path = os.path.join(BASE_DIR, "user.txt")
    try:
        if os.path.exists(user_path):
            with open(user_path,"r",encoding = "utf-8") as f:
                user = [line.strip() for line in f.readlines() if line.strip()]
                return user
        else:
            st.error("file user khong ton tai")
    except Exception as e:
        st.error(f"loi khi doc file user: {e}")
        return []
def login_page():
    st.title("Muốn tính giai thừa à, thế có trong team của t k ?")

    username = st.text_input("Cho cin cái tên đê:")

    if st.button("Vô"):
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
    st.title("chào mừng vượt được ải tên đăng nhập")

    st.write(f"tốt lắm con vk {st.session_state.username}")

    if st.button("Cút"):
        st.session_state.login = False
        st.session_state.username = ""
        st.rerun()
    # co divi nma k bt de lam gi
    st.divider()

    number = st.number_input("chao cau")

    if st.button("tinh giai thua"):
        res = giaithua(number)
        st.write(f"Trả bài nhé: {res}")

def greating_page():
    st.title("Ni hao")
    st.write(f"Ni hao ma {st.session_state.username}")
    st.write("Rất tiếc rất lấy làm tiếc")

    if st.button("Quay lai dang nhap di onichan ><"):
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

