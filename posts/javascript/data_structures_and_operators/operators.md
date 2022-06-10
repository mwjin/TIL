---
layout: default
title: Operators
parent: Data Structures and Operators
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

## Short Circuiting

### OR Logical Operator (||)

```javascript
console.log(3 || "minwoo"); // 3
console.log(null || "minwoo"); // minwoo
console.log(undefined || null); // null (even if it is falsy)
console.log(undefined || 0 || "" || "Hello" || 23 || null); // Hello
console.log(undefined || 0 || "" || null || undefined); // undefined
```

- **첫번째로 만난 truthy value expression을 return 한다.**
- truthy value가 없는 경우 맨 마지막 value expression을 return 한다.

#### Practical Example

```javascript
const obj = { a: 1, b: 2, c: 3 };
// const d = obj.d ? obj.d : 10;
const d = obj.d || 10;
console.log(d); // 10
```

### AND Logical Operator (&&)

```javascript
console.log(0 && "Minwoo"); // 0
console.log("Minwoo" && "Minho"); // Minho
console.log("Hello" && 23 && null && "Jonas"); // null
```

- **첫번째로 만난 falsy value expression을 return 한다.**
- Falsy value가 없는 경우 맨 마지막 value expression을 return 한다.

#### Practical Example

```javascript
// practical example
const obj2 = {
  add: function (a, b) {
    return a + b;
  },
};

/*
if (obj2.add) {
  obj2.add(1, 2)
}
*/
const result = obj2.add && obj2.add(1, 2);
console.log(result); // 3
```

위에서 `obj2.add(1, 2)` 같은 function call expression도 실행되고 난 뒤 그 결과값이 할당된다.

## Nullish Coalescing Operator (ES2020)

```javascript
const obj = { a: 1, b: 2, c: 3 };
const d = obj.d ?? 10;
console.log(d); // 10
```

- Short circuiting과 유사하게 `??` operator를 사용하면 _nullish가 아닌_ 첫 번째 value expression을 return 한다.
- **Nullish**: `null` or `undefined`
- 모두 nullish인 경우 맨 마지막 value expression이 return 된다.

### OR Logical Operator와 비교

```javascript
const obj = { a: 1, b: 2, c: 3 };
// const d = obj.d ? obj.d : 10;
obj.d = 0;
let d = obj.d || 10;
console.log(d); // 10, which is not what we intended to
d = obj.d ?? 10;
console.log(d); // 0
```

`0`은 *falsy*이나 *nullish*는 아니다. 때문에 위와 같은 결과값 차이가 발생한다.

## Logical Assignment Operators (ES2021)

다음과 같이 두 오브젝트가 정의되어 있다고 가정하자.

```javascript
const rest1 = {
  name: "Capri",
  numGuests: 20,
};

const rest2 = {
  name: "La Pizza",
  owner: "Giovanni Rossi",
};
```

### OR assignment operator

```javascript
rest1.numGuests ||= 10; // rest1.numGuests = rest1.numGuests || 10;
rest2.numGuests ||= 10; // rest2.numGuests = rest2.numGuests || 10;
console.log(rest1.numGuests); // 20
console.log(rest2.numGuests); // 10
```

### Nullish assignment operator

```javascript
rest1.numGuests ??= 10; // rest1.numGuests = rest1.numGuests ?? 10;
rest2.numGuests ??= 10; // rest2.numGuests = rest2.numGuests ?? 10;
console.log(rest1.numGuests); // 20
console.log(rest2.numGuests); // 10
```

### AND assignment operator

```javascript
rest1.owner &&= "<ANONYMOUS>"; // nothing happened because the variable does not exist
rest2.owner &&= "<ANONYMOUS>";
console.log(rest1); // undefined
console.log(rest2); // "<ANONYMOUS>"
```

위에서 `rest1.owner &&= "<ANONYMOUS>"`는 `rest1.owner = rest1.owner && "<ANONYMOUS>"`와 같지 않다. `rest1.owner` 가 존재하지 않는 경우 `&&=`는 아무런 동작을 수행하지 않는 반면, 후자는 `rest1.owner`가 `undefined`로 할당된다.

## Optional Chaining

### Object

위 `restaurant` object에서

```javascript
// console.log(restaurant.openingHours.mon.open); // Reference Error

console.log(restaurant.openingHours.mon?.open); // undefined
console.log(restaurant.openingHours.fri?.open); // 11
```

위와 같이 object 상 존재하지 않는 property (`mon`)에 접근할 때 **에러 대신 `undefined`를 return** 하도록 하고 싶은 경우 `?.`로 해당 object에 접근하면 된다. 복잡한 `if-else`문을 사용하지 않아도 된다는 장점이 있다.

### Multiple Optional Chaining

```javascript
console.log(restaurant.openingHours?.mon?.open); // undefined
```

위와 같이 사용할 수 있다.

### Access with Dynamic Property Keys

```javascript
const days = ["mon", "tue", "wed", "thu", "fri", "sat", "sun"];

for (const day of days) {
  const open = restaurant.openingHours[day]?.open ?? "closed"; // with dynamic property key
  console.log(`On ${day}, we open at ${open}.`);
}
```

Dynamic property key로 접근하고 싶을 때는 dot notation 대신 `[]`을 사용한다. 이 뒤에 `?.`를 붙여 optional chaining을 할 수 있다.

### Method

```javascript
console.log(restaurant.order?.(0, 1) ?? "Method does not exist");
console.log(restaurant.otherOrder?.(0, 1) ?? "Method does not exist"); // Method does not exist
```

Method 명 바로 뒤에 `?.(...args)` 와 같은 형태로 작성함으로써 optional 하게 호출할 수 있다. Method가 존재하지 않는 경우 `undefined`를 return 한다.

### Array

```javascript
const users = [{ name: "Minwoo", email: "Hello@World.com" }];

/*
if (users.length > 0) console.log(users[0].name);
else console.log('User array empty');
*/

console.log(users[0]?.name ?? "User array empty");
console.log(users[1]?.name ?? "User array empty"); // User array empty
```

위와 같이 `[]` 뒤에 `?.`를 붙이는 식으로 사용할 수도 있다.
