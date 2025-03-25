export default function appendToEachArrayValue(array, appendString) {
  const result = [];
  for (const [index, value] of array.entries()) {
    result[index] = appendString + value;
  }
  return result;
}
