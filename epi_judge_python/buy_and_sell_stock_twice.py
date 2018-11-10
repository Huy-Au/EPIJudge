from test_framework import generic_test


def buy_and_sell_stock_twice(prices):
    profit = 0
    min = prices[0]
    for ele in prices:
        if ele > min:
            if ele - min > profit:
                profit = ele - min
        elif ele < min:
            min = ele
    return profit + buy_and_sell_stock_twice()

arr = [12, 11, 13, 9, 12, 8, 14, 13, 15]
print(buy_and_sell_stock_twice(arr))

# if __name__ == '__main__':
#     exit(
#         generic_test.generic_test_main("buy_and_sell_stock_twice.py",
#                                        "buy_and_sell_stock_twice.tsv",
#                                        buy_and_sell_stock_twice))
