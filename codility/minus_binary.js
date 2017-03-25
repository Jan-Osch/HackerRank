"use strict";

function solution(A) {
    const parsed = parseMinusBinary(A);

    const reversed = -parsed;

    return convert(null, [], reversed, 0);
}

function getShorterArray(first, second) {
    if (!first) return second;

    if (!second) return first;

    return first.length < second.length
        ? first
        : second;
}

function convert(previousShortest, result, remainder, power) {
    if (remainder === 0) return result;
    if (Math.abs(remainder) < Math.pow(2, power)) return null;
    if (previousShortest && result.length > previousShortest.length) return null;

    const remainderWith = remainder - Math.pow(-2, power);
    const resultWith = convert(previousShortest, result.concat(1), remainderWith, power + 1);

    const newShortest = getShorterArray(previousShortest, resultWith);
    const resultWithout = convert(newShortest, result.concat(0), remainder, power + 1);

    return getShorterArray(resultWithout, newShortest);
}


function parseMinusBinary(array) {
    return array.reduce(
        (previous, current, index) => previous + current * Math.pow(-2, index),
        0
    )
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
