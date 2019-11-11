# ninjagold
Assignment: Ninja Gold
Objectives:
1. Practice using session
2. Practice having the server use data sent by the client in a form
3. Practice using hidden inputs

Create a simple game to test your understanding of flask, and implement the functionality below.
For this assignment, you're going to create a mini-game that helps a ninja make some money! When you start the game, your ninja should have 0 gold. The ninja can go to different places (farm, cave, house, casino) and earn different amounts of gold. In the case of a casino, your ninja can earn or LOSE up to 50 golds. Your job is to create a web app that allows this ninja to earn gold and to display past activities of this ninja.
Guidelines
1. Refer to the wireframe below.
2. Have the four forms appear when the user goes to http://localhost:5000.
3. For the farm, your form would look something like <form action="/process_money" method="post">
4.   <input type="hidden" name="building" value="farm" />
5.   <input type="submit" value="Find Gold!"/>
6. </form>
7.  In other words, you want to include a hidden value in the form and have each form submit the form information to /process_money.
8. Have /process_money determine how much gold the user should have.
9. You should only have 2 routes -- '/' and '/process_money' (reset can be another route if you implement this feature).
![alt text](https://github.com/RanCSS9/ninjagold/blob/master/NinjaGoldScreenShot.png)
