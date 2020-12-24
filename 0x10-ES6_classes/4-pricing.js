// comment
import Currency from './3-currency'

export default class Pricing {
  constructor(amount, currency) {
    this._currency = currency;
    this._amount = amount;
  }

  set amount(amount) {
      if (typeof amount === 'number') {
        this._amount = amount;
      }
  }

  get amount() {
    return this._amount;
  }

  set currency(currency) {
      if (value instanceof Currency) {
        this._currency = currency;
      }
  }

  get currency() {
    return this._currency;
  }

  displayFullPrice() {
    return `${this.amount} ${this.currency.displayFullCurrency()}`;
  }

  static convertPrice(amount, conversionRate) {
    return amount * conversionRate;
  }
}
