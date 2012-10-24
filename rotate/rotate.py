def amountShifted(array):
    return compareSection(array, 0, len(array) - 1)

#recursively compare the start and end values of an array subsection
#continue comparing smaller subsections containing a start
#value higher than the end value, meaning the shift is in that subsection
#this is an O(log(n)) solution
def compareSection(array, start, end):
    #if the subsection is of length 1, the subsection ending index
    #is also how many places to the right the array is shifted
    if end - start == 1:
        return end
    middle = (end + start)/2
    #if the start of this section is greater than the middle,
    #the shift occurs in the first half of this subsection
    if (array[start] > array[middle]):
        return compareSection(array, start, middle)
    #if the end of this section is less than the middle,
    #the shift occurs in the second half of this subsection
    elif (array[middle] > array[end]):
        return compareSection(array, middle, end)
    #handle the case where the array is not shifted at all
    else:
        return 0
