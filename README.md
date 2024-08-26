this is all done with lots of practice #commented for references for future guide and understanding...
Below is the list of Python Programming Practical Questions to perform:
1. Enter any no. at runtime and creating swapping program using 3rd variable?
    2. Enter any length and width of rectangle at runtime and find out area of rectangle? explain step by step in detain in hinglish language...
    3. Enter any 5 different Subjects marks at runtime and find out aggregate marks and average? Each subjects out of 100 marks?
    4. Enter any radius of circle at runtime and find out area of circle?
    5. Enter any no. of days at runtime and find out how many years, how many months and how many remaining days?
    6. Enter any no. at runtime and find out Square?
    7. Enter any no. at runtime and find out Cube?
    8. Check whether a given number is even or odd?
    9. Check whether a given year is leap or not?
    10. WAP to find maximum between two numbers?
    11. WAP to find maximum among three numbers?
    12. WAP to check whether a triangle is Equilateral, Isosceles or     Scalene?
    13. WAP to check whether an alphabet is a vowel or consonant?
    14. WAP to calculate profit and loss on a transaction?
    15. WAP to check whether a number is positive, negative or zero?
    16. WAP to input week number and print week days?
    17. WAP to input month number and print number of days in that month?
    18. WAP to display the first 10 natural number?
    19. WAP to display natural number up to n?
    20. WAP to display the sum of first 10 natural number?
    21. WAP to display the sum of natural number up to n?
    22. WAP to print even number between 1 to 100?
    23. WAP to print odd number between 1 to 100?
    24. WAP to print sum of even number between 1 to 100?
    25. WAP to print sum of odd number between 1 to 100?
    26. WAP to find the factorial of given number?
    27. WAP to print the table of a given number?
    28. WAP to print fibbonacci series?
    29. WAP to count the digit of a given number?
    30. WAP to find first and last digit of a given number?
    31. WAP to calculate the sum of digit of a given number?
    32. WAP to calculate the product of digit of a given number?
    33. WAP to find the reverse of given number?
    34. WAP to check whether a given number is palindrome or not?
    35. WAP to check whether a given number is prime or not?

2/2

ChatGPT said:
ChatGPT
Let's start by solving the problems one by one without adding any functions and by providing detailed explanations suitable for beginners. I will begin with a few examples and explain the logic behind them in an easy-to-understand manner.

1. Enter any number at runtime and create a swapping program using a 3rd variable:
Problem Explanation:
Swapping means exchanging the values of two variables. In this problem, you will input two numbers, and then their values will be swapped using a third variable.

Code:
python
Copy code
# Step 1: Input the numbers
a = int(input("Enter the first number (a): "))
b = int(input("Enter the second number (b): "))

# Step 2: Use a third variable to swap the values
temp = a  # Save the value of 'a' in 'temp'
a = b     # Assign the value of 'b' to 'a'
b = temp  # Assign the value of 'temp' (which is the original value of 'a') to 'b'

# Step 3: Print the swapped values
print("After swapping, the value of a is:", a)
print("After swapping, the value of b is:", b)
Explanation:
Input: The program first takes two numbers a and b from the user.
Swapping:
We save the value of a in a temporary variable temp.
We assign the value of b to a.
Finally, we assign the value of temp (which holds the original value of a) to b.
Output: The values of a and b are now swapped, and the new values are printed.
2. Enter any length and width of a rectangle at runtime and find out the area of the rectangle (explained in Hinglish):
Problem Explanation:
Is problem mein hum ek rectangle ka area nikalna seekhenge. Rectangle ka area nikalne ke liye humein uski length aur width ki zaroorat hoti hai. Area ka formula hota hai length * width.

Code:
python
Copy code
# Step 1: Length aur width ko input karen
length = float(input("Rectangle ki length daaliye: "))
width = float(input("Rectangle ki width daaliye: "))

# Step 2: Area ka formula apply karen
area = length * width

# Step 3: Area ko print karen
print("Rectangle ka area hai:", area)
Explanation:
Input: Pehle hum user se rectangle ki length aur width input lete hain.
Calculation: Phir hum length aur width ko multiply karke area calculate karte hain.
Output: Lastly, hum area ko print karte hain.
3. Enter any 5 different Subjects marks at runtime and find out aggregate marks and average:
Problem Explanation:
Is problem mein humein 5 alag-alag subjects ke marks input karne hain, fir unka aggregate aur average nikalna hai. Aggregate marks ka matlab hota hai total marks aur average ka matlab hota hai average marks per subject.

Code:
python
Copy code
# Step 1: 5 subjects ke marks input karen
marks1 = int(input("Pehle subject ke marks daaliye: "))
marks2 = int(input("Dusre subject ke marks daaliye: "))
marks3 = int(input("Teesre subject ke marks daaliye: "))
marks4 = int(input("Chauthe subject ke marks daaliye: "))
marks5 = int(input("Paanchve subject ke marks daaliye: "))

# Step 2: Aggregate marks calculate karen (total marks)
aggregate = marks1 + marks2 + marks3 + marks4 + marks5

# Step 3: Average marks calculate karen
average = aggregate / 5

# Step 4: Aggregate aur average marks ko print karen
print("Aggregate marks hain:", aggregate)
print("Average marks hain:", average)
Explanation:
Input: User 5 subjects ke marks input karta hai.
Aggregate Calculation: Sabhi marks ko add karke total yaani aggregate nikalte hain.
Average Calculation: Aggregate ko 5 se divide karke average nikalte hain.
Output: Aggregate aur average dono ko print karte hain.
4. Enter any radius of the circle at runtime and find out the area of the circle:
Problem Explanation:
Is problem mein humein circle ka area nikalna hai. Circle ka area nikalne ke liye humein radius ki zaroorat hoti hai aur formula hota hai π * radius^2.

Code:
python
Copy code
# Step 1: Circle ka radius input karen
radius = float(input("Circle ka radius daaliye: "))

# Step 2: Area ka formula apply karen (π = 3.14159)
area = 3.14159 * radius * radius

