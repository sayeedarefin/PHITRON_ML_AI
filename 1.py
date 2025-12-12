# threshold = int(input("threshold: "))
# brightness = int(input("brightness: "))



# if (brightness >= threshold):
#     print("ON")
# else:
#     print("OFF")


# x min_v max_v

x, min_v, max_v = map(float, input().split())

norm = (x - min_v) / (max_v - min_v)
print(f"{norm:.2f}")


