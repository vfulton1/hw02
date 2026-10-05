# ------------------------------------------------------
#        Name: Vivian Fulton
#  References: How to Think Like a Computer Scientist: Interactive Edition
#
# [X] you added your name to the top comments of the python file
# [X] runs without syntax errors (or -50%)
# [X] adds a few small but informative comments (or -5%)
# [X] adds docstrings to each function (or -5%)
# [X] Passes all tests (or lose 15% per missed test). If you do not pass all tests, do not check this box
# [X] You checked the correct boxes
# ------------------------------------------------------

# Task 1.1:
#  Complete the function "read_two_ints" below:
def read_two_ints():
    """
    This function takes two integer inputs from the user.
    
    The function asks the user for integer inputs that are assigned to x and y
    variables. It then casts these inputs as integers since they are automatically
    input as strings. These integers are now assigned to variables a and b. The
    function then returns the two variables.

    PARAMS:
        - x: string chosen by user
        - y: string chosen by user
    
    RETURNS:
        - a: x cast as an integer
        - b: y cast as an integer
        
    Example Use:
    If the user inputs 3 to assign to x and 5 to assign to y, the function will cast
    these as integers a and b respectively, and return the values.
    """
    # the return shown below is a placeholder to make sure this runs
    # TODO: complete the function instead of the line shown below
    x = input("give me x: ")
    #must cast the string x as an int
    a = int(x)
    y = input("give me y: ")
    #must cast the string y as an int
    b = int(y)
    return a,b
  
# Task 2.1:
#  Complete the function "compute_multadd" below:
def compute_multadd(a, b):
    """
    This function takes the returned values and preforms computations with them.
    
    The function takes the returned variables a and b from the function read_two_ints
    and first multiples a and b together, then prints the result. The funtion then adds
    a and b together, then prints the result. The funtion then divides the
    multiplication result by the addition result and returns this value.

    PARAMS:
        - a: integer chosen by the user from first function
        - b: integer chosen by the user from first function
    
    RETURNS:
        - ab_multadd: float of a * b divided by a + b
        
    Example Use:
    If we have the integer 3 assigned to the varible a and the integer 5 assigned to
    the variable b, the function will first calculate
    a * b
    15
    
    then calculate
    a + b
    8
    
    and print as follows:
    mult result: 15
    add result:8
    
    The function will then calculate the division of the multiplication result by the
    addition result:
    (a * b)/(a + b)
    1.875
    
    and will then return the final result
    """
    # the pass shown below is a placeholder to make sure this runs
    # TODO: complete the function instead of the line shown below
    mult = a * b
    print("mult result:",mult)
    add = a + b
    print("add result:",add)
    #mult/add is the final result & output for the function, referred to as ab_multadd
    return mult/add

# Task 3.1:
#  Complete the function "print_fancy" below:
def print_fancy(a, b, ab_multadd):
    """
    This function prints the results from previous functions.
    
    The function prints a formated display of the two integers decided by the user in
    the first function, and the mult/add result from the function above. It formats
    them by printing a line of stars above and a line of equal signs below.

    PARAMS:
        - a: integer chosen by the user from first function
        - b: integer chosen by the user from first function
        - ab_multadd: result of second function, calculated by (a * b)/(a + b)
    
    RETURNS:
        - NONE
        
    Example Use:
    If we have the integer 3 assigned to the varible a and the integer 5 assigned to
    the variable b, and the result of ab_multadd was 1.875, then the function would
    print as follows:
    
    ****************
    RESULTS:
    first number: 3
    second number: 5
    multadd result: 1.875
    ================
    """
    # the pass shown below is a placeholder to make sure this runs
    # TODO: complete the function instead of the line shown below
    #adding empty print line at the top of the print script for better readablitiy
    print()
    print("****************")
    print("RESULTS:")
    print("first number:",a)
    print("second number:",b)
    print("multadd result:",ab_multadd)
    print("================")
    #adding empty print line at the bottom of the print script for better readablitiy
    print()

def main ():
    """
    This function calls the previous functions and prints an ending statement.
    
    The function asks calls on the three functions above and then afterwards,prints a
    statement saying "The End" to indicate that the script is finished running. 

    PARAMS:
        - NONE
    
    RETURNS:
        - NONE
        
    Example Use:
    If the user inputs 3 to assign to x and 5 to assign to y, the function will call
    on the previous three functions, resulting in the printing of the following:
    give me x: 3
    give me y: 5
    mult result: 15
    add result: 8

    ****************
    RESULTS:
    first number: 3
    second number: 5
    multadd result: 1.875
    ================

    The End
    """
    # Task 1.2:
    #  Add one line below to call read_two_ints (note that it returns two values)
    #  the call should provide no arguments
    #  store the returned values into two variables: x and y
    
    a,b =read_two_ints()

    # Task 2.2:
    #  Add one line below to call multadd (note that it returns one value)
    #  the call should provide the arguments x, and y you obtained above;
    #  store the returned value in a variable called xy_multadd

    ab_multadd =compute_multadd(a, b)

    # Task 3.2:
    #  Complete The line below to call print_fancy
    #  the call should provide the arguments x, y, and xy_multadd you obtained above;

    print_fancy(a, b, ab_multadd)


    # Do not modify this final print statement
    print("The End")

# Do not modify these two lines
if __name__ == "__main__":
    main()
