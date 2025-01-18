def main():
    import check_mod as m
    r = float(input("Enter the radius of the circle: "))
    result_1 = m.circumference(r)
    result_2 = m.area(r)
    print(result_1)
    print(result_2)
main()