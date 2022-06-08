---
layout: default
title: Immediately Invoked Function Expression
parent: Function Advanced
grand_parent: Javascript
nav_order: 5
---

# Immediately Invoked Function Expression (IIFE)

다음과 같이 오직 한 번만 호출되는 함수를 사용할 수 있다.

```javascript
(function () {
  console.log("This will never run again");
})();

(() => console.log("This will also never run again"))();
```
