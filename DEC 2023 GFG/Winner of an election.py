class Solution:
    #Complete this function
    #Function to return the name of candidate that received maximum votes.
    def winner(self,arr,n):
        # Your code here
        # return the name of the winning candidate and the votes he recieved
        votes_count = {}
        
        # Iterate through the array to count votes
        for candidate in arr:
            if candidate in votes_count:
                votes_count[candidate] += 1
            else:
                votes_count[candidate] = 1

        # Find the candidate with the maximum votes
        max_votes = 0
        winner_name = ""
        for candidate, votes in votes_count.items():
            if votes > max_votes or (votes == max_votes and candidate < winner_name):
                max_votes = votes
                winner_name = candidate

        return winner_name, max_votes
