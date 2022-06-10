---
layout: default
title: Looping
parent: Data Structures and Operators
grand_parent: Javascript
nav_order: 2
---

# Looping

다음과 같이 데이터가 정의되어 있다고 가정하자.

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
};
const menu = [...restaurant.starterMenu, ...restaurant.mainMenu];
```

## Array

### For-of Loop

다음과 같이 간단하게 array 상에서 looping을 할 수 있다.

```javascript
for (const item of menu) console.log(item);
```

만약 index가 필요한 경우 다음과 같이 `entries` 메소드를 이용한다.

```javascript
for (const [i, item] of menu.entries()) {
  console.log(`${i + 1}: ${item}`);
}
```

## Object

### `Object.keys()`

```javascript
const properties = Object.keys(openingHours); // Array of the keys
console.log(properties);
```

인자로 넣는 object의 property 들을 array 형태로 return 한다.

```javascript
let openStr = `We are open on ${properties.length} days: `;

for (const day of Object.keys(openingHours)) {
  openStr += `${day}, `;
  console.log(day);
}
console.log(openStr);
```

`for-of` loop와 혼용하여 사용 시 유용하다.

### `Object.values()`

```javascript
const values = Object.values(openingHours);
console.log(values);
```

인자로 넣는 object property value들을 array 형태로 return 한다.

### `Object.entries()`

```javascript
const entries = Object.entries(openingHours);
console.log(entries);

for (const [day, { open, close }] of entries) {
  console.log(`On ${day} we open at ${open} and close at ${close}.`);
}
```

위와 같이 key와 value를 동시에 가져오고 싶은 경우 `entries` 메소드를 사용한다. 인자로 넣는 object의 각 property에 대한 `[key, value]`들을 array 형태로 return 한다.
