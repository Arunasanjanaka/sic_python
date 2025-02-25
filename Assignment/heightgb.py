def can_be_arranged(a, b):
    a.sort()
    b.sort()

    if len(a) != len(b):
        return "NO"
    
    combined1 = []
    combined2 = []

    # Try starting with a boy
    i, j = 0, 0
    while i < len(a) and j < len(b):
        combined1.append(a[i])
        combined1.append(b[j])
        i += 1
        j += 1
    if i < len(a):
        combined1.append(a[i])
    if j < len(b):
        combined1.append(b[j])
    
    # Try starting with a girl
    i, j = 0, 0
    while i < len(a) and j < len(b):
        combined2.append(b[j])
        combined2.append(a[i])
        j += 1
        i += 1
    if j < len(b):
        combined2.append(b[j])
    if i < len(a):
        combined2.append(a[i])

    def is_valid(arr):
        for k in range(1, len(arr)):
            if arr[k] < arr[k - 1]:
                return False
        for k in range(1, len(arr)):
            if (arr[k] in a and arr[k - 1] in a) or (arr[k] in b and arr[k - 1] in b):
                return False
        return True

    if is_valid(combined1) or is_valid(combined2):
        return "YES"
    else:
        return "NO"

# Take input from user
a = list(map(int, input("Enter the values for a separated by spaces: ").split()))
b = list(map(int, input("Enter the values for b separated by spaces: ").split()))
print(can_be_arranged(a, b))
