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


'''
1 Friend distance (path version)
* Input: adjacency matrix friends, users userA and userB.
* Return: the shortest path as a list between userA and userB.
* Example:

friends = [[0,1,0],[1,0,1],[0,1,0]]
friend_distance_path(friends, 0, 2) # => [0,1,2]

function friend_distance_path(friends, userA, userB):
    queue = [(userA, [userA])]   # node, path so far
    visited = set(userA)
    
    while queue not empty:
        current, path = queue.pop_front()
        
        if current == userB:
            return path
        
        for neighbor in friends[current]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, path + [neighbor]))
    
    return -1   # no path exists
''' 






'''
All friends at distance k

Input: adjacency matrix or list, user userA, integer k.

Return: list of all users exactly k friends away from userA.

Example:
friends = [[0,1,0],[1,0,1],[0,1,0]]
friends_at_distance_k(friends, 0, 2) # => [2]

function friends_at_distance_k(friends, userA, k):
    queue = [(userA, 0)]   # node, current distance
    visited = set(userA)
    result = []
    
    while queue not empty:
        current, dist = queue.pop_front()
        
        if dist == k:
            result.append(current)
        elif dist < k:
            for neighbor in friends[current]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, dist + 1))
    
    return result

'''



'''
Largest friend circle

Input: adjacency list/matrix of the network.

Return: the size of the largest connected component.

Example:

friends = [[0,1,0,0],[1,0,0,0],[0,0,0,1],[0,0,1,0]]
largest_friend_circle(friends) # => 2

function largest_friend_circle(friends):
    visited = set()
    max_size = 0
    
    for user in all users:
        if user not in visited:
            size = bfs_size(friends, user, visited)
            max_size = max(max_size, size)
    
    return max_size

function bfs_size(friends, start, visited):
    queue = [start]
    visited.add(start)
    size = 0
    
    while queue not empty:
        current = queue.pop_front()
        size += 1
        for neighbor in friends[current]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    
    return size

'''



'''
Check if users are connected

Input: adjacency list/matrix, userA and userB.

Return: True/False depending on whether there exists any path between them.

Example:

friends = [[0,1,0],[1,0,0],[0,0,0]]
are_connected(friends, 0, 2) # => False

function are_connected(friends, userA, userB):
    queue = [userA]
    visited = set() 
        
    while queue not empty:
        current = queue.pop_front()
        if userA in visited: 
            continue 
        visited.add(userA)
        if current == userB:
            return True
        for neighbor in friends[current]:
            if neighbor not in visited:
                queue.append(neighbor)
    
    return False


'''





'''
Degrees of separation

Input: adjacency matrix/list.

Return: maximum distance between any two connected users (like LinkedIn degrees of separation).

Example:

friends = [[0,1,0],[1,0,1],[0,1,0]]
max_friend_distance(friends) # => 2

function max_friend_distance(friends):
    max_dist = 0
    
    for userA in all users:
        distances = bfs_distances(friends, userA)
        for dist in distances:
            if dist != -1:
                max_dist = max(max_dist, dist)
    
    return max_dist

function bfs_distances(friends, start):
    queue = [(start, 0)]
    visited = set(start)
    distances = array of -1 for all users
    distances[start] = 0
    
    while queue not empty:
        current, dist = queue.pop_front()
        for neighbor in friends[current]:
            if neighbor not in visited:
                visited.add(neighbor)
                distances[neighbor] = dist + 1
                queue.append((neighbor, dist + 1))
    
    return distances

'''