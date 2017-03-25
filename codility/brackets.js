"use strict";

function solution(S) {
    const reference = prepareReference(S);

    for (let index = 0; index <= S.length; index++) {
        const opened = getOpenedOnLeft(reference, index);
        const closed = getClosedOnRight(reference, index);

        if (opened === closed) return index;
    }

    return 0;
}

function getOpenedOnLeft(referenceObject, amount) {
    return amount === 0
        ? 0
        : referenceObject.opening[amount - 1];
}

function getClosedOnRight(referenceObject, amount) {

    const lastClosing = referenceObject.closing[referenceObject.size - 1];
    const leftClosing = amount === 0
        ? 0
        : referenceObject.closing[amount - 1];

    return lastClosing - leftClosing;
}

function prepareReference(subjectString) {
    const array = subjectString.split('');

    let result = {
        opening: [],
        closing: [],
        size: array.length,
    };

    let open = 0;
    let close = 0;

    array.forEach(char => {
        if (char === ')') {
            close++;
        } else {
            open++;
        }
        result.closing.push(close);
        result.opening.push(open);
    });

    return result;
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

test('prepare', () => {
    const string = '(())';
    const res = prepareReference(string);
    expect(res).to.deep.equal(
        {
            opening: [1, 2, 2, 2],
            closing: [0, 0, 1, 2],
            size: 4,
        }
    )
});

test('left', () => {
        const string = '(())';
        const reference = prepareReference(string);

        expect(getOpenedOnLeft(reference, 0)).to.deep.equal(0);
        expect(getOpenedOnLeft(reference, 4)).to.deep.equal(2);
    }
);

test('right 1', () => {
        const string = '(())';
        const reference = prepareReference(string);

        expect(getClosedOnRight(reference, 2)).to.deep.equal(2);
    }
);

test('right 1', () => {
        const string = '(())';
        const reference = prepareReference(string);

        expect(getClosedOnRight(reference, 4)).to.deep.equal(0);
    }
);

test('right 3', () => {
        const string = '(())';
        const reference = prepareReference(string);

        expect(getClosedOnRight(reference, 0)).to.deep.equal(2);
    }
);

test('solution 1', () => {
        const string = '(())';
        expect(solution(string)).to.equal(2);
    }
);
test('solution empty', () => {
        const string = '';
        expect(solution(string)).to.equal(0);
    }
);
test('solution 2', () => {
        const string = '(';
        expect(solution(string)).to.equal(0);
    }
);
test('solution 3', () => {
        const string = ')';
        expect(solution(string)).to.equal(1);
    }
);


