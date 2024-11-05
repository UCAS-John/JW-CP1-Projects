#John Wangwang SkillPractice: Counting characters

def main():

    count = {}

    grid = [
        ['A', 'B', 'C', 'A', 'D'],
        ['C', 'A', 'B', 'D', 'E'],
        ['A', 'D', 'C', 'E', 'A'],
        ['B', 'A', 'C', 'A', 'D'],
        ['D', 'C', 'B', 'E', 'A'] ]

    for row in grid:
        for char in row:
            if char not in count:
                count[char] = 1
            else:
                count[char] += 1

    for counted in count:
        print(f"{counted}: {count[counted]}")

if __name__ == "__main__":
    main()