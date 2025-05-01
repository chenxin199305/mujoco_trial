import time
import mujoco.viewer


def main():
    # Create a viewer
    viewer = mujoco.viewer.MujocoViewer()

    # Load a model
    model = mujoco.MjModel.from_xml_path("path/to/your/model.xml")

    # Set the model to the viewer
    viewer.set_model(model)

    # Main loop
    while True:
        # Render the viewer
        viewer.render()

        # Sleep for a short duration to control the frame rate
        time.sleep(0.01)


if __name__ == "__main__":
    main()
