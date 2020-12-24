// comment
export default function updateUniqueItems(map) {
  if (map instanceof Map) {
    for (const i of map.entries()) {
      if (i[1] === 1) map.set(i[0], 100);
    }
    return map;
  } throw Error('Cannot process');
}
