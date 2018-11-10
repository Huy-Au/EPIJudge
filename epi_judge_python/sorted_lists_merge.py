from test_framework import generic_test
from list_node import ListNode

def merge_two_sorted_lists(L1, L2):
    dummy_head = tail = ListNode()

    return None


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("sorted_lists_merge.py",
                                       'sorted_lists_merge.tsv',
                                       merge_two_sorted_lists))