# Step 3: Area ko print karen
print("Circle ka area hai:", area)
Explanation:
Input: User circle ka radius input karta hai.
Calculation: Hum π * radius^2 formula lagake area calculate karte hain.
Output: Circle ka area print karte hain.
5. Enter any number of days at runtime and find out how many years, how many months, and how many remaining days:
Problem Explanation:
Is problem mein hum given days ko years, months, aur remaining days mein convert karenge. 1 year mein 365 days hote hain aur 1 month mein 30 days hote hain (standard assumption).

Code:
python
Copy code
# Step 1: Days ko input karen
days = int(input("Kitne din hain daaliye: "))

# Step 2: Years calculate karen
years = days // 365

# Step 3: Remaining days nikal kar months calculate karen
remaining_days = days % 365
months = remaining_days // 30

# Step 4: Baaki ke days calculate karen
remaining_days = remaining_days % 30

# Step 5: Results print karen
print("Years:", years)
print("Months:", months)
print("Remaining Days:", remaining_days)
Explanation:
Input: User total days input karta hai.
Years Calculation: Total days ko 365 se divide karke years nikalte hain.
Months Calculation: Remaining days ko 30 se divide karke months nikalte hain.
Remaining Days: Jo remaining days bachte hain wo final mein print karte hain.
These examples cover basic concepts and calculations that beginners often encounter. Let me know if you'd like to continue with more problems or have any questions!





You said:
solve these problems with easy way dont add any functions and also explain the problem solved in details for beginners here is a list  6. Enter any no. at runtime and find out Square?
    7. Enter any no. at runtime and find out Cube?
    8. Check whether a given number is even or odd?
    9. Check whether a given year is leap or not?
    10. WAP to find maximum between two numbers?
    11. WAP to find maximum among three numbers?
    12. WAP to check whether a triangle is Equilateral, Isosceles or     Scalene?
    13. WAP to check whether an alphabet is a vowel or consonant?
    14. WAP to calculate profit and loss on a transaction?
    15. WAP to check whether a number is positive, negative or zero?
    16. WAP to input week number and print week days?
    17. WAP to input month number and print number of days in that month?
    18. WAP to display the first 10 natural number?
    19. WAP to display natural number up to n?
    20. WAP to display the sum of first 10 natural number?
    21. WAP to display the sum of natural number up to n?
    22. WAP to print even number between 1 to 100?
    23. WAP to print odd number between 1 to 100?
    24. WAP to print sum of even number between 1 to 100?
    25. WAP to print sum of odd number between 1 to 100?
    26. WAP to find the factorial of given number?
    27. WAP to print the table of a given number?
    28. WAP to print fibbonacci series?
    29. WAP to count the digit of a given number?
    30. WAP to find first and last digit of a given number?
    31. WAP to calculate the sum of digit of a given number?
    32. WAP to calculate the product of digit of a given number?
    33. WAP to find the reverse of given number?
    34. WAP to check whether a given number is palindrome or not?
    35. WAP to check whether a given number is prime or not? explain them in hinglish.
ChatGPT said:
ChatGPT
Memory updated
Let's solve the next set of problems step-by-step in Hinglish. I'll explain each problem in detail to make it easy for beginners to understand.

6. Enter any number at runtime and find out the Square:
Problem Explanation:
Is problem mein humein ek number ka square nikalna hai. Square ka matlab hota hai kisi number ko khud se multiply karna, jaise number * number.

Code:
python
Copy code
# Step 1: Number ko input karen
num = int(input("Koi bhi number daaliye: "))

# Step 2: Square calculate karen
square = num * num

# Step 3: Square ko print karen
print("Is number ka square hai:", square)
Explanation:
Input: User se ek number input lete hain.
Calculation: Us number ko khud se multiply karke square nikalte hain.
Output: Square ko print karte hain.
7. Enter any number at runtime and find out the Cube:
Problem Explanation:
Cube ka matlab hota hai kisi number ko teen baar multiply karna, jaise number * number * number.

Code:
python
Copy code
# Step 1: Number ko input karen
num = int(input("Koi bhi number daaliye: "))

# Step 2: Cube calculate karen
cube = num * num * num

# Step 3: Cube ko print karen
print("Is number ka cube hai:", cube)
Explanation:
Input: User se ek number input lete hain.
Calculation: Us number ko teen baar multiply karke cube nikalte hain.
Output: Cube ko print karte hain.
8. Check whether a given number is even or odd:
Problem Explanation:
Is problem mein humein check karna hai ki diya gaya number even hai ya odd. Agar ek number ko 2 se divide karne par remainder 0 aata hai, toh wo even hota hai, warna odd hota hai.

Code:
python
Copy code
# Step 1: Number ko input karen
num = int(input("Koi bhi number daaliye: "))

# Step 2: Even ya odd check karen
if num % 2 == 0:
    print(num, "even hai.")
else:
    print(num, "odd hai.")
Explanation:
Input: User se ek number input lete hain.
Check: Number ko 2 se divide karke remainder check karte hain.
Output: Agar remainder 0 hai toh even print karte hain, warna odd.
9. Check whether a given year is leap or not:
Problem Explanation:
Leap year wo hota hai jo 4 se divide hota hai aur 100 se divide nahi hota, ya phir 400 se divide hota hai. Is logic ke according humein year ko check karna hai.

Code:
python
Copy code
# Step 1: Year ko input karen
year = int(input("Koi bhi year daaliye: "))

# Step 2: Leap year check karen
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(year, "leap year hai.")
else:
    print(year, "leap year nahi hai.")
Explanation:
Input: User se ek year input lete hain.
Check: Year ko 4, 100, aur 400 se divide karke conditions check karte hain.
Output: Agar conditions match hoti hain toh leap year print karte hain, warna nahi.
10. WAP to find maximum between two numbers:
Problem Explanation:
Is problem mein humein do numbers ke beech maximum number find out karna hai.

Code:
python
Copy code
# Step 1: Do numbers ko input karen
num1 = int(input("Pehla number daaliye: "))
num2 = int(input("Dusra number daaliye: "))

