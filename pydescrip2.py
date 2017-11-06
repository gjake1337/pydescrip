#pydescrip version 0.2
import tkinter as tk
import tkinter.messagebox
version = 'pydescrip version 0.2 BETA'
textBoxWidth = 80
requiredLength = 51 #overall length must be over 50
HTML = 'Nothing generated yet!'
tdStyle = ' style ="border-style: none; color: gray;"'

descriptionText = ''
tableL = []
tableR = []
helpString = '''Use the product description box to enter a paragraph about the item.

Use the the table box to enter information in a table format.The append table
button will save the current table boxs and may be replaced after to add another
row to the table.

Use the GenHTML button to generate the html for the product listing.
'''
shortDescription = 'The description you entered is less than 50 characters!'
saeSizes = ['']
bgColor = "gray"


#functions
def do_nothing():
    print('doing nothing...')

def fileNew():
    print('making new file.')

def removeLast():
    if len(tableR) > 0:
        tableR.pop()
        tableL.pop()
        genHtml()
    else:
        do_nothing()

def clear():
    HTML = ''
    descriptionText = ''
    del tableR[:]
    del tableL[:]
    tableRText.delete(1.0, tk.END)
    tableLText.delete(1.0, tk.END)
    plainDescription.delete(1.0, tk.END)
    outputText.delete(1.0, tk.END)

def clearTable():
        del tableR[:]
        del tableL[:]
        genHtml()

def clearHTML():
    outputText.delete(1.0, tk.END)

#forces size of 150char or more, adds <p> tags as well.
def makeParagraph():
    descriptionText = plainDescription.get("1.0", tk.END)
    stringLength = len(descriptionText)
    if stringLength < requiredLength:
        leftOver = ': ' + str(requiredLength-stringLength) + ' characters needed'
        tk.messagebox.showinfo('ERROR!', shortDescription + leftOver)
    descriptionText = '<p>\n' + descriptionText + '</p>\n'
    return descriptionText

def makeTable():
    tableString = ''
    for index in range(len(tableR)): #can either be L or R
        tableString+= '<tr>\n<td' + tdStyle +'>'+ tableL[index] + '</td>\n'
        tableString += '<td' + tdStyle +'>'+ tableR[index] + '</td>\n<tr>\n'
    tableString = '<table>\n' + tableString + '</table>\n'
    return tableString

def appendTable():
    tr = tableRText.get("1.0", tk.END)
    tl = tableLText.get("1.0", tk.END)
    if  len(tr) < 2: #allow the use of one rightColumn for multiple left items.
        tk.messagebox.showinfo('ERROR!', ' empty table!')
    else:
        tableR.append(tr)
        tableL.append(tl)
        genHtml()
        tableRText.delete(1.0, tk.END)
        tableLText.delete(1.0, tk.END)

def genHtml():
    clearHTML()
    HTML = makeParagraph()
    HTML = HTML + makeTable()
    outputText.insert(tk.END, HTML)

def showHelp():
    tkinter.messagebox.showinfo("Help File", helpString)

#the graphical stuff here

#make window
root = tk.Tk()

#top menu
menu = tk.Menu(root)
root.config(menu = menu)
root.title(version) #prints the version as title
root.configure(background = bgColor)

fileMenu = tk.Menu(menu)
menu.add_cascade(label = "File", menu = fileMenu)
fileMenu.add_command(label = "New", command = fileNew)
fileMenu.add_command(label = "Help", command = showHelp)
fileMenu.add_separator()
fileMenu.add_command(label = "Exit", command = root.destroy)

tableMenu = tk.Menu(menu)
menu.add_cascade(label = "Table", menu = tableMenu)
tableMenu.add_command(label= "Remove last", command = removeLast)
tableMenu.add_command(label = "Clear Table", command = clearTable)
tableMenu.add_command(label = "Table Editor", command = do_nothing)

automateMenu = tk.Menu(menu)
menu.add_cascade(label = "Automate", menu = automateMenu)
automateMenu.add_command(label = "automate window", command = do_nothing)
automateMenu.add_command(label = "quick")


#BUTTON AREA
genarateButton = tk.Button(root, text = "GenHTML", command = genHtml)
genarateButton.grid(row = 0, sticky = tk.W)

clearButton = tk.Button(root, text = "CLEAR", command = clear)
clearButton.grid(row = 0, sticky = tk.W, padx = 100)

#simple input box for the description part of the thing
plainLabel = tk.Label(root, text = "Product Description", bg = bgColor)
plainLabel.grid(row = 1)

plainDescription = tk.Text(root, height = 5, width = textBoxWidth, fg = "black", bg = "white")
plainDescription.grid(row = 2)

#the table input area
tableLLabel = tk.Label(root, text = "Table Left:", bg = bgColor)
tableLLabel.grid(row = 3, column = 0, sticky = tk.W)
tableLText = tk.Text(root, height = 1, width = int(textBoxWidth/4), fg = "black", bg = "white")
tableLText.grid(row = 3, column = 0, sticky = tk.W, padx = 100)

tableRLabel = tk.Label(root, text = "Table Right:", bg = bgColor)
tableRLabel.grid(row = 4, column = 0, sticky = tk.W)
tableRText = tk.Text(root, height = 1, width = int(textBoxWidth/4), fg = "black", bg = "white")
tableRText.grid(row = 4, column = 0, sticky = tk.W, padx = 100)

tableAppend = tk.Button(root, text = "Table Append", command = appendTable)
tableAppend.grid(row = 3, column = 0, sticky = tk.E)

#the output textbox
outputLabel = tk.Label(root, text = "Output(HTML)", bg = bgColor )
outputLabel.grid(row = 5)
outputText = tk.Text(root, height=10, width= textBoxWidth, fg = "black", bg = "white")
outputText.grid(row = 6)
outputText.insert(tk.END, '')



root.mainloop() #loop through all the code until action!
