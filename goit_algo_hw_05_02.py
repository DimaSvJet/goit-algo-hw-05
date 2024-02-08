def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0
    count = 0
    upper_el = arr[-1]
    result_tuple = (None, None)
    if upper_el < x:
        return -1 
 
    while low <= high:
        count += 1
 
        mid = (high + low) // 2
 
        # якщо x більше за значення посередині списку, ігноруємо ліву половину
        if arr[mid] < x:
            low = mid + 1
 
        # якщо x менше за значення посередині списку, ігноруємо праву половину
        elif arr[mid] > x:
            upper_el = arr[mid]
            high = mid - 1
 
        # інакше x присутній на позиції і повертаємо його
        else:
            upper_el = mid
            print(f"Element is present at index {mid}")
            result_tuple = (count, upper_el)
            return result_tuple
 
    # якщо елемент не знайдений
    result_tuple = (count, upper_el)
    return result_tuple

arr = [2.1, 3.45, 4.5, 5.1, 5.3, 5.8, 10.1, 40.9]
x = 4.5
result = binary_search(arr, x)
if result == -1:
    print("Element is not present in array")
else:
    print(f"A number of iterations are {result[0]}, and the upper element is {result[1]}")
