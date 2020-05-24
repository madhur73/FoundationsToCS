class Sorting:
    # make unsorted array global to class

    def _swap(self, source, des, arr):
        temp = arr[source]
        arr[source] = arr[des]
        arr[des] = temp

        return arr

    def insertion_sort(self, unsorted_arr):
        prefix = 0
        array_size = len(unsorted_arr)
        while prefix < array_size - 1:
            if unsorted_arr[prefix + 1] >= unsorted_arr[prefix]:
                prefix += 1
            else:
                unsorted_arr = self._swap(prefix, prefix + 1, unsorted_arr)
                current = prefix
                prefix += 1
                while current >= 1:
                    if unsorted_arr[current] < unsorted_arr[current - 1]:
                        unsorted_arr = self._swap(current, current - 1, unsorted_arr)
                        current -= 1

                    if unsorted_arr[current] > unsorted_arr[current - 1]:
                        break

        return unsorted_arr

    def merge_sort(self, unsorted_arr):
        if not unsorted_arr:
            return None

        r = len(unsorted_arr) - 1
        sorted_array = self.start_merge_sort(0, r, unsorted_arr)
        return sorted_array

    def start_merge_sort(self, left_index, right_index, unsorted_arr):
        if left_index == right_index:
            return
        len_arr = left_index + right_index + 1
        pivot = len_arr // 2
        self.start_merge_sort(left_index, pivot - 1, unsorted_arr)
        self.start_merge_sort(pivot, right_index, unsorted_arr)
        return self.merge_arrays(left_index, pivot, pivot - 1, right_index, unsorted_arr)

    def merge_arrays(self, first_left_index, second_left_index, first_right_index, second_right_index, unsorted_arr):
        sorted_arr = []
        # may change to right index
        left_arr = unsorted_arr[first_left_index:first_right_index + 1]
        right_arr = unsorted_arr[second_left_index: second_right_index + 1]

        i = j = 0
        while i < len(left_arr) or j < len(right_arr):

            if j >= len(right_arr) or (i < len(left_arr) and left_arr[i] <= right_arr[j]):
                sorted_arr.append(left_arr[i])
                i += 1

            elif i >= len(left_arr) or (j < len(right_arr) and right_arr[j] < left_arr[i]):
                sorted_arr.append(right_arr[j])
                j += 1

        i = first_left_index
        c = 0
        while i <= second_right_index:
            unsorted_arr[i] = sorted_arr[c]
            c += 1
            i += 1
        return unsorted_arr

    # def start_quick_sort(self):

def test_sorting():
    sorting_obj = Sorting()
    arr = [7, 6, 5, 4, 3, 2, 1]
    assert sorting_obj.insertion_sort(arr) == [1, 2, 3, 4, 5, 6, 7], "non-decreasing test failed"
    assert sorting_obj.insertion_sort([]) == [], "null value test failed"
    assert sorting_obj.merge_sort([1, 4, 2, 3]) == [1, 2, 3, 4], " Simple Merge Sort Failed"


if __name__ == "__main__":
    test_sorting()
    print("Everything Passed")
