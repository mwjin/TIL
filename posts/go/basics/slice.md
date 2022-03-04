---
layout: default
title: Slice
parent: Basics
grand_parent: Go
nav_order: 13
---

# Slice

## Basic

- **동적 배열**, 즉 선언 시 이미 길이가 정해져 있는 Array와 달리 가변 길이를 가지는 배열이다.
- 다음과 같이 선언한다.

```go
var slice []int // slice
var array [10]int // array
```

- 초기화 없이 선언만 한 경우 길이는 0이다.
- **초기화 방법**

  - 요솟값 지정

    ```go
    var slice1 = []int{1, 2, 3}  // Length: 3
    var slice2 = []int{1, 3: 2, 7: 4}  // [1, 0, 0, 2, 0, 0, 0, 4]

    // Array
    var array = [...]int{1, 2, 3}
    ```

  - `make()` 이용
    ```go
    var slice = make([]int, 3)  // Length: 3
    ```

- 요소 접근 방식, 순회 방식은 array와 동일하다.
- **`append()`**

  ```go
  var slice = []int{1, 2, 3}
  slice2 := append(slice, 4)

  fmt.Println(slice)  // [1, 2, 3]
  fmt.Println(slice2)  // [1, 2, 3, 4]

  slice3 := append(slice2, 5, 6, 7, 8)
  fmt.Println(slice3)  // [1, 2, 3, 4, 5, 6, 7, 8]
  ```

## Slice 동작 원리

### Slice 구조

`reflect` 패키지의 `SliceHeader` 구조체를 통해 구조를 엿볼 수 있다.

```go
type SliceHeader struct [
    Data uintptr
    Len int
    Cap int
]
```

- `Data`: 배열의 시작 부분을 가리키는 포인터
- `Len`: 현재 배열이 가지고 있는 요소의 개수
- `Cap`: 허용할 수 있는 최대 요소의 개수.

### 선언

`Len` 뿐만 아니라 `Cap` 까지 고려하여 다음과 같이 선언할 수 있다.

```go
var slice = make([]int, 3)  // 기본적인 선언
var slice2 = make([]int, 3, 5)  // Len: 3, Cap: 5
```

`slice2`의 남은 빈공간 사이즈는 2이며, 빈 공간은 `0`으로 세팅되어 있다.

### 배열과 슬라이스의 동작 차이

- Slice는 내부에 실제 배열의 포인터를 가지고 있는 형태이다.
- 때문에 기존 slice 변수를 새로운 slice 변수에 assign 시 두 변수는 같은 배열을 가리키고 있는 형태이다.
- 이는 다음과 같은 동작의 원인이 된다.

  ```go
  slice1 := make([]int, 3)
  slice1[0] = 1
  slice1[1] = 2
  slice1[2] = 3
  slice2 := slice1
  slice2[0] = 5
  fmt.Println(slice1)  // [5, 2, 3]
  ```

- `append`
  - append 시 기존 slice에 빈 공간 (`Cap` - `Len`)이 남아 있는 경우 기존 slice 배열에 새로운 요소 추가 후 `Len` 값을 1 증가 시킨다.
  - 따라서 아래의 두 slice는 실제로 같은 배열을 가리키고 있다.
    ```go
    slice1 := make([]int, 3, 5)
    slice1[0] = 1
    slice1[1] = 2
    slice1[2] = 3
    slice2 := append(slice1, 4)
    ```
  - `append` 연산 과정에서 `Len`이 `Cap`을 초과하는 경우 더 큰 `Cap`을 가진 (일반적으로 2배) slice가 새로 만들어진다.

## Slicing

```go
array[start:end]
```

- 배열의 일부를 잡아내는 기능
- 위와 같이 작성 시 `start` index 부터 `end - 1` index 까지의 요소들을 나타내는 slice가 반환.
- 배열을 새로 만드는 것이 아니라 **배열의 일부를 포인터로 가리키고 있는 것임에 유의**
- Output으로 나오는 slice의 내부 값
  - `Data`: `array`의 `start` 인덱스를 가리키고 있는 포인터
  - `Len`: `end` - `start`
  - `Cap`: 실제 `array` 길이 - `start`
