---
layout: default
title: Array
parent: Data Structures and Operators
grand_parent: Javascript
nav_order: 7
---

# Array

- Javascript Array에 대한 advanced method들을 정리.
- 더 많은 내용은 [MDN Array Document](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array) 참조.

## `slice(...)`

- Target array의 subarray를 *새로 생성*하여 return
- String의 `slice()` method와 사용법은 유사하다.

```javascript
console.log(arr.slice(2));
console.log(arr.slice(2, 4));
console.log(arr.slice(-2));
console.log(arr.slice(-1));
console.log(arr.slice(1, -2));
```

- Array를 새로 생성하여 return 한다는 점을 이용, 다음과 같이 *shallow copy*를 할 수 있다.

```javascript
console.log(arr.slice());
// Equal to console.log([...arr]);
```

## `splice(...)`

- Target array로부터 element들을 제거하기 위해 사용한다.
- Arguments
  - First: 제거할 element들의 array 상 첫 번째 index
  - Second: 제거할 element들의 개수
- 제거한 element들로 구성된 array를 return한다.
- **이 메소드는 target array 자체를 바꾸는 것에 유의하자.**

```javascript
const arr = ["a", "b", "c", "d", "e"];
console.log(arr.splice(-1)); // ["e"] (Remove the last element)
console.log(arr); // ['a', 'b', 'c', 'd']
console.log(arr.splice(1, 2)); // ['b', 'c']
console.log(arr); // ['a', 'd']
```

## `reverse()`

- Target array의 원소들을 거꾸로 재배치한다.
- **이 메소드는 target array 자체를 바꾸는 것에 유의하자.**

```javascript
const arr = [1, 2, 3, 4, 5];
console.log(arr.reverse()); // [5, 4, 3, 2, 1]
console.log(arr); // [5, 4, 3, 2, 1]
```

## `concat(...)`

- 두 array를 concatenation 한 형태의 array를 새로 만들어 return한다.

```javascript
const arr1 = [1, 2, 3];
const arr2 = [4, 5, 6];
const nums = arr1.concat(arr2);
console.log(nums); // [1, 2, 3, 4, 5, 6]
```

## `join(...)`

- Array 내의 모든 element들을 하나의 string으로 concatenate하여 return 한다.
- Delimeter를 인자로 하는 경우 각 element는 이 delimeter로 구분된다.
- Argument가 없는 경우 default로 `,`로 구분한다.

```javascript
const letters = ["a", "b", "c"];
console.log(letters.join(",")); // 'a,b,c'
console.log(letters.join("+")); // 'a+b+c'
console.log(letters.join()); // 'a,b,c'
console.log(letters.join("")); // 'abc'
```

## `at(...)` (ES2022)

- Array의 element를 조회할 때 사용한다.
- `[]`와 유사한 동작을 하나 negative index가 지원된다.

```javascript
const arr = [23, 11, 54];
console.log(arr.at(0)); // 23 (equal to arr[0])
console.log(arr.at(-1)); // 54 (equal to arr[arr.length - 1])
```

## `map(callbackfn)`

### Explain

- 한 array를 바탕으로 또 다른 array를 만들고자 할 때 사용하는 method
- 인자로 넣은 `callbackfn`을 바탕으로 각 element로부터 새로운 element를 계산한다.
- 새로운 array는 위에서 생성된 새로운 element들로 구성된 array이다.

```javascript
const arr = [3, 1, 4, 3, 2];
console.log(arr.map((v) => v * 2)); // [6, 2, 8, 6, 2]
```

### Callback Function

Callback function은 다음과 같은 형태를 가질 수 있다.

```javascript
function (value, i, arr) {
  ...
}
```

각 인자에 대한 설명은 다음과 같다.

- `value`: Current element
- `i`: Current index of the element
- `arr`: Current array

`i`, `arr`가 필요하지 않은 경우 `value`만 받는 형태의 callback function을 사용한다.

### vs. `forEach`

- `map`의 callback function 은 새로운 array를 생성하기 위한 value를 return 한다.
- `forEach`는 새로운 array를 생성하기 위한 용도가 아니다. 단, callback function으로 각 element를 print하는 등의 동작을 수행할 수 있으며 이를 *side effect*라고 한다.

## `filter(callbackfn)`

- 기존 array의 각 element들에 대해 callback function을 수행 시, `true`인 element들만 포함하여 새로운 array를 만든다.
- `callbackfn`의 형태는 `map`의 callback function과 동일하다.

```javascript
const arr = [3, 1, 4, 3, 2];
console.log(arr.filter((v) => v > 2)); // [3, 4, 3]
```

## `reduce(callbackfn, [initial value])`

### Explain

- Array로부터 callback function을 바탕으로 single value를 만든다.
- Callback function의 인자로 *accumulator*가 들어가는데, `initial value`는 이에 대한 초기값이다.
- Callback function은 이 accumulator와 array 상의 각 element 간의 연산들로 구성되어 있다.

```javascript
const arr = [3, 1, 4, 3, 2];
console.log(arr.reduce((acc, v) => acc + v, 0)); // 13
```

### Callback Function

Callback function은 다음과 같은 형태를 가질 수 있다.

```javascript
function (acc, value, i, arr) {
  ...
}
```

- `acc`: *Accumulator*로, 이 callback function의 return 값은 이 accumulator에 누적된다.
- 그 외의 인자에 대한 설명은 `map`과 같다.
- `i`와 `arr`는 callback function을 정의하여 사용할 수 있다.

### Initial Value

`reduce`의 두 번째 인자로 들어가는 initial value는 위 callback function의 `acc`에 대한 초기값이다.

