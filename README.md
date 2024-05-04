01.Problem:  Sum Seconds
Three athletes finish with some number of seconds (between 1 and 50). Write a program that reads the times of the contestants and calculates their combined time in "minutes:seconds" format. Seconds are to be printed with a leading zero (2 -> "02", 7 -> "07", 35 -> "35").

input	output	input	output  input	output	input	output
35            22            50            14    
45            7             50            12
44	  2:04		34    1:03	  49  	2:29    10    0:36

02.Problem: Bonus points
Given an integer - initial number of points. Bonus points are accrued on it according to the rules described below. To write a program that calculates the bonus points that the number receives and the total number of points (the number + the bonus).
• If the number is up to and including 100, the bonus points are 5;
• If the number is greater than 100, the bonus points are 20% of the number;
• If the number is greater than 1000, the bonus points are 10% of the number.

• Additional bonus points (charged separately from the previous ones):
o For an even number  + 1 pt.
o For a number that ends in 5 + 2 pts.

input	output		input	output	        input	output	        input	output	
20	6               175     37.0            2703    270.3           15875   1589.5
        26		        212.0                   2973.3                  17464.5

03.Problem: Time + 15 minutes
To write a program that reads the hour and minutes of a 24-hour day entered by the user and calculates what the time will be in 15 minutes. 
Print the result in hours:minutes format. Hours are always between 0 and 23 and minutes are always between 0 and 59. 
Hours are written as one or two digits. Minutes are always written as two digits, with a leading zero when necessary.

input	output		input	output		input	output		input	output		input	output	
1                       0       0:16            23	0:14            11      11:23           12      13:04
46	2:01		01                      59                      08                      49

04.Problem: Toy shop
Petya has a children's toy shop. She gets a big order to fulfill. With the money he will earn, he wants to go on an excursion.
Toy prices:
• Puzzle - BGN 2.60.
• Talking doll - BGN 3
• Teddy bear - BGN 4.10.
• Mignon - BGN 8.20.
• Truck - BGN 2
If the ordered toys are 50 or more, the store makes a discount of 25% of the total price. From the money earned, Petya must give 10% for the rent of the shop. To calculate whether the money will be enough for her to go on an excursion.
input
6 lines are read from the console:
1. Excursion price - a real number in the interval [1.00 … 10000.00]
2. Number of puzzles - an integer in the range [0… 1000]
3. Number of talking dolls - an integer in the interval [0 … 1000]
4. Number of teddy bears - an integer in the interval [0 … 1000]
5. Number of minions - an integer in the interval [0 … 1000]
6. Number of trucks - an integer in the range [0 … 1000]
output
The console prints:
• If the money is sufficient, the following is printed:
o "Yes! {remaining money} lv left."
• If the money is NOT enough, the following is printed:
o "Not enough money! lv needed."

The result must be formatted to the second decimal place.
input	output
40.8
20
25
30
50
10	Yes! 418.20 lv left.

input	output
320
8
2
5
5
1	Not enough money! 238.73 lv needed.

05.Godzilla vs. Kong
Filming for the highly anticipated Godzilla vs. Kong movie begins. Screenwriter Adam Wingard asks you to write a program 
to calculate whether the budgeted funds are sufficient to make the film. The shoot will require a certain number of extras, clothing for each extra, and decor.
It is known that:
• The set for the film is worth 10% of the budget.
• For more than 150 extras, there is a 10% clothing discount.
input
3 lines are read from the console:
Line 1. Budget for the film - a real number in the interval [1.00 … 1000000.00]
Line 2. Number of extras – an integer in the interval [1 … 500]
Line 3. Price for clothing of one extra - real number in the interval [1.00 … 1000.00]
output
Two lines should be printed to the console:
• If the money for the decor and clothes is more than the budget:
o "Not enough money!"
o "Wingard needs {money lacking for film} leva more."
• If the money for the decor and clothes is less than or equal to the budget:
o "Action!"
o "Wingard starts filming with {remaining money} leva left."
The result must be formatted to the second decimal place.

input	output
20000   Action!
120     Wingard starts filming with 11340.00 leva left.
55.5

input	output
15437.62
186
57.99	Action!
        Wingard starts filming with 4186.33 leva left.

input	output
9587.88
222
55.68	Not enough money!
        Wingard needs 2495.77 leva more.

06.Problem: World swimming record
Ivan decides to improve the World Record in long distance swimming. Enter the record in seconds that Ivan needs to beat, the distance in meters that he needs to swim, and the time in seconds that he needs to swim 1 m on the console. Write a program that calculates whether he has completed the task by considering that: water resistance slows him down every 15 m by 12.5 seconds. When calculating how many times Ivan will slow down due to water resistance, the result should be rounded down to the nearest whole number.
Calculate the time in seconds for Ivan to swim the distance and the difference to the World Record.
input
3 lines are read from the console:
1. The record in seconds – a real number;
2. The distance in meters – a real number;
3. The time in seconds for which he swims a distance of 1 m. - a real number.
output
Printing to the console depends on the result:
• If Ivan has improved the World Record (his time is less than the record) we print:
o "Yes, he succeeded! The new world record is {Ivan's time} seconds."
• If he has NOT broken the record (his time is greater than or equal to the record) we print:
o "No, he failed! He was {missing seconds} seconds slower."
The result must be formatted to the second decimal place.

input   output
10464
1500
20	No, he failed! He was 20786.00 seconds slower.

input   output
55555.67
3017
5.03	Yes, he succeeded! The new world record is 17688.01 seconds.

07.Shopping
Peter wants to buy N video cards, M processors and P number of RAM. If the number of video cards is greater than the number of processors, you get a 15% discount on the final bill. The following prices apply:
• Video card – BGN 250/pc.
• Processor – 35% of the price of purchased video cards/pcs.
• RAM memory – 10% of the price of purchased video cards/pcs.
To calculate the amount needed to purchase the materials and to calculate whether the budget will be enough.
input
The input consists of four lines:
1. Peter's budget - a real number in the interval [1.0…100000.0]
2. The number of video cards - an integer in the interval [1…100]
3. The number of processors - an integer in the interval [1…100]
4. The number of RAM memory - an integer in the interval [1...100]
output
1 line is printed to the console, which should look like this:
• If the budget is sufficient:
"You have {remaining budget} leva left!"
• If the amount exceeds the budget:
"Not enough money! You need leva more!"
Format the result to the second decimal place.

input	output
900
2
1
3	You have 198.75 leva left!

input   output
920.45
3
1
1	Not enough money! You need 3.92 leva more!






	






			
		
			
	


		

		

	
