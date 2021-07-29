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
