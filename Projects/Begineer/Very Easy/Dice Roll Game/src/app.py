# Dice Roll Game
import random #using random module (simple)
import numpy as np #Using numpy module (fast and best by performence)
# ASCII Arts
'''
+-------+
|       |
|   o   |
|       |
+-------+

+-------+
| o     |
|       |
|     o |
+-------+

+-------+
| o     |
|   o   |
|     o |
+-------+

+-------+
| o   o |
|       |
| o   o |
+-------+
+-------+
| o   o |
|   o   |
| o   o |
+-------+

+-------+
| o   o |
| o   o |
| o   o |
+-------+

'''

One = '''
+-------+
|       |
|   o   |
|       |
+-------+
Number : 01
'''

Two = '''
+-------+
| o     |
|       |
|     o |
+-------+
Number : 02
'''
Three = '''
+-------+
| o     |
|   o   |
|     o |
+-------+
Number : 03
'''
Four = '''
+-------+
| o   o |
|       |
| o   o |
+-------+
Number : 04
'''
Five = '''
+-------+
| o   o |
|       |
| o   o |
+-------+
Number : 05
'''
Six = '''
+-------+
| o   o |
| o   o |
| o   o |
+-------+
Number : 05
'''
Random_Dices = [One , Two , Three , Four , Five , Six]
#Random_Dice_Roll = random.choice(Random_Dices) #using random module (default , simple and not fast)
Random_Dice_Roll = np.random.choice(Random_Dices) #using numpy random choice (best and fast by performence)
print(f"Here the roll : \n")
print(Random_Dice_Roll)
