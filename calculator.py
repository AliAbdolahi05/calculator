def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "خطا: تقسیم بر صفر مجاز نیست!"
    return x / y

def main():
    print("ماشین حساب ساده")
    while True:
        print("\nعملیات‌ها:")
        print("1. جمع")
        print("2. تفریق")
        print("3. ضرب")
        print("4. تقسیم")
        print("5. خروج")

        choice = input("انتخاب کنید (1/2/3/4/5): ")

        if choice == "5":
            print("خداحافظ!")
            break

        if choice not in ["1", "2", "3", "4"]:
            print("گزینه نامعتبر است.")
            continue

        try:
            num1 = float(input("عدد اول: "))
            num2 = float(input("عدد دوم: "))
        except ValueError:
            print("لطفاً عدد معتبر وارد کنید.")
            continue

        if choice == "1":
            print(f"نتیجه: {add(num1, num2)}")
        elif choice == "2":
            print(f"نتیجه: {subtract(num1, num2)}")
        elif choice == "3":
            print(f"نتیجه: {multiply(num1, num2)}")
        elif choice == "4":
            print(f"نتیجه: {divide(num1, num2)}")

if __name__ == "__main__":
    main()
