shop_menus = ["만두", "떡볶이", "오뎅", "사이다", "콜라"]
shop_orders = ["오뎅", "콜라", "만두"]


def is_exist_target_number_binary(target, array):
    current_min = 0
    current_max = len(array) - 1
    current_guess = (current_min + current_max) // 2

    while current_min <= current_max:
        if array[current_guess] == target:
            return True
        elif array[current_guess] < target:
            current_min = current_guess + 1
        else:
            current_max = current_guess - 1
        current_guess = (current_min + current_max) // 2

    return False

def is_available_to_order(menus, orders):
    menus.sort()

    # 주문된 모든 메뉴가 메뉴판에 있는지 확인
    for order in orders:
        if not is_exist_target_number_binary(order, menus):
            return False

    return True


result = is_available_to_order(shop_menus, shop_orders)
print(result)