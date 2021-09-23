### UnpassWord - Removing passwords from DOC documents (Python3 + TTK theme)
UnpassWord - Удаление паролей из документов DOC (Python3 + TTK тема)

## `Version 1.2` (current)
- The interface has been redesigned, the new one is made on the basis of the most lightweight TTK theme.
- Improved script logic
- You can open multiple files at once
- Checking for Updates

---

- Переработан интерфейс, новый сделан на основе максимально облегченной ТТК темы.
- Улучшена логика работы скрипта
- Можно открывать сразу несколько файлов
- Проверка наличия обновлений

#### Version | Версия: 1.0
- First version, main function: search and remove password from document
- Первая версия, основная функция: поиск и удаление пароля из документа


![Screenshot](https://github.com/blyamur/unpassword/blob/main/screenshot.png)
###### Screenshot taken on windows 7 | Скриншот сделан на windows 7

## How to use | Как использовать

## Principle of operation | Принцип работы

##  Known bugs | Известные ошибки
- `Can't find the password in some documents`.

You can try on line 118 to change the value of psf [2] to psf [0] or psf [1], may vary depending on the version of the file.

- `Error opening some files`

Due to some differences in documents created in different versions of Word

- `Sometimes the temporary folder is not deleted`

The problem is related to a file access error. It often happens when a document is opened from a cloud folder or during operation the antivirus starts to recheck the created temporary files. When you open the next file, the folder is deleted automatically or when you start the program again.

---

- `В некоторых документах не находит пароль`. 

Можно попробовать в строке 118 поменять значение psf[2] на psf[0] или psf[1], может меняться в зависимости от версии файла.
- `Ошибка при открытии некоторых файлов`

Связано с некоторыми различиями в документах, созданных в разных версиях Word 
- `Иногда не удаляется временная папка` 

Проблема связана с ошибкой доступа к файлам. Происходит зачастую когда документ открывается из облачной папки или во время работы антивирус начинает перепроверять созданные временные файлы. При открытии следующего файла, папка удаляется автоматически или при новом запуске программы. 


---

Non-commercial use only, for personal use

TTK Theme `Spring-Drops` based on theme: Sun-Valley [rdbende](https://github.com/rdbende/Sun-Valley-ttk-theme) and Spring-Noon [blyamur](https://github.com/blyamur/Spring-Noon-ttk-theme)

The script is presented in Russian and English versions. There is also an icon in .ICO  and .PNG format

---

*Для тех кто хочет меня отблагодарить: ( [yoomoney](https://yoomoney.ru/to/41001158104834) or [PayPal](https://paypal.me/enkonu) or [ko-fi](https://ko-fi.com/W7W460SQ3) )*

*If You want to help me, you can buy me a cup of cup of coffee ( [yoomoney](https://yoomoney.ru/to/41001158104834) or [PayPal](https://paypal.me/enkonu) or [ko-fi](https://ko-fi.com/W7W460SQ3) )*
