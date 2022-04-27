def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
    
  return result

print("\n\nRecursion Example Results")
tri_recursion(6)

# 1 => 1+0          => 1
# 2 => 2+1+0        => 3
# 3 => 3+1+0        => 6
# 4 => 4+3+2+1+0    => 10
# 5 => 5+4+3+2+1+0  => 15
# 6 => 6+5+4+3+2+1+0=> 21