#### Please add your answers to the **_Analysis of Algorithms_** exercises here.

## Exercise I

a)

<!-- a = 0
    while (a < n * n * n):
      a = a + n * n -->

O(n) - there is only one loop which does run from 0 -> n^3 but the variable is increasing by n^2 each time so it's actually probably going to run less than n times in most cases.

b)

<!-- sum = 0
    for i in range(n):
      j = 1
      while j < n:
        j *= 2
        sum += 1 -->

O(n^2) - there are nested for loops that will each run in O(n) time. So O(n) \* O(n) = O(n^2)

c)

<!-- def bunnyEars(bunnies):
      if bunnies == 0:
        return 0

      return 2 + bunnyEars(bunnies-1) -->

O(n) - this recursive loop will subtract 1 from bunnies(n) until it equals 0. Therefor the function will be called once for every bunny or O(n)

## Exercise II

n = highest story in building (provided argument)
f = highest story that egg will break when dropped (goal to calculate and return)

We can loop through the floors from 1 to n
and drop the egg from each floor until it breaks
once the egg breaks return f

def eggs(n):
for f in range(len(n)):
result = drop_egg(f) # returns True or False
if result:
return f  
 return False

This example would run in O(n) time in the worst case scenario being that the egg never breaks and we run the loop n times.

Another option to acheive O(log(n)) runtime would be to use a binary search tree method by first finding the middle floor (n // 2), then drop the egg from the middle floor. If it breaks find the mid point of the first floor to the old mid point and try again. If the egg does not break find a new mid point from the old mid to n and try again. This way we are reducing the size of n each loop.
