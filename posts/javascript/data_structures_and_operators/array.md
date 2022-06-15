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
