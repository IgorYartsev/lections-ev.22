# GIT - > Распределенная система контроля версий.
# Эта система для отслеживания и ведения истории изменения файлом, в вашем проекте.

# Репозиторий - > хранилище вашего кода и истории его изменений .

# GitHub - > веб сайт для размещения  git - репозиториев и  совместной разработки проектов. 



# Команды Git 

# 1. git init - >  она создает новый репозиторий локально на вашем пк.

# 2. git commit - > как только  мы достигаем определенного момента в разработке,
# то тогда мы сохраняем и коментируем изменения (фиксация изменений в репозитории)
# git commit -m '<comment>'

# 3. git add - > когда мы создаем  или изменяем файлы, 
# то при помощи этой команды мы загружаем все изменения в локальное хранилище(репозиторий)
# git add <название файла>
# git add .

# 4. git remote add - >  эта команда для того чтобы связать ваш проект с удаленным репозиторием(репо в гитхаб)
# git remote add <название подключения> <ссылка на репо>
# git remote add origin <url>

# 5. git push - > после коммита изменений при помощи этой команды мы отправляем наши изменения на удаленный репозиторий.
# git push <origin> <название ветки>

#------------------------------------------
# 6. git branch ->  Ветки очень важны в git . 
# При помощи веток несколько программистов могут работать парралельно на одном и том же проекте.
# При помощи команды git branch мы можем создавать , просматривать или удалять ветки.
# Создание ветки: git branch <название ветки>
# Просмотр ветки: git branch or git branch --list
# Удаление ветки: git branch -d <название ветки>

# 7. git  checkout - > команда используется для работы в команде, она помогает переключатся по веткам.
# git checkout <название ветки>


# 8. git clone - > команда которая создает не пустой локальный репозиторий ,
# который мы склонировали с удаленного репозитория в гитхаб
# git clone <Ссылка на репо>

# 9. git pull - > команда которая используется для загрузки изменений(обновлений) из удаленного репзитория
# git pull <origin> <branch>


