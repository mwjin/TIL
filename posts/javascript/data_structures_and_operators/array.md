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
