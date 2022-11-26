from tkinter import *
import tkinter as tk
from tkinter import ttk
from graph import Graph
from algorithms import *
from matplotlib.figure import Figure 
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,NavigationToolbar2Tk) 

window = tk.Tk()
window.title("Theory Of Graphs Application")
window.geometry("1080x720")
window.iconbitmap("app.ico")
#window.resizable(width=False, height=False)
bg = tk.PhotoImage(file="yess.png")
my_label=tk.Label(window, image=bg)
my_label.place(x=0,y=0,relwidth=1,relheight=1)
#window.config(background="#5d8a82")
page_1 = tk.Frame(window)
page_2 = tk.Frame(window)
main_page = tk.Frame(window)
page_4 = tk.Frame(window)
graph_info2_frame = tk.Frame(window, pady=200, padx=200)


#******************************************************************************
def AboutUs():
    window.destroy()
    import AboutUs


#-------------------------MENU--------------------------------------------------

#1) -creer la barre des menu

menuBar = Menu(window)

# 2) -creer les menus principaux

buttonHome= Button(menuBar)
buttonAbtus= Button(menuBar)


# 3) -ajouter les menus principaux a la barre des menus
menuBar.add_cascade(label ="Home",menu=buttonHome)
menuBar.add_cascade(label ="About us",menu=buttonAbtus,command=AboutUs)

window.config(menu=menuBar)


#------------------------------------------------------------------------------
inputs = []
kruskal_list = []
is_oriented_variable = tk.BooleanVar(page_2)
is_weighted_variable = tk.BooleanVar(page_2)
algorithm_input_variable = tk.StringVar(page_4)



#-------------------------------FUNCTIONS & PAGES-----------------------------

def show_graph():
    new_graph = Graph(inputs=inputs, is_wheited=is_weighted_variable.get())
    if is_oriented_variable.get():
        new_graph.display_digraph()
    else:
        new_graph.display_graph()
        

#def plot(): 
  
   # fig = Figure(figsize = (5, 5), 
   #             dpi = 100) 
   
   # plot1 = fig.add_subplot(111) 
   # plot1.plot() 
  
   # canvas = FigureCanvasTkAgg(fig,master = window)   
   # canvas.draw() 
   # canvas.get_tk_widget().pack() 
   # toolbar = NavigationToolbar2Tk(canvas,window) 
   # toolbar.update() 
   # canvas.get_tk_widget().pack() 

#plot_button = Button(master = window,  
                     #command = plot, 
                     #height = 2,  
                     #width = 10, 
                     #text = "Plot")   
#plot_button.pack()         


def graph_carac():
    
    new_graph = Graph(inputs=inputs, is_wheited=is_weighted_variable.get())
    new_graph.create_arcs()
    new_graph.create_nodes()
    new_graph.create_adjacency_list()
    new_graph.create_incidence_matrix()
    is_simple = new_graph.is_simple()
    is_complete = new_graph.is_complete()
    is_related = new_graph.is_related()
    is_euler = new_graph.is_eulerian()
    graph_info_frame = tk.Frame(window, pady=80, padx=80)
    graph_info_frame.pack()
    infos_label = tk.Label(graph_info_frame,
                           text="""-------------Here are Your Graphs Caracteristics:-------------
                               
                               \n"""""
                                f'1/ Is Your Graph Simple ?   ---> {is_simple} \n'
                                f'2/ Is Your Graph Connex ?   ---> {is_related} \n'
                                f'3/  Is Your Graph Complete ? ---> {is_complete} \n'
                                f'4/  Is Your Graph Eulerian  ? ---> {is_euler}',font=("Courrier",10))
    infos_label.pack()


#---------------------------------------------------------------------------------------------------------------------    

