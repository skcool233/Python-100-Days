# module.py

def print_hello():
    print("Hello from module.py!")

if __name__ == '__main__':
    print("module.py is being run directly")
else:
    print("__name__ in module.py is", __name__)
