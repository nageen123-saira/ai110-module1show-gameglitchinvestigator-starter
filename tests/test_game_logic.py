from logic_utils import check_guess, update_score, parse_guess


# --- Fix 1: hints point the correct direction ---

def test_too_high_says_go_lower():
    # Guess above the secret should tell the player to go LOWER
    assert check_guess(60, 50) == ("Too High", "📉 Go LOWER!")


def test_too_low_says_go_higher():
    # Guess below the secret should tell the player to go HIGHER
    assert check_guess(40, 50) == ("Too Low", "📈 Go HIGHER!")


def test_correct_guess_wins():
    # Matching guess should be a win
    assert check_guess(50, 50) == ("Win", "🎉 Correct!")


# --- Fix 2: score never goes negative on a wrong guess ---

def test_wrong_guess_does_not_change_score():
    # A non-winning outcome leaves the score unchanged
    assert update_score(0, "Too High", 1) == 0


def test_win_adds_points_to_score():
    # A win on the first attempt adds the full 100 points
    assert update_score(0, "Win", 1) == 100


# --- Fix 3: invalid input is rejected for free ---

def test_invalid_input_is_rejected():
    # "abc" is not a number, so parse_guess should report failure
    assert parse_guess("abc")[0] is False


def test_valid_input_is_accepted():
    # A numeric string should parse successfully
    assert parse_guess("42")[0] is True
