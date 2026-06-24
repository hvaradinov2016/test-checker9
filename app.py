import streamlit as st

st.title("Проверка на тестове (A, B, C, D)")

st.write("Качи снимка и въведи верните отговори")

# 📸 Качване на снимка
uploaded_file = st.file_uploader("Качи снимка на тест", type=["jpg", "png"])

# ✍️ Верни отговори
correct_answers = st.text_input("Въведи верни отговори (пример: B A D C)")

# ✍️ Отговори на ученик
student_answers = st.text_input("Въведи отговори на ученика (пример: B C D C)")

# ▶️ Бутон
if st.button("Провери теста"):

    if not correct_answers or not student_answers:
        st.error("Моля въведи и двата реда с отговори!")
    else:
        correct = correct_answers.split()
        student = student_answers.split()

        score = 0

        for i in range(min(len(correct), len(student))):
            if correct[i].upper() == student[i].upper():
                score += 1

        st.success(f"Резултат: {score} от {len(correct)}")
        st.info(f"Процент: {round(score / len(correct) * 100, 2)}%")

# 📷 показване на снимка (само визуално)
if uploaded_file:
    st.image(uploaded_file, caption="Качена снимка на теста")