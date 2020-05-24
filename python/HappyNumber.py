class Solution:
    def isHappy(self, n: int) -> bool:

        def get_squared_digits_from_number(number):
            digits_list = []

            while number != 0:
                last_digit = number % 10
                number = number // 10
                squared_number = get_square_of_number(last_digit)
                digits_list.append(squared_number)

            return digits_list

        def get_square_of_number(num):
            return num * num
        
        
        
    

        def get_squared_numbers_sum(square_digit_list):
            return sum(square_digit_list)

        def is_sum_repeating(unique_sum_set, sumof_squared_nums):
            if sumof_squared_nums in unique_sum_set:
                return True
            else:
                return False

        unique_sum_set = dict()
        new_sum = n
        terminating_num = 1
        while True:
            square_digit_list = get_squared_digits_from_number(new_sum)
            new_sum = get_squared_numbers_sum(square_digit_list)
            if new_sum == terminating_num:
                return True

            if is_sum_repeating(unique_sum_set, new_sum):
                return False
            else:
                unique_sum_set[new_sum] = 1
