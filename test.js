var totalFruit = function (fruits) {
    let mpp = new Map();
    let l = 0, r = 0, maxLen = 0;

    while (r < fruits.length) {
        mpp.set(fruits[r], (mpp.get(fruits[r]) || 0) + 1);

        if (mpp.size > 2) {
            mpp.set(fruits[l], mpp.get(fruits[l]) - 1);
            if (mpp.get(fruits[l]) === 0) {
                mpp.delete(fruits[l]);
            }
            l++;
        }

        if (mpp.size <= 2) {
            maxLen = Math.max(maxLen, r - l + 1);
        }
        r++;
    }

    return maxLen;
};

totalFruit()