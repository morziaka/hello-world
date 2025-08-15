game_field = [['-','-','-'], ['-','-','-'], ['-','-','-']]
#создаем поле для игры - список списков с дефисами

def check_conditions(L):
#проверяем условия, при которых игра заканчивается - это ничья или победа

#сначала прописываем условия, при которых игра оканчивается вничью -
# все клетки заняты, никто к этому моменту не победил

#в этот список собираем результаты проверки, остались ли свободные клетки (-):
   draw_conditions = []

   for i in range(len(L)):
      for j in range(len(L[i])):
         if L[i][j] == '-':
            draw_conditions.append(True)
         else:
            draw_conditions.append(False)

#пока остаются свободные клетки, игра продолжается:
   if any(draw_conditions):
      end_game = False
   else:
      end_game = True

#прописываем все условия для прекращения игры: условия победы плюс условия игры вничью:
   conditions = [str(L[0][0]) == str(L[0][1]) == str(L[0][2]) != '-',
                 str(L[0][0]) == str(L[1][0]) == str(L[2][0]) != '-',
                 str(L[0][1]) == str(L[1][1]) == str(L[2][1]) != '-',
                 str(L[1][0]) == str(L[1][1]) == str(L[1][2]) != '-',
                 str(L[2][0]) == str(L[2][1]) == str(L[2][2]) != '-',
                 str(L[0][0]) == str(L[1][1]) == str(L[2][2]) != '-',
                 str(L[0][2]) == str(L[1][2]) == str(L[2][2]) != '-',
                 str(L[2][0]) == str(L[1][1]) == str(L[0][2]) != '-',
                 end_game]


   if any(conditions):
      print('Игра окончена')

#проверяем, игра прошла вничью или победил один из пользователей:
      if conditions[-1] and not any(conditions[:-1]):
#все клетки заняты, при этом нет ни одной комбинации для победы
         print('Ничья')
#в ином случае - победа одного из игроков
      elif username == username1:
         print('Победил игрок '+username1)
      elif username == username2:
         print('Победил игрок '+username2)
      result = False
   else:
      result =  True

   return result

#функция, которая выводит игровое поле на печать:
def printer(L):
   print('  0 1 2')
   for i in range(len(L)):
      print(i, *L[i])

#первый вывод поля до начала игры
printer(game_field)


#запрашиваем имена двух игроков:
username1 = input('Введите имя игрока1: ')
username2 = input('Введите имя игрока2: ')

#Создаем переменные для определения, чей сейчас ход.
# Нечетный счетчик - пользователь1, четный - пользователь2
counter = 0
username = ''

#функция самой игры:
def game():
# переменная, для проверки верности ввода - является ли введенная информация числом,
# находится ли оно в пределах поля, не занята ли уже клетка:
   correct = False
   global counter
   global username
   counter += 1
   if counter % 2 == 1:
      username = username1
   else:
      username = username2
#запуск проверки на корректность ввода
   while not correct:
      num1 = input(username + ', ведите номер строки: ')
      num2 = input(username + ', ведите номер столбца: ')
      try:
         num1 = int(num1)
         num2 = int(num2)
      except:
         print("Это не число! Введите число от 0 до 2")
         continue
      if num1 > 2 or num1 < 0 or num2 > 2 or num2 < 0:
         print('Число должно быть от 0 до 2!')

#помещаем на выбранную клетку Х, если играет игрок1, и 0, если играет игрок2.
      for i in range(len(game_field)):
         for j in range(len(game_field[i])):
            if i == num1 and j == num2:
#проверяем, не занята ли выбранная клетка:
               if game_field[i][j] not in "X0":
                  if username == username1:
                     game_field[i][j] = 'X'
                  else:
                     game_field[i][j] = '0'
                  correct = True
               else:
                  print('Эта клетка занята!')
   printer(game_field)


#пока не сработало одно из условий прекращения игры, играем:
while check_conditions(game_field):
   game()
else:
   print('Ура!')



