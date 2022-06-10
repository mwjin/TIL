---
layout: default
title: Sets
parent: Data Structures and Operators
grand_parent: Javascript
nav_order: 4
---

# Sets

## Explain

```javascript
const ordersSet = new Set(["Pasta", "Pizza", "Pizza", "Risotto", "Pasta"]);
console.log(ordersSet); // {'Pasta', 'Pizza', 'Risotto'}
console.log(new Set("Minwoo"));
console.log(new Set());
```

- _고유한_ 값들에 대한 _unordered_ collection
- `new Set()` 을 통해 생성한다.
- Array에 비해 특정 요소를 찾거나 제거하는 과정이 더 빠르다.
- ES6부터 도입

## Methods

### `size`

```javascript
console.log(ordersSet.size); // 3
```

- Set의 크기를 조회

### `has()`

```javascript
console.log(ordersSet.has("Bread")); // false
console.log(ordersSet.has("Pizza")); // true
```

- 특정 값의 존재 유무를 조회

### `add()`

```javascript
ordersSet.add("Garlic Bread");
ordersSet.add("Garlic Bread"); // Nothing happened
```

- 특정 값을 추가
- 중복되는 값을 추가 시도하는 경우 아무 일도 발생하지 않는다.

### `delete()`

```javascript
ordersSet.delete("Risotto");
ordersSet.delete("Risotto"); // Nothing happened
```

- 특정 값을 제거
- 존재하지 않는 값을 제거하려고 하는 경우 아무 일도 발생하지 않는다.

### `clear()`

```javascript
ordersSet.clear();
console.log(ordersSet); // {} (Empty)
```

- Set에 있는 모든 값을 지운다.

## Looping

```javascript
for (const order of ordersSet) console.log(order);
```

Array와 유사한 방법으로 looping이 가능하다.

## Usage Examples

### Remove Duplicates

```javascript
const staff = ["Waiter", "Chef", "Waiter", "Manager", "Chef", "Waiter"];
const staffUnique = [...new Set(staff)];
console.log(staffUnique);
console.log(staffUnique.size);
```

Array 상의 중복되는 값을 제거하기 위해 자주 사용된다.

### String 상의 고유한 글자 개수 세기

```javascript
console.log(new Set("Minwoo Jeong").size); // 9
```
