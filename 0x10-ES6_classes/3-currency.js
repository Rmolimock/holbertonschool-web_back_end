// comment
export default class Currency {
    constructor(code, name) {
        this._code = code;
        this._name = name;
    }

    get code() {
        return this._code;
    }

    get name() {
        return this._name;
    }

    set code(value) {
        if (typeof value === 'string') {
            this._code = value;
        }
        else {
            throw TypeError('code must be a String')
        }
    }

    set name(value) {
        if (typeof value !== 'string') {
            throw TypeError('name must be a String')
        }
        else {
            this._name = name;
        }
    }

    displayFullCurrency() {
        return `${this._name} (${this._code})`
    }
}
