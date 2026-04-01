#For loops

# for i in range (10):
#     print(i)

# for i in range(10):
#     print("I Love Python" )


a= list(range(1,100, 2))
print(a)

b="Hello World"

for letter in b:
    print(letter)

bag= ["apple", "banana", "orange", "grape", "watermelon"]

for item in bag:
    print(item)

# lst=[50, 10, 3, -2, 15,0, 5, 14, 25,11,7.17, 3.14] 
# for i in lst:
#     if i<=20:
#         print(i)  

# for i in lst:
#     if i%3==0 and i%5==0:
#         print(i)

sum=0
for i in range(1,6):
    sum+=i

print(sum)