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
import sys
coordinates = (1,2,3)

x,y,z = coordinates;
print(x);
print(y);
print(z);

coordinates = [1,2,3]

x,y,z = coordinates;
print(x);
print(y);
print(z);

try:
    coordinates = [1,2,3,4,5,6,7] #Error HERE

    x,y,z = coordinates;
    print(x);
    print(y);
    print(z);
except:
    print(f'Oops! {sys.exc_info()} occured.')
