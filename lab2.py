# https://ita.skanev.com/04/problems/06.html
# class array:
#     m =0
#     n =0
#     step =0
#     data = [[10,17,13,28,23],[17,22,16,29,23],[24,28,22,34,24],[11,13,6,17,7],[45,44,32,37,23],[36,33,19,21,6],[75,66,51,53,34]]
#  Not the step is the the row we will step on first, so if we want evens the we have to step ata every 2 steps
def get(array, i,  j):#TODO
    return array[i][j]

def half(array): # DONE
    global step
    # result = [[len(array)]]
    index =1
    sindex = 2
    w, h = int(len(array)/2), len(array[0])
    Matrix = [[0 for y in range(h)] for x in range(w)]
    for i in range(w):
        if step ==2:
            index = (i+1)*2
            Matrix[i] = array[index]
        if step == 1:
            index = i*2
            Matrix[i] = array[index]

    return Matrix

def height(array,step):
    return len(array) / step

def min_index( array,row,left,right): # DONE Calculate the minimum number in that array
    minimum = array[row][left]
    min =left
    for i in range(left, right):
        if (get(array,row, i) < get(array, row, min)):
            minimum = get(array,row, i)
    return minimum

def findminMatrix(arr, mins,step):
    global final
    if int(height(arr,step)) == 1:
        mins[0] = min_index(arr, 0, 0, len(arr[0]))
    else:
        evens = half(arr)
        even_minimums = [[]]

        findminMatrix(evens, even_minimums, step)
        # step = step + 1
        leftmost =0
        print(range(int(height(arr,step))))
        for i in range(len(arr)):
            leftmost = min_index(arr, len(even_minimums) , leftmost, len(arr[0]))
            print(leftmost)
            mins[2 * i] = leftmost
            final.append(leftmost)
        # if height(arr,step) % 2:
        #     mins[height(arr,step) - 1] = min_index(arr, height(arr) - 1, leftmost, arr)


if __name__ == '__main__':
    final = []
    #let's creat a matrix as a 2 day array
    arr1 = [[10,17,13,28,23],[17,22,16,29,23],[24,28,22,34,24],[11,13,6,17,7],[45,44,32,37,23],[36,33,19,21,6],[75,66,51,53,34]]
    mins =[[]]
    step =1
    # call the calculate min matrix to find the min of each row
    # print the result
    findminMatrix(arr1, mins, step)
