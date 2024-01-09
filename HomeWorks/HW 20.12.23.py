# Задание
# Вывести на экран фигуры, заполненные звездочками.
# Диалог с пользователем реализовать при помощи меню.

# a. * * * * * b. *       c.  * * * d.        e. * * *
#      * * * *    * *          * *                * *
#        * * *    * * *         *        *         *
#          * *    * * * *               * *       * *
#            *    * * * * *            * * *     * * *

# f. *       * g. *     h.     * i. * * * * * j.         *
#    * *   * *    * *        * *    * * * *            * *
#    * * * * *    * * *    * * *    * * *            * * *
#    * *   * *    * *        * *    * *            * * * *
#    *       *    *            *    *            * * * * * 

variant = input('Какую фигуру нарисовать?\n\
                \na. * * * * * b. *       c.  * * * d.        e. * * *\
                \n     * * * *    * *          * *                * *\
                \n       * * *    * * *         *        *         *\
                \n         * *    * * * *               * *       * *\
                \n           *    * * * * *            * * *     * * *\n\
                \nf. *       * g. *     h.     * i. * * * * * j.         *\
                \n   * *   * *    * *        * *    * * * *            * *\
                \n   * * * * *    * * *    * * *    * * *            * * *\
                \n   * *   * *    * *        * *    * *            * * * *\
                \n   *       *    *            *    *            * * * * *\
                \n >>> ')
if variant == 'a':
    for i in range(0, 5):
        print('  ' * i + '* ' * (5 - i))
elif variant == 'b':
    for i in range(0, 6):
        print('* ' * i + '  ' * (5 - i))
elif variant == 'c':
    for i in range(1, 4):
        print(' ' * i + '* ' * (4 - i) + ' ' * i)
elif variant == 'd':
    for i in range(1, 4):
        print(' ' * (4 - i) + '* ' * i)
elif variant == 'e':
    for i in range(1, 4):
        print(' ' * i + '* ' * (4 - i) + ' ' * i)
    for i in range(2, 4):
        print(' ' * (4 - i) + '* ' * i)
# elif variant == 'f':

# elif variant == 'g':
# elif variant == 'h':
# elif variant == 'i':
# elif variant == 'j':