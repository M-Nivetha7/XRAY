import matplotlib.pyplot as plt

def show_pipeline(images, titles):
    plt.figure(figsize=(12,8))
    for i in range(len(images)):
        plt.subplot(2,3,i+1)
        plt.imshow(images[i], cmap='gray')
        plt.title(titles[i])
        plt.axis('off')
    plt.tight_layout()
    plt.show()
