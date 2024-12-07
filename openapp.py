import os
import time
import sys

def download_animation():
    """Display a matrix-like downloading animation."""
    matrix_chars = ["|", "/", "-", "\\"]
    for _ in range(20):  # Adjust the range for how many times it repeats
        for char in matrix_chars:
            sys.stdout.write(f"\rDownloading {char}")
            sys.stdout.flush()
            time.sleep(0.2)

def open_app():
    """Open an app based on user input."""
    app_name = input("Enter the app package name to open (e.g., com.whatsapp): ")

    # Run the downloading animation in the background
    download_animation()

    # After the animation finishes, open the app using 'am start' command
    print("\nOpening app...")
    os.system(f"am start -n {app_name}")

if __name__ == "__main__":
    open_app()