"use strict";
/**
 * Vending machine * 15 minutes *
 ================================

 A vending machine has the following denominations: 1c, 5c, 10c, 25c, 50c, and $1. Your task is to write a program that will be used in a vending machine to return change. Assume that the vending machine will always want to return the least number of coins or notes. Devise a function getChange(M, P) where M is how much money was inserted into the machine and P the price of the item selected, that returns an array of integers representing the number of each denomination to return.

 Example:
 getChange(5, 0.99) should return [1,0,0,0,0,4]

 ===========
 Test cases:

 getChange(3.14, 1.99) should return [0,1,1,0,0,1]
 getChange(4, 3.14) should return [1,0,1,1,1,0]
 getChange(0.45, 0.34) should return [1,0,1,0,0,0]
 */

const DENOMINATIONS = [100, 50, 25, 10, 5, 1];


function getChange(paid, cost) {
    let left = Math.floor(paid * 100) - Math.floor(cost * 100);

    return DENOMINATIONS.map(
        (denomination) => {
            if (left >= 0 && left >= denomination) {
                const total = Math.floor(left / denomination);
                left -= total * denomination;

                return total;
            }

            return 0;
        })
        .reverse();
}


console.log(getChange(0.04, 0));
console.log(getChange(3.14, 1.99));
console.log(getChange(4, 3.14));
console.log(getChange(0.45, 0.34));