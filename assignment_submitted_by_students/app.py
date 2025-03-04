import streamlit as st
import random
import time


def bmi_calculator():
    st.title("Body Mass Index Calculator")
    weight = st.number_input("Enter your weight (kilograms)", min_value=10, max_value=300, step=1, format="%d")
    height_ft = st.number_input("Enter your height (feet)", min_value=1, max_value=8, step=1, format="%d")
    height_in = st.number_input("Enter additional inches", min_value=0, max_value=11, step=1, format="%d")
    height_m = (height_ft * 0.3048) + (height_in * 0.0254)
    if st.button("Calculate Body Mass Index"):
        bmi = weight / (height_m ** 2)
        st.write(f"Your Body Mass Index is: {bmi:.2f}")
        
        if bmi < 18.5:
            category = "Underweight"
            st.warning("You are underweight. Consider a healthy diet plan with nutrient-rich foods.")
        elif 18.5 <= bmi < 24.9:
            category = "Normal weight"
            st.success("You have a normal weight. Keep up the healthy lifestyle!")
        elif 25 <= bmi < 29.9:
            category = "Overweight"
            st.warning("You are overweight. Consider exercising regularly and maintaining a balanced diet with lean proteins, vegetables, and whole grains.")
            st.write("Suggested Exercises: Cardio workouts like running, cycling, swimming, and strength training.")
        else:
            category = "Obese"
            st.error("You are obese. A proper diet and workout plan are recommended.")
            st.write("Suggested Healthy Diet: High-fiber foods, lean proteins, low-carb meals, and plenty of water.")
            st.write("Recommended Exercises: Low-impact cardio like walking, swimming, resistance training, and yoga.")
        
        st.write(f"Category: {category}")

def mad_libs():
    st.title("Mad Libs Game")
    
    st.subheader("Word Definitions:")
    st.write("**Noun:** A person, place, or thing (e.g., cat, city, book)")
    st.write("**Adjective:** A word that describes a noun (e.g., happy, blue, fast)")
    st.write("**Verb:** An action word (e.g., run, eat, jump)")
    
    story_type = st.selectbox("Choose a story type:", ["Adventure", "Fantasy", "Sci-Fi", "Custom Story"])
    
    noun = st.text_input("Enter a noun:")
    adjective = st.text_input("Enter an adjective:")
    verb = st.text_input("Enter a verb:")
    
    custom_story = ""
    if story_type == "Custom Story":
        custom_story = st.text_area("Write your custom story (use {noun}, {adjective}, {verb} as placeholders)")
    
    if st.button("Generate Story"):
        if story_type == "Adventure":
            st.write(f"One day, a {adjective} {noun} decided to {verb} across the world in search of treasure!")
        elif story_type == "Fantasy":
            st.write(f"In a magical land, the {adjective} {noun} used its power to {verb} and save the kingdom!")
        elif story_type == "Sci-Fi":
            st.write(f"A {adjective} {noun} was programmed to {verb} on a distant planet, discovering new life forms!")
        elif story_type == "Custom Story" and custom_story:
            st.write(custom_story.format(noun=noun, adjective=adjective, verb=verb))
        else:
            st.warning("Please fill in the required fields!")

def guess_number_computer():
    st.title("Guess the Number (Computer)")
    number = random.randint(1, 30)
    guess = st.number_input("Guess a number between 1 and 30", min_value=1, max_value=100)
    if st.button("Check"): 
        if guess == number:
            st.success("Congratulations! You guessed it right!")
        else:
            st.error(f"Wrong guess! The number was {number}")

def rock_paper_scissors():
    st.title("Rock, Paper, Scissors Game")
    choices = ["Rock", "Paper", "Scissors"]
    user_choice = st.selectbox("Choose Rock, Paper, or Scissors", choices)
    if st.button("Play"):
        computer_choice = random.choice(choices)
        st.write(f"Computer chose: {computer_choice}")
        if user_choice == computer_choice:
            st.info("It is a tie!")
        elif (user_choice == "Rock" and computer_choice == "Scissors") or \
             (user_choice == "Scissors" and computer_choice == "Paper") or \
             (user_choice == "Paper" and computer_choice == "Rock"):
            st.success("You win!")
        else:
            st.error("You lose!")