def apply_algorithm():
    my_graph = Graph(inputs=inputs, is_wheited=is_weighted_variable.get())
    algorithm_name = algorithm_input_variable.get()
    kruskal_list = []
    
    
    def draw_result_kruskal():
        final_shape = Graph(inputs=kruskal_list, is_wheited=is_weighted_variable.get())
        final_shape.display_graph()

    def draw_result_prim():
        final_shape_prim = Graph(inputs=run_prime(), is_wheited=is_weighted_variable.get())
        final_shape_prim.display_graph()

    def draw_result_dijkstra():
        final_shape_dijkstra = Graph(inputs=run_dijkstra(), is_wheited=is_weighted_variable.get())
        final_shape_dijkstra.display_graph()
        
    if algorithm_name == 'Kruskal':
           graph_info2_frame.destroy()
           kruskal_frame = tk.Frame(window)
           kruskal_frame.pack()
           kruskal_list = [(item[0] + item[2], item[1]) for item in my_graph.kruskal()]
           kruskal_header = tk.Label(kruskal_frame, text=f'KRUSKAL RESULT \n : {kruskal_list}', font='Courrier 15')
           kruskal_header.pack()
           kruskal_draw_button = tk.Button(kruskal_frame, text="KRUSKAL GRAPH", command=draw_result_kruskal)
           kruskal_draw_button.pack()

    elif algorithm_name == 'Prim':

        def run_prime():
            prim_frame.destroy()
            prim2_frame = tk.Frame(window)
            prim2_frame.pack()
            prime_list = my_graph.prime(start_point.get())
            prim_header = tk.Label(prim2_frame, text=f'PRIM RESULT \n : {prime_list}', font='Arial 15')
            prim_header.pack()
            prim_draw_button = tk.Button(prim2_frame, text="PRIM GRAPH", command=draw_result_prim)
            prim_draw_button.pack()
            return prime_list
        
        graph_info2_frame.destroy()
        prim_frame = tk.Frame(window)
        prim_frame.pack()
        prime_start_node_variable = tk.StringVar(prim_frame)
        prime_start_node_label = tk.Label(prim_frame, text="Le Point De Depart: ")
        prime_start_node_label.pack()
        prime_start_node_entry = tk.Entry(prim_frame, textvariable=prime_start_node_variable)
        prime_start_node_entry.pack()
        prime_start_node_button = tk.Button(prim_frame, text="Start", command=run_prime)
        prime_start_node_button.pack()
        start_point = prime_start_node_variable
        
    elif algorithm_name == 'Dijkstra':
        def run_dijkstra():
            dijkstra_frame.destroy()
            dijkstra2_frame = tk.Frame(window)
            dijkstra2_frame.pack()
            dijkstra_list = my_graph.dijkstra(start_point_dijkstra.get())
            dijkstra_header = tk.Label(dijkstra2_frame,
                                       text='Les Listes finales de votres Graphe : ',
                                       font='Arial 15')
            dijkstra_header.pack()
            dijkstra_table = tk.Label(dijkstra2_frame, text=f'{dijkstra_list}')
            dijkstra_table.pack()
            dijkstra_draw_button = tk.Button(dijkstra2_frame, text="Forme Graphique", font='Arial 10' )  # command=draw_result_dijkstra
            dijkstra_draw_button.pack()

        graph_info2_frame.destroy()
        dijkstra_frame = tk.Frame(window)
        dijkstra_frame.pack()
        dijkstra_start_node_variable = tk.StringVar(dijkstra_frame)
        dijkstra_start_node_label = tk.Label(dijkstra_frame, text="Le Point De Depart: ")
        dijkstra_start_node_label.pack()
        dijkstra_start_node_entry = tk.Entry(dijkstra_frame, textvariable=dijkstra_start_node_variable)
        dijkstra_start_node_entry.pack()
        dijkstra_start_node_button = tk.Button(dijkstra_frame, text="Start", command=run_dijkstra)
        dijkstra_start_node_button.pack()
        start_point_dijkstra = dijkstra_start_node_variable
        
    elif algorithm_name == 'Bellman-Ford':
     def run_bellmanf():
            bellmanf_frame.destroy()
            bellmanf2_frame = tk.Frame(window)
            bellmanf2_frame.pack()
            bellmanf_list = my_graph.bellman_ford(start_point_bellmanf.get())
            bellmanf_header = tk.Label(bellmanf2_frame,
                                       text=f'Les Listes finales de votres Graphe : ',
                                       font='Arial 15')
            bellmanf_header.pack()
            bellmanf_table = tk.Label(bellmanf2_frame, text=f'{bellmanf_list}')
            bellmanf_table.pack()
            bellmanf_draw_button = tk.Button(bellmanf2_frame, text="Forme Graphique", )  # command=draw_result_dijkstra
            bellmanf_draw_button.pack()
            return bellmanf_list

     graph_info2_frame.destroy()
     bellmanf_frame = tk.Frame(window)
     bellmanf_frame.pack()
     bellmanf_start_node_variable = tk.StringVar(bellmanf_frame)
     bellmanf_start_node_label = tk.Label(bellmanf_frame, text="Le Point De Depart: ")
     bellmanf_start_node_label.pack()
     bellmanf_start_node_entry = tk.Entry(bellmanf_frame, textvariable=bellmanf_start_node_variable)
     bellmanf_start_node_entry.pack()
     bellmanf_start_node_button = tk.Button(bellmanf_frame, text="Start", command=run_bellmanf)
     bellmanf_start_node_button.pack()
     start_point_bellmanf = bellmanf_start_node_variable
        
    elif algorithm_name == 'DFS':
        pass
    elif algorithm_name == 'BFS':
        pass

