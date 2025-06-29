import decimal
from decimal import Decimal, getcontext, ROUND_DOWN

getcontext().prec = 4


print(Decimal("0.1") + Decimal("0.2") == Decimal("0.3"))
print(Decimal("0.1") + Decimal("0.2"))


getcontext().prec = 6
print(Decimal("1") / Decimal("7"))

getcontext().prec = 8
print(Decimal("1") / Decimal("7"))

getcontext().prec = 6
print(Decimal("233") / Decimal("7"))


print("-------------------------")


number = Decimal("3.14159")

rounded_number = number.quantize(Decimal("0.00"), rounding=ROUND_DOWN)

print(rounded_number)


# number = Decimal("1.45")
print(number)

print("Округлення за замовчуванням ROUND_HALF_EVEN:", number.quantize(Decimal("0.0")))

print(
    "Округлення вгору ROUND_HALF_UP:",
    number.quantize(Decimal("0.0"), rounding=decimal.ROUND_HALF_UP),
)

print(
    "Округлення вниз ROUND_FLOOR:",
    number.quantize(Decimal("0.0"), rounding=decimal.ROUND_FLOOR),
)

print(
    "Округлення вгору ROUND_CEILING:",
    number.quantize(Decimal("0.0"), rounding=decimal.ROUND_CEILING),
)

print(
    "Округлення до трьох десяткових знаків:",
    number.quantize(Decimal("0.000")),
)
