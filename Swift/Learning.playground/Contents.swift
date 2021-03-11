import Foundation
/*
 Welcome to my Swift Notes! This will include my journey through the Apple Documentation and also the Apple resources, enjoy the read through and I will make it as comprehensive as I can!
 */

// The notes are from the specifc platform/documentation that is noted at the start of every section



// Apple Education. “Develop in Swift Fundamentals.” Apple Inc. - Education, 2020. Apple Books. https://books.apple.com/au/book/develop-in-swift-fundamentals/id1511184145


/* Storing Values*/

//Constants: A variable that won't change throughout the lifetime of the program

let var1 = "John" // Syntax
print(var1)


//Variables: A variable that can change throughout the lifetime of the program

var var2 = 29
print(var2)

//Naming Conventions

/*
 Rules:
 - Cannot contain mathematical symbols
 - Cannot contain spaces
 - Cannot begin with a number
 
 Best Practices:
 - Names should be clear and descriptive
 - Use 'Camel Case' (i.e. somethingLikeThis)
 -
*/

//Types:

/*
Integer: 'Int' , represents whole numbers/integers (e.g. 4)
String: ' String', represents text/characters (e.g. this is a test)
Double: 'Double', represents numbers that require a decimal point/real numbers (e.g. 9.4)
Boolean: 'Bool', represents 'True' or 'False'
*/

//You cannot mismatch types, as it will be flagged, and it will not compile

//Changing types on the fly:

let x = 3
let y = 0.1415927
let pi = Double(x) + y

// You can use underscores to assist in reading, as in:

var largeUglyNumber = 1000000000
var largeNiceNumber = 1_000_000_000

//How to declare a variable/constant with a specific data-type:

let cityName: String = "San Francisco"
let pi1: Double = 3.1415927

//You can match with a different data type, and compieler will adjust
let number: Double = 3
print(number)

//When to declare a variable with a specific data-type:

//When you create a constant, but have not assigned it a value
let firstName: String
//...
firstName = "Bob"

// When the value could be interpreted by the comiler as a different type
let middleInitial: Character = "J"
var remainingDistance: Double = 30

//When you create your own type definition
struct Car{
    var make:String
    var model:String
    var year:Int
}

//Example program for 'Storing Values':

let defaultScore = 100
var playerOneScore = defaultScore
var playerTwoScore = defaultScore

print(playerOneScore)
print(playerTwoScore)

playerOneScore = 200
print(playerOneScore)

//Example 2

struct Person {
    let firstName: String
    let lastName: String
    
    func sayHello() {
      print("Hello there! My name is \(firstName) \(lastName).")
    }
    
}

let Jacob = Person(firstName: "Jacob", lastName: "Edwards")
let Candace = Person(firstName: "Candace", lastName: "Salinas")

Jacob.sayHello()
Candace.sayHello()


/* Operators*/

/*
Operations:
+ : Addition
- : Substraction
* : Multiplication
/ : Division
= : Equals to
% : Remainder (a.k.a. 'Modulo')
*/

//Basic Arithmetic

var opponentScore = 3 * 8

var myScore = 100 / 4

var totalScore = opponentScore + myScore

//Updating a Variable
myScore += 3 //Updates score and adds 3
myScore -= 5 //Updates score and minuses 5
myScore *= 2 //Updates score and times by 2
myScore /= 2 //Updates score and divides by 2

//Calculating the Remainder
let dividend = 10
let divisor = 3
let quotient = dividend / divisor // Value of 3 as rounded down
let remainder = dividend % divisor // Value of 1

let totalDistance = 3.9
var distanceTravelled = 1.2
var remaingDistance = totalDistance - distanceTravelled


/* Control Flow*/

