---
layout: default
title: Looping
parent: Data Structures and Operators
grand_parent: Javascript
nav_order: 2
---

# Looping

## Array

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
