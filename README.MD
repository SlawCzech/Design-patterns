# DESIGN PATTERNS

1. Creational (kreacyjne), służą do tworzenia obiektów
2. Structural, object composition (jak obiekty leżą obok siebie)
3. Behavioral, object interaction and responsibility

## Factory / Virtual Constructor

- creational
- tworzenie interfejsu do tworzenia obiektu
- defers instantiation to subclass  (instancjonowanie obiektów jest przesunięte do runtime'u)

## Abstract Factory / Kit Pattern

- creational
- similar to Factory
- Factory tworzy jeden obiekt, a Abstract Factory tworzy rodzinę obiektów

## Builder

- creational
- separates construction from representation (oddziela tworzenie od reprezentacji)
- Encapsulates construction of object
- Allows for multistep construction process
- User sees only abstraction

## Singleton

- creational
- only one instance of class
- access control to limited resources

## Adapter / Wrapper pattern

- structural
- converts interface of one class to another's
- may offer additional functionalities
- if object adapter -> composition
- if class adapter -> inheritance

## Decorator / Wrapper pattern

- structural
- adds new functionalities to objects
- dynamically at runtime

## Fasade

- structural
- united interface to a set of interfaces (example ORM in Django)

## Proxy

- structural
- access control to the real object
- exposes an identical interface

## Observer / Dependence pattern / Publish-subscribe pattern

- behavioral
- relations one to many among objects

## Memento / Token pattern

- behavioral
- drops objects to hard drive and load back
