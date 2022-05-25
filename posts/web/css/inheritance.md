---
layout: default
title: Inheritance
parent: CSS
grand_parent: Web
nav_order: 3
---

# Inheritance

```css
body {
  color: #444;
  font-size: 16px;
  font-family: sans-serif;

  border-top: 10px solid #1098ad;
}

h1 {
  color: #1098ad;
  font-size: 32px;
  text-transform: uppercase;
}
```

- Parent element의 property가 child element에 적용되는 것을 *Inheritance*라 한다.
- 위 예시에서 `body`의 property는 `h1`으로 상속되고 있다.
- 그러나 child element에서 만약 parent element의 property에 새로운 값을 할당하는 경우 상속받은 값을 덮어쓰게 되는데 이를 *Override*라 한다.
- 위에서 `color`, `font-size` property들은 override 된 것이다.
- **모든 property가 상속되는 것은 아니다**. 대부분 text와 관련된 애들만 상속된다고 생각하자.