# Step 2: Maximum check karen
if num1 > num2:
    print("Maximum number hai:", num1)
else:
    print("Maximum number hai:", num2)
Explanation:
Input: User se do numbers input lete hain.
Check: Dono numbers ko compare karte hain.
Output: Jo number bada hota hai wo print karte hain.
11. WAP to find maximum among three numbers:
Problem Explanation:
Is problem mein humein teen numbers ke beech maximum number find out karna hai.

Code:
python
Copy code
# Step 1: Teen numbers ko input karen
num1 = int(input("Pehla number daaliye: "))
num2 = int(input("Dusra number daaliye: "))
num3 = int(input("Teesra number daaliye: "))

# Step 2: Maximum check karen
if num1 > num2 and num1 > num3:
    print("Maximum number hai:", num1)
elif num2 > num3:
    print("Maximum number hai:", num2)
else:
    print("Maximum number hai:", num3)
Explanation:
Input: User se teen numbers input lete hain.
Check: Pehle num1 ko compare karte hain, fir num2 ko.
Output: Jo number sabse bada hota hai wo print karte hain.
12. WAP to check whether a triangle is Equilateral, Isosceles, or Scalene:
Problem Explanation:
Triangle ko hum uske sides ke base par categorize kar sakte hain:

Equilateral: Jismein teeno sides barabar hoti hain.
Isosceles: Jismein do sides barabar hoti hain.
Scalene: Jismein teeno sides alag hoti hain.
Code:
python
Copy code
# Step 1: Triangle ki teen sides ko input karen
side1 = int(input("Pehli side daaliye: "))
side2 = int(input("Dusri side daaliye: "))
side3 = int(input("Teesri side daaliye: "))

# Step 2: Triangle type check karen
if side1 == side2 == side3:
    print("Ye Equilateral triangle hai.")
elif side1 == side2 or side2 == side3 or side1 == side3:
    print("Ye Isosceles triangle hai.")
else:
    print("Ye Scalene triangle hai.")
Explanation:
Input: User se triangle ki teen sides input karte hain.
Check: Sides ko compare karke triangle ka type determine karte hain.
Output: Jo type match karta hai wo print karte hain.
Let me know if you'd like to continue with more problems or need any further clarification!





You said:
solve these problems with easy way dont add any functions and also explain the problem solved in details for beginners here is a list ---- 13. WAP to check whether an alphabet is a vowel or consonant?
    14. WAP to calculate profit and loss on a transaction?
    15. WAP to check whether a number is positive, negative or zero?
    16. WAP to input week number and print week days?
    17. WAP to input month number and print number of days in that month?
    18. WAP to display the first 10 natural number?
    19. WAP to display natural number up to n?
    20. WAP to display the sum of first 10 natural number?
    21. WAP to display the sum of natural number up to n?
    22. WAP to print even number between 1 to 100?
    23. WAP to print odd number between 1 to 100?
    24. WAP to print sum of even number between 1 to 100?
    25. WAP to print sum of odd number between 1 to 100?
    26. WAP to find the factorial of given number?
    27. WAP to print the table of a given number?
    28. WAP to print fibbonacci series?
    29. WAP to count the digit of a given number?
    30. WAP to find first and last digit of a given number?
    31. WAP to calculate the sum of digit of a given number?
    32. WAP to calculate the product of digit of a given number?
    33. WAP to find the reverse of given number?
    34. WAP to check whether a given number is palindrome or not?
    35. WAP to check whether a given number is prime or not? explain in hinglish.
ChatGPT said:
ChatGPT
Chaliye, agle set of problems ko step-by-step solve karte hain aur unhe detail mein Hinglish mein samajhte hain.

13. WAP to check whether an alphabet is a vowel or consonant:
Problem Explanation:
Is problem mein humein ek alphabet input karna hai aur check karna hai ki wo vowel hai ya consonant. Vowels hain: a, e, i, o, u (chhote aur bade letters dono).

Code:
python
Copy code
# Step 1: Alphabet ko input karen
ch = input("Koi bhi alphabet daaliye: ")

# Step 2: Vowel ya consonant check karen
if ch in ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'):
    print(ch, "vowel hai.")
else:
    print(ch, "consonant hai.")
Explanation:
Input: User se ek alphabet input karte hain.
Check: Alphabet ko vowels ke group se compare karte hain.
Output: Agar alphabet vowel hai toh print karte hain, warna consonant print karte hain.
14. WAP to calculate profit and loss on a transaction:
Problem Explanation:
Is problem mein humein profit ya loss calculate karna hai. Agar selling price (SP) zyada hai cost price (CP) se, toh profit hota hai. Agar selling price kam hai cost price se, toh loss hota hai.

Code:
python
Copy code
# Step 1: Cost price aur selling price ko input karen
cp = float(input("Cost price daaliye: "))
sp = float(input("Selling price daaliye: "))

# Step 2: Profit ya loss check karen
if sp > cp:
    profit = sp - cp
    print("Profit hua:", profit)
elif cp > sp:
    loss = cp - sp
    print("Loss hua:", loss)
else:
    print("Na profit, na loss.")
Explanation:
Input: Cost price aur selling price input lete hain.
Check: SP aur CP ko compare karte hain.
Output: Agar SP zyada hai toh profit print karte hain, warna loss. Agar dono equal hain, toh "No profit, no loss."
15. WAP to check whether a number is positive, negative or zero:
Problem Explanation:
Is problem mein humein check karna hai ki diya gaya number positive hai, negative hai, ya zero hai.

Code:
python
Copy code
# Step 1: Number ko input karen
num = float(input("Koi bhi number daaliye: "))

# Step 2: Positive, negative ya zero check karen
if num > 0:
    print(num, "positive number hai.")
elif num < 0:
    print(num, "negative number hai.")
else:
    print(num, "zero hai.")
Explanation:
Input: User se ek number input lete hain.
Check: Number ko 0 ke saath compare karte hain.
Output: Agar number 0 se bada hai toh positive print karte hain, agar chhota hai toh negative, aur agar equal hai toh zero.
16. WAP to input week number and print week days:
Problem Explanation:
Is problem mein humein ek week number (1-7) input karna hai aur uske corresponding week day ka naam print karna hai.

