"use strict";

function getPossiblePosition(x, y) {
    let result = [];



}




//TESTS

const expect = require('chai').expect;

function test(name, fun) {
    try {
        fun();
        console.log(`${name} : OK`);
    } catch (e) {
        console.log(`${name} : FAILED: ${e}`);
    }
}

test('convert #1', () => {
    expect(convert(null, [], 9, 0)).to.deep.equal([1, 0, 0, 1, 1]);
});
test('convert #2', () => {
    expect(convert(null, [], -9, 0)).to.deep.equal([1, 1, 0, 1]);
});

test('convert #3', () => {
    expect(convert(null, [], 123321, 0))
});

test('parseMinusBinary', () => {
    expect(parseMinusBinary([1, 1, 0, 1])).to.equal(-9);
});

test('parseMinusBinary #2', () => {
    expect(parseMinusBinary([1, 0, 0, 1, 1])).to.equal(9);
});

test('parseMinusBinary zero', () => {
    expect(parseMinusBinary([])).to.equal(0);
});
test('parseMinusBinary zero', () => {
    expect(parseMinusBinary([])).to.equal(0);
});

test('parseMinusBinary zero', () => {
    expect(parseMinusBinary([0])).to.equal(0);
});

test('solution', () => {
    expect(solution([])).to.deep.equal([]);
});

test('solution #1', () => {
    expect(solution([1])).to.deep.equal([1, 1]);
});

test('solution negative to positive', () => {
    expect(solution([1, 0, 0, 1, 1, 1])).to.deep.equal([1, 1, 0, 1, 0, 1, 1]);
});
