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

#WAP to print the English text for the phone number entered.
try:
    mapping = {1: "One", 2: "Two", 3: "Three", 4: "Four", 5: "Five", 6: "Six", 7: "Seven", 8: "Eight", 9: "Nine"};
    phoneNumber = input("Please enter you phone Number:\n");
    phoneNumberText = "";
    for itr in phoneNumber:
        phoneNumberText += f'{mapping.get(int(itr))} ';

    print(phoneNumberText);

except:
    print("Error Occurred");
