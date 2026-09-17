import streamlit as st

st.set_page_config(page_title="MATH BATTLE", page_icon="⚔️")

# -------------------------
# ตั้งค่าเริ่มต้น
# -------------------------
if "stage" not in st.session_state:
    st.session_state.stage = 1

if "score" not in st.session_state:
    st.session_state.score = 0

if "lives" not in st.session_state:
    st.session_state.lives = 3

# -------------------------
# ข้อมูลโจทย์
# -------------------------
questions = {
    1: ("8 + 7 = ?", 15, "ลองบวก 8 กับ 7"),
    2: ("20 - 8 = ?", 12, "20 ลบ 8"),
    3: ("6 × 4 = ?", 24, "6 + 6 + 6 + 6"),
    4: ("36 ÷ 6 = ?", 6, "6 × อะไร = 36"),
    5: ("5² = ?", 25, "5 × 5")
}

# -------------------------
# ชื่อเกม
# -------------------------
st.title("⚔️ MATH BATTLE ⚔️")
st.subheader("เกมตะลุยด่านคณิต")

st.write(f"❤️ ชีวิต: {st.session_state.lives}")
st.write(f"🏆 คะแนน: {st.session_state.score}")

# -------------------------
# ตรวจสอบจบเกม
# -------------------------
if st.session_state.lives <= 0:
    st.error("💀 เกมจบแล้ว! ชีวิตหมด")
    st.write(f"คะแนนที่ได้: {st.session_state.score}")

    if st.button("🔄 เล่นใหม่"):
        st.session_state.stage = 1
        st.session_state.score = 0
        st.session_state.lives = 3
        st.rerun()

elif st.session_state.stage > 5:
    st.success("🎉 ชนะแล้ว! ผ่านครบทุกด่าน")
    st.balloons()
    st.write(f"🏆 คะแนนรวม: {st.session_state.score} / 5")

    if st.button("🔄 เล่นใหม่"):
        st.session_state.stage = 1
        st.session_state.score = 0
        st.session_state.lives = 3
        st.rerun()

else:
    # -------------------------
    # แสดงโจทย์
    # -------------------------
    question, answer, hint = questions[st.session_state.stage]

    st.info(f"⚔️ ด่านที่ {st.session_state.stage}")
    st.header(question)

    # คำใบ้
    if st.button("💡 ขอคำใบ้"):
        st.warning(f"คำใบ้: {hint}")

    user_answer = st.number_input(
        "✏️ คำตอบ",
        step=1,
        value=0
    )

    if st.button("⚔️ ตอบคำถาม"):
        if user_answer == answer:
            st.success("✅ ถูกต้อง! +1 คะแนน")
            st.balloons()

            st.session_state.score += 1
            st.session_state.stage += 1
            st.rerun()

        else:
            st.error("❌ ผิด! เสีย 1 ชีวิต")
            st.session_state.lives -= 1
            st.rerun()
