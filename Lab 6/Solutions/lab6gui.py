from tkinter import *
import tkinter.font as TkFont
from lab6tree import *

number_color='#D4D4D2'
operator_color='#ff9500'
func_color='#808080'
bg_color='#1c1c1c'
label_color='WHITE'

class CalculatorWindow:
    def __init__(self):
        self.master = Tk()
        self.master.configure(bg=bg_color)
        self.master.resizable(width=False, height=False)
        self.master.title('Calculator')
        self.main_frame = Frame(self.master, bg=bg_color)
        self.result_frame = Frame(self.master, bg=bg_color)
        self.cursor = 0

        self.expr_label = Label(self.result_frame, text='Expression:', bg=bg_color, fg=label_color)
        self.read_label = Label(self.result_frame, text='Reading as:', bg=bg_color, fg=label_color)
        self.result_label = Label(self.result_frame, text='Result:', bg=bg_color, fg=label_color)
        self.expr_label.grid(row=0, column=0)
        self.read_label.grid(row=1, column=0)
        self.result_label.grid(row=2, column=0)

        self.entry = Entry(self.result_frame, width=40, bg=bg_color)
        self.entry.insert(0, '|')
        self.entry.configure(state=DISABLED)
        self.read = Entry(self.result_frame, width=40, state=DISABLED, bg=bg_color)
        self.result = Entry(self.result_frame, width=40, state=DISABLED, bg=bg_color)
        self.entry.grid(row=0, column=1, sticky=EW)
        self.read.grid(row=1, column=1, sticky=EW)
        self.result.grid(row=2, column=1, sticky=EW)

        self.main_frame.grid(row=1, column=0)
        self.result_frame.grid(row=0, column=0, sticky=EW)

        self.button1 = Button(self.main_frame, text='1', command=lambda: self.entry_input(1, 1), width=4, bg=number_color)
        self.button2 = Button(self.main_frame, text='2', command=lambda: self.entry_input(2, 1), width=4, bg=number_color)
        self.button3 = Button(self.main_frame, text='3', command=lambda: self.entry_input(3, 1), width=4, bg=number_color)
        self.button4 = Button(self.main_frame, text='4', command=lambda: self.entry_input(4, 1), width=4, bg=number_color)
        self.button5 = Button(self.main_frame, text='5', command=lambda: self.entry_input(5, 1), width=4, bg=number_color)
        self.button6 = Button(self.main_frame, text='6', command=lambda: self.entry_input(6, 1), width=4, bg=number_color)
        self.button7 = Button(self.main_frame, text='7', command=lambda: self.entry_input(7, 1), width=4, bg=number_color)
        self.button8 = Button(self.main_frame, text='8', command=lambda: self.entry_input(8, 1), width=4, bg=number_color)
        self.button9 = Button(self.main_frame, text='9', command=lambda: self.entry_input(9, 1), width=4, bg=number_color)
        self.button0 = Button(self.main_frame, text='0', command=lambda: self.entry_input(0, 1), width=4, bg=number_color)
        self.button_dot = Button(self.main_frame, text='.', command=lambda: self.entry_input('.', 1), width=4, bg=number_color)
        self.button_evl = Button(self.main_frame, text='=', command=lambda: self.evaluate(), width=6, bg=func_color)
        self.button_add = Button(self.main_frame, text='+', command=lambda: self.entry_input('+', 1), width=6, bg=operator_color)
        self.button_sub = Button(self.main_frame, text='-', command=lambda: self.entry_input('-', 1), width=6, bg=operator_color)
        self.button_mul = Button(self.main_frame, text='*', command=lambda: self.entry_input('*', 1), width=6, bg=operator_color)
        self.button_div = Button(self.main_frame, text='/', command=lambda: self.entry_input('/', 1), width=6, bg=operator_color)
        self.button_pow = Button(self.main_frame, text='^', command=lambda: self.entry_input('^', 1), width=6, bg=operator_color)
        self.button_fac = Button(self.main_frame, text='!', command=lambda: self.entry_input('!', 1), width=6, bg=operator_color)
        self.button_mod = Button(self.main_frame, text='mod(x)', command=lambda: self.entry_input('mod()', 4), width=12, bg=operator_color)
        self.button_sqr = Button(self.main_frame, text='sqrt(x)', command=lambda: self.entry_input('sqrt()', 5), width=12, bg=operator_color)
        self.button_abs = Button(self.main_frame, text='abs(x)', command=lambda: self.entry_input('abs()', 4), width=12, bg=operator_color)
        self.button_rev = Button(self.main_frame, text='1/x', command=lambda: self.entry_input('1/()', 3), bg=operator_color)
        self.button_log = Button(self.main_frame, text='log(x)', command=lambda: self.entry_input('log()', 4), width=12, bg=operator_color)
        self.button_par_left = Button(self.main_frame, text='(', command=lambda: self.entry_input('(', 1), width=4, bg=func_color)
        self.button_par_right = Button(self.main_frame, text=')', command=lambda: self.entry_input(')', 1), width=6, bg=func_color)
        self.button_left = Button(self.main_frame, text='<', command=lambda: self.move_cursor_by(-1), width=4, bg=func_color)
        self.button_right = Button(self.main_frame, text='>', command=lambda: self.move_cursor_by(1), width=4, bg=func_color)
        self.button_clear_all = Button(self.main_frame, text='CE', command=lambda: self.remove_all(), width=12, bg=func_color)
        self.button_clear_last = Button(self.main_frame, text='<x', command=lambda: self.remove_last(), width=4, bg=number_color)
        self.button_show_tree = Button(self.main_frame, text='Show tree', command=lambda: self.show_tree_window(), bg=func_color)

        self.button1.grid(row=1, column=0)
        self.button2.grid(row=1, column=1)
        self.button3.grid(row=1, column=2)
        self.button4.grid(row=2, column=0)
        self.button5.grid(row=2, column=1)
        self.button6.grid(row=2, column=2)
        self.button7.grid(row=3, column=0)
        self.button8.grid(row=3, column=1)
        self.button9.grid(row=3, column=2)
        self.button0.grid(row=4, column=1)
        self.button_dot.grid(row=4, column=2)

        self.button_left.grid(row=0, column=0)
        self.button_right.grid(row=0, column=1)
        self.button_par_left.grid(row=0, column=2)
        self.button_par_right.grid(row=0, column=3)
        self.button_evl.grid(row=0, column=4)
        self.button_evl.grid(row=0, column=4)
        self.button_add.grid(row=1, column=3)
        self.button_sub.grid(row=2, column=3)
        self.button_mul.grid(row=3, column=3)
        self.button_div.grid(row=1, column=4)
        self.button_pow.grid(row=2, column=4)
        self.button_fac.grid(row=3, column=4)
        self.button_mod.grid(row=1, column=5)
        self.button_sqr.grid(row=2, column=5)
        self.button_abs.grid(row=3, column=5)
        self.button_log.grid(row=4, column=5)
        self.button_rev.grid(row=4, column=3, columnspan=2, sticky=EW)
        self.button_clear_all.grid(row=0, column=5)
        self.button_clear_last.grid(row=4, column=0)
        self.button_show_tree.grid(row=5, column=0, columnspan=6, sticky=EW)

        self.master.mainloop()

    def entry_input(self, input_s, size):
        self.insert_result('')
        self.insert_read('')
        self.entry.configure(state=NORMAL)
        self.entry.insert(self.cursor, input_s)
        self.move_cursor_by(size)

    def move_cursor_by(self, move):
        self.entry.configure(state=NORMAL)
        temp = self.entry.get()
        temp = temp.replace('|', '')
        self.cursor = self.cursor + move
        if self.cursor < 0:
            self.cursor = 0
        elif self.cursor > len(temp):
            self.cursor = len(temp)

        temp = temp[:self.cursor]+'|'+temp[self.cursor:]
        self.entry.delete(0, len(temp))
        self.entry.insert(0, temp)
        self.entry.configure(state=DISABLED)

    def remove_last(self):
        self.insert_result('')
        self.insert_read('')
        self.entry.configure(state=NORMAL)
        temp = self.entry.get()
        temp = temp.replace('|', '')
        self.cursor = self.cursor - 1
        if self.cursor < 0:
            self.cursor = 0
        elif self.cursor > len(temp):
            self.cursor = len(temp)

        temp = temp[:self.cursor]+'|'+temp[self.cursor+1:]
        self.entry.delete(0, len(temp)+1)
        self.entry.insert(0, temp)
        self.entry.configure(state=DISABLED)


    def remove_all(self):
        self.entry.configure(state=NORMAL)
        self.entry.delete(0, len(self.entry.get()))
        self.entry.configure(state=DISABLED)
        self.insert_read('')
        self.insert_result('')

    def evaluate(self):
        expr = self.entry.get()
        expr = expr.replace('|', '')
        tree = ExpressionTree()
        tree.populate_tree(expr)

        self.insert_read(self.get_expression(expr))
        try:
            tree.Evaluate()
            self.insert_result(tree.root.value)
        except:
            self.insert_result('SYMTAX ERROR')

    def get_expression(self, expr):
        tree = ExpressionTree()
        tree.populate_tree(expr)
        return tree.GetExpression()

    def insert_read(self, expr):
        self.read.configure(state=NORMAL)
        self.read.delete(0, len(self.read.get()))
        self.read.insert(0, expr)
        self.read.configure(state=DISABLED)

    def insert_result(self, expr):
        self.result.configure(state=NORMAL)
        self.result.delete(0, len(self.result.get()))
        self.result.insert(0, expr)
        self.result.configure(state=DISABLED)

    def show_tree_window(self):
        tree_window = Tk()
        tree_window.configure(bg=bg_color)
        tree_window.minsize(200,100)
        tree_window.title('Tree')

        tree = ExpressionTree()
        expr = self.entry.get()
        expr = expr.replace('|', '')
        tree.populate_tree(expr)

        tree_print = tree.printTree()
        tree_entry = Label(tree_window, text=tree_print, font=TkFont.Font(family='Courier'), fg=label_color, bg=bg_color)
        tree_entry.pack()


if __name__ == '__main__':
    cal = CalculatorWindow()
