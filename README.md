# Twitter
Пример работы микро-сервиса на flask
Программа может создавать, редактировать, удалять и отображать как все созданные твиты, так и делать поиск по id 

СОЗДАНИЕ ТВИТА (['POST'])
{"body": "Hello World", "author": "@sova270", "id": 1}
"body" => текст твита 
"author" => автор твита 
"id" => id твита(указанное число не имеет значение, добавиться порядковый номер в массиве)

ПОЛУЧЕНИЕ ВСЕХ ТВИТОВ (['GET'])
/twit/

ПОИСК ТВИТА ПО ID (['GET'])
/twit/<int:twit_id> 
<int:twit_id> = ID нужного твита 

УДАЛЕНИЕ ТВИТА (['DELETE'])
/twit/<int:twit_id> 
<int:twit_id> = ID нужного твита 

ИЗМИНЕНИЕ ТВИТА (['PUT'])
/twit/<int:twit_id> 
<int:twit_id> = ID нужного твита 
{"body": "New Hello World"}
"body" => текст изминенного твита 
