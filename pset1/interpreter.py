def main():
    #prompting the user for an arithmetic expression
    exp = input("Expression: ")
    #splitting the expression into operands and an operator for calculation
    x, y, z = exp.split()

    #typecasting the operands as integers
    x = int(x)
    z = int(z)

    #checking the operator and do the calculation accordingly
    match y:
        case '+':
            print(f"{x+z:.1f}")
        case '-':
            print(f"{x-z:.1f}")
        case '*':
            print(f"{x*z:.1f}")
        case '/':
            print(f"{x/z:.1f}")

main()