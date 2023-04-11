from till import Till

headers = ['Till Start', 'Transaction Total', 'Paid', 'Change Total', 'Change Breakdown']
print(f'{headers[0]:<20} {headers[1]:<20} {headers[2]:<20} {headers[3]:<20} {headers[4]:<20}')


lines = []

with open('data/input.txt', 'r') as f:
    lines = [line.strip() for line in f]

till = Till(lines)
till.process()







