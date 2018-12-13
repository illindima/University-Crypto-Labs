from GreetingHelper import GreetingHelper
from Ngram import TextMapper,OneGramWorker,BiGramWorker

alphabet = 'абвгдежзийклмнопрстуфхцчшщыьэюя'
alphabetWithSpace = alphabet + ' '

TextMapper.setAlphabet(alphabet)


sample1 = OneGramWorker(TextMapper.checkFile('./text.txt'),alphabet)

print("Monogram entropy: {0}".format(sample1.makeAllStuf()))

sample3 = BiGramWorker(TextMapper.checkFile('./text.txt'),alphabet)

print("Bigram entropy: {0}".format(sample3.makeAllStuf()))

TextMapper.setAlphabet(alphabetWithSpace)

sample2 = OneGramWorker(TextMapper.checkFile('./text.txt'),alphabetWithSpace)

print("Monogram entropy with space: {0}".format(sample2.makeAllStuf()))


sample4 = BiGramWorker(TextMapper.checkFile('./text.txt'),alphabetWithSpace)

print("Bigram entropy with space: {0}".format(sample4.makeAllStuf()))





