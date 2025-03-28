text = input("Enter a string: ")
desired_width = int(input("Enter the total width: "))

if len(text) >= desired_width:
    print(text)
else:
    extra_spaces = desired_width - len(text)
    spaces_before = extra_spaces // 2
    spaces_after = extra_spaces - spaces_before

    print(' ' * spaces_before + text + ' ' * spaces_after)