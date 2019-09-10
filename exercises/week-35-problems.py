def max_of_two_numbers(a,b):
    return max(a, b)

def fizz_buzz(num):
    RESULT=""
    if num % 3 == 0: RESULT+="Fizz"
    if num % 5 == 0: RESULT+="Buzz"
    return RESULT if RESULT != "" else num

def check_driving_speed(speed):
    if speed < 70: print("Ok")
    else:
        points = (speed-70)//5
        if points > 12: print("License Suspended")
        else: print("Points: "+str(points))

def showNumbers(limit):
    for i in range(limit+1):
        print(i, "EVEN") if i % 2 == 0 else print(i, "ODD")

def sum_multiples_3_and_5(max):
    multiples=[]
    for i in range(max+1):
        if i % 5 == 0 or i % 3 == 0: multiples.append(i)
    return sum(multiples)

def showStars(rows):
    for i in range(1, rows+1):
        print('*' * i)

def printing_primes(limit):
  sieve = [True] * (limit+1)
  for i in range(2, limit+1):
    if sieve[i]:
      print(i)
      for j in range(i, limit+1, i):
        sieve[j] = False

if __name__ == "__main__":
    #print(max_of_two_numbers(25,10))
    #print(fizz_buzz(15))
    #check_driving_speed(190)
    #showNumbers(3)
    #print(sum_multiples_3_and_5(20))
    #showStars(5)
    printing_primes(10)