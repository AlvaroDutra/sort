import random
from sorting import insertion_sort, selection_sort, bubble_sort

any_numbers= random.sample(range(1, 1000), 40)

already_sorted = [1, 2, 3, 4, 5, 6 ,77 ,88 ,99 ,123 ,125 ,234 ,269]

inversed= [117, 90, 88, 83, 80, 76, 74, 69, 63, 61, 58, 52, 47, 44, 41, 33, 31, 27, 22, 18, 14, 10, 8, 7, 6, 4, 2, 1]

repetido=[7,7,7,7,1,1,1,6,6,6,9,9,9,4,4,4,4,1,7,9,9]

if __name__=="__main__":    
    
    lista=inversed
    print(lista)
    bubble_sort(lista)
    print("\n Ordenado:")
    print(lista)

input()