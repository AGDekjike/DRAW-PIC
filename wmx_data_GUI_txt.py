from tkinter import *
from tkinter.filedialog import *
import wmx_handle_data 
import wmx_draw_pic
def choose_file():
   fileName.set(askopenfilename())
   fName=fileName.get()
   fin=open(fName)
   flag=True
   for line in fin:
      textA.insert(END,line)
      if flag:
         optionXY=line.split()
         flag=False
   fin.close()
   varOptX.set(optionXY[0])
   oMenuX = OptionMenu(fA,varOptX,*optionXY)
   oMenuX.grid(row=1,column=1)
   varOptY.set(optionXY[1])
   oMenuY = OptionMenu(fA,varOptY,*optionXY)
   oMenuY.grid(row=1,column=3) 
def to_pic():
   fName=fileName.get()
   #USE wmx_handle_data TO HANDLE DATA
   dictData=wmx_handle_data.txt_records(fName)
   #USEwmx_draw_pic.draw_plot TO PLOT
   wmx_draw_pic.draw_plot(varOptX,varOptY,\
                          dictData[varOptX.get()],dictData[varOptY.get()])

root=Tk()
choseBtn=Button(root,text='CHOOSE FILE',command=choose_file)
choseBtn.grid()
fileName=StringVar()
labelName=Label(root,textvariable=fileName,width=30)
labelName.grid(row=0,column=1)
fA=LabelFrame(root,text='DATA')
fA.grid(columnspan=15)
textA=Text(fA)
textA.grid(columnspan=14)
scrollA=Scrollbar(fA,command=textA.yview)
scrollA.grid(row=0,column=15,sticky=N+S)
textA['yscrollcommand']=scrollA.set
labelX=Label(fA,text='X-axis:')
labelX.grid()
labelY=Label(fA,text='Y-axis:')
labelY.grid(row=1,column=2)
drawBtn=Button(fA,text='DRAW PIC',command=to_pic)
drawBtn.grid(row=1,column=4)
varOptX=StringVar()
varOptY=StringVar()
root.mainloop()