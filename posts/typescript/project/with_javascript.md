---
layout: default
title: With Javascript
parent: Project
grand_parent: Typescript
nav_order: 2
---

# With Javascript

Typescript로 프로젝트를 진행할 때 필연적으로 Javascript로 작성된 모듈 혹은 패키지를 사용하게 된다. 본 문서는 Typescript로 작성된 프로젝트에서 Javascript로 작성된 객체들을 사용할 수 있는 방법을 다룬다.

## Type definition 정의하기

```javascript
// src/myPackage.js
export function add(a, b) {
  return a + b;
}
```

위 함수를 ts 코드에서 사용하고 싶을 때 다음과 같이 declaration file (`.d.ts`)에 type definition을 정의한다.

```typescript
// src/myPackage.d.ts
declare module "myPackage" {
  function add(a: number, b: number): number;
}
```

위와 같이 작성하면 다음과 같이 module로 사용이 가능하다.

```typescript
// src/index.ts
import { add } from "myPackage";
...
```

## JSDoc

Type definition 대신 다음과 같이 javascript 파일에 *JSDoc*을 추가할 수 있다.

```javascript
// @ts-check
/**
 * Add two numbers
 * @param {number} a
 * @param {number} b
 * @returns {number}
 */
export function add(a, b) {
  return a + b;
}
```

다음으로 `tsconfig.json`에 `"allowJS": true`를 추가하면 다음과 같이 직접 JS 파일로부터 함수를 import할 수 있다.

```typescript
// src/index.ts
import { add } from "./myPackage";
...
```

## DefinitelyTyped

- JS로 작성된 패키지를 사용하는 경우 type definition을 [DefinitelyTyped](https://github.com/DefinitelyTyped/DefinitelyTyped)부터 가져올 수 있다.
- `npm`을 이용하여 원하는 JS 패키지의 type definition을 다음과 같이 설치할 수 있다. 일반적으로 이렇게 사용을다.

  ```bash
  npm i @types/{Package you want}
  ```

- `ts-node`를 설치하면 node에서 주로 사용하는 type definition들이 기본적으로 내장되어 있는 것으로 보인다.
