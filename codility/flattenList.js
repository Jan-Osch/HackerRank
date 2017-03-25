/**
 ============================
 * Flattenlist * 15 minutes *
 ============================


 Devise a function that accepts an arbitrarily-nested array with elements of arbitrary types, and returns a flattened version of it. Do not solve the task using a built-in function that can accomplish the whole task on its own.

 Example:
 ["This is a string", 1, 2, [3], [4, [5, 6]], [[7]], 8, "[10, 11]"] -> ["This is a string", 1, 2, 3, 4, 5, 6, 7, 8, "[10, 11]"]

 ===========
 Test cases:

 [1, 2, [3], [4, [5, 6], 5, 6], [[7], [8, [9]]], 10] -> [1, 2, 3, 4, 5, 6, 5, 6, 7, 8, 9, 10]
 [1, 2, [3], [4, [5, 6], 5, 6], [[7], [8, [9]]], 10, [[[11], 12]]] -> [1, 2, 3, 4, 5, 6, 5, 6, 7, 8, 9, 10, 11, 12]
 [1, "a", "b", [ "c", ["d",2 ] ], "e", [ [ [ "f" ] ] ] ] -> [ 1, "a", "b", "c", "d", 2, "e", "f" ]

 */
"use strict";


function flattenList(subject) {
    return Array.isArray(subject)
        ? subject.reduce(
        (previous, current) => {
            const flattened = flattenList(current);

            return previous.concat(flattened);
        },
        []
    )
        : [subject]
}

function arraysAreEqual(array1, array2) {
    if (array1.length !== array2.length) {
        return false;
    }

    for (let i = 0; i < array1.length; i++) {
        if (array1[i] !== array2[i]) {
            return false;
        }
    }

    return true;
}

console.log('Case 0', flattenList([]));
console.log('Case 1', flattenList([1, 2, [3], [4, [5, 6], 5, 6], [[7], [8, [9]]], 10]));
console.log('Case 2', flattenList([1, 2, [3], [4, [5, 6], 5, 6], [[7], [8, [9]]], 10, [[[11], 12]]]));
console.log('Case 3', flattenList([1, "a", "b", ["c", ["d", 2]], "e", [[["f"]]]]));

