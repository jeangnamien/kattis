import pytest
from kattis.hissingmicrophone import hissing_microphone


class TestHissingMicrophone:
    """Test cases for the hissing_microphone function."""

    def test_contains_hiss(self):
        """Test strings that contain consecutive 's'."""
        assert hissing_microphone("amiss") == "hiss"
        assert hissing_microphone("kiss") == "hiss"
        assert hissing_microphone("mississippi") == "hiss"
        assert hissing_microphone("hiss") == "hiss"
        assert hissing_microphone("boss") == "hiss"

    def test_no_hiss(self):
        """Test strings that do not contain consecutive 's'."""
        assert hissing_microphone("hello") == "no hiss"
        assert hissing_microphone("microphone") == "no hiss"
        assert hissing_microphone("abcde") == "no hiss"
        assert hissing_microphone("python") == "no hiss"
        assert hissing_microphone("s") == "no hiss"

    def test_edge_cases(self):
        """Test edge cases like minimum and maximum length strings."""
        # Minimum length (1 character)
        assert hissing_microphone("s") == "no hiss"
        assert hissing_microphone("a") == "no hiss"

        # Maximum length example (100 characters, no consecutive 's')
        max_len_str = "a" * 100
        assert hissing_microphone(max_len_str) == "no hiss"

        # Maximum length example with 'ss' in the middle
        max_len_hiss = "a" * 49 + "ss" + "b" * 49
        assert hissing_microphone(max_len_hiss) == "hiss"

if __name__ == "__main__":
    pytest.main([__file__, "-v"])
