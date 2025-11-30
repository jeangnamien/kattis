"""Quick fixes for remaining PyLint issues."""

import re
from pathlib import Path


def fix_pytest_in_main():
    """Fix undefined pytest in test files."""
    for test_file in Path("tests").glob("test_*.py"):
        content = test_file.read_text(encoding="utf-8")
        
        # Pattern: if __name__ == "__main__":\n    pytest.main(...)
        pattern = r'if __name__ == "__main__":\n    pytest\.main\('
        replacement = 'if __name__ == "__main__":\n    import pytest\n    pytest.main('
        
        new_content = re.sub(pattern, replacement, content)
        
        if new_content != content:
            test_file.write_text(new_content, encoding="utf-8")
            print(f"✓ Fixed {test_file}")


def fix_unused_n_lvable():
    """Fix unused variable n in lvable.py."""
    file_path = Path("src/kattis/lvable.py")
    content = file_path.read_text(encoding="utf-8")
    
    content = content.replace(
        "n = int(input())",
        "_ = int(input())  # Line count not needed"
    )
    
    file_path.write_text(content, encoding="utf-8")
    print("✓ Fixed unused n in lvable.py")


def fix_else_after_return():
    """Fix else-after-return in hissingmicrophone.py."""
    file_path = Path("src/kattis/hissingmicrophone.py")
    content = file_path.read_text(encoding="utf-8")
    
    # Simple pattern for this specific case
    old = '''    if "ss" in s:
        return "hiss"
    else:
        return "no hiss"'''
    
    new = '''    if "ss" in s:
        return "hiss"
    return "no hiss"'''
    
    content = content.replace(old, new)
    file_path.write_text(content, encoding="utf-8")
    print("✓ Fixed else-after-return in hissingmicrophone.py")


def fix_game_2048():
    """Fix game_2048.py issues."""
    file_path = Path("src/kattis/game_2048.py")
    content = file_path.read_text(encoding="utf-8")
    
    # Fix enumerate
    content = content.replace(
        "    for i in range(len(non_zero)):",
        "    for i, value in enumerate(non_zero):"
    )
    content = content.replace(
        "        if i + 1 < len(non_zero) and non_zero[i] == non_zero[i + 1]:",
        "        if i + 1 < len(non_zero) and value == non_zero[i + 1]:"
    )
    content = content.replace(
        "            merged.append(non_zero[i] * 2)",
        "            merged.append(value * 2)"
    )
    content = content.replace(
        "            merged.append(non_zero[i])",
        "            merged.append(value)"
    )
    
    # Fix elif to if
    content = content.replace("    elif direction == 1:", "    if direction == 1:")
    content = content.replace("    elif direction == 2:", "    if direction == 2:")
    content = content.replace("    elif direction == 3:", "    if direction == 3:")
    
    file_path.write_text(content, encoding="utf-8")
    print("✓ Fixed game_2048.py")


if __name__ == "__main__":
    print("Applying quick fixes...\n")
    
    fix_pytest_in_main()
    fix_unused_n_lvable()
    fix_else_after_return()
    fix_game_2048()
    
    print("\n✅ All fixes applied!")
    print("\nRun: poetry run pylint src tests")