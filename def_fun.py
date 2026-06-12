"""def compare(x,y):
    return x**y #type:ignore
a = compare(2,4)
print(a)"""

#-----Local and Global Variable------
# Example demonstrating local vs global variables

# Global variable
"""count = 0

def func_local():
    # local variable: only accessible inside this function
    local_var = "I'm local"
    print('Inside func_local, local_var:', local_var)

def shadow_local():
    # this creates a new local variable named 'count'
    # it does NOT modify the global 'count'
    count = 10
    print('Inside shadow_local, count (local):', count)

def modify_global():
    # declare that we want to use the global 'count'
    global count
    count += 5
    print('Inside modify_global, modified count:', count)

print('Global count before:', count)
func_local()
# trying to access local_var here would raise NameError
shadow_local()
print('Global count after shadow_local:', count)
modify_global()
print('Global count after modify_global:', count)"""