Code:
python
Copy code
# Step 1: Week number ko input karen
week_num = int(input("Week number (1-7) daaliye: "))

# Step 2: Week day ko print karen
if week_num == 1:
    print("Monday")
elif week_num == 2:
    print("Tuesday")
elif week_num == 3:
    print("Wednesday")
elif week_num == 4:
    print("Thursday")
elif week_num == 5:
    print("Friday")
elif week_num == 6:
    print("Saturday")
elif week_num == 7:
    print("Sunday")
else:
    print("Invalid week number!")
Explanation:
Input: User se ek week number (1-7) input lete hain.
Check: Week number ke basis par corresponding day print karte hain.
Output: Agar number 1-7 ke beech hai, toh us din ka naam print hota hai, warna invalid week number print hota hai.
17. WAP to input month number and print number of days in that month:
Problem Explanation:
Is problem mein humein ek month number (1-12) input karna hai aur us month mein kitne days hote hain wo print karna hai.

Code:
python
Copy code
# Step 1: Month number ko input karen
month_num = int(input("Month number (1-12) daaliye: "))

# Step 2: Days ko print karen
if month_num == 1 or month_num == 3 or month_num == 5 or month_num == 7 or month_num == 8 or month_num == 10 or month_num == 12:
    print("31 days")
elif month_num == 4 or month_num == 6 or month_num == 9 or month_num == 11:
    print("30 days")
elif month_num == 2:
    print("28 ya 29 days (leap year par depend karta hai)")
else:
    print("Invalid month number!")
Explanation:
Input: User se ek month number (1-12) input lete hain.
Check: Month ke hisaab se usme kitne din hain wo print karte hain.
Output: Agar month 1-12 ke beech hai, toh us month ke din print karte hain, warna invalid month number print karte hain.
18. WAP to display the first 10 natural numbers:
Problem Explanation:
Is problem mein humein pehle 10 natural numbers ko print karna hai. Natural numbers start hote hain 1 se.

Code:
python
Copy code
# Step 1: Loop use karke 1 se 10 tak ke numbers print karen
for i in range(1, 11):
    print(i)
Explanation:
Loop: Ek loop chalate hain jo 1 se 10 tak ke numbers ko print kare.
Output: 1 se 10 tak ke sabhi numbers print ho jaate hain.
19. WAP to display natural numbers up to n:
Problem Explanation:
Is problem mein humein n tak ke natural numbers print karna hai, jahan n user se input lete hain.

Code:
python
Copy code
# Step 1: n ko input karen
n = int(input("n ka value daaliye: "))

# Step 2: Loop use karke 1 se n tak ke numbers print karen
for i in range(1, n + 1):
    print(i)
Explanation:
Input: User se n value input lete hain.
Loop: Ek loop chalate hain jo 1 se n tak ke numbers ko print kare.
Output: 1 se n tak ke sabhi numbers print ho jaate hain.
Chaliye, yeh problems solve karte hain, aur agar aapko aur questions hain toh bataiye!





You said:
olve these problems with easy way dont add any functions and also explain the problem solved in details for beginners here is a list  20. WAP to display the sum of first 10 natural number?
    21. WAP to display the sum of natural number up to n?
    22. WAP to print even number between 1 to 100?
    23. WAP to print odd number between 1 to 100?
    24. WAP to print sum of even number between 1 to 100?
    25. WAP to print sum of odd number between 1 to 100?
    26. WAP to find the factorial of given number?
    27. WAP to print the table of a given number?
    28. WAP to print fibbonacci series?
    29. WAP to count the digit of a given number?
    30. WAP to find first and last digit of a given number?
    31. WAP to calculate the sum of digit of a given number? explain them for beginners in hinglish
ChatGPT said:
ChatGPT
Memory updated
Chaliye, ab in questions ko step-by-step solve karte hain aur beginners ke liye Hinglish mein samajhte hain.

20. WAP to display the sum of first 10 natural numbers:
Problem Explanation:
Is problem mein humein pehle 10 natural numbers ka sum calculate karna hai. Natural numbers start hote hain 1 se, aur humein 1 se 10 tak ke numbers ka sum nikalna hai.

Code:
python
Copy code
# Step 1: Sum ko initialize karen
sum = 0

# Step 2: Loop use karke 1 se 10 tak ke numbers ka sum calculate karen
for i in range(1, 11):
    sum += i  # sum = sum + i

# Step 3: Sum ko print karen
print("Pehle 10 natural numbers ka sum hai:", sum)
Explanation:
Initialize: Sum ko 0 se initialize karte hain.
Loop: 1 se 10 tak loop chalate hain aur har number ko sum mein add karte jaate hain.
Output: Final sum ko print karte hain.
21. WAP to display the sum of natural numbers up to n:
Problem Explanation:
Is problem mein humein n tak ke natural numbers ka sum calculate karna hai. N ka value user se input lete hain.

Code:
python
Copy code
# Step 1: n ka value input karen
n = int(input("n ka value daaliye: "))

# Step 2: Sum ko initialize karen
sum = 0

# Step 3: Loop use karke 1 se n tak ke numbers ka sum calculate karen
for i in range(1, n + 1):
    sum += i  # sum = sum + i

# Step 4: Sum ko print karen
print("1 se", n, "tak ke natural numbers ka sum hai:", sum)
Explanation:
Input: User se n ka value lete hain.
Initialize: Sum ko 0 se initialize karte hain.
Loop: 1 se n tak loop chalate hain aur har number ko sum mein add karte hain.
Output: Final sum ko print karte hain.
22. WAP to print even numbers between 1 to 100:
Problem Explanation:
Is problem mein humein 1 se 100 tak ke even numbers print karne hain. Even numbers wo hote hain jo 2 se completely divide ho jaate hain.

Code:
python
Copy code
# Step 1: Loop use karke 1 se 100 tak ke even numbers print karen
for i in range(1, 101):
    if i % 2 == 0:  # Agar number 2 se completely divide ho raha hai, toh wo even hai
        print(i)
