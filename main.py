from bot.publisher import publish_one
from bot.state import load_state, save_state

def main():
    state = load_state()
    ok = publish_one(state)
    print("Published." if ok else "No suitable photo found; nothing posted.")
    save_state(state)

if __name__ == "__main__":
    main()
