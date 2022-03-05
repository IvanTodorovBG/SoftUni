def check_for_more(left_side, right_side, symbl):
    for count_repeat in range(7, 12):
        if symbl * count_repeat in left_side and symbl * count_repeat in right_side:
            continue
        else:
            return count_repeat - 1


text = input().replace(" ", "")
text = text.split(",")

for current_ticket in text:

    all_good = True

    if len(current_ticket) == 20:
        left = current_ticket[:10]
        right = current_ticket[10:]
        common_count = None
        symbol = ""

        if "$" * 6 in left and "$" * 6 in right:
            symbol = "$"
            common_count = check_for_more(left, right, symbol)
        elif "@" * 6 in left and "@" * 6 in right:
            symbol = "@"
            common_count = check_for_more(left, right, symbol)
        elif "#" * 6 in left and "#" * 6 in right:
            symbol = "#"
            common_count = check_for_more(left, right, symbol)
        elif "^" * 6 in left and "^" * 6 in right:
            symbol = "^"
            common_count = check_for_more(left, right, symbol)
        else:
            all_good = False
            print(f'ticket "{current_ticket}" - no match')

        if all_good:
            if 6 <= int(common_count) <= 9:
                print(f'ticket "{current_ticket}" - {common_count}{symbol}')
            elif int(common_count) == 10:
                print(f'ticket "{current_ticket}" - {common_count}{symbol} Jackpot!')

    else:
        print("invalid ticket")

















#        if len(left_used_symbol) == 10 and len(right_used_symbol) == 10:
#           print(f'ticket "{current_ticket}" - {max_left_side_count}{top_symbol[0]} Jackpot!')
#
#       elif 6 <= len(left_used_symbol) <= 9 and 6 <= len(right_used_symbol) <= 9:
#          print(f'ticket "{current_ticket}" - {min(max_left_side_count, max_right_side_count)}{top_symbol[0]}')
#
#       else:
#          print(f'ticket "{current_ticket}" - no match')
#
#   else:
#      print("invalid ticket")



