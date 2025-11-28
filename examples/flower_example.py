from src.rdsolver import gray_scott
import matplotlib.pyplot as plt

def main():
    u, v = gray_scott(
        backend="numpy",
        grid_size=150,
        steps=10000,
        time_step=1,
        u_diffusion=0.16,
        v_diffusion=0.08,
        feed_rate=0.055,
        kill_rate=0.062,
    )

    plt.figure(figsize=(10, 10))
    plt.imshow(v, cmap="inferno", vmin=0, vmax=1)
    plt.axis("off")
    plt.show()

if __name__ == "__main__":
    main()