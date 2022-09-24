class Solution:
    
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        c = image[sr][sc]
        if c == color:
            return image
        width = len(image[0])
        height = len(image)
        dir = [(1,0),(0,1),(-1,0),(0,-1)]
        
        def dfs(row: int, col: int):
            if not ((0 <= row < height) and (0 <= col < width)) or image[row][col] != c:
                return
            image[row][col] = color
            for x,y in dir:
                dfs(row + x, col + y)
        
        dfs(sr,sc)
        return(image)
    
