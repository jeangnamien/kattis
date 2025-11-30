"""Solution for Kattis problem."""


def hissing_microphone(s):
    """
    Check if the string contains consecutive 's' characters.

    Args:
        s (str): Input string

    Returns:
        str: "hiss" if "ss" is found, otherwise "no hiss"

    Problem : https://open.kattis.com/problems/hissingmicrophone
    """
    # If "ss" appears anywhere in the string, return "hiss"
    if "ss" in s:
        return "hiss"
    return "no hiss"


def main():
    """Main function to read input and print output."""
    s = input().strip()  # read the string
    result = hissing_microphone(s)
    print(result)


if __name__ == "__main__":
    main()
