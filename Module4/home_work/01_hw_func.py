# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.

def lucky_ticket(ticket_number):
    # TODO: your code here
    pass


# Тестируем функцию
print(lucky_ticket(123006))
print(lucky_ticket(12321))
print(lucky_ticket(436751))

def lucky_ticket(lucky_ticket):
    lucky_ticket = str(lucky_ticket)
    if len(lucky_ticket) != 6:
        print("Это не билет", end=" ")
        return False
    if int(lucky_ticket[0])+int(lucky_ticket[1])+int(lucky_ticket[2]) == int(lucky_ticket[3])+int(lucky_ticket[4])+int(lucky_ticket[5]):
        return True
    else:
        return False
