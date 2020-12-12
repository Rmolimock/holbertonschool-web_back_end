export default function appendToEachArrayValue(array, appendString) {
  const ret = [];
  for (const v of array) {
    ret.append(appendString + v);
  }
  return ret;
}
