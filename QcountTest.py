import Qcount as QQ

"""
Kyle Pickford
Simple test cases for functions in Qcount
"""

#test cases
print("Test Case #0: Qresult format test")
QQ.Qresult()

print("\nTest Case #1")
testR = QQ.Qcount("no vlid")
print(testR)
print("expected \n[0, 0, 0, 0, 7, 0, 0, 0, 0, 100, 0, 0, 0, 0")

print("\nTest Case #2")
testR = QQ.Qcount("aAaActctctGgGGG")
print(testR)
print("expected \n[4, 3, 5, 3, 0, ~26, 20, ~33, 20, 0, 4, 1, 5, 1")

print("\nTest Case #3")
testR = QQ.Qcount("This test includes \t \n whitespace and  %^^&**$%^#%@)(*_+")
print(testR)
print("expected \n[2, 2, 0, 4, 48, ~3, ~3, 0, ~7, ~85, 1, 1, 0, 1")

print("\nTest Case #4")
testR = QQ.Qcount("GATTTGGGGTTCAAAGCAGTATCGATCAAATAGTAAATCCATTTGTTCAACTCACAGTTT")
print(testR)
print("expected \n[19, 10, 11, 20, 0, ~31, ~16, ~18, ~33, 0, 3, 2, 4, 3")

print("\nTest Case #5")
testR = QQ.Qcount()
print(testR)
print("expected \n[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0")