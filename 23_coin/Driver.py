from Coin import Coin

class Driver:
    coin = Coin("quarter", "heads")
    other = Coin("quarter", "heads")

    print(coin)
    print(other)
    print("\nAfter flipping...")
    coin.flip()
    other.flip()
    print(coin)
    print(other)
    print("are equal? " + str(coin.equals(other)))

    print(coin.value)
