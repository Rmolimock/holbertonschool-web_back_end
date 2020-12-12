export default function iterateThroughObject(reportWithIterator) {
  let each = '';
  let nxt = reportWithIterator.next();
  while (!nxt.done) {
    each += `${nxt.value} | `;
    nxt = reportWithIterator.next();
  }
  return each.slice(0, each.length - 3);
}