Explanation:
Loop: 1 se 100 tak loop chalate hain.
Check: Har number ko 2 se divide karte hain aur check karte hain ki remainder 0 hai ya nahi. Agar 0 hai, toh number even hai.
Output: Even numbers ko print karte hain.
23. WAP to print odd numbers between 1 to 100:
Problem Explanation:
Is problem mein humein 1 se 100 tak ke odd numbers print karne hain. Odd numbers wo hote hain jo 2 se completely divide nahi hote.

Code:
python
Copy code
# Step 1: Loop use karke 1 se 100 tak ke odd numbers print karen
for i in range(1, 101):
    if i % 2 != 0:  # Agar number 2 se completely divide nahi ho raha hai, toh wo odd hai
        print(i)
Explanation:
Loop: 1 se 100 tak loop chalate hain.
Check: Har number ko 2 se divide karte hain aur check karte hain ki remainder 0 nahi hai. Agar 0 nahi hai, toh number odd hai.
Output: Odd numbers ko print karte hain.
24. WAP to print sum of even numbers between 1 to 100:
Problem Explanation:
Is problem mein humein 1 se 100 tak ke even numbers ka sum calculate karna hai.

Code:
python
Copy code
# Step 1: Sum ko initialize karen
sum = 0

# Step 2: Loop use karke 1 se 100 tak ke even numbers ka sum calculate karen
for i in range(1, 101):
    if i % 2 == 0:  # Agar number 2 se completely divide ho raha hai, toh wo even hai
        sum += i  # sum = sum + i

# Step 3: Sum ko print karen
print("1 se 100 tak ke even numbers ka sum hai:", sum)
Explanation:
Initialize: Sum ko 0 se initialize karte hain.
Loop: 1 se 100 tak loop chalate hain aur even numbers ko sum mein add karte hain.
Output: Final sum ko print karte hain.
25. WAP to print sum of odd numbers between 1 to 100:
Problem Explanation:
Is problem mein humein 1 se 100 tak ke odd numbers ka sum calculate karna hai.

Code:
python
Copy code
# Step 1: Sum ko initialize karen
sum = 0

# Step 2: Loop use karke 1 se 100 tak ke odd numbers ka sum calculate karen
for i in range(1, 101):
    if i % 2 != 0:  # Agar number 2 se completely divide nahi ho raha hai, toh wo odd hai
        sum += i  # sum = sum + i

# Step 3: Sum ko print karen
print("1 se 100 tak ke odd numbers ka sum hai:", sum)
Explanation:
Initialize: Sum ko 0 se initialize karte hain.
Loop: 1 se 100 tak loop chalate hain aur odd numbers ko sum mein add karte hain.
Output: Final sum ko print karte hain.
26. WAP to find the factorial of given number:
Problem Explanation:
Is problem mein humein kisi bhi given number ka factorial calculate karna hai. Factorial ka matlab hota hai us number se chhote ya barabar sabhi numbers ka product.

Code:
python
Copy code
# Step 1: Number input karen
n = int(input("Kisi number ka factorial nikalne ke liye number daaliye: "))

# Step 2: Factorial ko initialize karen
factorial = 1

# Step 3: Loop use karke factorial calculate karen
for i in range(1, n + 1):
    factorial *= i  # factorial = factorial * i

# Step 4: Factorial ko print karen
print("Factorial of", n, "hai:", factorial)
Explanation:
Input: User se number input lete hain.
Initialize: Factorial ko 1 se initialize karte hain.
Loop: 1 se n tak loop chalate hain aur har number se factorial ko multiply karte hain.
Output: Final factorial ko print karte hain.
27. WAP to print the table of a given number:
Problem Explanation:
Is problem mein humein kisi bhi given number ka multiplication table print karna hai.

Code:
python
Copy code
# Step 1: Number input karen
n = int(input("Kisi number ka table print karne ke liye number daaliye: "))

# Step 2: Loop use karke table print karen
for i in range(1, 11):
    print(n, "x", i, "=", n * i)
Explanation:
Input: User se number input lete hain.
Loop: 1 se 10 tak loop chalate hain aur har step pe us number ko current loop number se multiply karte hain.
Output: Multiplication table ko print karte hain.
28. WAP to print Fibonacci series:
Problem Explanation:
Is problem mein humein Fibonacci series print karna hai. Fibonacci series mein har number previous do numbers ka sum hota hai. Series start hoti hai 0 aur 1 se.

Code:
python
Copy code
# Step 1: Number of terms input karen
n = int(input("Kitne terms chahiye Fibonacci series mein: "))

# Step 2: First two terms initialize karen
a, b = 0, 1

# Step 3: Loop use karke Fibonacci series print karen
print(a)
print(b)
for i in range(2, n):
    c = a + b
    print(c)
    a = b
    b = c
Explanation:
Input: User se terms ka number input lete hain.
Initialize: Pehle do terms ko 0 aur 1 set karte hain.
Loop: Loop chalate hain jo har term ko previous do terms ke sum ke barabar set karta hai.
Output: Har step pe naya number print karte hain.
29. **WAP to count




You said:
solve these problems with easy way dont add any functions and also explain the problem solved in details for beginners here is a list  20. WAP to display the sum of first 10 natural number? 29. WAP to count the digit of a given number?
    30. WAP to find first and last digit of a given number?
    31. WAP to calculate the sum of digit of a given number?
    32. WAP to calculate the product of digit of a given number?
    33. WAP to find the reverse of given number? also explain  them n detail for beginners  in hinglish
    34. WAP to check whether a given number is palindrome or not?
    35. WAP to check whether a given number is prime or not? 

2/2

ChatGPT said:
ChatGPT
Chaliye, in problems ko detail mein samajhte hain aur step-by-step code likhte hain. Main sab kuch Hinglish mein samjhaunga, taaki beginners ke liye aasaan ho.

20. WAP to display the sum of first 10 natural numbers:
Problem Explanation:
Is problem mein humein pehle 10 natural numbers ka sum calculate karna hai. Natural numbers 1 se start hote hain, toh humein 1 se 10 tak ke numbers ka sum nikalna hai.

