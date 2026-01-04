class NestedChest:
    def __init__(self, value=None):
        if value is None:
            self.value = []
        else:
            self.value = value

    def add(self, item):
        self.value.append(item)

    def __repr__(self):
        return str(self.value)


def parse_chest(s):
    stack = []
    num = ""
    negative = False

    for ch in s:
        if ch == '[':
            stack.append(NestedChest())
        elif ch == '-':
            negative = True
        elif ch.isdigit():
            num += ch
        elif ch == ',' or ch == ']':
            if num:
                val = int(num)
                if negative:
                    val = -val
                stack[-1].add(val)
                num = ""
                negative = False

            if ch == ']' and len(stack) > 1:
                last = stack.pop()
                stack[-1].add(last)

    return stack[0] if stack else int(s)


s = input("Enter serialized chest: ")
result = parse_chest(s)
print(result)
