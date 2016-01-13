__author__ = 'sergey'


#
# from random import random
# from kivy.app import App
# from kivy.uix.widget import Widget
# from kivy.uix.button import Button
# from kivy.graphics import Color, Ellipse, Line
#
#
# class MyPaintWidget(Widget):
#
#     def on_touch_down(self, touch):
#         color = (random(), 1, 1)
#         with self.canvas:
#             Color(*color, mode='hsv')
#             d = 30.
#             Ellipse(pos=(touch.x - d / 2, touch.y - d / 2), size=(d, d))
#             touch.ud['line'] = Line(points=(touch.x, touch.y))
#
#     def on_touch_move(self, touch):
#         touch.ud['line'].points += [touch.x, touch.y]
#
#
# class MyPaintApp(App):
#
#     def build(self):
#         parent = Widget()
#         self.painter = MyPaintWidget()
#         clearbtn = Button(text='Clear')
#         clearbtn.bind(on_release=self.clear_canvas)
#         parent.add_widget(self.painter)
#         parent.add_widget(clearbtn)
#         return parent
#
#     def clear_canvas(self, obj):
#         self.painter.canvas.clear()
#
#
# if __name__ == '__main__':
#     MyPaintApp().run()


from kivy.garden.graph import Graph, MeshLinePlot
graph = Graph(xlabel='X', ylabel='Y', x_ticks_minor=5,
x_ticks_major=25, y_ticks_major=1,
y_grid_label=True, x_grid_label=True, padding=5,
x_grid=True, y_grid=True, xmin=-0, xmax=100, ymin=-1, ymax=1)
plot = MeshLinePlot(color=[1, 0, 0, 1])
plot.points = [(x, sin(x / 10.)) for x in range(0, 101)]
graph.add_plot(plot)

