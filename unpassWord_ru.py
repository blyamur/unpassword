import os
from os import path
import tkinter as tk
from tkinter import IntVar
from tkinter import StringVar
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
from PIL import Image, ImageEnhance
import webbrowser
import requests
import time
import shutil
import zipfile
import xml.etree.ElementTree as ET




__author__ = "Mons (https://blog.mons.ws)"
__copyright__ = "Copyright 2021"
__credits__ = ["Code: Mons (https://github.com/blyamur/)", "TTK Theme spring-drops based on theme rdbende (https://github.com/rdbende/Sun-Valley-ttk-theme)"]
__license__ = "non-commercial use only, for personal use"
__version__ = "1.1.0"
__maintainer__ = "Mons"
__email__ = "mons@mons.ws"
__status__ = "Production"

class App(ttk.Frame):
	def __init__(self, parent):
		ttk.Frame.__init__(self)
		for index in [0, 1, 2]:
			self.columnconfigure(index=index, weight=1)
			self.rowconfigure(index=index, weight=1)
		self.setup_widgets()

	def setup_widgets(self):
		global delete_im
		global quality_im
		global enhance_im
		global status
		delete_im = IntVar()
		status = StringVar()
		status.set('')
		self.widgets_frame = ttk.Frame(self, padding=(0, 0, 0, 10))
		self.widgets_frame.grid(
			row=1, column=1, padx=10, pady=(30, 10), sticky="nsew", rowspan=3
		)
		self.widgets_frame.columnconfigure(index=0, weight=1)
		self.label = ttk.Label(
			self.widgets_frame,
			text="Выберите файл Word [.doc,.docx]",
			justify="center",
			font=("-size", 15, "-weight", "bold"),
		)
		self.label.grid(row=1, column=0,padx=0, pady=25, columnspan=2, sticky="S")
		self.accentbutton = ttk.Button(
			self.widgets_frame, text="Выбрать файл(ы)", style="Accent.TButton",command=open_file
		)
		self.accentbutton.grid(row=2, column=0, padx=2, pady=10, sticky="nsew")

		self.labels = ttk.Label(
			self.widgets_frame,
			textvariable = status,
			foreground="#FBAFE6",
			justify="center",
			font=("-size", 11, "-weight", "bold"),
		)
		self.labels.grid(row=6, column=0, padx=10, pady=11, columnspan=11, sticky="n")
		
		self.copy_frame = ttk.Frame(self, padding=(0, 0, 0, 10))
		self.copy_frame.grid(row=5, column=0, padx=(10, 10), pady=0, columnspan=10 , sticky="n")
		self.UrlButton = ttk.Button(
			self.copy_frame, text="© blog.mons.ws", style="Url.TButton",command=openweb
		)
		self.UrlButton.grid(row=1, column=0, padx=20, pady=0, columnspan=1, sticky="n")
		self.UrlButton = ttk.Button(
			self.copy_frame, text="Версия " +currentVersion+" ", style="Url.TButton",command=checkUpdate
		) 
		self.UrlButton.grid(row=1, column=4, padx=20, pady=0, columnspan=1, sticky="w")
		self.UrlButton = ttk.Button(
			self.copy_frame, text="Donate", style="Url.TButton",command=donate
		)
		self.UrlButton.grid(row=1, column=7, padx=20, pady=0, columnspan=1, sticky="w")
		


