class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        num_list = {}
        i = 0
        for c in order:
            num_list[c] = i
            i+=1
        # print(num_list)

        for i in range(len(words)-1):
            for j in range(len(words[i])):

                if j >= len(words[i+1]):
                    return False
                if words[i][j] != words[i+1][j]:
                    if num_list[words[i][j]] > num_list[words[i+1][j]]:
                        return False
                    break

        return True





        