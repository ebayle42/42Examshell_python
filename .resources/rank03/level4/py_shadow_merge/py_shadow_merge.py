def shadow_merge(list1: list[int], list2: list[int]) -> list[int]:
    i = j = 0
    result = []
    while i < len(list1) and j < len(list2):
        if list1[i] <= list2[j]:
            result.append(list1[i])
            i += 1
        else:
            result.append(list2[j])
            j += 1
    return result + list1[i:] + list2[j:]
