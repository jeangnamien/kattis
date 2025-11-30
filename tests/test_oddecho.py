import io
import sys
from kattis.oddecho import odd_echo  # assuming your function is in odd_echo.py


def run_odd_echo_with_input(input_data):
    """Helper to capture the output of odd_echo given input_data as string."""
    # Backup original stdin and stdout
    original_stdin = sys.stdin
    original_stdout = sys.stdout

    sys.stdin = io.StringIO(input_data)
    sys.stdout = io.StringIO()

    try:
        odd_echo()
        # Get output and split into lines
        output = sys.stdout.getvalue().strip().split("\n")
    finally:
        sys.stdin = original_stdin
        sys.stdout = original_stdout

    return output


def test_basic_case():
    input_data = "5\nhello\nworld\nthis\nis\nfun\n"
    expected_output = ["hello", "this", "fun"]
    assert run_odd_echo_with_input(input_data) == expected_output


def test_single_word():
    input_data = "1\necho\n"
    expected_output = ["echo"]
    assert run_odd_echo_with_input(input_data) == expected_output


def test_two_words():
    input_data = "2\nfirst\nsecond\n"
    expected_output = ["first"]
    assert run_odd_echo_with_input(input_data) == expected_output


def test_even_number_of_words():
    input_data = "6\na\nb\nc\nd\ne\nf\n"
    expected_output = ["a", "c", "e"]
    assert run_odd_echo_with_input(input_data) == expected_output


def test_odd_number_of_words():
    input_data = "7\none\ntwo\nthree\nfour\nfive\nsix\nseven\n"
    expected_output = ["one", "three", "five", "seven"]
    assert run_odd_echo_with_input(input_data) == expected_output
