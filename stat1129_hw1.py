#Exercise 1
nums=list(range(30,65,5))
print(nums)
print(nums[::-1])
nums.append(65)
print(nums[::-1])

#Exercise 2
x = []
x = list(range(0,21,1))
print(x)

x.remove(0)
print(x)

print(len(x))
print(max(x))
print(min(x))

sum(x)
print(sum(x))

#Exercise 3
weatherdictionary = {'Sunny': 'play','Rainy': 'watch TV','Cloudy': 'walk'}
for key, value in weatherdictionary.items():
    print('When', key,'let us', value)
weatherdictionary.update({'Snowy':'ski'})
print(weatherdictionary)   


