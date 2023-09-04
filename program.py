# program.py
import sys

def main():
    if len(sys.argv) < 2:
        print("Please provide a string argument.")
        return

    string_to_save = sys.argv[1]
    print(string_to_save)

if __name__ == "__main__":
    main()
