def clean_string(text):
  
  # Add a single-line docstring
  """Swap spaces to underscores and convert text to lowercase."""  
  
  no_spaces = text.replace(" ", "_")
  clean_text = no_spaces.lower()
  return clean_text

# Access the docstring
print(clean_string.__doc__)