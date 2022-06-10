---
layout: default
title: Maps
parent: Data Structures and Operators
grand_parent: Javascript
nav_order: 5
---

# Maps

## Explain

```javascript
const rest = new Map();
// set => update the map
rest.set("name", "Classico Italiano");
rest.set(1, "Firenze, Italy");
```

- Object와 유사한 key-value pairs
- Object와 달리 string 외의 다른 type의 값들 또한 key로 사용이 가능하다.
- 특정 key 값들을 특정 value로 mapping 하기 위해 사용된다.
- key-value pair 데이터를 저장하고자 할 때 사용된다. Object 보다 performance 측면에서 좋다.
- **Key-value pair 데이터를 저장하기 위한 목적이라면 object 대신 map을 쓰자.**

## Methods

### `set()`

```javascript
rest.set("name", "Classico Italiano");
rest.set(1, "Firenze, Italy");
console.log(rest.set(2, "Lisbon, Portugal")); // Returns a map

// Chaining is also possible
rest
  .set("categories", ["Italian", "Pizzeria", "Vegetarian", "Organic"])
  .set("open", 11)
  .set("close", 23)
  .set(true, "We are open :D")
  .set(false, "We are closed :(");
```

- Map에 특정 key-value pair를 업데이트하기 위해 사용한다.
- 결과값으로 업데이트 된 map을 return 하기 때문에 chaining이 가능하다.

### `get()`

```javascript
console.log(rest.get("name"));
console.log(rest.get("true")); // undefined
console.log(rest.get(true));
```

- 특정 key에 mapping 된 value를 return 한다.
- 해당 key가 존재하지 않는 경우 `undefined`를 return

### `has()`

```javascript
console.log(rest.has("categories")); // true
```

- 특정 key가 존재하는지 확인한다.

### `delete()`

```javascript
rest.delete(2);
```

- 특정 key로 된 pair를 제거한다.

### `size`

```javascript
rest.size;
```

- Map에 저장된 key-value pair 개수를 return 한다.

## Collection type을 key로 사용할 때

```javascript
rest.set([1, 2], "Test"); // set the address of the array as a key
console.log(rest.get([1, 2])); // undefined
```

- *두 array literal 간 heap memory address가 다르다*는 점에 유의하라.

```javascript
const arr = [1, 2, 3];
rest.set(arr, "Test2");
console.log(rest.get(arr)); // work!
```

- Array를 key로 사용하고 싶다면 위와 같이 별도의 variable을 정의하자.

## Define Map from Other Data Structure

### Array

```javascript
const question = new Map([
  ["question", "What is the best programming language in the world?"],
  [1, "C"],
  [2, "Java"],
  [3, "Go"],
  [4, "Javascript"],
  ["Correct", 4],
  [true, "Correct :)"],
  [false, "Try again!"],
]);
```

### Object

```javascript
const openingHours = {
  thu: {
    open: 12,
    close: 22,
  },
  fri: {
    open: 11,
    close: 23,
  },
  sat: {
    open: 0, // Open 24 hours
    close: 24,
  },
};
const hoursMap = new Map(Object.entries(openingHours));
```

## Iteration

```javascript
for (const [key, value] of question) {
  if (typeof key === "number") console.log(`Answer ${key}: ${value}`);
}
```

- Array, Set과 유사한 방법으로 looping이 가능하다.
- Iteration 시 단일 item은 `[key, value]`로 되어 있다.

## Convert Map to Array

```javascript
console.log([...question]);
console.log([...question.entries()]);
console.log([...question.keys()]);
console.log([...question.values()]);
```

- `entries()`, `keys()`, `values()`를 통해 원하는 형태의 array를 만들 수 있다.
- 위 메소드들의 return type은 `MapIterator`이다. 따라서 별도의 spread operator를 사용해야 한다.
