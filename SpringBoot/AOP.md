# AOP

관점지향 프로그램 

- web layer: client 중심
- business layer: 비즈니스 로직
- data layer: db 연결

-> AOP 없으면 비즈니스 로직안에 조건문 같이 코드로 추가해야 함. 

-> 반복적인 코드를 넣어야함 

> 한곳으로 몰아서 코딩을 할 수 있게 해줌.


### 주요 anootation
```@Aspect``` : AOP를 정의하는 Class에 할당

```@Pointcut```: 지점 설정 

```@Before```: 메소드 실행 이전 

```@After```: 성공적으로 실행 후 예외가 발생하더라도 실행 

```@AfterReturning``` : 메소드 호출 성공 실행 시 

```@AfterThrowing```: 메소드 호출 실패 예외 발생

```@Around```: Before/after 모두 제어 

------


### Dependency 추가 필요함. 

```
implementation 'org.springframework.boot:spring-boot-starter-aop'
```

#### AOP로 작동시키기 
``` @Aspect ```


``` @Pointcut ```


```java
package com.example.aop.aop;

import org.aspectj.lang.JoinPoint;
import org.aspectj.lang.annotation.AfterReturning;
import org.aspectj.lang.annotation.Aspect;
import org.aspectj.lang.annotation.Before;
import org.aspectj.lang.annotation.Pointcut;
import org.aspectj.lang.reflect.MethodSignature;
import org.springframework.stereotype.Component;

import java.lang.reflect.Method;

@Aspect
@Component
public class ParameterApp {
    @Pointcut("execution(* com.example.aop.controller..*.*(..))")
    private void cut(){}

    @Before("cut()")
    public void before(JoinPoint joinPoint){
        MethodSignature methodSignature = (MethodSignature) joinPoint.getSignature();
        Method method = methodSignature.getMethod();
        System.out.println(method.getName());


        Object[] args = joinPoint.getArgs();
        for(Object obj: args){
            System.out.println("type: " + obj.getClass().getSimpleName());
            System.out.println(obj);
        }
    }

    @AfterReturning(value = "cut()", returning="returnObj")
    public void afterReturn(JoinPoint joinPoint, Object returnObj){
        System.out.println("return obj");
        System.out.println(returnObj);
    }
}
```
-> AOP를 갖고 로그를 찍을 때 좀 더 편리하고 간단하게 찍을 수 있음. 모든 메소드에 적용할 수 있음. 


```@Bean``` 은 클래스에 붙힐 수 없음. 
> component를 통해서 클래스 단위를 Bean에 등록을 시킬 수 있음. 
> Bean은 

걍갑자기 든 생각인데 자바 쓰니까 엄청 코드 중복을 줄일 수 있음 



