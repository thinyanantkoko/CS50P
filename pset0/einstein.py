def main():
    #the speed of light, c(in m/sec)
    c = 300000000

    #prompting the user for the mass, m(in kg)
    m = int(input("m: "))

    #the equivalent energy, E(in Joules)
    E = m * c ** 2
    print(f"E: {E}")

main()