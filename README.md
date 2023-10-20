### UnpassWord - Removing passwords from DOC documents (Python3 + TTK theme)
UnpassWord - Удаление паролей из документов DOC (Python3 + TTK тема)

![Screenshot](https://github.com/blyamur/unpassword/blob/main/screenshot.png)

## Version 1.2 (current)
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



## How to use | Как использовать

We run the script in the language of your choice. Click on the "select file" button and select the file or files from which you want to remove the restriction. After successful completion of the work, a new document with the unpassed prefix will appear in the same folder as the original.


Запускаем скрипт на выбранном вами языке. Нажимаем на кнопку "выбрать файл" и выбираем файл или файлы с которых необходимо снять ограничение. После успешного завершения работы, появится новый документ с префиксом  unpassed , в той же папке где и оригинал.

## Principle of operation | Принцип работы

After selecting the file, it is renamed into ZIP format, then the contents of the archive are unpacked into a temporary folder. From the file where the password is stored, the parameter with the password is deleted and everything is saved in the reverse order. And the temporary folder with the file is deleted.

После выбора файла, он переименовывется в формат ZIP, затем содержимое архива распаковывается во временную папку.Из файла, где хранится пароль, удаляется парамтр с паролем и все сохраняется в обратном порядке. А временная папка с файлом удаляется. 

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

*If You want to help me, you can buy me a cup of coffee :coffee: ( [yoomoney](https://yoomoney.ru/to/41001158104834) or [ko-fi](https://ko-fi.com/monseg), [boosty.to](https://boosty.to/monseg) )* 
