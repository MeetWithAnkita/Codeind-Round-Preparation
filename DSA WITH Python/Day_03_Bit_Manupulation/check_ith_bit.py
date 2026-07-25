# check i-th bit is set or not 

n = int(input())
i = int(input())

def check_set(n, i ):
    binary = int(bin(n)[2:])
    # //////////// Using Left shift ////////////
    # x = 1 << i
    # ans = binary & x 
    # if ans == 0:
    #     print("Not Set")
    # else:
    #     print("set")
    
    # explanation: 
    # i th bit = 1 => set, 0 => not set
    # 13 = 1101
    # i = 2  
    # x = 1 << 2 = 0001 << 2 = 0100
    # 1101
    # 0100
    # -----
    # 0100  ==> set (ans != 0)



    # //////////// Using Right Shift ////////////
    x = binary >> i
    ans = x & 1 
    if ans == 1:
        print("Set")
    else:
        print("Not Set")

check_set(n, i )



# TC = O(1)
