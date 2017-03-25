"use strict";

const expect = require('chai').expect;

function test(name, fun) {
    try {
        fun();
        console.log(`${name} : OK`);
    } catch (e) {
        console.log(`${name} : FAILED: ${e}`);
    }
}

function solution(A) {
    const sumArray = createSumArray(A);

    let results = [];

    for (let i = 0; i < A.length; i++) {
        const element = A[i];
        const leftSum = getLeftSumForIndex(sumArray, i);
        const leftSumWithElement = element + leftSum;
        const rightSum = getRightSumForIndex(leftSumWithElement, sumArray);

        if (rightSum == leftSum) {
            results.push(i);
        }
    }

    return results;
}

function getLeftSumForIndex(sumArray, index) {
    return index === 0
        ? 0
        : sumArray[index - 1];
}

function getRightSumForIndex(leftSumWithElement, sumArray) {
    const lastSum = sumArray[sumArray.length - 1];

    return lastSum - leftSumWithElement;
}

function createSumArray(array) {
    let summed = [];

    array.reduce((previous, current) => {
            const newSum = previous + current;
            summed.push(newSum);
            return newSum
        },
        0
    );

    return summed;
}



//TESTS

test('last index', () => {
    const tab = [-1, 3, -4, 5, 1, -6, 2, 1];
    expect(solution(tab)).to.have.members([1, 3, 7]);
})
test('very large', () => {
    const veryLargeTable = [4294967294, 12903102938129038012, 1]

    expect(solution(veryLargeTable)).to.have.length(0);
})
test('one large', () => {
    const test = [2, -1, -2, 1, -500]

    expect(solution(test)).to.deep.equal([4]);
})




