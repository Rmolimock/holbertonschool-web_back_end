const assert = require('assert');
const calculateNumber = require('./1-calcul.js');

describe('calculateNumber', () => {
    it('correctly adds 3 and 3', () => {
        assert.equal(calculateNumber('SUM', 3, 3), 4);
    })
    it('correctly adds 2.88 and 5.88', () => {
        assert.equal(calculateNumber('SUM', 2.88, 5.88), 9);
    })
    it('correctly adds 0 and 3.3', () => {
        assert.equal(calculateNumber('SUM', 0, 3.3), 3);
    })
    it('correctly adds -3.3 and 3.3', () => {
        assert.equal(calculateNumber('SUM', -3.3, 3.3), 0);
    })
    it('correctly adds 3.5 and 3.5', () => {
        assert.equal(calculateNumber('SUM', 3.5, 3.5), 6);
    })
    it('correctly adds 3.9999999 and 3', () => {
        assert.equal(calculateNumber('SUM', 3.9999999, 3), 5);
    })
    it('correctly adds -0.4999999 and 0', () => {
        assert.equal(calculateNumber('SUM', -0.4999999, 0), 0);
    })
    it('correctly adds 0 and 0', () => {
        assert.equal(calculateNumber('SUM', 0, 0), 0);
    })
    it('correctly subtracts 3 and 3', () => {
        assert.equal(calculateNumber('SUBTRACT', 3, 3), -2);
    })
    it('correctly subtracts 2.88 and 5.88', () => {
        assert.equal(calculateNumber('SUBTRACT', 2.88, 5.88), -3);
    })
    it('correctly subtracts 0 and 3.3', () => {
        assert.equal(calculateNumber('SUBTRACT', 0, 3.3), -3);
    })
    it('correctly subtracts -3.3 and 3.3', () => {
        assert.equal(calculateNumber('SUBTRACT', -3.3, 3.3), -2);
    })
    it('correctly subtracts 3.5 and 3.5', () => {
        assert.equal(calculateNumber('SUBTRACT', 3.5, 3.5), 2);
    })
    it('correctly subtracts 3.9999999 and 3', () => {
        assert.equal(calculateNumber('SUBTRACT', 3.9999999, 3), 3);
    })
    it('correctly subtracts -0.4999999 and 0', () => {
        assert.equal(calculateNumber('SUBTRACT', -0.4999999, 0), 0);
    })
    it('correctly subtracts 0 and 0', () => {
        assert.equal(calculateNumber('SUBTRACT', 0, 0), 0);
    })
    it('correctly divides 3 and 3', () => {
        assert.equal(calculateNumber('DIVIDE', 3, 3), 0.3333333333333333);
    })
    it('correctly divides 2.88 and 5.88', () => {
        assert.equal(calculateNumber('DIVIDE', 2.88, 5.88), 0.5);
    })
    it('correctly divides 0 and 3.3', () => {
        assert.equal(calculateNumber('DIVIDE', 0, 3.3), 0);
    })
    it('correctly divides -3.3 and 3.3', () => {
        assert.equal(calculateNumber('DIVIDE', -3.3, 3.3), -3);
    })
    it('correctly divides 3.5 and 3.5', () => {
        assert.equal(calculateNumber('DIVIDE', 3.5, 3.5), 2);
    })
    it('correctly divides 3.9999999 and 3', () => {
        assert.equal(calculateNumber('DIVIDE', 3.9999999, 3), 4);
    })
    it('correctly divides -0.48999 and 0', () => {
        assert.equal(calculateNumber('DIVIDE', -0.48999, 0), 'ERROR');
    })
    it('correctly divides 1 and 0', () => {
        assert.equal(calculateNumber('DIVIDE', 1, 0), 'ERROR');
    })
})
