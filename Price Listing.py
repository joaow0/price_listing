def line():
    print('-='*21)

product_list = ('keyboard', 150.40,
                'chair', 135.00,
                'mouse', 78.90,
                'monitor', 749.70,
                'sound', 91.00,
                'router', 115.00,
                'case', 420.00,
                'headphones', 97.00,
                'mousepad', 15.00,
                'fan', 300.00,
                'motherboard', 1250.00)
line()
print('PRICE LIST'.center(39))
line()

for i, v in enumerate(product_list):
    if i % 2 == 0:
        print(f'{product_list[i]:.<30}', end='')
    else:
        print(f'R${product_list[i]:>9.2f}')
line()