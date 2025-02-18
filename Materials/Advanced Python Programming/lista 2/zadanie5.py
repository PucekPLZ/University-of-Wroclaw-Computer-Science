import io
# https://wiersze.juniora.pl/tuwim/tuwim_l01.html
with io.open ("lokomotywa.txt", "r", encoding="utf8") as myfile1:
    poem = myfile1.read().split()

def compression(text):
    compressed = []

    for i in range(len(text)):
        word = []
        n = 1

        if len(text[i]) == 1:
            word.append((n, text[i][0]))
        else:
            for j in range(1, len(text[i])):
                if text[i][j-1] == text[i][j]:
                    n += 1
                else:
                    word.append((n, text[i][j-1]))
                    n = 1 

                if j == len(text[i]) - 1:
                    word.append((n, text[i][j]))

        compressed.append(word)

    return compressed

def decompression(text):
    decompressed = ""

    for word in text:
        for i in range(len(word)):
            decompressed += word[i][1] * word[i][0]

        decompressed += " "

    return decompressed

text = compression(poem)

print(text)
print("")
print(decompression(text))