#------------------PAGE 4-----------------------------------------------------------------
def page_4():
    main_page.destroy()
    page_4 = tk.Frame(window)
    page_4.pack(expand=True)
    label = tk.Label(page_4, text="""YOUR GRAPH IS CREATED SUCCESSFULY!  
                     """, font= "Courrier 20" )
    label.pack()
    label= tk.Label(page_4, text="YOUR GRAPH IS READY TO SHOW: ",font=("Courrier",10))
    label.pack()
    display_graph_button = tk.Button(page_4, text=" SHOW GRAPH ", bg="green", command=show_graph)
    display_graph_button.pack(padx=20, pady=10, ipady=5, ipadx=10)
    display_graph_info_button = tk.Button(page_4, text=" SHOW GRAPH CARACTERISTICS ",bg="green", command=graph_carac)
    display_graph_info_button.pack(padx=20, pady=10, ipady=5, ipadx=10)
    apply_algorithm_label = tk.Label(page_4, text="CHOOSE AN ALGORITHM TO APPLY ON YOUR GRAPH:",font=("Courrier",10))
    apply_algorithm_label.pack(pady=10)
    values = ['Kruskal', 'Prim', 'Dijkstra', 'Bellman-Ford', 'BFS', 'DFS']
    algorithm_input_variable.set(values[3])
    algorithms_input = tk.OptionMenu(page_4, algorithm_input_variable,*values)
    algorithms_input.pack()
    algorithms_input.config(bg="green")
    algorithms_input["menu"].config(bg="GREEN", fg="BLACK", activebackground="GREEN", activeforeground="BLACK")
    algorithm_apply_button = tk.Button(page_4, text='APPLY ALGORITHM',bg="green", command=apply_algorithm)
    algorithm_apply_button.pack(pady=20)
    kruskal_label = tk.Label(page_4, text=f'ALGORITHM RESULT : \n {kruskal_list}',font=("Courrier",10))
    kruskal_label.pack()

#------------------PAGE 2--------------------------------------------------------------------
def graph_info_page():
    page_1.destroy()
    page_2.pack(expand=True)
    page_2_header = tk.Label(page_2, text="CHOOSE YOUR GRAPH'S CARACTERISTICS:", font="Courrier 26")
    page_2_header.pack()
    edges_variable = tk.IntVar(page_2)
    edge_label = tk.Label(page_2, text='Number Of Edges:')
    edge_label.pack()
    edges_entry = tk.Entry(page_2, textvariable=edges_variable)
    edges_entry.pack()
    edges_number_error = tk.Label(page_2, fg='red')
    edges_number_error.pack()

    
    is_oriented_label = tk.Label(page_2, text="Select If your graph is Directed(DIGRAPH): ")
    is_oriented_label.pack()
    is_oriented_input = tk.Checkbutton(page_2, variable=is_oriented_variable)
    is_oriented_input.pack()
    
    is_weighted_label = tk.Label(page_2, text="Select To add Capacity to your Edges:")
    is_weighted_label.pack()
    is_weighted_input = tk.Checkbutton(page_2, variable=is_weighted_variable)
    is_weighted_input.pack(pady=5, ipady=5)

