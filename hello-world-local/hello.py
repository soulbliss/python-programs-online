name = input()
text = input()


greeting = "Hello world, welcome {}!".format(name)

output_string = text*10

print({"greeting": greeting, "result": output_string})