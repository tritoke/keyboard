#!/usr/bin/env python

from decimal import Decimal
import math


def parallel(*rs: Decimal):
    return 1 / sum(1 / r for r in rs)


beta = Decimal(3590)
r25 = Decimal(100_000)
e = Decimal(math.e)

kelvin_zero = Decimal("273.15")
t25 = kelvin_zero + 25
tl = kelvin_zero
th = kelvin_zero + 50

rtl = r25 * pow(e, beta * (1 / tl - 1 / t25))
rth = r25 * pow(e, beta * (1 / th - 1 / t25))

k1 = Decimal("0.45")
k2 = Decimal("0.8")

r1 = (rtl * rth * (k2 - k1)) / ((rtl - rth) * k1 * k2)
r2 = (rtl * rth * (k2 - k1)) / (rtl * (k1 - k1 * k2) - rth * (k2 - k1 * k2))

print("Ideal resistors:")
print(f"R1 = {round(r1 / 1000, 1)}kΩ")
print(f"R2 = {round(r2 / 1000, 1)}kΩ")

# For real resistors what values of k do we get?
r1_actual = Decimal(44_000)
r2_actual = Decimal(420_000)
print()

k1_actual = parallel(r2_actual, rtl) / (r1_actual + parallel(r2_actual, rtl))
k2_actual = parallel(r2_actual, rth) / (r1_actual + parallel(r2_actual, rth))
print("Real resistors:")
print(f"R1 = {round(r1_actual / 1000, 1)}kΩ")
print(f"R2 = {round(r2_actual / 1000, 1)}kΩ")
print(f"K1 = {round(k2_actual, 4)} (>0.45)")
print(f"K2 = {round(k1_actual, 4)} (<0.8)")
