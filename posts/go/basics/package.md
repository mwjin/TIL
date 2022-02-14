---
layout: default
title: Package
parent: Basics
grand_parent: Go
nav_order: 12
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

## Module

### Basics

- Go 패키지들을 모아놓은 **Go 프로젝트의 단위**
- 모든 Go 코드들은 Go 모듈 아래 있어야 한다. (1.16 버전 이후)
- `go build`를 하기 위해선 반드시 Go 모듈 루트 폴더에 `go.mod` 파일이 있어야 한다.

### Go 모듈을 구성하는데 있어서 필요한 파일들

- `go.mod`: 모듈 이름과 Go 버전, 필요한 외부 패키지들을 명시
- `go.sum`: 외부 패키지 버전 정보 및 패키지 위조 여부 판별을 위한 checksum 결과를 포함

### Go 모듈을 생성하기 위해 수행하는 명령어

- `go mod init [package name]`
  - `go.mod` 파일을 생성한다.
  - `[package name]`은 이 모듈을 패키지로 여기고 접근하기 위해 사용하는 이름이다.
- `go mod tidy`
  - Go 모듈을 구성하기 위해 필요한 패키지를 다운로드
  - 필요한 패키지 정보를 `go.mod`에 적음
  - `go.sum`을 생성하고 내용물을 적음
  - 외부에 공개된 패키지 외에는 `go mod init` 한 폴더 내에 정의된 패키지만 찾을 수 있다.
- `go mod edit -replace [local module]=[its path]`
  - `go mod tidy`로 찾지 못하는 패키지의 경로를 직접 설정해주기 위해 사용하는 명령어이다.

## 패키지명과 패키지 외부 공개

- 패키지명은 쉽고 간단하게 하자.
- **모든 문자를 소문자로 할 것**을 권장한다.
- **패키지 외부로 공개되는 것의 규칙**
  - 맨 앞 글자가 대문자인 함수, 구조체, 전역 변수는 외부 공개
  - 외부 공개된 구조체 내에 맨 앞 글자가 대문자로 정의된 필드는 외부 공개
  - 이 외에는 모두 외부로 공개되지 않는다.

## 패키지 초기화

- 패키지를 import 할 때
  - 패키지 내의 전역 변수를 먼저 초기화
  - `init` 함수를 호출
- `init` 함수는 어떠한 파라미터도, 리턴값도 설정되어 있지 않아야 한다.
  ```go
  func init() {
      ...
  }
  ```
