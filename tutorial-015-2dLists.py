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
"""WAP to remove the duplicates in a sorted array"""

array = [1,1,2,2,3,3,3,3,4,4,5,5,6,6,7,7,7,8,8];

print(f'Array prior to cleanup: {array}');
i = 0;
j = 1;
while j < len(array):
    if array[j] != array[j-1] :
        array[i] = array[j];
        i = i+1;
    j += 1;
while(i < len(array)):
    array[i] = 0;
    i += 1;
print(f'Array after to cleanup: {array}');

"""WAP to remove the duplicates in a non array"""

array = [1,1,2,2,3,3,3,3,4,4,5,5,6,6,7,7,7,8,8];
array2 = [];
for itr in array:
    if itr not in array2:
        array2.append(itr);

print(array2);

