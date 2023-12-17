# coding: utf-8
# license: GPLv3

from solar_objects import Star, Planet


def read_space_objects_data_from_file(input_filename):
    """Cчитывает данные о космических объектах из файла, создаёт сами объекты
    и вызывает создание их графических образов

    Параметры:

    **input_filename** — имя входного файла
    """

    objects = []
    with open(input_filename) as input_file:
        for line in input_file:
            if len(line.strip()) == 0 or line[0] == '#':
                continue  # пустые строки и строки-комментарии пропускаем
            object_type = line.split()[0].lower()
            if object_type == "star":
                star = Star()
                parse_star_parameters(line, star)
                objects.append(star)
            elif object_type == "planet":
                planet = Planet()
                parse_planet_parameters(line, planet)
                objects.append(planet)
            else:
                print("Unknown space object")

    return objects


def parse_star_parameters(line, star):
    """Считывает данные о звезде из строки.
    Входная строка должна иметь слеюущий формат:
    Star <радиус в пикселах> <цвет> <масса> <x> <y> <Vx> <Vy>

    Здесь (x, y) — координаты зведы, (Vx, Vy) — скорость.
    Пример строки:
    Star 10 red 1000 1 2 3 4

    Параметры:

    **line** — строка с описание звезды.
    **star** — объект звезды.
    """

    # Разбиваем строку на отдельные элементы, используя пробел как разделитель
    elements = line.split()

    # Заполняем поля объекта star с учетом порядка данных в строке
    lines = line.split()
    star.R = float(lines[1])
    star.color = (lines[2])
    star.m = float(lines[3])
    star.x = float(lines[4])
    star.y = float(lines[5])
    star.Vx = float(lines[6])
    star.Vy = float(lines[7])


def parse_planet_parameters(line, planet):
    """Считывает данные о планете из строки.
    Предполагается такая строка:
    Входная строка должна иметь слеюущий формат:
    Planet <радиус в пикселах> <цвет> <масса> <x> <y> <Vx> <Vy>

    Здесь (x, y) — координаты планеты, (Vx, Vy) — скорость.
    Пример строки:
    Planet 10 red 1000 1 2 3 4

    Параметры:

    **line** — строка с описание планеты.
    **planet** — объект планеты.
    """
    # Разбиваем строку на отдельные элементы, используя пробел как разделитель
    elements = line.split()

    # Заполняем поля объекта star с учетом порядка данных в строке
    lines = line.split()
    planet.R = float(lines[1])
    planet.color = (lines[2])
    planet.m = float(lines[3])
    planet.x = float(lines[4])
    planet.y = float(lines[5])
    planet.Vx = float(lines[6])
    planet.Vy = float(lines[7])


def write_space_objects_data_to_file(output_filename, space_objects):
    """Сохраняет данные о космических объектах в файл.
    Строки должны иметь следующий формат:
    Star <радиус в пикселах> <цвет> <масса> <x> <y> <Vx> <Vy>
    Planet <радиус в пикселах> <цвет> <масса> <x> <y> <Vx> <Vy>

    Параметры:

    **output_filename** — имя входного файла
    **space_objects** — список объектов планет и звёзд
    """
    with open(output_filename, 'w') as out_file:
        for obj in space_objects:
            # Determine the object type based on its attributes
            obj_type = "Star" if isinstance(obj, Star) else "Planet"

            # Write the object data in the specified format
            out_file.write(
                f"{obj_type} {obj.radius} {obj.color} {obj.mass} "
                f"{obj.x} {obj.y} {obj.Vx} {obj.Vy}\n"
            )

if __name__ == "__main__":
    print("This module is not for direct call!")