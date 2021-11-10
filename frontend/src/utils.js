/**
* Deep equal comparison between objects as per
* https://stackoverflow.com/a/32922084/5348860
*
* @param {Object} x
* @param {Object} y
* @returns boolean
*/
export const deepEqual = (x, y) => {
    const ok = Object.keys,
        tx = typeof x,
        ty = typeof y;
    return x && y && tx === 'object' && tx === ty
        ? ok(x).length === ok(y).length && ok(x).every((key) => deepEqual(x[key], y[key]))
        : x === y;
};


/*
Flattens a nested dict into a one dimensional mapping of
the concatenated keys to the leaf values.

Converts a dict like:
    {
        a: 1, 
        b: {c:2, d:3}, 
        f: {g: 4}
    }

Into: 
    {
        "a": 1,
        "b.c": 2,
        "b.d": 3,
        "f.g": 4
    }

*/
export function recursiveDictFlatten(dict, curpath = "") {
    let out = {};
    Object.entries(dict).forEach(([key, value]) => {
        if (_isDict(value)) {
            out = {...out, ...rx(value, _cleanName(curpath, key))}
        } else {
            out[_cleanName(curpath, key)] = value
        }
    })
    return out
}

function _isDict(value) {
    return typeof value == "object" 
        && !Array.isArray(value) 
        && value !== null
}

function _cleanName(curpath, key) {
    return (curpath + "." + key).replace(/^\./g, '');
}
