time = int(input('Сколько сейчас часов? > '))



if time >= 0 and time < 6:
    print('Good Night')
elif time >= 6 and time < 13:
    print('Good Morning')
elif time >= 13 and time < 17:
    print('Good Day')
elif time >= 17 and time < 24:
    print('Good Evening')
else:
    print('У вам земные сутки?')