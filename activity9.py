username = 'Terrence'
password = '1234'

#print(username == 'Terrence')
print((username == 'Terrence')and(password == '1234'))
print((username == 'Terrence')and(password == '4321'))
print(not(username == 'Terrence')and(password == '1234'))
print(not(username == 'Terrence')and(password == '4321'))
print((username == 'Terrence')or(password == '1233'))
print((username == 'Skyler')or(password == '1233'))
print(not(username == 'Terrence')or(password == '1233'))
print(not((username == 'Skyler')or(password == '1233')))