def hangman():
    st.title("Hangman Game")

    words = {
        "python": "A popular programming language",
        "streamlit": "A Python library for creating web apps",
        "developer": "A person who writes code",
        "coding": "The process of writing programs"
    }

    if "word" not in st.session_state:
        st.session_state.word, st.session_state.hint = random.choice(list(words.items()))
        st.session_state.word_display = ["_"] * len(st.session_state.word)
        st.session_state.used_letters = set()
        st.session_state.lives = 7

    st.write(f"Hint: {st.session_state.hint}")
    st.write(f"Word to guess: {' '.join(st.session_state.word_display)}")
    st.write(f"Used letters: {', '.join(st.session_state.used_letters) if st.session_state.used_letters else 'None'}")
    st.write(f"Lives left: {st.session_state.lives}")

    guess = st.text_input("Enter a letter:", key="guess_input").lower()

    if guess and len(guess) == 1 and guess.isalpha():
        if guess in st.session_state.used_letters:
            st.warning("You already guessed this letter!")
        else:
            st.session_state.used_letters.add(guess)
            if guess in st.session_state.word:
                for i, letter in enumerate(st.session_state.word):
                    if letter == guess:
                        st.session_state.word_display[i] = guess
            else:
                st.session_state.lives -= 1
                st.error("Wrong guess! Try again.")

    if "_" not in st.session_state.word_display:
        st.success(f"Congratulations! You guessed the word: {st.session_state.word}")
        st.button("Play Again", on_click=lambda: st.session_state.clear())
    elif st.session_state.lives == 0:
        st.error(f"Game over! The word was: {st.session_state.word}")
        st.button("Try Again", on_click=lambda: st.session_state.clear())


def countdown_timer():
    st.title("Countdown Timer")
    time_unit = st.selectbox("Select time unit:", ["Seconds", "Minutes", "Hours"])
    time_value = st.number_input("Enter countdown time:", min_value=1, max_value=3600, step=1)
    
    if time_unit == "Minutes":
        seconds = time_value * 60
    elif time_unit == "Hours":
        seconds = time_value * 3600
    else:
        seconds = time_value
    
    stop_flag = st.button("Stop Countdown")
    
    if st.button("Start Countdown"):
        with st.empty():
            for i in range(seconds, 0, -1):
                if stop_flag:
                    st.warning("⏹ Countdown Stopped!")
                    break
                mins, secs = divmod(i, 60)
                hrs, mins = divmod(mins, 60)
                time_format = f"{hrs:02}:{mins:02}:{secs:02}"
                st.write(f"⏳ Countdown: {time_format}")
                time.sleep(1)
                st.empty()
    else:
            st.success("⏰ Time's up!")

def password_generator():
    st.title("Password Generator")
    length = st.slider("Select password length", min_value=6, max_value=20, value=12)
    if st.button("Generate Password"):
        characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()"
        password = "".join(random.choice(characters) for _ in range(length))
        st.text_input("Generated Password", value=password, disabled=True)

def python_website():
    st.title("Build a Python Website with Streamlit")
    
    st.subheader("What is Streamlit?")
    st.write("Streamlit is an open-source Python library that makes it easy to create and share beautiful, custom web apps for machine learning and data science projects.")
    
    st.subheader("Features of Streamlit:")
    st.write("""
    - **Simple and Fast:** No front-end experience required.
    - **Interactive Widgets:** Easily add sliders, buttons, text inputs, and more.
    - **Data Visualization:** Supports popular Python libraries like Matplotlib, Plotly, and Altair.
    - **Live Code Updates:** Instant reloading when making changes.
    """)
    
    st.subheader("How to Create a Basic Website with Streamlit")
    st.code("""
    import streamlit as st

    st.title("My First Streamlit App")
    st.write("Welcome to my Python-powered web app!")
    """, language="python")
    
    st.subheader("Deployment")
    st.write("You can deploy your Streamlit app on platforms like **Streamlit Cloud, Heroku, AWS, and Google Cloud**.")

    st.subheader("Try it Yourself!")
    if st.button("Run Demo"):
        st.success("You just built your first Streamlit web page! 🚀")

st.sidebar.title("Select a Project")
options = [
    "Body Mass Index Calculator", "Guess the Number (Computer)", "Rock, Paper, Scissors", "Hangman", 
    "Countdown Timer", "Password Generator", "Mad Libs", "Python Website"
]
choice = st.sidebar.selectbox("Choose a project:", options)

if choice ==  "Body Mass Index Calculator":
    bmi_calculator()
elif choice == "Guess the Number (Computer)":
    guess_number_computer()
elif choice == "Rock, Paper, Scissors":
    rock_paper_scissors()
elif choice == "Hangman":
    hangman()
elif choice == "Countdown Timer":
    countdown_timer()
elif choice == "Password Generator":
    password_generator()
elif choice == "Mad Libs":
    mad_libs() 
elif choice == "Python Website":
    python_website()