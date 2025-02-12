class Solution:
    # Return the kth smallest element in the given BST 
    def kthSmallest(self, root, k): 
        #code here.
        count = 0
        curr = root
        kth_val = -1  # Default value if kth smallest element does not exist
        
        while curr:
            # If there is no left child, visit the node and move to right child.
            if curr.left is None:
                count += 1
                if count == k:
                    kth_val = curr.data
                    return kth_val
                curr = curr.right
            else:
                # Find the inorder predecessor of current
                pre = curr.left
                while pre.right is not None and pre.right != curr:
                    pre = pre.right
                
                # Make current the right child of its inorder predecessor
                if pre.right is None:
                    pre.right = curr
                    curr = curr.left
                else:
                    # Revert the changes made in the 'if' part to restore the original tree.
                    pre.right = None
                    count += 1
                    if count == k:
                        kth_val = curr.data
                        return kth_val
                    curr = curr.right
        
        return -1  # kth smallest element not found
