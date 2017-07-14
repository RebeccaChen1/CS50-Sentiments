import nltk

class Analyzer():
    """Implements sentiment analysis."""
    

    def __init__(self, positives="positive-words.txt", negatives="negative-words.txt"):
        """Initialize Analyzer."""
        # opens positive words file and copies them into self.pwords
        self.pwords = set()
        pfile = open(positives, "r")
        for line in pfile:
            if line[0] != ';':
                self.pwords.add(line.rstrip("\n"))
        pfile.close()
        
        # opens negative words file and copites them into self.nwords
        self.nwords = set()
        nfile = open(negatives, "r")
        for line in nfile:
            if line[0] != ';':
                self.nwords.add(line.rstrip("\n"))
        nfile.close()

       

    def analyze(self, text):
        """Analyze text for sentiment, returning its score."""
        # splits sentences up into arrays of words
        tokenizer = nltk.tokenize.TweetTokenizer()
        tokens = tokenizer.tokenize(text)
        
        self.score = 0
        # checks if word is positive or negative and adjusts score 
        for i in range(len(tokens)):
            if tokens[i].lower() in self.pwords:
                self.score = self.score + 1
            elif tokens[i].lower() in self.nwords:
                self.score = self.score - 1
            

        return self.score
