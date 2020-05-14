# Coins: Given an infinite number of quarters (25 cents), dimes (1O cents), nickels (5 cents), and pennies (1 cent),
# write code to calculate the number of ways of representing n cents.

# with mem


def represent_n_cents(n, coins, flag, mem):
    # check if value already in mem
    if mem[n][flag] > 0:
        return mem[n][flag]
    # if the end of coins is reached  - then only one way to give change
    if flag >= len(coins) - 1:
        return 1
    coin_change = coins[flag]
    rest = n // coin_change
    counter = 0
    for i in range(rest + 1):
        counter += represent_n_cents(n - i * coin_change, coins, flag + 1, mem)
    mem[n][flag] = counter
    return counter


def represent(n, coins):
    flag = 0    # defines which coins have been used already
    mem = [[0 for _ in range(len(coins))] for _ in range(n+1)]
    return represent_n_cents(n, coins, flag, mem)


if __name__ == "__main__":
    coins = [25, 10, 5, 1]
    n = 20
    print('Number of ways of representing', n, 'cents:', represent(n, coins))
