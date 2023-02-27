# Spring boot

- 스프링 부트
- 스프링 클라우드 
- 스프링 데이터
- 스프링 배치 
- 스프링 시큐리티(권한 관련)

-----------

## AOP
 >스프링 데이터, 트랜잭션 관리, AOP를 통해서 로깅

## 객체 
>이식 가능한 추상화, 관전 중심 프로그램, 의존 관계 주입 


## IOC/DI
### IOC==제어의 역전 
>- spring container에 만들어져서 들어가있음 -> 싱글톤 
>- 프레임워크가 객체를 관리함

2023.02.23
### DI: 외부에서 사용하고 있는 객체를 상속시켜서 주입시켜줌. 
>- 객체를 사용하기 위한 것 
>- 제어의 역전이 일어남 
>- 의존성: 코드 테스트에 용이함 
>- Mock -> 안정적으로 테스트가 가능함 
>- Mocking: 어떠한 응답이 올거라는 기대값 
>- 코드 변경할때 영향 취소화(추상화)
>- 순환참조를 막음: 객체1 객체2 서로 참조 안함. 

```JAVA
Encoder encoder = new Encoder(new Base64Encoder());
String result = encoder.encode(url);
```
-> 주입 객체 `new Base64Encoder()` 만 바꿔줌 
> - 만약 Base64Encoder() 라는 객체 대신 다른 객체를 사용하고 싶으면 new Base64Encoder()대신 사용하고 싶은 객체를 주입해주면 됨. 여기서 Base64Encoder()는 외부에서 사용하고 있던 객체임. 
> - 테스트할때 Encoder는 바꿔줄 필요가 없음. 테스트할때는 DI 부분의 객체만 넣어서 테스트를 할 수 있음 -> 테스트할때 편할 것 같음 !! 굳이 코드 안바꾸고 테스트 객체 하나 더 만들면 되니까 
> - 코드의 관리가 쉬울듯! 
>

Interface 추가 전 
```JAVA
Encoder encoder = new Encoder();
String result = encoder.encode(url);
```

Interface 추가 
```JAVA
 IEncoder encoder = new Base64Encoder();
 String result = encoder.encode(url);

 IEncoder urlEncoder = new UrlEncoder();
 String urlResult = urlEncoder.encode(url);

```
->Interface 추가해주는 이유: Interface를 추가하기 전에는 계속해서 객체를 생성해줘야 하는 문제가 있었음. 

------

2023.02.24
### Spring에 객체로 관리해달라고 요청하기 
 ``` 
 @Component 
 ```
-> 싱글톤 패턴으로 바꿔어서 스프링부트에서 관리할 수 있도록 함.
-> 스프링이 관리할 수 있도록 권한을 넘김. (제어의 역전)

*<span style="color:gray"> 싱글톤패턴이란? </span>*
*<span style="color:gray"> 인스턴스가 오직 1개만 생성되어야 하는 경우에 사용함 </span>*
*<span style="color:gray"> 자세한건 ....[싱글톤패턴](https://github.com/Sunjung-Dev/MS/blob/main/SpringBoot/SingleTone.md) </span>*



encoder에 setIEncoder 추가함 
```Java
encoder.setIEncoder(urlEncoder);
result = encoder.encode(url);
```

- 스프링에서 두개의 객체에 대해서 component를 붙혀주면 안됨 ->  스프링에서 어떤 것을 매칭할지 잘 모름
-> @Qualifier 지정 
```
@Qualifier("urlEncoder")
```
>> -  class명이 앞글자는 소문자로 변하게 되고, Component이름 지정 가능함. 


## 한개의 클래서에서 여러개의 bin을 등록할때, Configuration
```java
@Configuration
class AppConfig{
    
    @Bean("base64Encoder")
    public Encoder encoder(Base64Encoder base64Encoder){
        return new Encoder(base64Encoder);
    }
    
    @Bean("urlEncode")
    public Encoder encoder(UrlEncoder urlEncoder){
        return new Encoder(urlEncoder);
    }
}   
```

직접 객체를 불러올 때 :spring에서 주입 받을 수 있는 장소 -> 변수, 생성자, set method

### 용어 정리 
- bean: 객체 
- spring container: 객체가 관리되는 곳 
- ioc: spring이 관리하게 됨 -> 제어의 역전 