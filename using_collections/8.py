text = "It's probably pining for the fjords!"

print(text[21:35].rfind('f'))     # 8
print(text.rfind('f', 21, 35))    # 29

# The first rfind returns 8 because it's searching within the sliced string " for the fj".
# The second rfind returns 29 because it's searching within the original string text, but constrained to the range 21 to 34. The index 29 corresponds to the last 'f' within that range in the original string.
