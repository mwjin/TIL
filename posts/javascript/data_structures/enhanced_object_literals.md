---
layout: default
title: Enhanced Object Literals
parent: Data Structures
grand_parent: Javascript
nav_order: 3
---

# Enhanced Object Literals

ES6 기준으로 enhanced 된 object literal을 정리하였다. 아래 데이터를 예시로 작성하였다.

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
console.log(menu);

// Looping Arrays: for-of loop
for (const item of menu) console.log(item);

// when we need indexes
for (const [i, item] of menu.entries()) {
  console.log(`${i + 1}: ${item}`);
}
```

## Nested Object

위 데이터에 대해 다음과 같이 정리 가능하다.

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

const restaurant = {
    ...,
    openingHours,
    ...
}
```

위와 같이 작성하면 자동으로 key가 `openingHours`인 object property가 만들어진다.

## New Method Syntax

```javascript
const restaurant = {
    ...,
    order(starterIndex, mainIndex) {
        return [this.starterMenu[starterIndex], this.mainMenu[mainIndex]];
    },
    ...
}
```

위와 같이 `function` 키워드 생략이 가능하다.

## Dynamic Property Keys

Object의 property name은 다음과 같이 expression으로 정의 가능하다.

```javascript
const weekdays = ["mon", "tue", "wed", "thu", "fri", "sat", "sun"];
const openingHours = {
  [weekdays[3]]: {
    open: 12,
    close: 22,
  },
  [weekdays[4]]: {
    open: 11,
    close: 23,
  },
  [weekdays[5]]: {
    open: 0, // Open 24 hours
    close: 24,
  },
  [`day-${2 + 4}`]: {
    open: 0,
    close: 24,
  },
};
```

Property name으로 사용할 expression을 `[]`로 감싸야 한다.
