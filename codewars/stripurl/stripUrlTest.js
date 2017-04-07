const {expect} = require('chai');

const stripUrlParams = require('./stripUrlParams');

describe('Strip url', () => {
    it('should exists', () => {
        expect(stripUrlParams).to.be.defined;
    });

    const examples = [
        {
            input: 'www.codewars.com?a=1&b=2&a=2',
            expected: 'www.codewars.com?a=1&b=2'
        },
        {
            input: 'www.codewars.com?a=1&b=2&a=2',
            params: ['b'],
            expected: 'www.codewars.com?a=1'
        },
        {
            input: 'www.codewars.com',
            params: ['b'],
            expected: 'www.codewars.com'
        },
    ];

    examples.forEach(
        example => it(`${example.input} with params: ${example.params} should return ${example.expected}`, () => {
            expect(stripUrlParams(example.input, example.params)).to.equal(example.expected);
        })
    );
});