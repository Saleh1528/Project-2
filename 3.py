def calculate(num1, operator, num2):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        if num2 != 0:
            return num1 / num2
        else:
            return "تقسیم بر صفر امکان‌پذیر نیست"
    else:
        return "عملگر نامعتبر است"


try:
    num1 = float(input("عدد اول را وارد کنید: "))
    operator = input("عملگر را وارد کنید (+, -, *, /): ")
    num2 = float(input("عدد دوم را وارد کنید: "))

    
    result = calculate(num1, operator, num2)
    print("نتیجه:", result)

except ValueError:
    print("ورودی نامعتبر است. لطفاً عدد وارد کنید.")
