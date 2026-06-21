# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
 (for example: "the hints were backwards").

- The hints are completely backwards — guessing lower than the 
  secret says "Go Lower" instead of "Go Higher"
- The score calculation is wrong — winning in 3 guesses gave 
  60 points instead of the expected 80
- Clicking New Game does not fully reset the game — old score, 
  history, and win status carry over
- Typing invalid input like "abc" still costs an attempt, it should be free

**Bug Reproduction Log**
| Input Used | Expected Behavior | Actual Behavior | Console Error / Output |
|---|---|---|---|
| Guess of 10 (secret was 25) | "Go Higher" hint shown | "Go Lower" hint shown | none |
| Guess of 80 (secret was 25) | "Go Lower" hint shown | "Go Higher" hint shown | none |
| Won in 3 guesses | Score = 80 points | Score = 60 points | none |
| Clicked New Game | Score resets to 0, history clears | Score stayed 60, old history visible | none |
| Typed "abc" as guess | Error shown, attempts unchanged | "That is not a number" BUT attempts went down by 1 | none |

---


## 2. How did you use AI as a teammate?

- Which AI tools did you use?
I used Claude (claude.ai) and the VS Code AI coding 
assistant to help debug and fix the game.

- Give one example where AI was CORRECT and helpful:
I asked the AI to explain why hints were backwards in 
check_guess. It correctly identified that the hint 
messages were on the wrong branches — "Too High" was 
returning "Go HIGHER" instead of "Go LOWER". I verified 
this by testing in the browser with a known secret number 
and confirming the hint direction was wrong.

- Give one example where AI was INCORRECT or misleading:
The AI initially suggested keeping the TypeError fallback 
in check_guess to handle string comparisons. This was 
wrong because it was masking the real bug — the secret 
number was being converted to a string on even attempts. 
I rejected this and fixed the root cause instead by 
removing the str() conversion entirely.

---



## 3. Debugging and testing your fixes

- How did you decide a bug was really fixed?
I tested each fix manually in the browser using the 
Developer Debug Info panel to see the secret number, 
then verified the correct behavior. I also wrote 7 
pytest tests that all pass to confirm fixes work.

- Describe at least one test you ran:
test_too_high_says_go_lower — checks that guessing 60 
when secret is 50 returns "Too High" and "Go LOWER". 
This directly verifies the flipped hints bug is fixed.

- Did AI help you design or understand any tests? How?
Yes. I described the 3 bugs I fixed to the AI and asked 
it to generate pytest tests for each one. The AI read 
logic_utils.py and wrote 7 tests covering hint direction, 
score calculation, and invalid input handling. It also 
caught that the existing starter tests were broken — they 
were comparing a tuple to a string which always fails. 
I verified all 7 tests passed by running 
python -m pytest tests/ -v in the terminal myself.

---



## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and 
session state to a friend who has never used Streamlit?

Streamlit reruns the entire Python script from top 
to bottom every single time you click a button or 
interact with anything on the page. This means every 
variable resets to its original value on every click.

Session state is like a memory box that survives 
these reruns. Anything you store in 
st.session_state stays saved between clicks.

For example in our game, the secret number is stored 
in st.session_state.secret. Without that, every time 
you clicked Submit the secret would change to a new 
random number and you could never win. With session 
state, the secret stays the same for the whole round.

Think of it like this — Streamlit is like a whiteboard 
that gets erased after every click. Session state is 
a sticky note on the side that never gets erased.
---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project 
  that you want to reuse in future labs or projects?
  
I want to keep using the habit of testing manually 
BEFORE writing automated tests. Playing the game 
with the Debug Info panel open helped me see exactly 
what was broken before I even touched the code. 
I will also keep committing after every single bug 
fix instead of one big commit at the end.

- What is one thing you would do differently next 
  time you work with AI on a coding task?
  
Next time I would ask AI to explain its suggestion 
in simple terms BEFORE accepting it. A few times 
the AI gave correct fixes but I didn't fully 
understand why until I asked for a simpler 
explanation. Understanding the fix matters more 
than just applying it.

- In one or two sentences, describe how this project 
  changed the way you think about AI generated code.
  
AI generated code can look completely correct and 
still be wrong in subtle ways that only show up 
during actual use. I learned to always test AI code 
myself rather than trusting it just because it 
looks professional and runs without crashing.
