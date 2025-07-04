from typing import List

class TrieNode:
    def __init__(self):
        self.children = {}

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, num: int):
        node = self.root
        for i in range(31, -1, -1):  # 32-bit integer
            bit = (num >> i) & 1
            if bit not in node.children:
                node.children[bit] = TrieNode()
            node = node.children[bit]

    def getMaxXOR(self, num: int) -> int:
        node = self.root
        if not node.children:
            return -1  # if no numbers added to trie yet
        xor = 0
        for i in range(31, -1, -1):
            bit = (num >> i) & 1
            toggled_bit = 1 - bit
            if toggled_bit in node.children:
                xor |= (1 << i)
                node = node.children[toggled_bit]
            else:
                node = node.children.get(bit)
        return xor


class Solution:
    def maximizeXor(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        nums.sort()
        queries = sorted([(mi, xi, idx) for idx, (xi, mi) in enumerate(queries)])
        res = [0] * len(queries)

        trie = Trie()
        n_idx = 0

        for mi, xi, q_idx in queries:
            # Insert eligible nums ≤ mi into trie
            while n_idx < len(nums) and nums[n_idx] <= mi:
                trie.insert(nums[n_idx])
                n_idx += 1

            max_xor = trie.getMaxXOR(xi)
            res[q_idx] = max_xor

        return res
