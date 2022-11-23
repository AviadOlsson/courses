# Различные шпоры и полезные штуки

## Шпора по конструкции "match/case"

Конструкция "match/case" является аналогом проверки условий но удобнее для чтения кода:

```python
command = "print"
argument = "hello"

match command:                          # Запускает проверку на соответствие case
    case "print":                       # Если переменная command == "print" тогда print(argument)
        print(argument)
    case "decorate":
        print("decorated", argument)    # Если переменная command == "decorate" тогда print("decorated", argument)
    case _:                             # аналог else с использованием анонимной переменной (переменная принимает любое значение)
        print("error")

# hello
```

При написании блока `case` конструкции, работают все логичиские оперторы.
