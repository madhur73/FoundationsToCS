class Sorting:
    # make unsorted array global to class
    def __init__(self):
        self.unsorted_arr = []

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

    def start_quick_sort(self):
        pass

    def quick_sort(self, left, right, unsorted_arr):
        # Partition(arr) :-> return array with partition index
        # stop when left == right
        # quickSort(left,partition -1)
        # quickSort(partition + 1,right)
        self.unsorted_arr = unsorted_arr
        if left == right:
            return
        pivot = 0
        if left - 1 >= 0:
            pivot = left - 1
        partition_index = self._partition(self.unsorted_arr, left+1, right, pivot)
        self.quick_sort(left, partition_index - 1)
        self.quick_sort(partition_index + 1, right)

        return unsorted_arr

    def _partition(self, unsorted_arr, left, right, pivot):
        # while left < right
        # select pivot
        # Find new value for pivot swap with first element and left
        partition_index = 0
        while left < right:
            while left < right and unsorted_arr[left] <= unsorted_arr[pivot]:
                left += 1
            while left < right and unsorted_arr[right] > unsorted_arr[pivot]:
                right -= 1
            unsorted_arr = self._swap(left, right, unsorted_arr)

        if unsorted_arr[left - 1] <= unsorted_arr[pivot]:
            unsorted_arr = self._swap(left - 1, pivot, unsorted_arr)
            partition_index = left - 1

        return unsorted_arr, partition_index


def test_sorting():
    sorting_obj = Sorting()
    arr = [7, 6, 5, 4, 3, 2, 1]
    # print(sorting_obj._partition([10, 8, 3, 12, 7, 15, 20, 30, 5, 2, 29, 14], 1, 11, 0))
    # assert sorting_obj._partition([10, 8, 3, 12, 7, 15, 20, 30, 5, 2, 29, 14], 1, 11, 0) == (
    #    [5, 8, 3, 2, 7, 10, 20, 30, 15, 12, 29, 14], 5), "Partition function error "

    assert sorting_obj.quick_sort(0, 3, [3, 1, 2]) == [1, 2, 3], "QuickSort Error"
    assert sorting_obj.insertion_sort(arr) == [1, 2, 3, 4, 5, 6, 7], "non-decreasing test failed"
    assert sorting_obj.insertion_sort([]) == [], "null value test failed"
    assert sorting_obj.merge_sort([1, 4, 2, 3]) == [1, 2, 3, 4], " Simple Merge Sort Failed"


if __name__ == "__main__":
    test_sorting()
    print("Everything Passed")