/*
Logical and Comparision Operators
== : Comparison (two items must be equal)
!= : Comparison (two items must not be equal)
>  : Comparison (value on left must be greater than value on right)
>= : Comparison (value on left must be greater or equal to value on right)
<  : Comparison (value on right must be greater than value on left)
<= : Comparison (value on right must be greater or equal to value on left)
&& : Logical (AND - The conditional statement on the left and right must be true)
|| : Logical (OR  - The conditional statement on the left or right must be true)
|  : Logical (NOT - Returns the logical opposite of the conditional statement immediately following the operator)
*/

//You can also use Boolean values here for logic!

//Examples using Logic:

//'if' statements
let temperature = 100
if temperature >= 100 {
    print("The water is boiling")
}

//'if-else' statements
let temperature01 = 100
if temperature01 >= 100 {
    print("The water is boiling.")
} else {
    print("The water is not boiling.")
}

//Another example using 'if-else' statements

var finishPosition = 2

if finishPosition == 1 {
    print("Congratulations, you have won a gold medal!")
} else if finishPosition == 2 {
    print("You can in second place, you won a silver medal!")
} else {
    print("You did not recieve a medal :(")
}

//Using Boolean for logic

let number04 = 1000
let isSmallNumber = number < 10
print(isSmallNumber)

//Usig Boolean for logic (v2):

let speedLimit = 65
let currentSpeed = 72
let isSpeeding = currentSpeed > speedLimit
//Assigned as 'true' value

//You can also invert a Bool value by using thr NOT operator:

var isSnowing = false

if !isSnowing {
    print("It is not snowing")
}

//Using multiple operators to make sure a value satisfies multiple criteria

let temperature02 = 70

if temperature02 >= 65 && temperature <= 75 {
    print("The temperature is just right")
} else if temperature < 65 {
    print("It is too cold")
} else {
    print("It is too hot")
}

// the logical 'OR' operator represented by ||

var isPluggedIn = false
var hasBatteryPower = true

if isPluggedIn || hasBatteryPower {
    print("You can use your laptop.")
} else {
    print("You cannot use your laptop")
}

//Switch Statements

/*
Explanation:
As a long list of if and if-else statements can get confusing very quicky, also getting very messy and hard to edit. Swift has a function called 'Switch Statements' that is optimal for working with multiple options, as it allows for you to run seperate code for each option. A nice feature is the 'default' definition, which allows for you to set a 'default' for any conditions that you have not defined.
*/

//Example using switch statements

let numberOfWheels = 2
switch numberOfWheels {
case 0:
    print("Missing something?")
case 1:
    print("Unicycle")
case 2:
    print("Bicycle")
case 3:
    print("Tricycle")
case 4:
    print("Quadcycle")
default:
    print("That is a lot of wheels!")
}

/*
Explanation of code:
Given the constant 'numberOfWheels', the code provides a seperate action if it is 0, 1, 2, 3, 4. it also provides an action for anything else that is not defined (the 'default'), although this could have been written using if-else statements, it is a lot neater to write this way.
*/

//using case statements

/*
Allows for the evaluation of multiple statements at once. Makes code more efficient.
*/

let character = "z"

switch character {
case "a", "e", "i", "o", "u":
    print("This character is a vowel")
default:
    print("This character is a consonant")
}

// When working with numbers, you can use interval matching to check for inclusion within a range.

let distance = 98

switch distance {
case 0...9:
    print("Your destination is close")
case 10...99:
    print("Your destination is a medium distance")
case 100...999:
    print("Your destination is far from here")
default:
    print("Are you sure you want to travel so far?")
}

//an interesting use case for an if statement is to define another variable, usually through somr kind of logic.

var largest: Int

let a = 15
let b = 4

if a > b {
  largest = a
} else {
  largest = b
}

//Ternary Operator (?:)

/*
Three parts of a ternary operator:
 
1. A question with a true or false answer
2. A value if the answer to the question is true
3. A value if the answer to the question is false.
*/

//Example og Ternary Operator:

largest = a > b ? a : b

//How to read the above: If 'a' > 'b' assign a ot the variable 'largest', otherwise assign 'b'

//For an easier and more intuitve way of finding the largest value, use the 'max' function

largest = max(a, b)


