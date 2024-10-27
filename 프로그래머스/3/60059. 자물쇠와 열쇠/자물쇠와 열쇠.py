def key_rotation(key):
    size = len(key[0])
    rotation_key = [[0]*size for _ in range(size)]
    
    for i in range(size):
        for j in range(size):
            rotation_key[i][j] = key[j][(size-1)-i]
    
    return rotation_key


def make_key(key,all_key,lock_size):
    size = len(key[0])
    for i in range(-(size-1),lock_size):
        for j in range(-(size-1),lock_size):
            add_key = []
            for a in range(size):
                for b in range(size):
                    if key[a][b] == 1:
                        add_key.append([a+i,b+j])
            all_key.append(add_key)
                


def solution(key, lock):
    size = len(lock[0])
    direction_key = [key]
    all_key = []
    
    for _ in range(3):
        now = direction_key[-1]
        rotation_key = key_rotation(now)
        direction_key.append(rotation_key)
    for k in direction_key:
        make_key(k,all_key,len(lock))
    
    lock_empty = []
    for i in range(size):
        for j in range(size):
            if lock[i][j] == 0:
                lock_empty.append([i,j])
                
    lock_empty_set = set(map(tuple, lock_empty))

    for answer in all_key:
        answer_set = set(map(tuple,answer))
        
        if lock_empty_set.issubset(answer_set):
            is_valid = True
            for i,j in answer_set:
                if 0<=i<size and 0<=j<size and lock[i][j] == 1:
                    is_valid = False
                    break
            
            if is_valid:
                return True
    
    return False
    
    