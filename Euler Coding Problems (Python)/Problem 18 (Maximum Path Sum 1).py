paths = [
'75',
'95 64',
'17 47 82',
'18 35 87 10',
'20 04 82 47 65',
'19 01 23 75 03 34',
'88 02 77 73 07 63 67',
'99 65 04 28 06 16 70 92',
'41 41 26 56 83 40 80 70 33',
'41 48 72 33 47 32 37 16 94 29',
'53 71 44 65 25 43 91 52 97 51 14',
'70 11 33 28 77 73 17 78 39 68 17 57',
'91 71 52 38 17 14 91 43 58 50 27 29 48',
'63 66 04 68 89 53 67 30 73 16 69 87 40 31',
'04 62 98 27 23 09 70 98 73 93 38 53 60 04 23']


#instead of a 1D array of strings, we can make it a 2D array of integers # The split() method splits a string into a list.
paths = [row.split() for row in paths]        #this line of code turns the paths variable to a 2D array of STRINGS
paths = [[int(i) for i in row] for row in paths] #this line converts the strings into integers
print(paths)



for i in range(len(paths)-1, 0, -1): #start at the last row
    for j in range(len(paths[i])-1): #iterate in order from left to right ecept do not go to lasr term
        paths[i-1][j] += max(paths[i][j], paths[i][j+1]) #ex 63 (on 2nd most bttom row) we wll start there and compare the values below it 4 and 62 in this case and see which one is greater
print(paths[0][0]) #print the new number on the first index of the line, ex 63 >> 125 after iteration
    



