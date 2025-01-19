def safe_divide(numerator, denominator):
    """
    Perform division of numerator by denominator with error handling.

    Args:
        numerator (str): The numerator as a string (to allow for validation).
        denominator (str): The denominator as a string (to allow for validation).

    Returns:
        str: The result of the division or an appropriate error message.
    """
    try:
        # Convert inputs to floats
        num = float(numerator)
        den = float(denominator)

        # Attempt division
        if den == 0:
            return "Error: Cannot divide by zero."
        result = num / den
        return f"The result of the division is {result:.2f}"

    except ValueError:
        return "Error: Please enter numeric values only."