Code:
python
Copy code
# Step 1: Sum ko initialize karen
sum = 0

# Step 2: Loop use karke 1 se 10 tak ke numbers ka sum calculate karen
for i in range(1, 11):
    sum += i  # sum = sum + i

# Step 3: Sum ko print karen
print("Pehle 10 natural numbers ka sum hai:", sum)
Explanation:
Initialize: Sum ko 0 se initialize karte hain.
Loop: 1 se 10 tak loop chalate hain aur har number ko sum mein add karte jaate hain.
Output: Final sum ko print karte hain.
29. WAP to count the digits of a given number:
Problem Explanation:
Is problem mein humein kisi bhi given number ke digits ki ginti karni hai. Example ke liye, agar number 1234 hai, toh uske 4 digits hain.

Code:
python
Copy code
# Step 1: Number input karen
n = int(input("Kisi number ko daliye: "))

# Step 2: Digit count karne ke liye counter ko initialize karen
count = 0

# Step 3: Loop tab tak chale jab tak number 0 nahi ho jaata
while n > 0:
    n = n // 10  # Number ko 10 se divide karte jaate hain, last digit remove hoti hai
    count += 1  # Har baar count badhata hai

# Step 4: Digit count ko print karen
print("Digits ki total ginti hai:", count)
Explanation:
Input: User se number input lete hain.
Initialize: Digit count ko 0 se initialize karte hain.
Loop: Loop tab tak chalate hain jab tak number 0 nahi ho jaata. Har iteration mein, number ko 10 se divide karte hain aur last digit ko remove karte hain.
Output: Final digit count ko print karte hain.
30. WAP to find the first and last digit of a given number:
Problem Explanation:
Is problem mein humein kisi number ki pehli aur aakhri digit find karni hai. Example: 1234 mein pehli digit 1 hai aur aakhri digit 4 hai.

Code:
python
Copy code
# Step 1: Number input karen
n = int(input("Kisi number ko daliye: "))

# Step 2: Last digit find karen
last_digit = n % 10  # Modulo 10 se last digit milti hai

# Step 3: First digit find karne ke liye loop chalate hain
while n >= 10:
    n = n // 10  # Number ko 10 se divide karte hain, taaki first digit last bachi rahe

# Step 4: First digit n mein bachi hoti hai
first_digit = n

# Step 5: Pehli aur aakhri digit ko print karen
print("Pehli digit hai:", first_digit)
print("Aakhri digit hai:", last_digit)
Explanation:
Input: User se number input lete hain.
Last Digit: Modulo 10 use karke last digit find karte hain.
First Digit: Loop chalate hain aur number ko tab tak 10 se divide karte hain jab tak single digit nahi bachti.
Output: First aur last digit ko print karte hain.
31. WAP to calculate the sum of digits of a given number:
Problem Explanation:
Is problem mein humein kisi number ke digits ka sum nikalna hai. Example: 1234 ka sum 1+2+3+4 = 10 hota hai.

Code:
python
Copy code
# Step 1: Number input karen
n = int(input("Kisi number ko daliye: "))

# Step 2: Sum ko initialize karen
sum = 0

# Step 3: Loop tab tak chale jab tak number 0 nahi ho jaata
while n > 0:
    digit = n % 10  # Last digit nikalte hain
    sum += digit  # Sum mein add karte hain
    n = n // 10  # Last digit remove karte hain

# Step 4: Sum ko print karen
print("Digits ka sum hai:", sum)
Explanation:
Input: User se number input lete hain.
Initialize: Sum ko 0 se initialize karte hain.
Loop: Last digit ko modulo 10 se nikalte hain aur usko sum mein add karte hain. Phir number ko 10 se divide karke last digit ko remove karte hain.
Output: Final sum ko print karte hain.
32. WAP to calculate the product of digits of a given number:
Problem Explanation:
Is problem mein humein kisi number ke digits ka product nikalna hai. Example: 1234 ka product 1x2x3x4 = 24 hota hai.

Code:
python
Copy code
# Step 1: Number input karen
n = int(input("Kisi number ko daliye: "))

# Step 2: Product ko initialize karen
product = 1

# Step 3: Loop tab tak chale jab tak number 0 nahi ho jaata
while n > 0:
    digit = n % 10  # Last digit nikalte hain
    product *= digit  # Product mein multiply karte hain
    n = n // 10  # Last digit remove karte hain

# Step 4: Product ko print karen
print("Digits ka product hai:", product)
Explanation:
Input: User se number input lete hain.
Initialize: Product ko 1 se initialize karte hain.
Loop: Last digit ko modulo 10 se nikalte hain aur usko product mein multiply karte hain. Phir number ko 10 se divide karke last digit ko remove karte hain.
Output: Final product ko print karte hain.
33. WAP to find the reverse of a given number:
Problem Explanation:
Is problem mein humein kisi given number ka reverse find karna hai. Example: 1234 ka reverse 4321 hota hai.

Code:
python
Copy code
# Step 1: Number input karen
n = int(input("Kisi number ko daliye: "))

# Step 2: Reverse number ko initialize karen
reverse = 0

# Step 3: Loop tab tak chale jab tak number 0 nahi ho jaata
while n > 0:
    digit = n % 10  # Last digit nikalte hain
    reverse = reverse * 10 + digit  # Reverse ko update karte hain
    n = n // 10  # Last digit remove karte hain

# Step 4: Reverse number ko print karen
print("Number ka reverse hai:", reverse)
Explanation:
Input: User se number input lete hain.
Initialize: Reverse number ko 0 se initialize karte hain.
Loop: Last digit ko modulo 10 se nikalte hain aur usko reverse mein update karte hain (previous reverse ko 10 se multiply karna aur phir digit ko add karna).
Output: Final reversed number ko print karte hain.
34. WAP to check whether a given number is palindrome or not:
Problem Explanation:
Is problem mein humein check karna hai ki given number palindrome hai ya nahi. Palindrome wo number hota hai jo reverse hone par bhi same rahta hai. Example: 121, 12321.

