"""
Merge function for 2048 game.
"""

def merge(line):
    """
    Function that merges a single row or column in 2048.
    """
    result=[]
    mresult=[]
    fresult=[]
    for dummy_x in range(len(line)):
        result.append(0)
        fresult.append(0)

    index=0
    for dummy_x in line:
        if dummy_x!=0:
            result[index]=dummy_x
            index+=1

    jump = True
    mresult=[]


    for dummy_y in range(len(result)):

        if dummy_y+1<=len(result)-1:
            print dummy_y

            if result[dummy_y] == result[dummy_y+1] and jump==True:
                mresult.append(result[dummy_y]*2)
                mresult.append(0)
                jump=False
            elif result[dummy_y] != result[dummy_y+1] and jump==True:
                mresult.append(result[dummy_y])
            else:
                jump=True
        elif jump==True:
            mresult.append(result[dummy_y])
    index=0
    for dummy_z in mresult:
        if dummy_z!=0:
            fresult[index] =dummy_z
            index += 1


    return fresult



print merge([8,16,16,8])




























