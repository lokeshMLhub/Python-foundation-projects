def total(m1, m2, m3):
    return m1 + m2 + m3

def percentage(total_marks):
    return total_marks / 3

m1 = int(input("Enter mark 1: "))
m2 = int(input("Enter mark 2: "))
m3 = int(input("Enter mark 3: "))

t = total(m1, m2, m3)
p = percentage(t)

print("Total =", t)
print("percentage =", p)

