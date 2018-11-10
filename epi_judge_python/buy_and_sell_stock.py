from test_framework import generic_test


def buy_and_sell_stock_once(prices):
    profit = 0
    min = prices[0]
    for ele in prices:
        if ele > min:
            if ele - min > profit:
                profit = ele - min
        elif ele < min:
            min = ele
    return profit


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("buy_and_sell_stock.py",
                                       "buy_and_sell_stock.tsv",
                                       buy_and_sell_stock_once))
