# story_time.py

from pathlib import Path

# Constants for user input
YES = "y"
NO = "n"

# File path where the story is stored
path = Path("text_files/ten_traders.txt")


def load_story():
    """
    Load the story text from the file.
    Returns:
        str: The content of the story file if found, otherwise None.
    """
    try:
        open_file = path.read_text(encoding="utf-8")
        return open_file
    except FileNotFoundError:
        print("File not found!")
        return None  # Added explicit return for clarity


def listen():
    """
    Main function to interact with the user.
    Prompts user if they want to hear a story, then loads and displays it.
    """
    print("Weird Stories")
    story_time = True

    while story_time:
        # Ask user whether they want to hear the story
        choice = input("\nDo you wish to hear a story? (y/n): ").lower().strip()

        if not choice:
            # If user just pressed Enter, ask again
            continue

        if choice == YES:
            story = load_story()
            if story:  # Only print if story was successfully loaded
                print(story)
                print("Thanks for reading!\nBye.")
            story_time = False

        elif choice == NO:
            print("\nIf you change your mind, I'll be right here.\nBye for now.")
            story_time = False

        else:
            # Invalid input, loop continues
            continue


if __name__ == "__main__":
    listen()
