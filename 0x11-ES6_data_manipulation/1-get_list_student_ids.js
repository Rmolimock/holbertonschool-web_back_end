// comment
export default function getListStudentIds(array) {
  if (Array.isArray(array)) return array.map((item) => item.id);
  return [];
}
