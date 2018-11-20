import pprint
import math


class TextMapper():
    
    alphabet = ''

    @staticmethod
    def setAlphabet(alphabet):
        TextMapper.alphabet = alphabet

    @staticmethod
    def openFile(path):
        with open(path,'r') as file:
            return file.read()
    @staticmethod
    def cleanFile(data,space=False):
        data = data.lower()

        cleaned = ''

        for item in data:
            if item in TextMapper.alphabet:
                cleaned += item

        return cleaned

    @staticmethod
    def checkFile(path):
         return TextMapper.cleanFile(TextMapper.openFile(path))


class OneGramWorker():
    
    def __init__(self,text,alphabet):
        self.text = text
        self.alphabet = alphabet
        self.oneGramDictionary = {}
        self.entropyForItem = {}

    def makeOneGramDictionary(self):
        for letter in self.alphabet:
            self.oneGramDictionary[letter] = 0
    
    def countLetterFrequency(self):

        for symbol in self.text:

            if symbol in self.oneGramDictionary:
                self.oneGramDictionary[symbol] += 1

    def getLetterFrequency(self):

        for item in self.oneGramDictionary:
            self.oneGramDictionary[item] = self.oneGramDictionary[item] / len(self.text)

        return self.oneGramDictionary



    def getEntropy(self):
        for ngram in self.oneGramDictionary:
            currentNGramValue = self.oneGramDictionary[ngram]

            if currentNGramValue == 0: continue
            self.entropyForItem[ngram] = currentNGramValue * math.log2(currentNGramValue)

        return self.entropyForItem

    def getTotalEntropy(self):
        entropy = 0
        for item in self.entropyForItem:
            entropy += self.entropyForItem[item]

        return entropy * -1

    def makeAllStuf(self):
        self.makeOneGramDictionary()
        self.countLetterFrequency()
        self.getLetterFrequency()
        self.getEntropy()

        return round(self.getTotalEntropy(),8)




class BiGramWorker():
    
    def __init__(self,text,alphabet):
        self.text = list(text)
        self.alphabet = alphabet
        self.biGramDictionary = {}
        self.entropyForItem = {}
        

    def makeBiGramDictionary(self):
        for letterColumn in self.alphabet:
            for letterRow in self.alphabet:
                self.biGramDictionary[letterColumn + letterRow] = 0
    
    def countLetterFrequency(self):


        textWidth = len(self.text)

        for step in range(0,textWidth - 1):

            currentBiGram = self.text[step] + self.text[step + 1]

            if currentBiGram in self.biGramDictionary:
                self.biGramDictionary[currentBiGram] += 1

    def getLetterFrequency(self):

        biGramQuantity = 0

        for item in self.biGramDictionary:
            biGramQuantity += self.biGramDictionary[item]

        for item in self.biGramDictionary:
            self.biGramDictionary[item] = self.biGramDictionary[item] / biGramQuantity

        return self.biGramDictionary


    def prettyPrint(self):


        for i in self.alphabet:
            print(" {0}".format(i.upper()),end=' ')
        
        print()

        for i in self.alphabet:
            print(i.upper(),end=' ')

            for n in self.alphabet:

                if i + n in self.biGramDictionary:
                    print(round(self.biGramDictionary[i + n],5),end=' ')

            print()

    def getEntropy(self):
        for ngram in self.biGramDictionary:
            currentNGramValue = self.biGramDictionary[ngram]

            if currentNGramValue == 0: continue
            self.entropyForItem[ngram] = currentNGramValue * math.log2(currentNGramValue)

        return self.entropyForItem


    def getTotalEntropy(self):
        entropy = 0
        for item in self.entropyForItem:
            entropy += self.entropyForItem[item]
        
        return entropy * -0.5

    def makeAllStuf(self):
        self.makeBiGramDictionary()
        self.countLetterFrequency()
        self.getLetterFrequency()
        #self.prettyPrint()
        self.getEntropy()


        return round(self.getTotalEntropy(),8)
                
