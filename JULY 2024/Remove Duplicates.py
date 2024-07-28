class Solution:
	def removeDups(self, st):
		# code here
		list_st = list(st)
        new_list = []
        for word in list_st:
            if word not in new_list:
                new_list.append(word)
                
        #string after removing duplicates
        string = ''
        for word in new_list:
            string = string + word
          
        return string
