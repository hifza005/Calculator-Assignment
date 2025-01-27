def add(n1, n2):  
    # Yeh function do numbers ko add karta hai.
    return n1 + n2

def subtract(n1, n2):  
    # Yeh function do numbers ko subtract karta hai.
    return n1 - n2

def multiply(n1, n2):  
    # Yeh function do numbers ko multiply karta hai.
    return n1 * n2

def divide(n1, n2):  
    # Yeh function pehla number doosray number se divide karta hai.
    return n1 / n2

# Ek dictionary banai gai hai jo har operation symbol ko uske function se link karti hai.
operations = {
    "+": add,       # "+" ka matlab add function hai.
    "-": subtract,  # "-" ka matlab subtract function hai.
    "*": multiply,  # "" ka matlab multiply function hai.
    "/": divide     # "/" ka matlab divide function hai.
}

def calculator():  
    # Yeh function calculator ka kaam karta hai.
    
    # Pehla number user se input le kar floating point (decimal) number mein convert karta hai.
    num1 = float(input("What's the first number?: "))
    
    # Har operation ka symbol print karta hai.
    for symbol in operations:
        print(symbol)
    
    # Ek flag variable banaya gaya hai jo loop chalane ke liye use hoga.
    should_continue = True  

    # Jab tak user 'n' na bole, loop chalega.
    while should_continue:  
        # User se ek operation symbol input liya jata hai.
        operation_symbol = input("Pick an operation: ")  
        
        # Dusra number input le kar floating point mein convert karta hai.
        num2 = float(input("What's the next number?: ")) 
        
        # Operations dictionary se user ka select kiya hua function retrieve karta hai.
        calculation_function = operations[operation_symbol] 
        
        # Function ko call karke result (answer) calculate karta hai.
        answer = calculation_function(num1, num2)  
        
        # Calculation ka result screen par print karta hai.
        print(f"{num1} {operation_symbol} {num2} = {answer}")  

        # User se puchhta hai ki woh calculation continue karna chahta hai ya naye number ke saath shuru karna chahta hai.
        if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ") == 'y':  
            # Agar user 'y' bole, toh pehla number result ke barabar ho jata hai.
            num1 = answer  
        else:  
            # Agar user 'n' bole, toh naya calculator call hota hai.
            should_continue = False  
            calculator()  

# Calculator function ko call karta hai taake program shuru ho.
calculator()