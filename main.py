import moderngl_window as mglw


class App(mglw.WindowConfig):
    window_size = (1600, 900)
    resource_dir = "shaders"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # create screen-aligned quad to draw on
        self.quad = mglw.geometry.quad_fs()

        # load shader program
        self.prog = self.load_program(vertex_shader='vertex_shader.glsl',
                                      fragment_shader='fragment_shader.glsl')

        self.set_uniform('resolution', self.window_size)

    def set_uniform(self, name, value):
        try:
            self.prog[name] = value
        except KeyError:
            print(f"Uniform '{name}' not found in shader.")

    def on_render(self, time, frame_time):
        self.ctx.clear()
        self.set_uniform('time', time)
        self.quad.render(self.prog)


if __name__ == "__main__":
    mglw.run_window_config(App)
