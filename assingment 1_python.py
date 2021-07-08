File = open("HarryPotterAndTheSorcerersStone.txt",'r')
#This helps in opening the file which is to be read
DictionaryOfWords = {}  # Dictionary mapping every word to a list (of indices of the words' occurences)
Novel = []  # List of all words in the order, in which they appear!

i = 0  # Counter Variable to keep track of index of words

for line in File.readlines():  # Iterate over all lines present in the text

    # Look at Python's Conciseness!

    line = line.replace(".", "").replace(",", "").replace('?', '').replace('!', '').replace('[', '').replace(']', '') \
        .replace('(', '').replace(')', '').replace('%', '').replace('/', '')

    # COMPLETE THE CODE FROM HERE:

    # This would split the line into many different words, and iterate over these words

    for word in line.split(' '):

        if word in DictonaryOfWords.keys():  # If the word is already present in the dictionary

            DictionaryOfWords[word] = [i]  # Add the index into the pre-existing list for this word
            else:
            DictionaryOfWords[word].append(i)  # Create a new list of indices for this word, with a single element

        Novel.append(word)  # Add the Word in the Novel's ordered list of words

        i += 1


        # COMPLETE THE CODE FROM HERE:

        def GetQuery():

            word = word = input()   # Get Input from the user regarding what word s/he wants to query for

            Number number = int(input()) # Get Input from the user regarding how many results the user wants to see

            return return(word,number)  # Return as output a tuple of the word and the Number of results


        def PrintContext(index):

            global Novel  # Declares the list Novel as a Global Variable

            # COMPLETE THE CODE FROM HERE:

            for i in range(index-5,index+6):  # Define the range so that the task above is fulfilled

                print(Novel[i], end=' ')  # Print the word (using List Indexing) with a space after that

            print('\n')

            def PrintResult(word, NumQuery):

                global DictionaryOfWords  # Allows us to use the Dictionary as a global variable

                # COMPLETE THE CODE FROM HERE:

                L = DictionaryOfWords[word]

                for i in range(0, min(len(L), NumQuery)):
                    PrintContext(L[i])  # Actually print the words surrounding the ith occurence of the given word
                while 1 > 0:

                    Choice = input('Press Y in order to Continue with the next query or N to end. \
                    Please press Enter after entering your choice!')

                    # COMPLETE THE CODE FROM HERE:

                    if Choice == 'Y':  # If the user wants to query

                        printResult(*GetQuery())  # Use some of the past defined function to do so

                    else:

                    break  # Else end the loop
