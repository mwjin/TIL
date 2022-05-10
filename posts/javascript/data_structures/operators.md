---
layout: default
title: Operators
parent: Data Structures
grand_parent: Javascript
nav_order: 1
---

# Operators

## Array Destructuring

- 다음과 같이 element-wise assignment를 수행할 수 있다.

  ```javascript
  const arr = [1, 2, 3];
  const [x, y, z] = arr;
  console.log(x, y, z); // 1 2 3
  ```

- 중간 element를 스킵하고 assignment를 할 수 있다.

  ```javascript
  const arr = [1, 2, 3];
  const [first, , last] = arr;
  console.log(first, last); // 1 3
  ```

- 변수 간 value swap을 할 수 있다.

  ```javascript
  let [x, y] = [1, 2];
  [y, x] = [x, y];
  console.log(x, y); // 2 1
  ```

- Nested array에 대해서도 destructuring 할 수 있다.

  ```javascript
  const nested = [1, 2, [3, 4]];
  const [aa, bb, [cc, dd]] = nested;
  console.log(aa, bb, cc, dd); // 1 2 3 4
  ```

- Array destructuring으로 value assign 시 default 값을 지정할 수 있다.

  ```javascript
  const [p = 1, q = 2, r = 3] = [4, 5];
  console.log(p, q, r); // 4 5 3
  ```

## Object Destructuring

다음과 같은 object가 있다고 하자.

```javascript
const restaurant = {
  name: "Classico Italiano",
  location: "Via Angelo Tavanti 23, Firenze, Italy",
  categories: ["Italian", "Pizzeria", "Vegetarian", "Organic"],
  starterMenu: ["Focaccia", "Bruschetta", "Garlic Bread", "Caprese Salad"],
  mainMenu: ["Pizza", "Pasta", "Risotto"],

  openingHours: {
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
  },

  order: function (starterIndex, mainIndex) {
    return [this.starterMenu[starterIndex], this.mainMenu[mainIndex]];
  },

  orderDelivery: function ({ startIndex = 0, mainIndex = 1, address, time }) {
    console.log(
      `Order delivered! ${this.starterMenu[startIndex]} and ${this.mainMenu[mainIndex]} to ${address} at ${time}`
    );
  },
};
```

- 특정 필드들을 가져오기

  ```javascript
  // 각 key에 해당하는 value들을 그대로 assign
  const { name, openingHours, categories } = restaurant;
  ```

- 다른 이름의 변수에 값을 assign하기

  ```javascript
  const {
    name: restaurantName,
    openingHours: hours,
    categories: categoryNames,
  } = restaurant;
  ```

- Destructuring 시 변수에 default 값 부여하기

  ```javascript
  const { menu = [], categories: categoryNames2 } = restaurant;
  console.log(menu, categoryNames2);
  ```

- Destructuring으로 변수 변경하기

  ```javascript
  let a = 1;
  let b = 2;
  const obj = { a: 11, b: 22, c: 12 };
  ({ a, b } = obj);
  console.log(a, b); // 11 22
  ```

  `{a, b} = obj`는 되지 않는데 그 이유는 `const`, `let`이 없는 `{}`는 code block으로 인식하기 때문이다.

- Nested object destructuring

  ```javascript
  // openingHours is equal to restaurant.openingHours
  const {
    fri: { open: o, close: c },
  } = openingHours;
  console.log(o, c); // 11 23
  ```

- Object destructuring 이용하여 함수에 인자 넘기기

  ```javascript
  restaurant.orderDelivery({
    startIndex: 1,
    mainIndex: 2,
    time: "13:00",
    address: "Seoul",
  });
  ```

  - 실제로는 오직 하나의 인자로서 object를 넘겨준 것이다.
  - 인자의 순서를 신경쓰지 않아도 된다는 것이 장점이다.
  - Object destructuring 규칙은 위에서 소개한 다른 규칙들과 똑같이 적용된다. (e.g. default value 설정 가능)

## Spread Operator

### Array

- 기본적인 동작은 다음과 같다.

  ```javascript
  const arr1 = [1, 2, 3];
  const arr2 = [...arr1, 4, 5];
  console.log(arr2); // [1, 2, 3, 4, 5];
  console.log(...arr2); // 1 2 3 4 5
  ```

  Array destructuring과 달리 array 상의 모든 요소들을 추출하며, 별도의 변수를 지정하지 않는다.

- Shallow Copy

  ```javascript
  const newArr = [...arr];
  ```

- Merge

  ```javascript
  const mergeArr = [...arr1, ...arr2];
  ```

### Object

- ES2018 이후 object에 spread operator 적용이 가능해졌다.
- 기본 동작은 다음과 같다.

  ```javascript
  const obj1 = { a: 1, b: 2, c: 3 };
  const obj2 = { d: 4, e: 5, ...obj1 };
  console.log(obj2); // {d: 4, e: 5, a: 1, b: 2, c: 3}
  ```

- Shallow Copy

  ```javascript
  const copyObj = { ...obj1 };
  ```

### 추가 설명

- _Iterable_ 인 data structure는 모두 spread operator 적용이 가능하다.

  ```javascript
  const str = "abc";
  const letters = [...str, "", "F"];
  console.log(letters); // ["a", "b", "c", "", "F"]
  console.log(...str); // a b c
  ```

- Template literal 내부에 사용할 수 없다.

  ```javascript
  // Impossible!
  console.log(`${...str} Hello!`);
  ```

- 여러 인자를 함수로 넘겨줄 때 유용하다.

  ```javascript
  function add(a, b) {
    return a + b;
  }

  const args = [1, 2];
  console.log(add(...args)); // 3
  ```

## Rest Syntax

*Spread Operator*는 composite type을 여러 개의 element로 unpacking하는 것이라면, *Rest Syntax*는 여러 개의 element를 하나의 Array로 모으는 것이다.

### Element 모으기

- Array

```javascript
const [a, b, ...others] = [1, 2, 3, 4, 5];
console.log(others); // [3, 4, 5]
```

- Object

```javascript
const { x, ...otherObj } = { x: 1, y: 2, z: 3 };
console.log(otherObj); // {y: 2, z: 3}
```

### Function Parameter로 사용하기

```javascript
function useRest(...arguments) {
  console.log(arguments);
  console.log(...arguments);
}

// ['a', 1, 2, 3]
// a 1 2 3
useRest("a", 1, 2, 3);
```

### String

```javascript
const [h, ...o] = "apple";
console.log(o); // ['p', 'p', 'l', 'e']
```
