''' 
Degrees of Friendship
We're building a new social network where users are friends with one another. In order to make better friend recommendations, we want to develop a "friend distance" algorithm.

Write a function friend_distance(friends, userA, userB) that returns the minimum distance between two users (similar to the "degree" of connection on LinkedIn).

The input to your function will be a 2D array friends, where each entry (A, B) contains the friendship status between user A and user B.

In the friends array, each user's friendships are represented by rows, and each column represents a user. For example, if friends[0][1] is 1, it means that user 0 is friends with user 1. Similarly, if friends[1][2] is 1, it indicates that user 1 is friends with user 2.

Python
def friend_distance(friends, userA, userB):
  # Your code here...
Examples
In this example, users 0 and 1 are friends, so the entries (0, 1) and (1, 0) are both 1. Users 1 and 2 are also friends, so entries (1, 2) and (2, 1) are also 1. Since they are direct friends, their friend distance is 1. Users 0 and 2 are not friends but are both connected to User 1, so their friend distance is 2.

Python
friends = [[0 1 0],
           [1 0 1],
           [0 1 0]]

friend_distance(friends, 0, 1) # => 1
friend_distance(friends, 1, 2) # => 1
friend_distance(friends, 0, 2) # => 2
Return -1 if there are no connections between the users.
'''

def friend_distance(friends, userA, userB): #takes in the friends graphs, user A int and user B int 
    '''
    If they are friends, return 1 since both entries are 1. 
    If both users are the same, return 0. DONE 
    If there is no connection, return 0 
    If they are connected by 1 middle man, return 1 + 1 = 2. 
    
    I feel like I should apply BFS to this to figure it out. 
    '''
    
    if userA == userB: 
        return 0 

    visited = set() 
    q = [(1, userA)]
    
    while q: 
        distance, user = q.pop(0)
        
        if user in visited: 
            continue 

        if friends[user][userB]: 
            return distance 
        
        visited.add(user) 
        
        for i in range(len(friends[user])): 
            if friends[user][i]: 
                q.append((distance + 1, i))
    return -1 
# Testing 

friends = [[0, 1, 0], [1, 0, 1], [0, 1, 0]]
userA, userB = 0, 1

print(friend_distance(friends, userA, userB))

friends = [[0, 1, 0], [1, 0, 1], [0, 1, 0]]
userA, userB = 0, 2

print(friend_distance(friends, userA, userB))

friends = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
userA, userB = 0, 2

print(friend_distance(friends, userA, userB))

friends = [[0, 1, 0, 0, 0], [1, 0, 1, 0, 0], [0, 1, 0, 1, 0], [0, 0, 1, 0, 1], [0, 0, 0, 1, 0]]
userA, userB = 0, 4

print(friend_distance(friends, userA, userB))