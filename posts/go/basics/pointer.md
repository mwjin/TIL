---
layout: default
title: Pointer
parent: Basics
grand_parent: Go
nav_order: 8
---

# Pointer

## Basics

- **Pointer**란 특정 type의 instance에 대한 *메모리 주소를 값으로 하는 변수*를 의미한다.
  - **Instance**: 메모리에 존재하는 데이터의 실체
- 기본적인 특징은 C의 포인터와 같다.
  - 대표적으로 _Call by Reference_

## Usage

- 다음과 같이 정의한다.
  ```go
  var p *T  // T: type
  ```
- 일반적인 경우 다음과 같이 할당한다.

  ```go
  var v T
  var p *T = &T

  // Or
  p := &v

  // Or
  p := new(T)
  ```

- Struct에 대한 포인터는 같은 경우 다음과 같이 정의할 수 있다.

  ```go
  type Data struct {
    value int
    data [200]int
  }

  var v Data
  p := &v

  // Or
  p := new(Data)

  // Or
  p := &Data{}
  ```

- `&Data{}` 와 같은 경우는 `{}`내에 초기값 설정이 가능하다.
  - e.g. `&Data{3, {1, 2}}`

## Go에서의 메모리 관리

### Stack and Heap

- Go의 instance가 할당되는 위치는 다른 언어와 마찬가지로 *stack memory*와 *heap memory*로 나뉜다.
- Stack memory는 함수 내부에서만 사용 가능한 영역으로, 함수가 종료되고 난 뒤에는 참조되지 못한다.
- Heap memory는 함수 외부에서도 참조할 수 있는 메모리 공간이다.
- Heap memory에 속한 인스턴스들은 일반적으로 수명이 정해져 있지 않기 떄문에 메모리 관리가 필요하다.
- Go는 _Garbage Collector_ 방식으로 heap memory를 관리한다.

### Escape Analysis

- **Go에서 인스턴스가 stack memory에 할당될지, heap memory에 할당될지 결정하는 방식**
- 함수 외부로 공개되는 인스턴스는 heap memory에 할당한다.
- Go에서는 함수 외부로 인스턴스가 공개되는지의 여부에 따라 stack memory에 할당할지 heap memory에 할당할지 결정된다.
- 예시

  ```go
  package main

  import "fmt"

  type Person struct {
    Name string
    Age int
  }

  func NewPerson(name string, age int) *Person {
    p := Person{name, age}
    return &p  // Will be allocated to the heap memory
  }

  func main() {
    p := NewPerson("Minwoo Jeong", 27)
    fmt.Println(*p)
  }
  ```

  위 `NewPerson`의 `p`는 함수 내에서 정의된 인스턴스이지만 *escape analysis*에 의해 함수가 끝난 뒤에도 사라지지 않는다.
