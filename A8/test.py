import docclass
import glob
from subprocess import check_output

cl = docclass.naivebayes(docclass.getwords)
try:
  check_output(['rm', 'spam.dm'])
except:
  print("No file")
#remove previous db file
cl.setdb('spam.db')
docclass.spamTrain(cl)
spampath="Testing/Spam/*.txt"
notspampath="Testing/NotSpam/*.txt"

print("Testing against spam emails.")
for filename in glob.glob(spampath):
    with open(filename, 'r') as myfile:
        data = myfile.read()
        print("Filename: ", filename, "Status: ", cl.classify(data))
print("Testing against regular emails.")
for filename in glob.glob(notspampath):
    with open(filename, 'r') as myfile:
        data = myfile.read()
        print("Filename: ", filename, "Status: ", cl.classify(data))
#with open("Spam/1.txt", 'r') as myfile:
    #data = myfile.read()
    #print(cl.classify(data))
#classify text: "the banking dinner" as spam or not spam
#print( cl.classify('the banking dinner') )
