# from typing import Union

# def add(a: float |int, b: Union[float, int]) -> float: ## we can also use a pipe operator instead of union
#     return float(a+b)

# print(add(2,5))
# print(add("2", "523")) # this one is not correct but it run correctly but to avoid issues like that we 
#                         # should add some type checking





### testing a duck typing vs type hints 

# class Duck:
#     def quack(self):
#         return "The duck is quacking"

# def make_it_quack(duck: Duck) -> str:
#     return duck.quack()

# class Person: ## error: Argument 1 to "make_it_quack" has incompatible type "Person"; expected "Duck"  [arg-type] 
#     def quack(self):
#         return "The person is imitating a duck quacking"

# print(make_it_quack(Duck()))
# print(make_it_quack(Person()))


### to fix the error where person is not a duck we can use inheritance 

# class QuackingThing:
#     def quack(self):
#         raise NotImplementedError(
#             "Subclasses must implement this method"
#         )

# class Duck(QuackingThing):
#     def quack(self):
#         return "The duck is quacking"

# class Person(QuackingThing):
#     def quack(self):
#         return "The person is imitating a duck quacking"

# def make_it_quack(duck: QuackingThing) -> str:
#     return duck.quack()

# print(make_it_quack(Duck()))
# print(make_it_quack(Person()))


### Static Duck typing with protocols 

