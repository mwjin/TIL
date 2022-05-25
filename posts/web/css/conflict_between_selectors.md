---
layout: default
title: Conflict Between Selectors
parent: CSS
grand_parent: Web
nav_order: 2
---

# Conflict Between Selectors

## Theory

한 CSS property에 여러 값이 동시에 적용될 수 있다. 다음 순서대로 우선 순위를 적용한다. (즉, 위로 갈수록 우선 순위가 높다.)

1. Declarations marked `!important`
2. Inline style (`style` attribute in _HTML_)
3. ID(`#`) selector
4. Class(`.`) or pseudo-class(`:`) selector
5. Element selector (`p`, `div`, `li`, etc.)
6. Universal selector(`*`)

위 리스트 상 동일한 우선 순위를 갖는 selector가 여러 개 있는 경우, 가장 나중에 작성된 selector가 적용된다.

## Example

다음과 같이 작성된 HTML과 CSS가 있다고 하자.

```html
<p id="copyright" class="copyright text">
  Copyright &copy; 2027 by The Code Magazine.
</p>
```

```css
/* lower priority than the other element selectors with pseudo-class */
a {
  color: red;
}

/* Theory 1: Conflicting Selector */
/* Resolving conflicts */
/* ID selector -> higher priority */
#copyright {
  color: red;
}

.copyright {
  color: blue;
}

/* Last Class Selector -> second priority */
.text {
  color: yellow;
}

footer p {
  color: green !important;
}
```

- `!important` 가 적시된 맨 아래의 selector의 property가 가장 우선 순위가 높다.
- 그 다음으로는 ID selector인 `#copyright` selector의 우선 순위가 높다.
- 그 다음으로는 `.text`이다. `.copyright`보다 나중에 작성되었기 때문이다.
- `.text`다음으로는 같은 class selector인 `.copyright`이다.
- `a`와 같은 element selector는 가장 낮은 우선 순위이다.

## Tip

- `!important`, inline styling을 하는 것은 추천하지 않는다.
- 어지간하면 class selector를 사용하자.
