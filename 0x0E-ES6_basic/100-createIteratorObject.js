export default function createIteratorObject(report) {
  let full = Object.values(report.fullEmployees).reduce((a, b) => {
    a.push(...b);
    return a;
  }, []);
  let current = 0;
  let end = full.length;
  return {
    next() {
      if (current > end) {
        return { value: null, done: true };
    }
      let result = { value: full[current], done: false };
      current += 1;
      return result;
    },
    [Symbol.iterator]: () => this.next(),};
}
