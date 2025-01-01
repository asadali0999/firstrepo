def greet(name: str) -> str:
    """
    Returns a greeting message.

    Parameters:
        name (str): The name to greet.
    
    Returns:
      str: A personalized greeting.
    """
    return f"Hello,{name}!"

name= greet('hina')
print(name)