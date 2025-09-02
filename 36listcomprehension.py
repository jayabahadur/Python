# squares=[x**2 for x in range(1,11)]
# for square in squares:
#     print("Square of number from 1 to 10", square)

numbers=[1,2,3,4,5,6,7,8,9,10,12,15,18,22]
even_numbers={x for x in numbers if x%2==0}
print(even_numbers)

letter=['apple','banana','cherry','mango', 'Gauva', 'Pineapple', 'Watermelon']
five_letters_word={x for x in letter if len(x)==5}
print(five_letters_word)
