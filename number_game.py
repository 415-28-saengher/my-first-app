import time
import streamlit as st

st.title("🎯 เกมทายตัวเลขสะสมคะแนน")
st.write("ทายตัวเลขให้ถูกต้อง พร้อมใช้คำใบ้ช่วย")

# กำหนดค่าเริ่มต้น
if "start" not in st.session_state:
    st.session_state.start = None

if "score" not in st.session_state:
    st.session_state.score = 0

if "is_ended" not in st.session_state:
    st.session_state.is_ended = False


# เริ่มเกมใหม่
def reset_game():
    st.session_state.start = time.time()
    st.session_state.score = 0
    st.session_state.is_ended = False


st.button("🎮 เริ่มเกม", on_click=reset_game)

# แสดงเวลา
if st.session_state.start is not None and not st.session_state.is_ended:

    time_left = int(30 - (time.time() - st.session_state.start))

    if time_left > 0:
        st.warning(f"⏳ เหลือเวลา {time_left} วินาที")
    else:
        st.session_state.is_ended = True
        st.rerun()

st.divider()

# ข้อ 1
st.write("### ข้อ 1")
st.write("💡 คำใบ้: ตัวเลขมากกว่า 3")
ans1 = st.number_input("ทายข้อ 1", 1, 10, key="ans1")

# ข้อ 2
st.write("### ข้อ 2")
st.write("💡 คำใบ้: ตัวเลขน้อยกว่า 8")
ans2 = st.number_input("ทายข้อ 2", 1, 10, key="ans2")

# ข้อ 3
st.write("### ข้อ 3")
st.write("💡 คำใบ้: ตัวเลขมากกว่า 4")
ans3 = st.number_input("ทายข้อ 3", 1, 10, key="ans3")

# ข้อ 4
st.write("### ข้อ 4")
st.write("💡 คำใบ้: ตัวเลขน้อยกว่า 6")
ans4 = st.number_input("ทายข้อ 4", 1, 10, key="ans4")

# ข้อ 5
st.write("### ข้อ 5")
st.write("💡 คำใบ้: ตัวเลขมากกว่า 5")
ans5 = st.number_input("ทายข้อ 5", 1, 10, key="ans5")


# ตรวจคำตอบ
if st.session_state.start is not None and not st.session_state.is_ended:

    if st.button("📥 ส่งคำตอบ"):

        score = 0

        if ans1 == 7:
            score += 1

        if ans2 == 5:
            score += 1

        if ans3 == 9:
            score += 1

        if ans4 == 2:
            score += 1

        if ans5 == 8:
            score += 1

        st.session_state.score = score
        st.session_state.is_ended = True
        st.rerun()


# แสดงผลคะแนน
if st.session_state.is_ended:

    st.divider()
    st.header("📊 ผลการเล่น")
    st.write(f"🏆 คะแนนรวม: {st.session_state.score} / 5 คะแนน")

    if st.session_state.score == 5:
        st.success("🏆 ยอดเยี่ยม!")
    elif st.session_state.score == 4:
        st.success("🥇 ดีมาก!")
    elif st.session_state.score == 3:
        st.info("🥈 ผ่านด่าน!")
    elif st.session_state.score >= 1:
        st.warning("❌ ไม่ผ่าน ต้องเล่นใหม่")
    else:
        st.error("💀 Game Over")

    st.button("🔄 เล่นใหม่", on_click=reset_game)

st.divider()
st.write("งานกลุ่มที่1")
