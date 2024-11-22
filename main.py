from menu.exercisesOne import designOneList,designOneDict
from menu.exercisesTwo import designTwoList, designTwoDict
from menu.exercisesthree import designThreeList, designThreeDict
from menu.exerciseFour import designFourList, designFourDict
from menu.exerciseFive import designFiveList,designFiveDict
from menu.exerciseSix import designSixList,designSixDict
from menu.exerciseTen import designTenList,designTenDict
from menu.exerciseSeven import designSevenList,designSevenDict
from menu.exerciseEight import designEightList,designEightDict
from menu.exerciseNine import designNineList,designNineDict
from menu.mmenu import designPrincipal,designList,designDict
    
()
import os 


while True:
    match designPrincipal():
        case 1:
            while True:
                options = designList()
                if (options == 1):
                    os.system('clear')
                    designOneList()
                elif (options == 2):
                    os.system('clear')
                    designTwoList()
                elif (options == 3):
                    os.system('clear')
                    designThreeList()
                elif (options == 4):
                    os.system('clear')
                    designFourList()
                elif (options == 5):
                    os.system('clear')
                    designFiveList()
                elif (options == 6):
                    os.system('clear')
                    designSixList()
                elif (options == 7):
                    os.system('clear')
                    designSevenList()
                elif (options == 8):
                    os.system('clear')
                    designEightList()
                elif (options == 9):
                    os.system('clear')
                    designNineList()
                elif (options == 10):
                    os.system('clear')
                    designTenList()
                elif (options == 11):
                    os.system('clear')
                break

        case 2:
            while True:
                options = designDict()
                if (options == 1):
                    os.system('clear')
                    designOneDict()
                elif (options == 2):
                    os.system('clear')
                    designTwoDict()
                elif (options == 3):
                    os.system('clear')
                    designThreeDict()
                elif (options == 4):
                    os.system('clear')
                    designFourDict()
                elif (options == 5):
                    os.system('clear')
                    designFiveDict()
                elif (options == 6):
                    os.system('clear')
                    designSixDict()
                elif (options == 7):
                    os.system('clear')
                    designSevenDict()
                elif (options == 8):
                    os.system('clear')
                    designEightDict()
                elif (options == 9):
                    os.system('clear')
                    print ("Exercise not available")
                #    designNineDict()
                elif (options == 10):
                    os.system('clear')
                    print ("Exercise not available")
                #    designTenDict()
                elif (options == 11):
                    os.system('clear')
                break       

        case 3:
            print("""
            =============================================
                ¡Thanks for reviewing the exercises :)!
            =============================================
            """)
            exit()