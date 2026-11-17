import json
from pathlib import Path

STATE_FILE = Path("database/published.json")
MAX_ITEMS = 800

def load_state():
    STATE_FILE.parent.mkdir(parents=True, exist_ok=True)
    state = {}
    if STATE_FILE.exists():
        try:
            state = json.loads(STATE_FILE.read_text(encoding="utf-8"))
        except (json.JSONDecodeError, OSError):
            state = {}
    state.setdefault("published", [])
    state.setdefault("n", 0)      # شمارنده نوبت دسته‌ها
    state.setdefault("idx", 0)    # نوبت مکان‌ها
    return state

def already_published(state, key):
    return key in state.setdefault("published", [])

def mark_published(state, key):
    items = state.setdefault("published", [])
    if key not in items:
        items.append(key)
    state["published"] = items[-MAX_ITEMS:]

def save_state(state):
    STATE_FILE.parent.mkdir(parents=True, exist_ok=True)
    STATE_FILE.write_text(
        json.dumps(state, ensure_ascii=False, indent=2),
        encoding="utf-8"
    )
