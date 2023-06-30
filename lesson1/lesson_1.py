s_test = "asd"*100000

def char_counter_1(str):
    k = 0
    for char1 in str:
        for char2 in str:
            if(char1 == char2):
                print(char1," ",k)


def char_counter_2(str):
    k = 0
    for char1 in set(str):
        for char2 in str:
            if(char1 == char2):
                print(char1," ",k)



def char_counter_3(str):
    my_dict = {}
    for char in str:
        my_dict[char] = my_dict.get(char,0) + 1
        
    for char, count in my_dict.items():
        print(char," ",count)

    
char_counter_1(s_test)
