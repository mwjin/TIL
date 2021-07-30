---
layout: default
title: Basics
parent: HTML
grand_parent: Web
nav_order: 1
---

# Basics

## Basic HTML Structure

기본적인 HTML structure는 다음과 같다.

```html
<!DOCTYPE html>
<html>
  <head></head>
  <body></body>
</html>
```

- `<!DOCTYPE html>`
  - 웹 브라우저에게 해당 문서가 HTML format으로 인식되어야 함을 알린다.
  - 웹 브라우저는 이 태그를 인지하면 _HTML5 specification_(?) 을 통해 해당 파일을 렌더링한다.
- `<html>`
  - 모든 HTML element 들의 **root**가 되는 태그. 본격적인 HTML 작성의 시작을 알린다.
- `<head>`
  - 웹 브라우저 상에 렌더링 되지는 않지만 웹 화면을 구성하기 위해 필요한 정보들을 포함하는 태그.
  - 대표적으로 Page title, CSS에 대한 link, 그 외 meta 정보들이 있다.
- `<body>`
  - 웹 브라우저 화면에 렌더링 되는 모든 Content를 포함하는 태그.
  - 우리가 눈으로 보는 모든 요소를 포함한다.
- **위 요소들은 모두 HTML 파일이 필수적으로 지녀야 할 요소들이다.**

## HTML Element

### Concepts

- HTML을 구성하는 요소들로, 일반적으로 다음과 같은 형태로 되어 있다.

  ```html
  <tag>My Content</tag>
  ```

  위에서 `<tag>`를 **Opening tag**, `</tag>`를 **Closing tag**, 가운데 `My Content`를 **Content**라고 지칭한다.

- `<img>`, `<meta>`와 같이 closing tag, content가 없는 element 또한 존재한다.

### Examples

- 주로 사용하는 대표적인 태그는 다음과 같다.

  - `<h1>`~`<h6>`
    - h는 **header**를 의미한다.
    - 숫자가 커질 수록 점점 더 작아진다.
    - `<h1>`은 관습적으로 HTML 문서 당 _하나만_ 사용한다.
    - 예시
      ```html
      <h1>Header 1</h1>
      ```
  - `<p>`
    - **Paragraph**를 의미한다.
    - HTML 상에서 문단을 표시할 때 사용한다.
    - 예시
      ```html
      <h2>Introduction</h2>
      <p>This is my first ....</p>
      ```
  - `<ul>`
    - **Unordered List**를 의미한다.
    - `<li>` 태그를 이용하여 **List Item**을 표시한다.
    - List의 각 item은 bullet으로 표시된다.
    - 예시
      ```html
      <ul>
        <li>Item 1</li>
        <li>Item 2</li>
        <li>Item 3</li>
      </ul>
      ```
    - 위 예시와 같이 한 element (`<li>`)가 다른 element (`<ul>`)에 종속되는 경우 후자는 전자의 _parent element_, 전자는 후자의 _child element_ 라고 일컫는다.
  - `<ol>`
    - **Ordered List**를 의미한다.
    - 사용 방법은 `<ul>`과 같다.
    - List의 각 item은 숫자로 표시되며, 1부터 시작하여 _순서에 따라_ 1씩 증가한다.
    - 예시
      ```html
      <ol>
        <li>Item 1</li>
        <li>Item 2</li>
        <li>Item 3</li>
      </ol>
      ```
  - `<b>` or `<strong>`
    - **Bold** 효과를 부여한다.
    - 후자가 더 *HTML semantics*에 맞는 표현 (more meaningful)
    - 예시
      ```html
      <h2>Introduction</h2>
      <p>This is my <string>first</strong> ....</p>
      ```
  - `<i>` or `<em>`
    - _Italic_ 체를 표현한다.
    - 후자가 더 *HTML semantics*에 맞는 표현 (more meaningful)
    - 예시
      ```html
      <h2>Introduction</h2>
      <p>This is my <em>first</em> ....</p>
      ```
