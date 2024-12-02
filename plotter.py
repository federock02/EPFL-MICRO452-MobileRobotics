import matplotlib.pyplot as plt
import numpy as np

class Plotter:
    def __init__(self):
        self.map = None
        self.goal = None
        self.start = None
        self.row_trajectory = []
        self.col_trajectory = []
        self.row_kalman_pred = []
        self.col_kalman_pred = []

        # initialize plot elements
        self.fig, self.ax = plt.subplots(figsize=(10, 10))
        self.map_image = None
        self.start_marker, = self.ax.plot([], [], 'go', label='Start')
        self.goal_marker, = self.ax.plot([], [], 'bo', label='Goal')
        self.path_scatter = None
        self.traj_plot, = self.ax.plot([], [], 'b-', label='Trajectory')
        self.pred_plot, = self.ax.plot([], [], 'g-', label='Kalman Prediction')

    def set_map(self, map, start, goal):
        # sets the map, start, and goal, and initializes the live view
        self.map = map
        self.start = start
        self.goal = goal
        rows, cols = self.map.shape

        # display the map
        self.map_image = self.ax.imshow(self.map, cmap='gray', origin='lower')

        # mark the start and goal positions
        self.start_marker.set_data([self.start[1]], [self.start[0]])
        self.goal_marker.set_data([self.goal[1]], [self.goal[0]])

        # set grid, labels, and legend
        self.ax.set_xticks(range(0, cols, max(1, cols // 10)))
        self.ax.set_yticks(range(0, rows, max(1, rows // 10)))
        self.ax.grid(color='gray', linestyle='--', linewidth=0.5)
        self.ax.invert_yaxis()  # match grid orientation to the array
        self.ax.set_title("Live View with Path")
        self.ax.legend()
        plt.show(block=False)
        plt.pause(0.1)

    def update_path(self, path):
        # updates the path on the live view
        self.path = path
        if self.path:
            path_rows, path_cols = zip(*self.path)
            if self.path_scatter is not None:
                self.path_scatter.remove()
            self.path_scatter = self.ax.scatter(path_cols, path_rows, c='red', s=50, label='Path')
        self.ax.legend()
        self.fig.canvas.draw_idle()
        plt.pause(0.1)

    def update_traj(self, row, col):
        # updates the trajectory on the plot
        self.row_trajectory.append(row)
        self.col_trajectory.append(col)
        self.traj_plot.set_data(self.col_trajectory, self.row_trajectory)
        self.ax.legend()
        self.fig.canvas.draw_idle()
        plt.pause(0.1)

    def update_pred(self, row, col):
        # updates the Kalman prediction on the plot
        self.row_kalman_pred.append(row)
        self.col_kalman_pred.append(col)
        self.pred_plot.set_data(self.col_kalman_pred, self.row_kalman_pred)
        self.ax.legend()
        self.fig.canvas.draw_idle()
        plt.pause(0.1)


    """
    def plot_trajectory(self, row_trajectory, col_trajectory):

        # plot the trajectory on the map
        rows, cols = self.map.shape
        plt.figure(figsize=(10, 10))
        plt.imshow(self.map, cmap='gray', origin='lower')
        if self.path != []:
            # plot the path
            path_rows, path_cols = zip(*self.path)
            plt.scatter(path_cols, path_rows, color='blue', marker='s', label='Path')

        plt.plot(col_trajectory, row_trajectory, color='red', marker='o', label='Trajectory')
        
        plt.xticks(range(0, cols, 5))
        plt.yticks(range(0, rows, 5))
        plt.grid(color='gray', linestyle='--', linewidth=0.5)
        plt.gca().invert_yaxis()
        plt.title("Grid Map with Trajectory")
        plt.legend()
        plt.show()

    def plot_kalman_prediction(self, x_pred, y_pred, angle_pred):
        # plot the kalman prediction
        plt.plot(x_pred, y_pred, label='Kalman Prediction')
        plt.xlabel('X')
        plt.ylabel('Y')
        plt.title('Kalman Prediction')
        plt.legend()
        plt.show()

    def plot_map(self):
        # plot the map
        rows, cols = self.map.shape
        # plot start and goal
        plt.figure(figsize=(10, 10))
        plt.imshow(self.map, cmap='gray', origin='lower')
        plt.plot(self.start[1], self.start[0], color='green', marker='o', label='Start')
        plt.plot(self.goal[1], self.goal[0], color='blue', marker='o', label='Goal')
        plt.xticks(range(0, cols, 5))
        plt.yticks(range(0, rows, 5))
        plt.grid(color='gray', linestyle='--', linewidth=0.5)
        plt.gca().invert_yaxis()  # Match grid orientation to the array
        plt.title("Grid Map with Start and Goal")
        plt.legend()
        plt.show()
    
    def plot_map_given(self, map, start, goal):
        # plot the map
        rows, cols = map.shape
        # plot start and goal
        plt.figure(figsize=(10, 10))
        plt.imshow(map, cmap='gray', origin='lower')
        plt.plot(start[1], start[0], color='green', marker='o', label='Start')
        plt.plot(goal[1], goal[0], color='blue', marker='o', label='Goal')
        plt.xticks(range(0, cols, 5))
        plt.yticks(range(0, rows, 5))
        plt.grid(color='gray', linestyle='--', linewidth=0.5)
        plt.gca().invert_yaxis()
        plt.title("Grid Map with Start and Goal")
        plt.legend()
        plt.show()
    """