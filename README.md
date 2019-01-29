First thing after creating soup object is to extract the text from it.
By setting strip=True, we remove the white spaces from the beggining and end of the bit of text.

Second step is Tokenization. Tokenization is process of creating smaller pieces from a given sequence of characters. 
for word tokens :  word_tokenize()
for sentence tokens : sent_tokenize()

Last step is finding the count 
FreqDist() created the frequency count for each tokens
