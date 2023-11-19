ip_address = input().split('.')

for i in range(len(ip_address)):
    if int(ip_address[i]) > 255:
        print('НЕТ')
        break
else:
    print('ДА')