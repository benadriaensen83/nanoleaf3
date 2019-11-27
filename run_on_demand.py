from nanoleaf import Nanoleaf
from colours import Picular

nano = Nanoleaf()
picular = Picular()

query = input('search for a light input here')

data = picular.search(query)
data = picular.rgb_to_HSB(data[:5])

print(data)
# data = [{'hue': 0.018140589569160998, 'brightness': 110.5, 'saturation': -0.6712328767123288}, {'hue': 0.004504504504504496, 'brightness': 123.5, 'saturation': -0.7551020408163265}, {'hue': 0.06318082788671024, 'brightness': 117.5, 'saturation': -0.6566523605150214}, {'hue': 0.1011904761904762, 'brightness': 219.0, 'saturation': -0.12844036697247707}, {'hue': 0.013725490196078438, 'brightness': 128.0, 'saturation': -0.6692913385826772}]

nano.display_scene(data)