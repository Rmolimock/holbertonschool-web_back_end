// comment
export default function getListStudentIds(array) {
  return array.reduce((acc, item,) => acc + item.id, 0);
}
