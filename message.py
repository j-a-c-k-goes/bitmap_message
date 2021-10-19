"""
display text emssage according to bitmap image
"""
import sys
# ................................................................ Imports
bitmap = """....................................................................
   **************   *  *** **  *      ******************************
  ********************* ** ** *  * ****************************** *
 **      *****************       ******************************
          *************          **  * **** ** ************** *
           *********            *******   **************** * *
            ********           ***************************  *
   *        * **** ***         *************** ******  ** *
               ****  *         ***************   *** ***  *
                 ******         *************    **   **  *
                 ********        *************    *  ** ***
                   ********         ********          * *** ****
                   *********         ******  *        **** ** * **
                   *********         ****** * *           *** *   *
                     ******          ***** **             *****   *
                     *****            **** *            ********
                    *****             ****              *********
                    ****              **                 *******   *
                    ***                                       *    *
                    **     *                    *
...................................................................."""

def create_bitmap(bit_depth = 1000):
    # for bit depth
    # create character @ i location
    # each location should be a "*" OR " "
    my_characters = ["*", " "]
    my_bit_map = """....................................................................
{}*******************************************************************
...................................................................."""
# ................................................................ Main Function
def make_bitmap_message(message):
    for line in bitmap.splitlines():
        for i, bit in enumerate(line):
            if bit == " ":
                print(" ", end="")
            else:
                print(message[i % len(message)], end="")
        print()
# ................................................................ On Run, Import
if __name__ == "__main__":

    print("enter a message to dispaly with global bitmap...")
    message = input(str("> "))
    if message == "":
        exit()
    else:
        make_bitmap_message(message)
    
