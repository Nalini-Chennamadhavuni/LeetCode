class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        for i in range(len(image)):
            #flip
            begin = 0
            end = len(image[i])-1
            while begin < end:
                tmp = image[i][begin] 
                image[i][begin] = image[i][end]
                image[i][end] = tmp
                begin += 1
                end -= 1
               
                
            #invert
            for j in range(len(image[i])):
                if image[i][j] == 1:
                    image[i][j] = 0  
                else :
                    image[i][j] = 1
        return (image)