506 Final Project Readme Template

1. Describe your project in 1-4 sentences. Include the rationale for doing it, the basic idea, and the output that it should generate.

For my project, I generated two REST APIs: Holiday API which contains a list of holidays and the iTunes Search API.  Since I was in the Holiday Spirit, I wanted to use the holiday API to get a list US Holidays in December and from there, use one of the Holidays to pick a movie in iTunes.  Since there are no movies about New Year’s Eve, I made sure to prompt the user to type in Christmas to generate a list of movies from there.  

After that, I used the sorted method to sort the movie description by longest to shortest.  For me, I like to know as much about a movie as I can before I watch it and as a result, used the sorting method to make a list of movies starting the the movie with the longest description.  I made that function because I know it helps me and hopefully others too.  

The next item that should be outputted is “You are choosing the movie Elf (2003) which is from the USA and you want to pay a maximum of $5.0 “  Since i used the formatting method in the __str__ method, whatever way the user wants to put in the class to call he/she can do.  For the purpose of the output, I just put Elf (2003) as the movie, the country of origin I’d like to watch the movie from, and the maximum I’d pay for the movie, in this case, $5. 

Proximately, the genre of the movie should be outputted next.  For the purpose of the output, Comedy is there since Elf (2003) is indeed a comedy.  A good one too! Highly recommend.  

Lastly, the next method I wrote will print a tuple with the movie, price if the movie fits in the budget of the user.  If not, “this movie is too expensive! Try another movie” will print.  Once again, since Elf is $9.99 and the maximum I put was $5, the string was outputted rather than the tuple. 


2. Explain exactly what needs to be done to run your program (what file to run, anything the user needs to input, anything else) and what we should see once it is done running (should it have created a new text file or CSV? What should it basically look like?).

First run python final.py 
Then when it asks for a year, enter a year greater than 0.  Any number will do.  After that you should get two holidays Christmas Day and New Year’s Eve, which prompts the user to pick Christmas for the reasons stated earlier.  After that everything will be outputted in the logically order I mentioned above.  


3. List all the names of the files you are turning in, with a brief description of each one. (At minimum, there should be 1 Python file, 1 file containing cached data, and the README, but if your project requires others, that is fine as well! Just make sure you have submitted them all.)

final.py 
cache.txt
holidayapi.txt
106_Final_Project_Readme_Template.txt

4. Any Python packages/modules that must be installed in order to run your project (e.g. requests ...):

import requests
import json
import pprint
import unittest 

5. What data sources did you use? Provide links here and any other description necessary.

https://affiliate.itunes.apple.com/resources/documentation/itunes-store-web-service-search-api/
https://holidayapi.com

6. Approximate line numbers in Python file to find the following mechanics requirements:
- Sorting with a key function:
- Class definition: line 119 
- Creating instance of a class: line 148
- Calling methods on a class instance (list all line numbers where you invoke any method on a class instance): line 152 and line 156
- Beginnings of each class method definition: line 125, line 128, line 136
- (If applicable) Beginnings of each function definition outside classes: line 83, line 95, line 107.  Other functions for caching were derived from the hackpad.  
- Beginning of code that handles data caching/using cached data: iTunes API is cached starting at line 14, Holiday API is cached starting at line 47 
- Test cases: line 163-line 167

8. Rationale for project: why did you do this project? Why did you find it interesting? Did it work out the way you expected?
As stated in the first question, I did this project to kind of mimic the iTunes search for movies to watch during the holiday (Christmas) season.  Luckily, my program did in fact work the way I thought it would!  Although it was at times a hard and frustrating process, figuring out the code was so rewarding that I had one of the best experiences overall.  I can’t wait to do another project in my future years. 