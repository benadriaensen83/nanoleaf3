import cv2
from sklearn.cluster import KMeans
from adobe import AdobeStock
from dominant_colours import Colours
import matplotlib.pyplot as plt
from colours import Picular
from nanoleaf import Nanoleaf



import urllib


def main(query, local = False):

    colours = Colours()
    picular = Picular()
    nano = Nanoleaf()

    if local:
        pass
    else:
        stock = AdobeStock()
        pic_url = stock.fetch_image_url(query = query)
        urllib.request.urlretrieve(pic_url, "foo.png")


    img = cv2.imread("foo.png")
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    img = img.reshape((img.shape[0] * img.shape[1],3))
    clt = KMeans(n_clusters=5)
    clt.fit(img)

    hist = colours.find_histogram(clt)
    bar = colours.plot_colors2(hist, clt.cluster_centers_)

    print(hist)

    colours_prob = []
    for i in range(len(clt.cluster_centers_)):
        print(clt.cluster_centers_[i])
        rgb_prob = (int(clt.cluster_centers_[i][0]),int(clt.cluster_centers_[i][1]),int(clt.cluster_centers_[i][2]),int(hist[i]*100))
        colours_prob.append(rgb_prob)
    print(colours_prob)

    data = picular.rgb_to_HSB(colours_prob)
    nano.display_scene(data)

    plt.axis("off")
    plt.imshow(bar)
    plt.show()



if __name__ == "__main__":

    main(query='clownfish')

