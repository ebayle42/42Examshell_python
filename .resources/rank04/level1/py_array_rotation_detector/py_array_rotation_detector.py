def array_rotation_detector(arr1: list, arr2: list) -> bool:
    n = len(arr1)
    if n != len(arr2):
        return False
    if n == 0:
        return True
    for shift in range(n):
        if all(arr1[(i + shift) % n] == arr2[i] for i in range(n)):
            return True
    return False
