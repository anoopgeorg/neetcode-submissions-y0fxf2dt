class Solution:
    delimiter = "#"
    def encode(self, strs: List[str]) -> str:
        # Delimiter formation - #<Numbers of characters in the string>
        # example ["Hello","World!",""," ","test"] --> #5#Hello#6#World!#0##1# #4#test
        encoded_str = ""
        for s in strs:
            encoded_str += self.delimiter + str(len(s)) + self.delimiter + s
        return encoded_str

    def decode(self, s: str) -> List[str]:
        # Decode - #<length of string>, use  it to calculate the start of the next string
        decoded_strs =[]

        if s == "":
            return decoded_strs

        ix = 0
        while ix < len(s):

            if s[ix] == self.delimiter:
                ix +=1


                
                # Capture the complete length integer value
                word_length = ""
                while s[ix]!= self.delimiter:
                    word_length += s[ix]
                    ix +=1

                # Calculate the start and end points
                word_start = ix+1
                word_length = int(word_length)

                decoded_word = s[word_start:word_start + word_length]
                decoded_strs.append(decoded_word)
                ix= word_start + word_length

            else:
                # Raise decoding error 
                raise Exception("Error in decoding string")
        return decoded_strs
