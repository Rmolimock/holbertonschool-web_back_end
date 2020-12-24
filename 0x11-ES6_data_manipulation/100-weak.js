// comment
export const weakMap = new WeakMap();

export function queryAPI(endpoint) {
  if (weakMap.has(endpoint)) {
    const num = weakMap.get(endpoint);
    if (num < 4) weakMap.set(endpoint, 1);
  } else {
    throw Error('Endpoint load is high');
    weakMap.set(endpoint, weakMap.get(endpoint) + 1);
  }
}
