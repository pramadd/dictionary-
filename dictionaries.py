dictionary = {"name" : "Pranathi", "age" : "26", "country of birth" : "India", "favorite language " : "Telugu"}
def dictionary_basics(bio):
   for key,data in bio.iteritems():
     print "My {} is {}".format(key,data)
 
dictionary_basics(dictionary)   