Code:
python
Copy code
# Step 1: Number input karen
n = int(input("Kisi number ko daliye: "))

# Step 2: Original number ko store karen
original = n

# Step 3: Reverse number ko calculate karen
reverse = 0
while n > 0:
    digit = n % 10  # Last digit nikalte hain
    reverse = reverse * 10 + digit  # Reverse ko update karte hain
    n = n // 10  # Last digit remove karte hain

# Step 4: Check karen original number aur reverse number equal hain ya nahi
if original == reverse:
    print(original, "ek palindrome number hai.")
else:
    print(original, "ek palindrome number nahi hai.")
Explanation:
Input: User se number input lete hain.
Original Number: Original number ko store karte hain taaki baad mein compare kar sakein.
Reverse Calculation: Number ka reverse find karte hain.
Check: Original aur reverse number ko compare karte hain. Agar equal hain, toh number palindrome hai; warna nahi.
35. WAP to check whether a given number is prime or not:
Problem Explanation:
Is problem mein humein check karna hai ki given number prime hai ya nahi. Prime number wo hota hai jo sirf 1 aur apne aap se divide hota hai. Example: 2, 3, 5, 7.

Code:
python
Copy code
# Step 1: Number input karen
n = int(input("Kisi number ko daliye: "))

# Step 2: Prime flag ko initialize karen
is_prime = True

# Step 3: Loop 2 se lekar sqrt(n) tak chale (basic optimization)
if n > 1:
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:  # Agar divisible hai toh prime nahi hai
            is_prime = False
            break
else:
    is_prime = False  # 1 aur usse chhote numbers prime nahi hote

# Step 4: Check karen aur output den
if is_prime:
    print(n, "ek prime number hai.")
else:
    print(n, "ek prime number nahi hai.")
Explanation:
Input: User se number input lete hain.
Prime Flag: Prime hone ka assumption karte hain (True).
Loop: 2 se lekar sqrt(n) tak loop chalate hain. Agar number kisi bhi divisor se divide hota hai, toh wo prime nahi hai.
Check: Agar prime flag True hai, toh number prime hai; warna nahi.
Ye saari problems beginners ke liye explain ki gayi hain, jisse unhe Python mein coding kaise karna hai, yeh samajh aayega.





You said:
prime number or not find karne ke liye true false kyu liya
ChatGPT said:
ChatGPT
Prime number check karne ke liye True aur False ka use karne ka reason yeh hai ki humein yeh decide karna hota hai ki number prime hai ya nahi. True aur False boolean values hain, jo humein condition ko track karne mein madad karte hain. Chaliye, detail mein samajhte hain:

Prime Number Check Process:
Prime Number Definition: Prime number wo hota hai jo sirf 1 aur apne aap se divide hota hai. Example ke liye, 2, 3, 5, 7 yeh saare prime numbers hain. Iska matlab hai ki agar ek number 2 ya usse zyada different numbers se divide hota hai (excluding 1 and the number itself), toh wo prime nahi hai.

Boolean Flag ka Use:

Hum initially assume karte hain ki number prime hai, isliye is_prime ko True set karte hain.
Agar loop mein humein aisa divisor milta hai jo given number ko divide kar sakta hai, toh is_prime ko False set kar dete hain, kyunki wo number prime nahi hai.
Example with Code:
Maan lijiye hum check kar rahe hain ki 29 prime hai ya nahi.

Code Explanation:
python
Copy code
n = 29  # Humne 29 ko check karna hai
is_prime = True  # Initially hum maan rahe hain ki 29 prime hai

# Loop chalate hain 2 se lekar sqrt(29) tak
for i in range(2, int(n**0.5) + 1):
    if n % i == 0:  # Agar koi bhi i 29 ko divide kar sakta hai
        is_prime = False  # Toh 29 prime nahi hai
        break  # Loop ko yahin rok dete hain

# Check karte hain prime flag
if is_prime:
    print(n, "ek prime number hai.")
else:
    print(n, "ek prime number nahi hai.")
Why True or False?
Initialization (True): is_prime = True ka matlab hai ki hum initially assume kar rahe hain ki number prime hai.
Condition Check (False): Loop mein agar humein koi aisa divisor milta hai jo number ko divide kar sakta hai, toh hum is_prime = False set karte hain. Iska matlab hai ki humne proof pa liya hai ki number prime nahi hai.
Final Output:
Agar is_prime True hai, toh number prime hai.
Agar is_prime False hai, toh number prime nahi hai.
Conclusion:
True aur False ka use karne se code clean aur easily understandable hota hai. Is method se hum efficiently check kar sakte hain ki given number prime hai ya nahi, bina unnecessary calculations ke.





You said:
you have been mastered into python now hemp me understand ---explain the logic behind all 35 exercises performed in python explain them in hinglish 
ChatGPT said:
ChatGPT
Certainly! Main aapko Python ke 35 exercises ka logic step-by-step Hinglish mein explain karta hoon. Yeh explanations aapko basic concepts ko samajhne mein help karengi aur coding ke tareeke ko easy banayengi.

