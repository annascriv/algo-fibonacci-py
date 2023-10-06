def fibonacci(n):
  fibs = [0,1]
  i=0

  if n == 0:
    return 0
  elif n == 1:
    return 1
  else:
    for x in range(n):
      fibs.append(fibs[i-2]+fibs[i-1])
  print(fibs)
  return   fibs[n]

print(fibonacci(11))


