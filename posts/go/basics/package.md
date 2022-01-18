---
layout: default
title: Package
parent: Basics
grand_parent: Go
nav_order: 11
---

# Package

## Basics

### Package

- Go 언어에서 코드를 묶는 가장 큰 단위
- 함수, 구조체, 전역 변수 등을 묶는다.
- Go로 작성된 프로그램은 **main package** 한 개와 한 개 이상의 main 외의 package들로 구성된다.

### Main Package

- 프로그램의 시작점을 포함한 패키지
- `main()` function을 가지고 있다.

### 그 외 패키지

- Local에서 별도로 선언한 package
- 외부에서 타인이 작성해 공개한 패키지들
- [표준 패키지 목록](https://golang.org/pkg/)
- 그 외 많이 사용하는 패키지들을 찾아보려면 [awesome-go](https://github.com/avelino/awesome-go) 참조

## Package Usage

- `import "fmt"` 같이 import
- 여러 패키지를 import 할 때는 다음과 같이 소괄호로 묶는다. (어차피 플러그인이 알아서 해준다.)
  ```go
  import (
      "fmt"
      "os"
      "math/rand"
  )
  ```
- 폴더 경로처럼 되어 있는 패키지들이 있는데, 이들은 맨 마지막 폴더 이름이 코드 내부에서 사용하는 패키지명이다.
- 패키지 맴버 접근 예시: `fmt.Println("Hello, World!)"`
- 패키지 이름에 alias 부여하는 방법
  ```go
  import (
      "text/template"
      htemplate "html/template"  // alias: htemplate
  )
  ```
- 사용하지 않는 패키지를 포함해야 하는 경우
  ```go
  import (
    "database/sql"
    _ "github.com/mattn/go-sqlite3"
  )
  ```
