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
#https://youtu.be/_uQrJ0TkZlc?t=6958
""" WAP TO FInd the Largest Number in a list"""

list = [2,2,1,4,100,21,3,45, 1000, 9999, 2,56]
max = list[0];
for itr in list:
    if max < itr:
        max = itr;
print(f'MAX Number in the list is: {max}');