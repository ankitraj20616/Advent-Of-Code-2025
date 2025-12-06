def solution(raw_input: list[str])-> int:
    res = 0
    seen = set()
    for section in raw_input:
        num1, num2 = map(int, section.split("-"))
        min_len = len(str(num1))
        max_len = len(str(num2))
        for total_len in range(min_len, max_len + 1):
            for base_len in range(1, total_len):
                if total_len % base_len != 0:
                    continue
                k = total_len // base_len
                if k < 2:
                    continue
                start = 10**(base_len - 1)
                end = 10**base_len
                for a in range(start, end):
                    repeated_str = str(a) * k
                    repeated_int = int(repeated_str)
                    if repeated_int > num2:
                        break
                    if num1 <= repeated_int <= num2 and repeated_int not in seen:
                        seen.add(repeated_int)
                        res += repeated_int
    return res

raw_input = "67562556-67743658,62064792-62301480,4394592-4512674,3308-4582,69552998-69828126,9123-12332,1095-1358,23-48,294-400,3511416-3689352,1007333-1150296,2929221721-2929361280,309711-443410,2131524-2335082,81867-97148,9574291560-9574498524,648635477-648670391,1-18,5735-8423,58-72,538-812,698652479-698760276,727833-843820,15609927-15646018,1491-1766,53435-76187,196475-300384,852101-903928,73-97,1894-2622,58406664-58466933,6767640219-6767697605,523453-569572,7979723815-7979848548,149-216"

raw_input = raw_input.split(",")
print(solution(raw_input))