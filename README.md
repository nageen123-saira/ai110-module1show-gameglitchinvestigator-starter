# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!



## 📝 Document Your Experience

- [x] Describe the game's purpose.
A number guessing game where the player guesses a secret 
number between 1-100. Hints guide the player higher or lower.

- [x] Detail which bugs you found.
1. Hints were flipped — Too Low said "Go LOWER" 
2. Score went negative on wrong guesses
3. Invalid input like "abc" cost an attempt
4. New Game didn't reset score/history/status
5. Secret number converted to string on even attempts

- [x] Explain what fixes you applied.
Fixed hint messages in check_guess, removed score penalty 
for wrong guesses, moved attempt counter after validation, 
reset all session state on New Game, removed str() conversion.


## 📸 Demo Walkthrough

Describe your fixed game in numbered steps so a reader can follow along without watching a video:

1. Game starts, secret number is generated (e.g. 42)
2. User guesses 20 → hint says "Go HIGHER"
3. User guesses 80 → hint says "Go LOWER" 
4. User guesses 42 → "Correct! You won!"
5. Final score = 80 points (won in 3 guesses)
6. New Game clicked → everything resets to zero


## 🧪 Test Results


```
#  pytest output here, e.g.:
#python -m pytest tests/ -v
# ========================= X passed in 0.XXs =========================
tests/test_game_logic.py::test_too_high_says_go_lower PASSED                                                                     [ 14%]
tests/test_game_logic.py::test_too_low_says_go_higher PASSED                                                                     [ 28%]
tests/test_game_logic.py::test_correct_guess_wins PASSED                                                                         [ 42%]
tests/test_game_logic.py::test_wrong_guess_does_not_change_score PASSED                                                          [ 57%]
tests/test_game_logic.py::test_win_adds_points_to_score PASSED                                                                   [ 71%]
tests/test_game_logic.py::test_invalid_input_is_rejected PASSED                                                                  [ 85%]
tests/test_game_logic.py::test_valid_input_is_accepted PASSED                                                                    [100%]

========================================= 7 passed in 0.06s ==========================================================



```
