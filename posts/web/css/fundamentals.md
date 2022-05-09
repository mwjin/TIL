---
layout: default
title: Fundamentals
parent: CSS
grand_parent: Web
nav_order: 1
---

# Fundamentals

## CSS를 HTML에 적용하기

- Inline CSS: HTML tag의 `style` attribute로 직접 입력 (not recommended)
- Internal CSS: HTML `<head>`에 `<style>` tag를 만들고 content로 CSS을 embedding
- **External CSS**: `style.css` 파일에 CSS를 모아두고 `index.html`에 다음과 같이 입력

  ```html
  <head>
    <link href="style.css" rel="stylesheet" />
  </head>
  ```

## CSS Rule

```css
h1 {
  color: blue;
  font-family: sans-serif;
  text-transform: uppercase;
  font-style: italic;
}
```

- `h1`: Selector
- `{...}`: Declaration block
- `color: blue;`와 같은 line: Declaration / Style
  - `color` : Property
  - `blue`: Value

## Combine Selectors

```css
h1,
h2,
h3,
h4,
p,
li {
  font-family: sans-serif;
}
```

위와 같이 각 selector에서 공통된 style만 모을 수 있다.

## Descent Selector

```css
footer p {
  font-size: 16px;
}

article header p {
  font-style: italic;
}
```

`footer p`는 `footer` 내에 속한 `p`를 가리킨다.

## ID Selector

```css
/*
<p id="author">
  Posted by <strong>Laura Jones</strong> on Monday, June 21st 2027
</p>
*/
#author {
  font-style: italic;
  font-size: 18px;
}
```

**Note.** `id` 값은 unique하다.

## Class Selector

```css
/*  <p class="related-author">By Jonas Schmedtmann</p>
*/
.related-author {
  font-size: 18px;
  font-weight: bold;
}
```

- Class 값은 unique하지 않다.
- **거의 대부분 id selector 대신 class selector를 사용함에 유의.** 이는 미래의 변화에 대비하기 위함이다.

## Color

```css
h3 {
  color: #1098ad;
  background-color: #f7f7f7;
}
```

- 대표적인 Properties: `color`, `background-color`
- 일반적으로 *hexadecimal color*를 이용
- Transparency를 적용하는 경우 _rgba_

## Pseudo Classes

```css
li:first-child {
  font-weight: bold;
}

li:last-child {
  font-style: italic;
}

li:nth-child(2) {
  color: red;
}
```

- `li:first-child`는 해석하면 무언가의 (e.g. `ul`) *첫번째 child element*인 `li`이다. 첫번째 `li`여도 첫번째 child element가 아니면 적용되지 않는다.

### Hyperlink에 대한 Style Pseudo Classes

```css
/* Styling links */
/* Only targets 'a' that has 'href' attribute */
a:link {
  color: #1098ad;
  text-decoration: none;
}

a:visited {
  color: #1098ad;
}

a:hover {
  font-weight: bold;
  color: orangered;
  text-decoration: underline dotted orangered;
}

a:active {
  background-color: black;
  font-style: italic;
}
```

- `:link`: 오직 `href` attribute를 가지고 있는 `a` element
- `:visited`: 이미 클릭한 경우
- `:hover`: 마우스를 올려둔 경우
- `active`: 클릭한 경우
- **LVHA**: Hyperlink에 대한 pseudo-class는 `link` -> `visited` -> `hover` -> `active` 순으로 정의하자.
  - 이유는...?
