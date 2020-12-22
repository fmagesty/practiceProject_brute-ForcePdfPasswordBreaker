# Forgot the password from a pdf file but I remember it was a simple english word.
# Create a list of word strings by reading dictionary.txt
# Loop over each word in this list, passing it to decrypt method.
# If the method returns integer 0, password is wrong. Continue to next.
# If decrypt() returns 1, password is correct so break out of the loop.
# Print the hacked password. Try both uppercase and lowercase of each word.

import PyPDF2

# Iterate of each word in dictionary.txt:
allWords = open('dictionary.txt')
allWords = allWords.read()
allWords = allWords.split('\n')
pdfFile = open('encryptedPDF.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFile)
print('Starting brute-force decryption. This may take a few minutes. Please wait.')
for word in allWords:
    print('Trying to break password with %s...' % (word))
    try:
        pdfReader.decrypt(word)
        if pdfReader.decrypt(word) == 1:
            print('Matching password found. File decrypted. The correct password is %s' % (word))
            allWords.close()
            break
        if pdfReader.decrypt(word.lower) == 1:
            print('Matching password found. File decrypted. The correct password is %s' % (word))
            allWords.close()
            break
    except:
        print('Password not found.')
print('Done.')