text = "dean is not nice"
words = text.split()
#print(words)
#if i %2 in words = 1:
#    print()
#    else i == 0:
#else i == 0: 
#        print(i)

max_len = max(len(word) for word in words)
box_width = max_len + 4  # padding around words for box

# Top border of the box
print("+" + "-" * (box_width - 2) + "+")

# Each word in the box
for word in words:
    print("| " + word.ljust(max_len) + " |")

# Bottom border of the box
print("+" + "-" * (box_width - 2) + "+")