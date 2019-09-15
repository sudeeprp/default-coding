## Stateless Functions

Habit: Look for parts that transform an input to an output. Model them as stateless functions.
Here's an example: Let's say we need to read parameters from a configuration json-file. Here's a sub-optimal implementation in a ConfigReader class. 
{% gist 638a7be3a5c71937f194532de90a1e2d %}
`__init__` is the constructor. It opens a file and reads the content into `self.config`, which is a data-member. They key-value pairs in the configuration become part of this object's state.

The method read_parameter can then return the value of a particular configuration parameter in the config.

There are many obvious issues here: What if the file doesn't exist? What if the json is corrupt? What if that parameter doesn't exist? 

And there could be a wish-list: What if I want default values for some configurations? Split my configuration into multiple files?

Suppose you were given these issues and the wish-list. You don't just want it to 'somehow work', you want to separate concerns and make the code unit-testable 'on its own'. 
If you continue with this class, what would you need to do, for testing?
* Test with a json-file having the parameter
* Test without the file
* Test with a corrupt file... non-json, json with an invalid parameter-value, invalid parameter-type, etc. 
* Test with a json-file not having the parameter

In every case, we would need to test all the states of the class with all its functions. Perhaps the class 'smells' of multiple responsibilities?

What if we exercise the habit of stateless functions? The functionality can be modeled as the following set of transformations:
* from a configuration-file to a configuration-dictionary
* from a dictionary to a parameter value

Here are the corresponding functions:
{% gist 06eb7daec8c080bbc4ec3b7b6f3d9bfe %}
The whole thing is testable function-by-function. Adding a test is trivial too.

These functions can be used within a class to couple them with state (e.g., to cache the dictionary).
This illustrates the habit of modeling with stateless functions, testing thoroughly and using classes only when there's need for some state to be coupled.
