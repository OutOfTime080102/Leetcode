class Solution(object):
    def maxPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        if len(points) <= 2:
            return len(points)
        
        max_points = 0  # Variable to store the maximum number of points
        
        for i in range(len(points)):
            slopes = defaultdict(int)  # Dictionary to store the frequency of slopes
            
            # Count the number of same points as the current point
            same_points = 1
            
            for j in range(i + 1, len(points)):
                # Calculate the slope of the line passing through points[i] and points[j]
                dx = points[j][0] - points[i][0]
                dy = points[j][1] - points[i][1]
                
                # Case of same points
                if dx == 0 and dy == 0:
                    same_points += 1
                    continue
                
                # Calculate the greatest common divisor (gcd) of dx and dy to normalize the slope
                gcd_val = self.gcd(dx, dy)
                slope = (dy // gcd_val, dx // gcd_val)
                
                # Increment the frequency of the slope in the dictionary
                slopes[slope] += 1
                
            # Update the maximum number of points for the current point
            max_points = max(max_points, same_points)
            
            # Update max_points using the frequencies of slopes
            for slope_freq in slopes.values():
                max_points = max(max_points, slope_freq + same_points)
        
        return max_points
    
    # Helper function to calculate the greatest common divisor (gcd)
    def gcd(self, a, b):
        while b:
            a, b = b, a % b
        return a
