def list(name): 
    return name.split()

def print_name(value):
    print("Nama panggilan saya adalah {}. Nama bali saya adalah {}".format(value[0],value[1]))

list_name= print_name(list("Ngakan Putu"))
list_name= print_name(list("William Wayan"))