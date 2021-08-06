if __name__ == '__main__':
    N = int(input())
    
    cmd_list = []
    result_list = []
    
    for i in range(N):
        cmd = input().split()
        #print(cmd)
        cmd_list.append(cmd)
        #print(cmd_list)
    
    for i in range(len(cmd_list)):
        exe_cmd = cmd_list[i][0]
        if exe_cmd == "insert":
            a = int(cmd_list[i][1])
            b = int(cmd_list[i][2])
            result_list.insert(a, b) 
        elif exe_cmd == "print":
            print(result_list)
        elif exe_cmd == "remove":
            a = int(cmd_list[i][1])
            result_list.remove(a)
        elif exe_cmd == "append":
            a = int(cmd_list[i][1])
            result_list.append(a)
        elif exe_cmd == "sort":
            result_list.sort()
        elif exe_cmd == "pop":
            result_list.pop()
        elif exe_cmd == "reverse":
            result_list.reverse()
