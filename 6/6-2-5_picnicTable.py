def print_picnic(items_dict, left_width, rigth_width):
    print('PICNIC ITEMS'.center(left_width + rigth_width, '-'))
    for k, v in items_dict.items():
        print(k.ljust(left_width, '.') + str(v).rjust(rigth_width))

picnic_items = {'sandwiches': 4, 'apples': 12, 'cups': 4, 'cookies':8000}
print_picnic(picnic_items, 12, 5)
print_picnic(picnic_items, 20, 6)
