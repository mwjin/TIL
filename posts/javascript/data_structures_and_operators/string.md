---
layout: default
title: String
parent: Data Structures and Operators
grand_parent: Javascript
nav_order: 6
---

# String

- 본 문서는 Javascript에서 string을 다룰 때 자주 사용되는 연산들을 모아둔 것이다.
- 더 많은 연산들은 [MDN String Document](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String)를 참조하자.

## Access to a specific character

```javascript
const plane = "A320";
console.log(plane[0]); // A
console.log(plane[1]); // 3
console.log(plane[2]); // 2
console.log("B237"[0]); // B
```

## String Length

`length` property를 이용한다.

```javascript
const airline = "TAP Air Portugal";
console.log(airline.length); // 16
```

## Find an index

`indexOf()`, `lastIndexOf()` 가 있다.

```javascript
// Find index
console.log(airline.indexOf("r")); // the first occurrence of the letter, 0-based
console.log(airline.lastIndexOf("r")); // 10
console.log(airline.indexOf("Portugal")); // 8 (the first occurrence of the string)
console.log(airline.indexOf("portugal")); // -1 (Nor found)
```

## Slice

`slice()` 메소드 사용 시 새로운 string을 return 한다.

```javascript
console.log(airline.slice(4)); // Air Portugal
console.log(airline.slice(4, 7)); // Air
console.log(airline.slice(0, airline.indexOf(" "))); // first word
console.log(airline.slice(airline.lastIndexOf(" ") + 1)); // last word
```

Slice 인자로 음수 `-n (n > 0)` 가 들어가면 _마지막에서 n번째를_ 의미한다.

```javascript
console.log(airline.slice(-2)); // the last two characters
console.log(airline.slice(1, -1));
```

## Change capitalization

`toLowerCase()`, `toUpperCase()`를 이용한다.

```javascript
console.log(airline.toLowerCase());
console.log(airline.toUpperCase());
```

### Example

```javascript
const passenger = "MiNWoo";
const passengerLower = passenger.toLowerCase();
const passengerCorrect =
  passengerLower[0].toUpperCase() + passengerLower.slice(1);
console.log(passenger, passengerCorrect);
```

## Trim

`trim()`은 String 양 옆의 whitespace들을 제거한다.

```javascript
const email = "hello@minwoo.io";
const loginEmail = "  Hello@Minwoo.Io \n";
const normalizedEmail = loginEmail.toLowerCase().trim();
console.log(normalizedEmail); // hello@minwoo.io
console.log(email === normalizedEmail);
```

## Replace substring

`replace(A, B)`는 첫 번째로 만난 A를 B로 치환하는 반면, `replaceAll(A, B)`는 모든 A를 B로 치환한다.

```javascript
const announcement =
  "All passengers come to barding door 23, Boarding door 23!";
console.log(announcement.replace("door", "gate")); // change the first occurrence
console.log(announcement.replaceAll("door", "gate")); // change all occurrences
console.log(announcement.replace(/door/g, "gate")); // with regex
```

## Check the occurrence of a substring

`includes()`, `startsWith` 가 있다.

```javascript
const plane2 = "Airbus A320neo";
console.log(plane2.includes("A320")); // true
console.log(plane2.includes("Boeing")); // false
console.log(plane2.startsWith("Air")); // true
console.log(plane2.startsWith("Aib")); // false
```

## Split a string

`split(delim)`은 `delim`을 기준으로 string을 쪼갠다.

```javascript
const [firstName, lastName] = "Minwoo Jeong".split(" ");
console.log(firstName); // Minwoo
console.log(lastName); // Jeong
```

## Join strings

`join(delim)` 여러 string을 `delim`으로 이어주는 형태로 concatenation 한다.

```javascript
const newName = ["Mr.", , firstName, lastName.toUpperCase()].join(" ");
console.log(newName); // Mr.  Minwoo JEONG
```

### Capitalize Name

```javascript
const capitalizeName = function (name) {
  const names = name.toLowerCase().split(" ");
  const newNames = [];

  for (const n of names) {
    // newNames.push(n[0].toUpperCase() + n.slice(1));
    newNames.push(n.replace(n[0], n[0].toUpperCase()));
  }
  console.log(newNames.join(" "));
};
const passenger = "jessica ann smith davis";
capitalizeName(passenger);
capitalizeName("minwoo jeong");
```

### Padding

Target string의 길이가 지정한 길이만큼 될 때 까지 명시한 글자를 string의 앞 (`padStart`)또는 뒤(`padEnd`)에 padding 한다.

```javascript
const message = "Go to gate 23!";
console.log(message.padStart(25, "+").padEnd(30, "+")); // pad '+' at the front until length 25 and do the same thing at the end until length 35
console.log("Minwoo".padStart(25, "+").padEnd(30, "+"));
```

### Repeat

`repeat(n)` 메소드는 target string을 `n`번 반복한 string을 return 한다.

```javascript
const planesInLine = function (n) {
  console.log(`There are ${n} planes in line ${"🛩".repeat(n)}`);
};
planesInLine(10);
```

## String에 메소드를 적용할 수 있는 원리

- Javascript에서 string 자체는 primitive type이다.
- 그러나 method 사용 시 javascript에서 자동으로 `new String()`을 통해 object로 변환되는데, 이를 *Boxing*이라 한다..

```javascript
console.log(new String("Minwoo"));
console.log(typeof new String("Minwoo")); // object
console.log(typeof new String("Minwoo").slice(1)); // string
```
