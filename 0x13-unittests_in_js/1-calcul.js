module.exports = function calculateNumber(type, a, b) {
    const a = Math.round(a);
    const b = Math.round(b);

    if (type === 'SUM') return a + b;

    else if (type === 'SUBTRACT') return a - b;

    else if (type === 'DIVIDE')
        return bActual === 0 ? 'ERROR' : a / b;
}
