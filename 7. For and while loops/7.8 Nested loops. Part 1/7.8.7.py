for bulls in range(11):
    for cows in range(21):
        for calfs in range(201):
            total = bulls + cows + calfs
            if total == 100 and 10 * bulls + 5 * cows + 0.5 * calfs == 100:
                print(bulls, cows, calfs)
    print()