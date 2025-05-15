import time

def separator():
    print("\n" + "-" * 50 + "\n")

def get_int_list(prompt, expected_len):
    while True:
        try:
            values = list(map(int, input(prompt).strip().split()))
            if len(values) != expected_len:
                raise ValueError(f"Expected {expected_len} values.")
            return values
        except ValueError as e:
            print(f"[!] {e}. Try again.")

def get_set(prompt, expected_len):
    return set(get_int_list(prompt, expected_len))

def show_mood(score):
    if score > 5:
        mood = "😁 You're radiating joy!"
    elif score > 0:
        mood = "🙂 You're doing okay!"
    elif score == 0:
        mood = "😐 Meh. Balanced vibes."
    else:
        mood = "😞 Uh-oh. Time to manifest positivity."

    print(f"\n💡 Final Happiness Score: {score}")
    print(f"✨ Mood: {mood}")

def main():
    print("🧠 Welcome to the Happiness Calculator CLI!")
    separator()

    # Input
    try:
        n, m = map(int, input("Enter n (size of array) and m (size of sets A & B): ").split())
        if n <= 0 or m <= 0:
            raise ValueError("n and m must be positive integers.")
    except ValueError:
        print("[!] Invalid input for n and m. Exiting.")
        return

    separator()
    arr = get_int_list(f"Enter {n} integers for the array: ", n)
    A = get_set(f"Enter {m} integers for Set A (happiness gain): ", m)
    B = get_set(f"Enter {m} integers for Set B (happiness loss): ", m)

    separator()
    print("🔍 Calculating happiness...\n")
    time.sleep(0.5)

    # Logic
    happiness = 0
    for item in arr:
        if item in A:
            print(f" +1 😊 Found {item} in Set A")
            happiness += 1
        if item in B:
            print(f" -1 😣 Found {item} in Set B")
            happiness -= 1
        if item not in A and item not in B:
            print(f"  0 😐 {item} is neutral.")

    separator()
    show_mood(happiness)

if __name__ == "__main__":
    main()