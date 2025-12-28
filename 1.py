# threshold = int(input("threshold: "))
# brightness = int(input("brightness: "))



# if (brightness >= threshold):
#     print("ON")
# else:
#     print("OFF")


# x min_v max_v

# x, min_v, max_v = map(float, input().split())

# norm = (x - min_v) / (max_v - min_v)
# print(f"{norm:.2f}")

#Your tiny trainer reports a stream of loss values. Read how many values to process, then read that many losses and compute the average. If the average loss is ≤ target, print PASS; otherwise print RETRY

# Sample Input 1

# 5
# 0.40
# 0.45
# 0.42
# 0.39
# 0.41
# 0.44
# Sample Output 1

# RETRY


# n, target = map(float, input().split())
# total = 0
# for _ in range(int(n)):
#     loss = float(input())
#     total += loss
# avg = total / n
# if avg <= target:
#     print("PASS")
# else:
#     print("RETRY")