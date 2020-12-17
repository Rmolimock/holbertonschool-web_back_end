export default function guardrail(mathFunction) {
  let res = 0;
  const queue = [];
  try {
    res = mathFunction();
  }
  catch (er) {
    res = `${er.name}: ${er.message}`;
  }
  queue.push(res);
  queue.push('Guardrail was processed');
  return queue;
}
