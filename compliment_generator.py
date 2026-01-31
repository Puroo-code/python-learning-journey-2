# python-learning-journey-2
My unique Python projects as a beginner
# Daily Compliment Generator
import random

# List of fun compliments
compliments = [
    "You are awesome! 😎",
    "Your smile can brighten anyone's day! 😊",
    "You are a coding superstar! 💻",
    "Keep being amazing! ✨",
    "You make the world better just by being you! 🌸",
    "Your brain is a powerhouse! 🧠",
    "Believe in yourself, you can do anything! 💪"
]

# Greet the user
print("Welcome to the Daily Compliment Generator!")
name = input("Enter your name: ")

# Pick a random compliment
compliment = random.choice(compliments)

# Show the compliment
print(f"\n{name}, here’s your compliment for today: {compliment}")
