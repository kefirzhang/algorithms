class Solution:
    def findRestaurant(self, list1, list2):
        helper_list1, helper_list2 = {}, {}
        for i, n in enumerate(list1):
            helper_list1[n] = i
        for i, n in enumerate(list2):
            helper_list2[n] = i

        ret = []
        min_index = len(list1) + len(list2)

        for i in helper_list1:
            if i in helper_list2:
                if helper_list1[i] + helper_list2[i] < min_index:
                    ret = [i]
                    min_index = helper_list1[i] + helper_list2[i]
                elif helper_list1[i] + helper_list2[i] == min_index:
                    ret.append(i)

        return ret


slu = Solution()
print(slu.findRestaurant(["Shogun", "Tapioca Express", "Burger King", "KFC"],
                         ["Piatti", "The Grill at Torrey Pines", "Hungry Hunter Steakhouse", "Shogun"]))
