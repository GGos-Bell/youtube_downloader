from selector import Selector

komeko_link = "https://www.youtube.com/watch?v=ERPlZKPYWuw"

komeko_video = Selector(komeko_link)

a = komeko_video.get_complete_video("./img_test/", "komeko.mp4")