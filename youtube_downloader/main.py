from selector import Selector

komeko_link = "https://www.youtube.com/watch?v=4EbRtU4z-nU"

# komeko "https://www.youtube.com/watch?v=ERPlZKPYWuw"
# kaguya "https://www.youtube.com/watch?v=CEygJomZvBc"
# trump "https://www.youtube.com/watch?v=4EbRtU4z-nU"
komeko_video = Selector(komeko_link)

a = komeko_video.get_complete_video("./img_test/", "trump.mp4")