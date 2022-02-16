#!/usr/bin/python3

HEADER = '''<!DOCTYPE html>
<HTML LANG="ru">
<HEAD>
    <TITLE>B6.13 Домашнее задание</TITLE>
    <META HTTP-EQUIV="Content-Type" CONTENT="text/html; charset=UTF-8"/>
</HEAD>
<BODY>
    <H1>Расчёт параметров геометрических фигур</H1>
    <P>На данный момент подразумеваются не произвольные типы фигур, а симметричные. То есть равнобедренные треугольники, правильные пирамиды, конусы и некоторые другие</P>
    <P></P>
    <HR>
'''

FORM_INI = '''    <FORM ID="iniform" STYLE="background: #ddddff; padding: 10px" ACTION="/figure" METHOD="post">
        <P>
            <LABEL>Выбор фигуры:&nbsp;&nbsp;
            <SELECT FORM="iniform" NAME="figtype" SIZE="1">
                <OPTION VALUE="Quadro" SELECTED>Квадрат</OPTION>
                <OPTION VALUE="Cone">Конус</OPTION>
                <OPTION VALUE="Circle">Круг</OPTION>
                <OPTION VALUE="Cube">Куб</OPTION>
                <OPTION VALUE="Parallelepiped">Параллелепипед</OPTION>
                <OPTION VALUE="Pyramid3F">Пирамида трёхгранная</OPTION>
                <OPTION VALUE="Pyramid4F">Пирамида четырёхгранная</OPTION>
                <OPTION VALUE="Rectangle">Прямоугольник</OPTION>
                <OPTION VALUE="Rhombus">Ромб</OPTION>
                <OPTION VALUE="Sphere">Сфера</OPTION>
                <OPTION VALUE="Trapezoid">Трапеция</OPTION>
                <OPTION VALUE="Triangle">Треугольник равнобедренный</OPTION>
                <OPTION VALUE="Cylinder">Цилиндр</OPTION>
            </SELECT>
            </LABEL>
        </P>
        <P>
            <INPUT TYPE="submit" VALUE="Далее">
        </P>
    </FORM>
'''

FORM_QUADRO = '''    <FORM ID="form_quadro" STYLE="background: #ddddff; padding: 10px" ACTION="/result" METHOD="post">
        <P>
            <LABEL>Сторона квадрата:&nbsp;&nbsp;
                <INPUT NAME="a_" FORM="form_quadro" TYPE="number" SIZE="50" REQUIRED PLACEHOLDER="Введите значение длины стороны квадрата">
            </LABEL>
        </P>
        <P>
            <INPUT TYPE="submit" VALUE="Вычислить">
        </P>
    </FORM>
'''

FOOTER = '''    <HR>
    <H2><A HREF="/">Начальная страница</A></H2>
    <P></P>
</BODY>
</HTML>'''

#####=====----- THE END -----=====########################################