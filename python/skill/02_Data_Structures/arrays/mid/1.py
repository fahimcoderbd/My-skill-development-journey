#E-commerce (find duplicate products)
#14/8/26

def find_duplicate_products(products:list):
    if not products: return

    freq_map = {} #id:freq

    for product_id in products:
        if product_id in freq_map: freq_map[product_id] += 1
        else: freq_map[product_id] = 1

    return freq_map

def display_product_freq(products_list:list):
      freq_dict = find_duplicate_products(products_list)

      #handling empty dict error
      if not freq_dict: return

      for product_id, freq in freq_dict.items():
        print(f"{product_id}: {freq}")

def highest_freq_product(products_list:list):
    freq_dict = find_duplicate_products(products_list)
    if not freq_dict: return
    highest_freq = 1
    highest_product_id = None

    for product_id, freq in freq_dict.items():
        if freq > highest_freq:
            highest_freq = freq
            highest_product_id = product_id

    return (
        f"Product id: {highest_product_id} \n"
        f"Frequency: {highest_freq}"
    )

#testing features
products = [101, 203, 101, 405, 203, 501, 203, 405]

print(display_product_freq([]))
display_product_freq(products)
print(highest_freq_product(products))