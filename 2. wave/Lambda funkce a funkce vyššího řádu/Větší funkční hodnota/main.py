# Tuto funkci implementuj.
def max_value(f, g):
    return lambda x: f(x) if f(x) > g(x) else g(x)


# Testy:
print(max_value(lambda x: x+1, lambda x: 2*x)(-5)) # -4
# -4 > -10
print(max_value(lambda x: x+1, lambda x: 2*x)(2)) # 4
# 4 > 3
