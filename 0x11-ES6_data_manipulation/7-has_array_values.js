// comment
export default function hasValuesFromArray(set, array) {
  for (const i of array) if (set.has(i)) return true;
  return false;
}
