# Дан список имен.
# Найдите самое длинное имя, если таких имен несколько - выведи любое их них

names = ["Иван", "Ирина", "Вячеслав", "Василий", "Петр"]

# TODO: your code here

mux_len_names = len(names[0])
for name in names:
    if len(name) > mux_len_names:
        mux_len_names = len(name)
# print(mux_len_names)

for long_name in names:
    if len(long_name) == mux_len_names:
        print(long_name)
