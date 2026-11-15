def compare( guess, fix):
  result = 0
  for i in range(6):
    if( guess[i] == fix[i] ):
      result += 2*3**(5-i)
    else if guess[i] in fix:
      result += 3**(5-i)
  return result
    
