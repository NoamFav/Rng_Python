import sympy as sp
import time

# Define symbols for the variable and the infinitesimal part
z = sp.symbols('z')
dz = sp.symbols('dz')  # Representing the derivative part ε

class DualComplexSymbolic:
    def __init__(self, real, imag=0, dual_real=0, dual_imag=0):
        self.real = real            # Real part (symbolic)
        self.imag = imag            # Imaginary part (symbolic)
        self.dual_real = dual_real  # Dual real part for derivative (symbolic)
        self.dual_imag = dual_imag  # Dual imaginary part for derivative

    def __add__(self, other):
        # Handle addition for dual complex numbers or scalars
        if isinstance(other, DualComplexSymbolic):
            return DualComplexSymbolic(
                self.real + other.real,
                self.imag + other.imag,
                self.dual_real + other.dual_real,
                self.dual_imag + other.dual_imag
            )
        else:
            # Adding a scalar to DualComplexSymbolic
            return DualComplexSymbolic(self.real + other, self.imag, self.dual_real, self.dual_imag)

    def __mul__(self, other):
        if isinstance(other, DualComplexSymbolic):
            # Multiplying two dual complex numbers
            real_part = self.real * other.real - self.imag * other.imag
            imag_part = self.real * other.imag + self.imag * other.real
            dual_real_part = (
                self.real * other.dual_real - self.imag * other.dual_imag 
                + self.dual_real * other.real - self.dual_imag * other.imag
            )
            dual_imag_part = (
                self.real * other.dual_imag + self.imag * other.dual_real 
                + self.dual_real * other.imag + self.dual_imag * other.real
            )
            return DualComplexSymbolic(real_part, imag_part, dual_real_part, dual_imag_part)
        else:
            # Multiplying DualComplexSymbolic by a scalar
            return DualComplexSymbolic(
                self.real * other, self.imag * other, 
                self.dual_real * other, self.dual_imag * other
            )

    def __rmul__(self, other):
        # Handles scalar * DualComplexSymbolic
        return self * other

    def derivative(self):
        # Returns only the dual components representing the derivative
        return f"{self.dual_real} + {self.dual_imag}i"

    def __repr__(self):
        # String representation for display
        return f"({self.real} + {self.imag}i) + ({self.dual_real} + {self.dual_imag}i)ε"

# Define a function that takes a DualComplexSymbolic and performs operations symbolically
def symbolic_differentiate(func):
    # Define z as the real part, dz as the dual part, and construct the dual complex
    z_dual = DualComplexSymbolic(real=z, dual_real=dz)
    f_z = func(z_dual)
    
    # Extract and simplify the derivative by dividing out `dz`
    derivative_z = sp.simplify(f_z.dual_real / dz)
    
    return f"f(z) = {f_z.real}, f'(z) = {derivative_z}"

# Example symbolic function
def example_func(z):
    # Define function in terms of dual complex numbers symbolically
    return z * z + 23 * z + 7 * z * z

# Compute the symbolic derivative
timer_start = time.time()
result = symbolic_differentiate(example_func)
print(result)
timer_end = time.time()

print(f"Time taken: {timer_end - timer_start:.6f} seconds")

timer_start = time.time()
result = sp.diff(example_func(z), z)
print(result)
timer_end = time.time()

print(f"Time taken: {timer_end - timer_start:.6f} seconds")
