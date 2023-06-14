# -------------------------------------------------------------------------------------------------------------------
# 1. Winning Lottery Ticket
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'winningLotteryTicket' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts STRING_ARRAY tickets as parameter.
#

def get_bit_ticket(ticket_id):
    bit_ticket_arr = ["0"] * 10
    for char in ticket_id:
        bit_ticket_arr[int(char)] = "1"
    return int("".join(bit_ticket_arr), 2)

def count_all(count_bit_tickets):
    result = 0
    for i in range(pow(2, 10)):
        for j in range(i + 1, pow(2, 10)):
            if i | j == pow(2, 10) - 1:
                result += count_bit_tickets.get(i, 0) * count_bit_tickets.get(j, 0)
    full_bit_ticket_count = count_bit_tickets.get(pow(2, 10) - 1, 0)
    if full_bit_ticket_count > 1:
        result += round(full_bit_ticket_count * (full_bit_ticket_count - 1) / 2)    
    return result
                
def winningLotteryTicket(tickets):
    count_bit_tickets = {}
    for ticket_id in tickets:
        bit_ticket = get_bit_ticket(ticket_id)
        if count_bit_tickets.get(bit_ticket):
            count_bit_tickets[bit_ticket] += 1
        else:
            count_bit_tickets[bit_ticket] = 1    
    return count_all(count_bit_tickets)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    tickets = []

    for _ in range(n):
        tickets_item = input()
        tickets.append(tickets_item)

    result = winningLotteryTicket(tickets)

    fptr.write(str(result) + '\n')

    fptr.close()
