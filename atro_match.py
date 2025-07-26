import json
from utils import get_sun_sign
import os

def load_compatibility_data(filepath="data/compatibility.json"):
    if not os.path.exists(filepath):
        print("⚠️ Compatibility file not found.")
        return {}
    with open(filepath, "r") as file:
        return json.load(file)

def check_compatibility(sign1, sign2, compatibility_data):
    return sign2 in compatibility_data.get(sign1, [])

def main():
    print("🌟 Welcome to AstroMatch 🌟")
    person1_dob = input("Enter Person 1 DOB (DD-MM-YYYY): ")
    person2_dob = input("Enter Person 2 DOB (DD-MM-YYYY)): ")

    sign1 = get_sun_sign(person1_dob)
    sign2 = get_sun_sign(person2_dob)

    compatibility_data = load_compatibility_data("data/compatibility.json")

    print(f"\nPerson 1 Sun Sign: {sign1}")
    print(f"Person 2 Sun Sign: {sign2}")

    if check_compatibility(sign1, sign2, compatibility_data):
        print("💞 Great Match! Cosmic vibes are flowing!")
    else:
        print("🤔 Hmm... Not a textbook match, but love breaks rules!")

if __name__ == "__main__":
    main()
    