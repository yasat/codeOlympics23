def COMPUTERFUNCTION(x,y):
  ans = ""
  if(x%10 == y%10):
    ans = str((x//10) + (y//10)) + str((x%10))
  elif(x%10 > y%10):
    a = x%10 - y%10
    ans = str(a + (y//10)) + str(0)
  elif(x%10 < y%10):
    a = y%10 - x%10
    ans = str((y//10) - a) + str(a)

  return ans

print(COMPUTERFUNCTION(10 , 20))
print(COMPUTERFUNCTION(17 , 35))
print(COMPUTERFUNCTION(61 , 233))
