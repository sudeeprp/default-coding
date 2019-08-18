## Stateless Functions

Habit: Look for parts that transform an input to an output. Model them as stateless functions.
Here's an example: Let's say we need to read parameters from a configuration json-file. Here's a sub-optimal implementation in a ConfigReader class. 
{% gist 638a7be3a5c71937f194532de90a1e2d %}
As you can see, it has a constructor to read from a file into a dictionary data-member called config. The method read_parameter can then return the value of a particular configuration parameter in the config.
There are many obvious issues here: What if the file doesn't exist? What if the json is corrupt? What if that parameter doesn't exist? 
And there could be a wish-list: What if I want to split my configuration into multiple files? Maybe I want this class to write to the config as well?
Suppose you were given these issues and the wish-list. You don't just want it to 'somehow work', you want to separate concerns and make the code unit-testable 'on its own'. 
If you continue with this class, what would you need to do, for testing?
. Test with a json-file having the parameter
. Test without the file
. Test with a corrupt file... non-json, json with an invalid parameter-value, invalid parameter-type, etc. 
. Test with a json-file not having the parameter
To test all of this, do we mock the file and the json parser, to return the jsons we need?.

Let's exercise our habit of stateless functions now. 
