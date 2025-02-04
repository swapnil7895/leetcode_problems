class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        sorted_arr = sorted( strs, key=len )
        f_string = sorted_arr[0]
        # print( sorted_arr) 
        if len( sorted_arr ) ==1:
            return sorted_arr[0]
        if f_string == "":
            return ""
    
        while f_string !="":
            # print(f"fs - '{f_string}'")
            for string2_index in range ( 1, len(sorted_arr) ) :
                # print(string2_index)
                if sorted_arr[ string2_index ].startswith( f_string ):
                    if sorted_arr[-1].startswith( f_string ):
                        # print(f"last el str -{f_string}")
                        return f_string
                elif string2_index == (len(sorted_arr) -1):
                    # print("in else")
                    # string2_index = 1
                    f_string = f_string[:-1]
                    # print(f"After removal of last char - {f_string}")
                else:
                    # print(f"el not matching breaking")
                    f_string = f_string[:-1]
                    break
                    # return ""
        if f_string == "":
            return ""    

    longestCommonPrefix( [ "flow", "flower"] )

