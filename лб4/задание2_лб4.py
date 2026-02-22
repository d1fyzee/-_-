def f(s, w):
    if len(s) >= w:
        return s
    n = (w - len(s)) // 2
    return ' ' * n + s

print(f("привет", 8))
print(f("пользователь", 14))
print(f("длинная строка", 16))