#-----------Page 3-------------------------------------------------------------
    def graph_edges_info_page():
        page_2.destroy()
        main_page.pack(fill="x",expand=True)
        my_canvas = tk.Canvas(main_page)
        my_canvas.pack(expand=True)
        
        scroll_bar = tk.Scrollbar(main_page, orient="vertical", command=my_canvas.yview)
        scroll_bar.pack(side="right", fill="y")

        my_canvas.configure(yscrollcommand=scroll_bar.set)
        my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion=my_canvas.bbox("all")))
        
        second_frame = tk.Frame(my_canvas)
        my_canvas.create_window((20,50), window=second_frame, anchor="nw")
        third_page_header = tk.Label(second_frame, text="   Enter Your Graph  Edges :", font="kefa 20")
        third_page_header.grid(row=0, columnspan=3)
        widgets_inputs_list = []

        # Get and Store The User Inputs

        def append_inputs():
            for item in widgets_inputs_list:
                if is_weighted_variable.get():
                    inputs.append((item[0].get(), item[1].get()))
                else:
                    inputs.append(item.get())

            page_4()

        # Get and Store The User Inputs End

        # Generate The List Of Entries For User Inputs(graph Information)

        edges_number = edges_variable.get()

        if is_weighted_variable.get():
            for i in range(edges_number):
                edge_weight_variable = tk.IntVar(second_frame)
                edge_name_label = tk.Label(second_frame, text= f'Edge {i + 1}')
                edge_weight_label = tk.Label(second_frame, text= f'Capacity {i + 1}')
                edge_name_label.grid(row=i + 1, column=i - i)
                edge_weight_label.grid(row=i + 1, column=i + 2 - i)
                edge_name_entry = tk.Entry(second_frame, )
                edge_weight_entry = tk.Entry(second_frame, textvariable=edge_weight_variable)
                edge_name_entry.grid(row=i + 1, column=i - (i - 1))
                edge_weight_entry.grid(row=i + 1, column=i + 3 - (i - 1))
                edges_weight_error = tk.Label(second_frame, fg='red')
                edges_weight_error.grid(row=i + 2, column=i + 3 - (i - 1))
                widgets_inputs_list.append((edge_name_entry, edge_weight_entry))

                # Error Handling
                def only_integer(data):
                    if data.isdigit():
                        return True
                    else:
                        return False

                def only_integers_errors(data):
                    edges_weight_error.configure(
                        text=f'Plz enter a valid number!'
                    )

                register_only_ints = page_2.register(only_integer)
                register_only_errors =page_2.register(only_integers_errors)
                edge_weight_entry.config(validate='all',
                                         validatecommand=(register_only_ints, '%P'),
                                         invalidcommand=(register_only_errors, '%P'))
                # Error Handling End
        else:
            for i in range(edges_number):
                edge_name_label = tk.Label(second_frame, text=f'EDGE {i}')
                edge_name_label.grid(row=i + 1, column=i - i)
                edge_name_entry = tk.Entry(second_frame, )
                edge_name_entry.grid(row=i + 1, column=i - (i - 1))
                widgets_inputs_list.append(edge_name_entry)

        # Generate The List Of Entries For User Inputs(graph's Information) End

        # Submit Button for inputs
        show_inputs_button = tk.Button(second_frame, text=" Create ",bg='green',command=append_inputs)
        show_inputs_button.grid(columnspan=2)
        label = tk.Label(second_frame, )
        label.grid()

        # Submit Button End

    # Start Error Handling for Edges Entry IN second_page

    def only_integers(data):
        if data.isdigit():
            return True
        else:
            return False

    def only_integers_error(data):
        edges_number_error.configure(
            text=f'Plz enter a valid Number!')

    register_only_int = page_2.register(only_integers)
    register_only_error = page_1.register(only_integers_error)
    edges_entry.config(validate='all',
                       validatecommand=(register_only_int, '%P'),
                       invalidcommand=(register_only_error, '%P'))

    # End of Error Handling

    # Submit Button for Second page

    submit_button = tk.Button(page_2, text=' Submit ',bg='green',command=graph_edges_info_page)
    submit_button.pack(padx=20, pady=10, ipady=5, ipadx=10)

    # Submit Button End

#----------------First Page-----------------------------------------------
def page__1():
    page_1.pack(expand=True)
    page_1_header = tk.Label(page_1, text="Welcome To Theory Of Graphs Application", font='Kefa 25 ',fg='#000')
    page_1_sub_header = tk.Label(page_1, text="Create And Manipulate Your Graphs with Us", font='Kefa 15',fg='#000')
    page_1_header.pack()
    page_1_sub_header.pack()
    create_button = tk.Button(page_1, text=" Create your Graph ", bg='green', command=graph_info_page)
    create_button.pack(padx=20, pady=10, ipady=5, ipadx=10)

page__1()


window.mainloop()
