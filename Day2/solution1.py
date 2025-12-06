
def solution(raw_input: list[str])-> int:
    res = 0
    for section in raw_input:
        num1, num2 = section.split("-")
        num1 = int(num1)
        num2 = int(num2)
        for i in range(num1, num2 + 1):
            curr_num = str(i)
            mid = len(curr_num)//2
            if curr_num[0: mid] == curr_num[mid:]:
                res += i
    return res

# Optimized Solution
def solutionOptimized(raw_input: list[str])-> int:
    res = 0
    for section in raw_input:
        num1, num2 = map(int, section.split("-"))
        min_len = len(str(num1))
        max_len = len(str(num2))
        for length in range(min_len, max_len + 1):
            if length % 2 != 0:
                continue
            
            half = length //2
            start = 10**(half - 1)
            end = 10**half
            for a in range(start, end):
                doubled = int(str(a) + str(a))
                if num1 <= doubled <= num2:
                    res += doubled
                if doubled > num2:
                    break
    return res 

raw_input = "67562556-67743658,62064792-62301480,4394592-4512674,3308-4582,69552998-69828126,9123-12332,1095-1358,23-48,294-400,3511416-3689352,1007333-1150296,2929221721-2929361280,309711-443410,2131524-2335082,81867-97148,9574291560-9574498524,648635477-648670391,1-18,5735-8423,58-72,538-812,698652479-698760276,727833-843820,15609927-15646018,1491-1766,53435-76187,196475-300384,852101-903928,73-97,1894-2622,58406664-58466933,6767640219-6767697605,523453-569572,7979723815-7979848548,149-216"

raw_input = raw_input.split(",")
print(solutionOptimized(raw_input))