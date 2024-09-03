from collections import deque
   # last_value => snake_case
    # LastValue => UpperCamelCase / PascalCase / CapsWord
    # lastValue => camelCase
    # last-value => kebab-case

    # PEP Python Enhancement Proposal
    # PEP8



def main():
    l = [10, 20, 30, 40, 50]
    l.append(60)
    print(l)
    last_value = l.pop()
    print(l)
    print(last_value)
    
    l.insert(0, -1)
    print(l)
    first_value = l.pop(0)
    print(first_value)
    print(l)
    
    d = deque(l)
    print(d)

    d.appendleft(-5)
    print(d)

    # first_value = d.popleft()
    print(d)
    print(l)

if __name__ == '__main__':
    main()
