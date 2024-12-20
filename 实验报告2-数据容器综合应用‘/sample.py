import math

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def contains_3_or_7(n):
    return '3' in str(n) or '7' in str(n)

def s1(A):
    result = []
    for num in A:
        if is_prime(num) and contains_3_or_7(num):
            result.append(num)
    return result

def s2(A):
    if len(A) % 2 == 1:
        A.pop() 
    points = []
    for i in range(0, len(A), 2):
        points.append((A[i], A[i + 1]))
    return points

def s3(points, B):
    P = tuple(B)
    max1 = -1
    farthest = None
    for point in points:
        distance = math.sqrt((point[0] - P[0]) ** 2 + (point[1] - P[1]) ** 2)
        if distance > max1:
            max1 = distance
            farthest = point
    return list(farthest)

def Try01(A, B):
    filtered_primes = s1(A)
    points = s2(filtered_primes)
    if not points:
        return [] 
    farthest_point = s3(points, B)
    return farthest_point


if __name__ == '__main__':
    print(Try01([2, 68, 4, 3, 5, 7, 90, 11, 13], [1, 1]))
    print(Try01([2, 68, 4, 3, 5, 7, 90, 11, 13, 17], [1, 1]))
    print(Try01([37, 2, 68, 4, 3, 5, 7, 90, 11, 13, 17, 19, 23, 29, 31, 37, 400, 37, 37], [37, 37]))
    print(Try01([37, 2, 68, 4, 3, 5, 7, 90, 11, 13, 17, 19, 23, 29, 31, 37, 400, 37, 37], [1, 1]))
    print(Try01([2, 68], [1, 1]))
    print(Try01([2, 5, 68], [1, 1]))
    print(Try01([2, 5, 7, 68], [1, 1]))
    print(Try01([2, 3, 7, 68], [1, 1]))
    print(Try01([2, 3, 3, 7, 68], [1, 1]))
    print(Try01([2, 3, 3, 7, 9, 68], [1, 1]))
