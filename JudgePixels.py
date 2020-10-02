import tkinter as tk

class JudgePixels():

    def __init__(self, master):
        self.master = master
        self.master.title("JudgePixels")
        self.master.geometry("400x150")
        self.title_frame_fn()
        self.geometry_frame_fn()
        self.v = tk.StringVar()
        self.grid_size = 40
    def title_frame_fn(self):
        self.title_frame = tk.Frame(self.master, height = 10)
        self.title_frame.pack(side="top")
        geo_label = tk.Label(self.title_frame, text="Window Geometry")
        geo_label.pack(side="top", pady=5)

    def get_geo_values(self):
        x = self.geo_x_entry.get()
        y = self.geo_y_entry.get()
        self.grid_size = int(self.grid_size_entry.get())
        self.master.geometry(str(x)+"x"+str(y))

        self.prepare_for_showing_pixels()

    def geometry_frame_fn(self):
        self.geometry_frame = tk.Frame(self.master, height=10)
        self.geometry_frame.pack(side="top", pady=10, padx=10)

        x_frame = tk.Frame(self.geometry_frame)
        x_frame.pack(side="top")
        geo_x_label = tk.Label(x_frame, text="X", width="20")
        geo_x_label.pack(side="left")
        self.geo_x_entry = tk.Entry(x_frame)
        self.geo_x_entry.pack(side="left")

        y_frame = tk.Frame(self.geometry_frame)
        y_frame.pack(side="top")
        geo_y_label = tk.Label(y_frame, text="Y" ,width="20")
        geo_y_label.pack(side="left")
        self.geo_y_entry = tk.Entry(y_frame)
        self.geo_y_entry.pack(side="left")

        grid_frame = tk.Frame(self.geometry_frame)
        grid_frame.pack(side="top")
        grid_label = tk.Label(grid_frame, text = "Grid size (pixels)", width="20")
        grid_label.pack(side="left")
        self.grid_size_entry = tk.Entry(grid_frame)
        self.grid_size_entry.pack(side="left")

        button_frame = tk.Frame(self.geometry_frame)
        button_frame.pack(side="top")
        geo_button = tk.Button(button_frame, text="Create Window", command = self.get_geo_values)
        geo_button.pack(side="top")



    def prepare_for_showing_pixels(self):
        self.title_frame.destroy()
        self.geometry_frame.destroy()
        self.create_grids()
        self.show_pixels()

    def create_grids(self):
        def on_click(arg, arg2):
            self.canvas.itemconfig(arg, fill='red')
        print("Creating grids")
        self.master.update()
        h = self.master.winfo_height()
        w = self.master.winfo_width()
        self.canvas = tk.Canvas(self.master, height = h, width = w, background = "white")
        horizontal_lines = round(w/self.grid_size)
        vertical_lines = round(h/self.grid_size)

        count = 1
        delta = 0
        for j in range(0, horizontal_lines):
            alpha = 0
            for i in range(0,vertical_lines):
                r = self.canvas.create_rectangle(alpha, delta, alpha+self.grid_size, delta+self.grid_size, fill="#aaaaaa", dash= (2, 2), tags = "game")
                t = self.canvas.create_text(alpha+15, delta+15, text=str(count))
                self.canvas.tag_bind("game", "<Button-1>", lambda arg = r, arg2 = t: on_click(arg, arg2))
                alpha+=self.grid_size
                count+=1
            delta+=self.grid_size

        self.canvas.place(x=0,y=0)

    def on_motion(self, event):
        x,y = event.x, event.y
        text = "X:"+str(x)+", Y:"+str(y)
        self.v.set(text)

    def show_pixels(self):
        self.pixels_label = tk.Label(textvariable = self.v)
        self.pixels_label.pack(side="bottom")
        self.master.bind('<Motion>', self.on_motion)

root = tk.Tk()
judge_pixels = JudgePixels(root)
root.mainloop()