1. Swapping Two Numbers Using a Third Variable:
Logic: Hum third variable ka use karke do numbers ko swap karte hain. Maan lo a = 5 aur b = 10. Ek temporary variable temp bana kar a ki value usme store kar lete hain, phir b ki value a mein daal dete hain aur temp ki value b mein daal dete hain. Isse dono numbers ki jagah swap ho jaati hai.
2. Calculate Area of a Rectangle:
Logic: Rectangle ka area length * width se nikalta hai. User se length aur width le kar unko multiply kar dete hain.
3. Aggregate and Average of 5 Subjects:
Logic: 5 subjects ke marks input le kar unko sum kar dete hain. Average nikalne ke liye sum ko 5 se divide kar dete hain.
4. Calculate Area of a Circle:
Logic: Circle ka area π * r^2 se nikalta hai. Yahaan π ki value 3.14 assume karte hain, aur r radius hoti hai.
5. Convert Days into Years, Months, and Remaining Days:
Logic: Pehle total days ko 365 se divide karke years nikal lete hain, phir bache hue days ko 30 se divide karke months, aur jo remaining days bachte hain unhe calculate kar lete hain.
6. Find the Square of a Number:
Logic: Kisi number ka square usse n * n ya n**2 karke nikalte hain.
7. Find the Cube of a Number:
Logic: Kisi number ka cube n * n * n ya n**3 karke nikalte hain.
8. Check Whether a Number is Even or Odd:
Logic: Agar number ko 2 se divide karne par remainder 0 aata hai toh wo even hai, warna odd hai. Iske liye modulus operator % ka use karte hain.
9. Check Whether a Year is Leap Year or Not:
Logic: Leap year wahi hota hai jo 4 se divide hota ho, lekin 100 se divisible nahi ho, ya 400 se divisible ho. Isko check karne ke liye if-else conditions use karte hain.
10. Find Maximum Between Two Numbers:
Logic: Simple if-else condition laga kar compare karte hain ki kaunsa number bada hai.
11. Find Maximum Among Three Numbers:
Logic: Yahan hum nested if-else conditions ka use karte hain. Pehle do numbers ko compare karte hain, phir result ko teesre number se compare karte hain.
12. Check Triangle Type (Equilateral, Isosceles, Scalene):
Logic: Equilateral triangle ke teeno sides equal hote hain, Isosceles ke do sides equal hote hain, aur Scalene ke teeno sides different hote hain. Sides ko compare karke type decide karte hain.
13. Check Whether an Alphabet is a Vowel or Consonant:
Logic: Alphabets a, e, i, o, u vowels hain aur baaki sab consonants. User se input le kar usko check karte hain ki yeh vowels mein se hai ya nahi.
14. Calculate Profit and Loss on a Transaction:
Logic: Cost price (CP) aur Selling price (SP) ko compare karke check karte hain. Agar SP > CP hai toh profit hoga, warna loss hoga. Profit/Loss ka amount SP-CP ya CP-SP karke nikalte hain.
15. Check Whether a Number is Positive, Negative, or Zero:
Logic: If-else conditions laga kar check karte hain ki number 0 se bada hai toh positive, 0 se chhota hai toh negative, aur agar 0 hai toh simply zero hai.
16. Input Week Number and Print Week Day:
Logic: Week number (1-7) ko input le kar switch-case ya if-elif-else se uske corresponding day ko print karte hain.
17. Input Month Number and Print Number of Days in that Month:
Logic: Month number (1-12) ko input le kar switch-case ya if-elif-else se us month mein kitne days hote hain, wo print karte hain. Special case February ka hota hai jo leap year mein 29 days ka hota hai.
18. Display First 10 Natural Numbers:
Logic: Simple loop (1 to 10) tak chalakar natural numbers ko print kar dete hain.
19. Display Natural Numbers up to n:
Logic: User se input le kar 1 se n tak loop chalakar numbers ko print karte hain.
20. Display Sum of First 10 Natural Numbers:
Logic: Loop (1 to 10) tak chalate hain aur sum variable mein sab numbers ka sum calculate karte hain.
21. Display Sum of Natural Numbers up to n:
Logic: User se input le kar loop (1 to n) tak chalakar sum variable mein total sum calculate karte hain.
22. Print Even Numbers Between 1 to 100:
Logic: Loop 1 se 100 tak chalakar % 2 == 0 condition se even numbers ko print karte hain.
23. Print Odd Numbers Between 1 to 100:
Logic: Loop 1 se 100 tak chalakar % 2 != 0 condition se odd numbers ko print karte hain.
24. Print Sum of Even Numbers Between 1 to 100:
Logic: Loop 1 se 100 tak chalakar % 2 == 0 condition se even numbers ka sum calculate karte hain.
25. Print Sum of Odd Numbers Between 1 to 100:
Logic: Loop 1 se 100 tak chalakar % 2 != 0 condition se odd numbers ka sum calculate karte hain.
26. Find the Factorial of a Given Number:
Logic: Factorial ka matlab hai n!, jisme 1 se n tak sab numbers ko multiply karte hain. Loop chalakar product calculate karte hain.
27. Print the Table of a Given Number:
Logic: User se input le kar 1 se 10 tak loop chalate hain aur given number ka table print karte hain (n * i).
28. Print Fibonacci Series:
Logic: Fibonacci series mein pehle do numbers 0 aur 1 hote hain, aur agla number previous two numbers ka sum hota hai. Loop chalate hain aur series print karte hain.
29. Count the Digits of a Given Number:
Logic: Loop chalate hain jab tak number 0 na ho jaye. Har iteration mein number ko 10 se divide karte hain aur counter increment karte hain.
30. Find First and Last Digit of a Given Number:
Logic: Last digit ko n % 10 se nikalte hain. First digit nikalne ke liye number ko repeatedly 10 se divide karte hain jab tak ek digit na bach jaye.
31. Calculate the Sum of Digits of a Given Number:
Logic: Loop chalate hain aur har digit ko nikal kar sum variable mein add karte hain (n % 10 se digit nikalte hain, phir n // 10 se number ko reduce karte hain).
32. Calculate the Product of Digits of a Given Number:
Logic: Loop chalate hain aur har digit ko nikal kar product variable mein multiply karte hain (n % 10 se digit nikalte hain, phir n // 10 se number ko reduce karte hain).
33. Find the Reverse of a Given Number:
Logic: Loop chalate hain aur har digit ko extract karke reverse order mein add karte hain (reverse variable mein multiply aur add karke store karte hain).
34. Check Whether a Given Number is Palindrome or Not:
Logic: Number ko reverse karke check karte hain ki original number ke barabar hai ya nahi. Agar reverse aur original number same hain, toh wo palindrome hai.
35. Check Whether a Given Number is Prime or Not:
Logic: Prime number wo hota hai jo sirf 1 aur apne aap se divisible hota hai. Loop 2 se sqrt(n) tak chalate hain aur check karte hain ki number kisi aur se divisible hai ya nahi. Agar hai toh prime nahi, warna prime hai.
Yeh








