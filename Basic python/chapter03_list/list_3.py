fib=['a',2,7,9,'kolkata','Bishop']
print(fib)
fib.insert(1,'Bhaumik')
print(fib)
foe=['Delhi','Bengaluru','Baranasi','Kasi','Hydrabad']
print(foe)
fib.extend(foe)
print(fib)
print(foe.sort())
fib.append(foe)
print(fib)
foe.remove('Hydrabad')
print(foe)
del fib[1]
fib.pop(1)
print(fib)