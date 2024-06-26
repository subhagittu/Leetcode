/**
 * @param {number[][]} intervals
 * @param {number[]} newInterval
 * @return {number[][]} 
 */
var insert = (intervals, newInterval) => {
  let [start, end] = newInterval;
  let ans = [];
  let pushed = false;
  for (let [currStart, currEnd] of intervals) {
    if (currEnd < start) {
      ans.push([currStart, currEnd]);
    } else if (currStart > end) {
      if (!pushed) {
        ans.push([start, end]);
        pushed = true;
      }
      ans.push([currStart, currEnd]);
    } else {
      start = Math.min(start, currStart);
      end = Math.max(end, currEnd);
    }
  }
  if (!pushed) {
    ans.push([start, end]);
  }
  return ans;
};
