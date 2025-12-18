raw_input = """123 328  51 64 
 45 64  387 23 
  6 98  215 314
*   +   *   + """

raw_input = raw_input.splitlines()
raw_input = [line.strip("\n") for line in raw_input]
raw_input = list(reversed(list(zip(*raw_input))))
group = []
groups = []
for col in raw_input:
    if set(col) == {" "}:
        groups.append(group)
        group = []
    else:
        group.append(col)
groups.append(group)



def solution(groups: list)-> int:
    total = 0
    for eq in reversed(groups):
        if not eq:
            continue
        operator = None
        for col in eq:
            if col[-1] in ("*", "+"):
                operator = col[-1]
        if operator == "*":
            curr_sol = 1
        else:
            curr_sol = 0
        for num in reversed(eq):
            if num[-1] in ("*", "+"):
                continue
            num = int("".join(c for c in num if c.isdigit()))
            if operator == "*":
                curr_sol *= num
            else:
                curr_sol += num
        total += curr_sol
    return total

print(solution(groups))