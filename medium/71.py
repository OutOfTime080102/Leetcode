class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        components = path.split('/')
        
        stack = []  # Use a stack to keep track of directories
        
        for component in components:
            if component == '..':
                # If component is '..', pop the last directory from stack (if not empty)
                if stack:
                    stack.pop()
            elif component and component != '.':
                # If component is not empty and not '.', push it onto the stack
                stack.append(component)
        
        # Construct the simplified path from the directories in the stack
        simplified_path = '/' + '/'.join(stack)
        
        return simplified_path
