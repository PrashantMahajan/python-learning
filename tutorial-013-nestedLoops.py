"""
/*
 * 
 * Prashant CONFIDENTIAL
 * __________________
 * 
 *  Prashant All Rights Reserved.
 * 
 * NOTICE:  All information contained herein is, and remains the property
 * of Prashant and its suppliers, if any.  The intellectual and technical
 * concepts contained herein are proprietary to Prashant and its suppliers
 * and may be covered by U.S. and Foreign Patents, patents in process, and are
 * protected by trade secret or copyright law. Dissemination of this information
 * or reproduction of this material is strictly forbidden unless prior written
 * permission is obtained from Prashant.
 */
/**
 * @author prashantmahajan
 */
 """
# https://youtu.be/_uQrJ0TkZlc?t=6474
# Draw F

characters = [5, 2, 5, 2, 2]

for i in characters:
    print("x" * i);

str = "";
j = 0;
print("--------------");
for i in characters:
    str = "";
    j = 0;
    while j < i:
        str += "x";
        j += 1;
    print(str)

print("--------------");
for i in characters:
    str = "";
    j = 0;
    for j in range(i):
        str += "x";
    print(str)


characters = [2,2,2,2,2,10]
print("--------------");
for i in characters:
    str = "";
    j = 0;
    for j in range(i):
        str += "x";
    print(str)

