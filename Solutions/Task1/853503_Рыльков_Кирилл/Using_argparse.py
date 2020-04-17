import sys
import argparse
import collections
import random

def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-n','--number', default = 1, type = int)
    parser.add_argument('-i','--input_path', default = 'Text.txt', type = str)
    parser.add_argument('-o','--output_path',default = 'Output.txt', type = str)
    parser.add_argument('-f','--fibonacci_number', default = 100,type = int)
    parser.add_argument('-c','--count',default = 10,type = int)
    return parser

def read_from_file(path):
    with open(path, "r") as file:
        data = (file.read().split())
    return data

def write_to_file(data, namespace):
    with open(namespace.output_path, "w") as file:
        if namespace.number == 1:
             for i in data:
                file.writelines(str(i) + " " + str(data[i]) + "\n")
        else:
             for i in data:
                file.writelines(str(i) + "\n")

def word_counter(namespace):
    text = read_from_file(namespace.input_path)
    dictionary = {}
    for i in text:
        if i in dictionary:
            dictionary[i] += 1
        else:
            dictionary[i] = 1

    write_to_file(dictionary, namespace)

    for i in dictionary:
        print(i, dictionary[i])

def most_common_words(namespace):
    collection = collections.Counter(read_from_file(namespace.input_path))
    most_common_words = list([i[0] for i in collection.most_common(namespace.count)])
    write_to_file(most_common_words, namespace)
    print(most_common_words)

def quick_sort(A, left, right):
    if  left >= right:
        return
    i, j = left, right
    pivot = A[random.randint(left, right)]
    
    while i <= j:
        while A[i] < pivot:i+=1
        while A[j] > pivot:j-=1
        if i <= j:
            A[i], A[j] = A[j],A[i]
            i, j = i + 1, j - 1
    quick_sort(A,left,j)
    quick_sort(A,i,right)

def merge(A, B):
    C = [0] * (len(A) + len(B))
    i = j = k = 0
    while i < len(A) and j < len(B):
        if A[i] <= B[j]:
            C[k] = A[i]
            i += 1
            k += 1
        else:
            C[k] = B[j]
            j += 1
            k += 1
    while i < len(A):
        C[k] = A[i]
        i += 1
        k += 1
    while j < len(B):
        C[k] = B[j]
        j += 1
        k += 1
    return C

def merge_sort(A):
    if len(A) <= 1:
        return
    middle = len(A) // 2
    #L = [A[i] for i in range(0, middle)]
    #R = [A[i] for i in range(middle, len(A))]
    L = A[middle:]
    R = A[:middle]
    merge_sort(L)
    merge_sort(R)
    C = merge(L,R)
    for i in range(len(A)):
        A[i] = C[i]

def sort(type):
    A = read_from_file(namespace.input_path)
    A = [int(i) for i in A]
    if type == 'Quck sort':
        quick_sort(A, 0, len(A) - 1)
    elif type == 'Merge sort':
        merge_sort(A)
    write_to_file(A, namespace)
    print(A)

def generator_fibonacci_numbers(n):
    first_number,second_numer = 0,1
    i = 0
    while i < n:
        yield first_number
        first_number,second_numer = second_numer,  first_number + second_numer
        i+=1

parser = create_parser()
namespace = parser.parse_args()
if namespace.number == 1:
    word_counter(namespace)
elif namespace.number == 2:
    most_common_words(namespace)
elif namespace.number == 3:
    sort('Quck sort')
elif namespace.number == 4:
    sort('Merge sort')
elif namespace.number == 5:
    for n in generator_fibonacci_numbers(namespace.fibonacci_number):
        print(n)




