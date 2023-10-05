def oxford_comma(elements):
    if len(elements) == 1:
        return elements[0]
    elif len(elements) == 2:
        return f"{elements[0]} and {elements[1]}"
    else:
        formatted_elements = ", ".join(elements[:-1])  # Join all elements except the last one with commas
        return f"{formatted_elements}, and {elements[-1]}"  # Add "and" before the last element
