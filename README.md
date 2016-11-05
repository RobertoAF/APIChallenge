# CODE 2040 APIChallenge

This repository contains responses to the 2017 CODE 2040 API challenge.
For this challenge, we were asked to complete the steps outlined below in any programming language of our choice. 
I chose to implement this in Python 3, mainly due to its simplicty, readability and multiparadigm approach. In order to improve the efficiency of my code, I tested the execution times of multiple solutions to some of the challenges using Python's timeit module; and so, I implemented my code accordingly.

<h3>Step 1: Register</h3>
<p>Challenge: Send registration information, including our unique API token and GIT url.</p>
<p>Approach: I used the JSON and urllib.request modules to send a POST request with my registration information.</p>

<h3>Step 2: Reverse</h3>
<p>Challenge: Reverse a given string and return it.</p>
<p>Approach: I formulated several solutions to the problem of reversing a string. Initially, I assumed that solution4 would be the most efficient. However, solution1 proved to be more efficient, which I ultimately implemented in my code to reverse the given string.</p>

```python
def solution1(string):
    return string[::-1]
    
def solution2(string):
    newString = ''
    index = len(string)
    while index:
        index -= 1                    
        newString += string[index] 
        
    return newString
    
def solution3(string):
    newString = []
    index = len(string)
    while index:
        index -= 1                       
        newString.append(string[index])
        
    return ''.join(newString)

def solution4(string):
    return ''.join(reversed(string))
```
```html
Solution1:  ecneics retupmoc ecneics retupmoc ecneics retupmoc
Execution time: --- 0.5086055979991215 seconds ---

Solution2:  ecneics retupmoc ecneics retupmoc ecneics retupmoc
Execution time: --- 11.397826668006019 seconds ---

Solution3:  ecneics retupmoc ecneics retupmoc ecneics retupmoc
Execution time: --- 13.587087155996414 seconds ---

Solution4:  ecneics retupmoc ecneics retupmoc ecneics retupmoc
Execution time: --- 2.4922737769957166 seconds ---

```
<h3>Step 3: Haystack</h3>
<p>Challenge: Find the index of a specific key in an array of strings and return it.</p>
<p>Approach: I chose Python's index method to find the specific item in the array of strings (solution3). </p>
```python
def solution1(needle, myList):  
    for index, item in enumerate(myList):
        if item == needle:
            return index
    
def solution2(needle, myList):
    for index in range(len(myList)):
        if myList[index] == needle:
            return index
    
def solution3(needle, myList):
    try:
        return myList.index(needle)
    except:
        pass
        
def solution4(needle, myList):
    if needle in myList:
        return myList.index(needle)
```
```html
Solution1: 
Item found at index: 4
Execution time: --- 1.0936356830061413 seconds ---

Solution2: 
Item found at index: 4
Execution time: --- 1.2851204390026396 seconds ---

Solution3: 
Item found at index: 4
Execution time: --- 0.564864708998357 seconds ---

Solution4: 
Item found at index: 4
Execution time: --- 0.6521950480018859 seconds ---
```
<h3>Step 4: Prefix</h3>
<p>Challenge: Process an array of strings, ignore those containing a specific substring (prefix), and
return an array with the remaining strings.</p>
<p>Approach: I chose solution3 to process the array since it was slightly more efficient than solution2 at iterating through the list of strings and appending the selected items to a new list.</p>
```python
def solution1(prefix, myList):
    return [item for item in myList if prefix != item[:len(prefix)]]
    
def solution2(prefix, myList):
    return [item for item in myList if item.find(prefix, 0, len(prefix))]

def solution3(prefix, myList):
    return [item for item in myList if item.startswith(prefix) is False]
```
```html
Solution1: 
tylcqpub
cylqbwgi
jokavnyi
juslenkh
Execution time: --- 4.216499283007579 seconds ---

Solution2: 
tylcqpub
cylqbwgi
jokavnyi
juslenkh
Execution time: --- 5.619274677010253 seconds ---

Solution3: 
tylcqpub
cylqbwgi
jokavnyi
juslenkh
Execution time: --- 3.765790985999047 seconds ---
```
<h3>Step 5: Dating</h3>
<p>Challenge: Given a specific time interval, add this value to a timestamp, parse and return in ISO8601 format.<p>
<p>Approach:
Using the datetime and iso8601 modules, I parsed the date into seconds, added the new time interval in seconds, and converted that into a new datestamp in ISO2601 format.<p>
