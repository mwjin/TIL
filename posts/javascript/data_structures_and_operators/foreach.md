---
layout: default
title: forEach
parent: Data Structures and Operators
grand_parent: Javascript
nav_order: 8
---

# forEach

## Explain

- `Array`, `Set`, `Map`을 구성하는 element 각각에 대해 반복되는 연산들을 수행하고 싶은 경우 일반적으로 `for-of` loop를 사용한다. 이 loop 대신 `forEach` 메소드를 사용할 수 있다.
- 이 메소드의 인자는 callback function이다.
- `forEach`는 이 callback function을 각 element에 대해 수행하는 메소드이다.

## In Array

### Callback Function Arguments

- First: Current element
- Second: Its index
- Third: Entire array

### Example

```javascript
const movements = [200, 450, -400, 3000, -650, -130, 70, 1300];
movements.forEach(function (mov, i, arr) {
  const text =
    mov > 0 ? `You deposited ${mov}` : `You withdrew ${Math.abs(mov)}`;
  console.log(`Movement ${i + 1}: ${text}`);
});
```

forEach의 callback function을 각 element를 인자로 하여 호출하는 것과 같다.

## In Map

### Callback Function Arguments

- First: Current value
- Second: Its key
- Third: Entire map

### Example

```javascript
const currencies = new Map([
  ["USD", "United States dollar"],
  ["EUR", "Euro"],
  ["GBP", "Pound sterling"],
]);

currencies.forEach(function (value, key, map) {
  console.log(`${key}: ${value}`);
});
```

## In Set

### Callback Function Arguments

- First: Current value
- _Second: Current value_
- Third: Entire map

Set은 index 혹은 key가 존재하지 않아 두 번째 인자로 첫 번째 인자와 동일한 값이 들어온다.

### Example

```javascript
const currenciesUnique = new Set(currencies.keys());
// 'key' is redundant
currenciesUnique.forEach(function (value, key, set) {
  console.log(`${key}: ${value}`); // key === value
});
```

## vs. for loop

- `forEach`가 더 간결하다는 장점이 있다.
- `break`, `continue`와 같은 statement가 허용되지 않는다.
