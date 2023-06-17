# 1D Function Integrator

This repository contains a simple Python class called `Integrator` that numerically integrates a given function `f(x)`.

## Usage

To use the `Integrator` class, follow these steps:

1. Clone the repository:

   ```shell
   git clone https://github.com/your-username/1D-Function-Integrator.git
   ```

2. Import the `Integrator` class into your Python script:

   ```python
   from integrator import Integrator
   ```

3. Define your own function to integrate, similar to the `f(x)` function provided in the example:

   ```python
   import numpy as np
   
   def f(x):
       return (x**2) * np.exp(-x) * np.sin(x)
   ```

4. Create an instance of the `Integrator` class, providing the function, minimum and maximum values for integration, and the number of intervals:

   ```python
   examp = Integrator(f, 1, 3, 200000)
   ```

   - `f`: The function to integrate.
   - `xMin`: The minimum value for integration.
   - `xMax`: The maximum value for integration.
   - `N`: The number of intervals for integration.

5. Perform the integration by calling the `integrate()` method:

   ```python
   examp.integrate()
   ```

6. Display the result by calling the `show()` method:

   ```python
   examp.show()
   ```

   This will print the rounded result of the integration.

7. Run your Python script:

   ```shell
   python your_script.py
   ```

## Example

The provided example demonstrates how to use the `Integrator` class to integrate the function `f(x) = x^2 * exp(-x) * sin(x)`:

```python
import numpy as np
from integrator import Integrator

def f(x):
    return (x**2) * np.exp(-x) * np.sin(x)

def main():
    examp = Integrator(f, 1, 3, 200000)
    examp.integrate()
    examp.show()

if __name__ == "__main__":
    main()
```

The integration is performed over the interval [1, 3] using 200,000 intervals (`N = 200000`). The result is then displayed using the `show()` method.

Feel free to modify the function and integration parameters to suit your needs.

## License

This project is licensed under the [MIT License](LICENSE).
