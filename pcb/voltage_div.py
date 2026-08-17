#!/usr/bin/env python

from decimal import Decimal as D


Vin = D("4.2")
Vout = D("3.0")
Z1 = D(10_000)

# Vout = (Z2 / (Z2 + Z1)) * Vin

# Vout = (Z2 / (Z2 + Z1)) * Vin

# (Vout / Vin) * (Z2 + Z1) = Z2

# A = (Vout / Vin)
A = Vout / Vin
# A * Z2 + A * Z1 = Z2

# Z2 * (A - 1) = -A * Z1
# Z2 * (1 - A) = A * Z1
# Z2 = A * Z1 / (1 - A)

Z2 = (A * Z1) / (1 - A)
print(f"Z2 = {Z2:.2f}")
