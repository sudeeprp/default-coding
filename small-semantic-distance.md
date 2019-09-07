## Small Semantic Distance

TDD with mocks makes you think about implementation. Since mocks test behavior (in the sense of sequence of calls), the tests get tied to the behavior - how your class uses other classes.
Stubs will test state, without caring about how that state was arrived at. This makes you come to the implementation later. 
See https://martinfowler.com/articles/mocksArentStubs.html

Domain-specific languages, Fluency and method chaining
https://martinfowler.com/bliki/FluentInterface.html
