#!/usr/bin/env python3
# Created By: Patrick
# Date: 10/17/2025
# This program calculates the Surface Area and Volume of a Tetrahedron

import math

def main():
    # Ask the user for input
    edge_length = float(
        input(
            "Enter a number for the Surface Area and Volume for the Tetrahedron (in cm): "
        )
    )

    # Calculate surface area
    surface_area = math.sqrt(3) * edge_length**2

    # Calculate volume
    volume = (edge_length**3) / (6 * math.sqrt(2))

    # Shows user the final results
    print(f"The Surface Area of the Tetrahedron is: {surface_area:.2f} ")
    print(f"The Volume of the Tetrahedron is: {volume:.2f} ")


if __name__ == "__main__":
    main()
