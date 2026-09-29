# corona
import math

print("=" * 55)
print("       CORONA CALCULATION - PEEK'S FORMULA")
print("=" * 55)

try:
    # Inputs
    r = float(input("Enter conductor radius (cm): "))
    D = float(input("Enter conductor spacing (cm): "))
    m0 = float(input("Enter surface irregularity factor m0: "))
    delta = float(input("Enter air density factor δ: "))

    # Input validation
    if r <= 0 or D <= 0 or m0 <= 0 or delta <= 0:
        print("Error: All values must be greater than zero.")

    elif D <= r:
        print("Error: Conductor spacing D must be greater than radius r.")

    else:
        # Peek's formula
        critical_voltage = (
            21.1 * m0 * delta * r *
            math.log(D / r)
        )

        print("\n------------- RESULT -------------")
        print(f"Conductor radius       : {r:.2f} cm")
        print(f"Conductor spacing      : {D:.2f} cm")
        print(f"Surface factor (m0)    : {m0:.3f}")
        print(f"Air density factor (δ) : {delta:.3f}")
        print("----------------------------------")
        print(
            f"Disruptive Critical Voltage: "
            f"{critical_voltage:.2f} kV"
        )
        print("----------------------------------")

except ValueError:
    print("Error: Please enter numerical values only.")
