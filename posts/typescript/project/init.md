---
layout: default
title: Init
parent: Project
grand_parent: Typescript
nav_order: 1
---

# Init

## Create NPM Project

- _Prerequisite_: `npm`과 `node`가 설치되어 있어야 한다.
- Install _Typescript_
  ```bash
  npm i -D typescript
  ```
  `-D, --save-dev`: 설치한 package를 `devDependencies`에 등록한다.
  위 플래그가 없으면 `dependencies`에 등록된다.
- Initialize npm project
  ```bash
  npm init -y
  ```
- Typescript를 이용한 원활한 개발을 위해 다음 패키지들을 설치해주면 좋다.
  ```bash
  npm i -D ts-node;
  npm i nodemon;
  ```

## Setting

- `tsconfg.json`

  ```json
  {
    "include": ["src"],
    "compilerOptions": {
      "outDir": "build",
      "target": "ES6",
      "lib": ["ES6"],
      "esModuleInterop": true,
      "module": "CommonJS",
      "strict": true
    }
  }
  ```

  - `lib`: 프로젝트에 포함시킬 built-in JS package에 대한 type definition
  - `esModuleInterop`: `CommonJS` module 방식이 ES6 module spec에 호환되도록 지원

- `package.json`

  ```json
  {
    ...
    "scripts": {
      "build": "tsc",
      "dev": "nodemon --exec ts-node src/index.ts",
      "start": "node build/index.js"
    }
    ...
  }
  ```

  - 위와 같이 세팅 후 `npm run build` 하면 `build/` 디렉토리에 javascript ES6 버전으로 compile 된 결과를 생성할 수 있다.
  - `npm run dev` 하면 일일이 compile 하지 않고도 프로젝트를 돌려볼 수 있다.
