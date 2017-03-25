const {expect}= require('chai');
const stripUrl = require('./stripUrl');

describe('Strip url', () => {
    it('exists', () => {
        expect(stripUrl).to.be.true;
    });
});cd