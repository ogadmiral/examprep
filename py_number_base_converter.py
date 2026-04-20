def number_base_converter(number: str, from_base: int, to_base: int) -> str:
    try:
        number = int(number, from_base)
    except Exception:
        print("Error")
        exit(1)
    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = ""
    if number == 0: return "0"
    while number > 0:
        result = digits[number % to_base] + result
        number = number // to_base
    return result
