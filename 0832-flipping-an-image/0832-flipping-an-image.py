class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        for i in range(len(image)):
            #flip
            begin = 0
            end = len(image[i])-1
            while begin < end:
                if image[i][begin] !=  image[i][end]:
                    image[i][begin], image[i][end]  = image[i][end], image[i][begin]
                
                begin += 1
                end -= 1
                
            #invert
            for j in range(len(image[i])):
                image[i][j] = 0  if image[i][j] else 1
        return image