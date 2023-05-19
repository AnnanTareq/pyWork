This python code shows how to any message encrypt and decrypt. 

Encryption method:
  1. If user passes 1 character, then it will not work
  2. if user passes 2 characters, then it go inside the conditional block and reverse the order. After that, 3 characters add in the first and last position.
  3. If user passes 3 characters or more, then it will go to the conditional block where matched. Later it will split into two pieces of string. Both strings has reversed using while loop. After that produce random numbers which length is same as first portion of splitted strings.
  4. Lastly it will concatenate all the produced strings. 
  5. Use File handling to save the data to .txt file

Decryption method:
  1. Fethch data from .txt file
  2. secondly, measure the length of particular string
  3. Thirdly, if strings size is equal to 8, then remove first and last 3 digits. After that, reverse the string. 
  4. Then, if strings size is equal to 8, then remove first and last 3 digits. After that, reverse the string, and push to .txt file
  5. Lastly, if strings size is more than 8, then this string has 5 part. 2nd and 4th portion have the original message. Using string slicing fetch the data from there. Now, reverse both data, and concatenate.  
  
 
