


# Installing wikipedia library into Python
# Type "pip install wikipedia" into shell 
# To import the library, include the following line at the beginning of your Python script:
import wikipedia

# You can then use the various functions provided by the wikipedia library to retrieve information from Wikipedia.
#Here's an example that demonstrates how to fetch a summary of a Wikipedia article and print it:

print(wikipedia.summary("Rohit Sharma", sentences=4))