def automate_generates_odd_numbers(number):
    value = [ x for x in range(1,number+1) if x%2!=0]
    return value

print(automate_generates_odd_numbers(101))