def uppercase(s):
    for char in s:
        # Check if the character is a lowercase letter
        if 'a' <= char <= 'z':
            # Convert the lowercase letter to uppercase by adjusting its ASCII value
            uppercase_char = chr(ord(char) - ord('a') + ord('A'))
            print(uppercase_char, end="")
        else:
            # Print characters that are not lowercase letters as they are
            print(char, end="")
    print()  # Print a newline after processing the string
