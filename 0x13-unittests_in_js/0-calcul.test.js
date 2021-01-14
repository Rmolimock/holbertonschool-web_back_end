const assert = require('assert');
const calculateNumber = require('./0-calcul.js');

describe('calculateNumber', () => {
    it('add 3 and 3', () => {
        assert.equal(calculateNumber(3, 3), 4)
    })
    it('add -3.93 and 3.93', () => {
        assert.equal(calculateNumber(-3.93, 3.93), 0)
    })
    it('add 3.95 and 3.95', () => {
        assert.equal(calculateNumber(3.95, 3.95), 4)
    })
    it('add 2.97 and 5.97', () => {
        assert.equal(calculateNumber(2.97, 5.97), 9)
    })
    it('add 0 and 3.93', () => {
        assert.equal(calculateNumber(0, 3.93), 3)
    })
    it('add 3 and 3.95', () => {
        assert.equal(calculateNumber(3, 3.95), 5)
    })
    it('add -0.94999999 and 0', () => {
        assert.equal(calculateNumber(-0.94999999, 0), 0)
    })
    it('add 3.99999999 and 3', () => {
        assert.equal(calculateNumber(3.99999999, 3), 5)
    })
    it('add 0 and 0', () => {
        assert.equal(calculateNumber(0, 0), 0)
    })
})
