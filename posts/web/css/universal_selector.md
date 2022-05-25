---
layout: default
title: Universal Selector
parent: CSS
grand_parent: Web
nav_order: 4
---

# Universal Selector

```css
* {
  border-top: 10px solid #1098ad;
}

body {
  color: #444;
  font-family: sans-serif;
  border-top: 10px solid red;
}
```

- `*`로 시작되는 selector가 *Universal Selector*이다.
- Universal selector의 모든 property는 모든 element에 적용된다. **이는 Inheritance와 다르다.**
- 그러나 child element는 이를 쉽게 override 할 수 있다. e.g. `body`의 `border-top`