def open_file():
	try:
		file_open = filedialog.askopenfilenames(parent=root,title='Пожалуйста выберите файл Word для снятия пароля.', filetypes=[('Word Files', ['.doc', '.docx', '.docm'])])
		files = root.tk.splitlist(file_open)
		for filename in files:
			full_name = path.basename(filename)
			dirname, fname  = os.path.split(filename)
			dir_name = path.splitext(full_name)[0]
			new_name = dir_name+'_unpassed'
			ext_name = path.splitext(full_name)[1]
			shutil.rmtree('./work/', ignore_errors=True)
			if ext_name.lower().endswith(('.doc', '.docx', '.docm')):
				#создаем рабочие папки для работы
				if not os.path.isdir('work'):
					os.makedirs('work/tmp/')
				else:
					pass
				#копируем файл
				shutil.copy2(filename, './work/')
				#переименовываем файл в zip
				os.rename('./work/' + full_name, './work/unpassed.zip')
				#распаковываем zip в папку tmp 
				try:
					with zipfile.ZipFile("./work/unpassed.zip","r") as zip_ref:
						zip_ref.extractall("./work/tmp/")
					#удаляем zip
					os.remove("./work/unpassed.zip")
					#разбираем xml
					tree = ET.parse("./work/tmp/word/settings.xml")
					psf=tree.getroot()
					element =psf[2]
					isk = str(element)
					count = isk.count("documentProtection")
					#удаляем из xml пароль
					if count == 1:
						psf.remove(element)
						#сохраняем xml
						tree.write("./work/tmp/word/settings.xml")
						#создаем zip
						fantasy_zip = zipfile.ZipFile("./work/unpassed.zip", mode='w')
						for folder, subfolders, files in os.walk('./work/tmp/'):
							for file in files:
								fantasy_zip.write(os.path.join(folder, file), os.path.relpath(os.path.join(folder,file), './work/tmp/'), compress_type = zipfile.ZIP_DEFLATED)
						fantasy_zip.close()
						#удаляем временную папку
						shutil.rmtree('./work/tmp/', ignore_errors=True)
						#переименовываем zip в doc
						os.rename('./work/unpassed.zip', './work/'+ new_name + ext_name)
						#копируем файл 
						shutil.copy2('./work/'+ new_name + ext_name, dirname)
						#удаляем все папки
						shutil.rmtree('./work/', ignore_errors=True)
						messagebox.showinfo("Пароль удален"," Файл успешно разблокирован!\n")
					else:
						shutil.rmtree('./work/', ignore_errors=True)
						messagebox.showwarning("Внимание"," Файл НЕ заблокирован!\n Пароль в файле не найден.")
				except zipfile.BadZipfile:
					messagebox.showwarning("Ошибка"," С данного типа файлов, пароли не снимаются.")
					shutil.rmtree('./work/', ignore_errors=True)
			else:
				messagebox.showerror("Ошибка", " Вы не выбрали файл!")
	except:
		messagebox.showerror("Ошибка", "Что-то пошло не так!")
		
def openweb():
	webbrowser.open_new_tab('https://blog.mons.ws')
def donate():
	webbrowser.open_new_tab('https://ko-fi.com/monseg')
def checkUpdate(method='Button'):
	try:
		# проверяем наличие последней версии в файле README GitHub
		github_page = requests.get('https://raw.githubusercontent.com/blyamur/unpassword/main/README.md')
		github_page_html = str(github_page.content).split()
		
		for i in range(0, 12):
			try:
				index = github_page_html.index(('1.' + str(i)))
				version = github_page_html[index]
			except ValueError:
				pass
			# отображать всплывающее окно, если найдено обновление
		if float(version) > float(currentVersion):
			updateApp(version)
		else:
			if method == 'Button':
				messagebox.showinfo(title='Обновления не найдены', message=f'Обновления не найдены.\nТекущая версия: {version}')

	# не проверять наличие обновлений в офлайн-режиме
	except requests.exceptions.ConnectionError:
		if method == 'Button':
			messagebox.showwarning(title='Нет доступа к сети', message='Нет доступа к сети.\nПроверьте подключение к интернету.')
		elif method == 'Button':
			pass

def updateApp(version):
	update = messagebox.askyesno(title='Найдено обновление', message=f'Доступна новая версия {version} . Обновимся?')
	if update:
		webbrowser.open_new_tab('https://github.com/blyamur/unpassword/')

if __name__ == "__main__":
	root = tk.Tk()
	w = root.winfo_screenwidth()
	h = root.winfo_screenheight()
	w = w//2 
	h = h//2 
	w = w - 200
	h = h - 200
	root.geometry('600x290+{}+{}'.format(w, h)) #размеры окна
	root.resizable(False, False)
	currentVersion = '1.2'
	root.title("UnpassWord - снятие пароля с документов MS Word") # заголовок окна приложения
	root.iconbitmap('icon.ico') # иконка окна приложения
	root.tk.call("source", "spring-drops.tcl") #установка темы оформления
	root.tk.call("set_theme", "light") #стиль темы оформления
	app = App(root)
	app.pack(fill="both", expand=True)
	root.update()
	root.mainloop()