### Example: Get the maximum value

```javascript
const maxValue = arr.reduce((acc, value) => Math.max(acc, value), arr[0]);
```

## `find(callbackfn)`

- Array 상에서 `callbackfn`에 명시된 condition을 충족하는 _첫번째_ element를 찾아준다.
- 없으면 `undefined`를 return한다.
- `filter`는 condition을 충족하는 element들을 모아 새로운 array를 만든다면, `find`는 single value를 return 한다는 차이가 있다.
- `callbackfn`의 형태는 `map`의 callback function과 동일하다.

```javascript
const account = accounts.find((acc) => acc.owner === "Jessica Davis");
console.log(account);
```

## `findIndex(callbackfn)`

- Array 상에서 `callbackfn`에 명시된 condition을 충족하는 _첫번째_ element의 index를 return한다.
- 없으면 `-1`을 return한다.
- `indexOf`는 value를 인자로 받는 반면, `findIndex`는 찾는 value의 condition을 명시한다는 차이가 있다.
- `callbackfn`의 형태는 `map`의 callback function과 동일하다.

```javascript
const accountIdx = accounts.find((acc) => acc.owner === "Jessica Davis");
console.log(accounts[accountIdx]);
```

## `some(callbackfn)`

- Array에서 어느 한 element라도 `callbackfn`으로 명시된 조건을 만족하면 `true`를 `return`한다.
- `includes` method는 value를 인자로 받는 반면, `some`은 조건을 인자로 받는다는 차이가 있다.
- `callbackfn`의 형태는 `map`의 callback function과 동일하다.

```javascript
const anyDeposits = movements.some((mov) => mov > 0);
console.log(anyDeposits);

// the below statements are the same
console.log(movements.includes(-130));
console.log(movements.some((mov) => mov === -130));
```

## `every(callbackfn)`

- Array 상 모든 element가 `callbackfn`으로 주어진 조건을 만족하는 경우 `true`
- `callbackfn`의 형태는 `map`의 callback function과 동일하다.

```javascript
console.log(movements.every((mov) => mov > 0)); // false
console.log(movements.every((mov) => mov !== 0)); // true
```

## `flat([depth])`

### Explain

Nested array를 평평하게 만든다.

```javascript
const arr = [[1, 2, 3], [4, 5, 6], 7, 8];
console.log(arr.flat()); // [1, 2, 3, 4, 5, 6, 7, 8]
```

Default로 깊이 1까지만 평평하게 만들며, 1 이상의 깊이에 있는 element들 또한 꺼내고 싶다면 `depth`에 원하는 깊이를 인자로 넘겨줘야 한다.

```javascript
const arrDeep = [[[1, 2], 3], [4, [5, 6]], 7, 8];
console.log(arrDeep.flat()); // [Array(2), 3, 4, Array(2), 7, 8]

// two levels deep
console.log(arrDeep.flat(2)); // [1, 2, 3, 4, 5, 6, 7, 8]
```

### Practical Example

주로 다음과 같이 `map` 과 함께 사용한다.

```javascript
const overallBalance = accounts
  .map((account) => account.movements)
  .flat()
  .reduce((acc, mov) => acc + mov, 0);
console.log(overallBalance);
```

## `flatMap()`

- 위 **practical example**처럼 `map` 다음 `flat`을 chaining으로 사용하는 패턴이 흔하여 아예 이 둘을 합친 `flatMap()` 메소드가 정의되었다.
- _깊이 1까지_ 밖에 못하는 것에 유의하자.

```javascript
// flatMap (map + flat)
const overallBalance2 = accounts
  .flatMap((account) => account.movements)
  .reduce((acc, mov) => acc + mov, 0);
console.log(overallBalance2);
```

## `sort([callbackfn])`

### Explain

- Array 내부 구성 요소들을 정렬하기 위해 사용하는 method로
- 새로운 array를 return 하는 것이 아닌 *기존 array 내용 자체를 변경*하는 동작임에 유의하자.

```javascript
const owners = ["Minwoo", "Jonas", "Adam", "Zck"];
console.log(owners.sort()); // ['Adam', 'Jonas', 'Minwoo', 'Zck']Mutate the original array
console.log(owners); // ['Adam', 'Jonas', 'Minwoo', 'Zck']
```

### Sorting based on strings

- `sort` method 자체가 기본적으로 구성 요소들을 string이라고 가정하고 sorting 한다.
- String이 아니라도 string으로 conversion 된 결과를 바탕으로 sorting 한다.
- Sorting을 위한 key function이 `String(...)`이라 생각하자.

```javascript
const arr = [-2, -1, 0, 1, 2];
console.log(arr.sort()); // [-1, -2, 0, 1, 2]
```

### Sorting based on numbers

- String 기반이 아닌 number 자체를 기반으로 sorting 하려면 별도의 callback 함수를 정의해야 한다.
- Callback 함수는 `(a, b) => ....` 와 같이 두 개의 인자로 정의할 수 있으며, `a`, `b`는 array를 구성하고 있는 연속적인 두 구성 요소들이다.
- Callback function의 결과가 음수이면 순서를 유지하고, 양수이면 순서를 바꾼다.
- 따라서 다음과 같이 sorting 할 수 있다.

```javascript
const arr = [1, -4, 3, 2, -2, 0];

// Ascending order: [-4, -2, 0, 1, 2, 3]
console.log(arr.sort((a, b) => a - b));

// Descending order: [3, 2, 1, 0, -2, -4]
console.log(arr.sort((a, b) => b - a));
```
