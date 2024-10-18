import flet as ft


def main(page: ft.Page):

    #funcion para reproducir audio
    def reproducir(evento):
        print("Prueba play")
        audio.play()
    #Funcion para pausar audio
    def pausar(evento):
        print("Prueba pause")
        audio.pause()

     #funcion para reproducir audio
    def reproducirVideo(evento):
        print("Prueba play")
        video.play()
    #Funcion para pausar audio
    def pausarVideo(evento):
        print("Prueba pause")
        video.pause()
    
    #Componente Audio
    audio=ft.Audio(src="https://res.cloudinary.com/dlktvgsna/video/upload/v1729274779/my-music-2-242790_ymug1l.mp3", autoplay=False, volume=1, )
    audio2=ft.Audio(src="https://res.cloudinary.com/dlktvgsna/video/upload/v1729274676/df_wahyumusicproduction-242793_se3y9r.mp3", autoplay=False, volume=1)
    #Component Video
    video=ft.Video(playlist=ft.VideoMedia("https://res.cloudinary.com/dlktvgsna/video/upload/v1729277034/5495890-hd_1080_1920_30fps_ytue1n.mp4"),title="Video de Prueba",show_controls=True,width=300,height=450)


    botonPlay=ft.CupertinoFilledButton(text="Play", on_click=reproducir)
    botonPause=ft.CupertinoFilledButton(text="Pausar", on_click=pausar)
    
    botonPlayVideo=ft.CupertinoFilledButton(text="Reproducir Video", on_click=reproducirVideo)
    botonPauseVideo=ft.FilledButton(text="Pausar Video",on_click=pausarVideo)


    page.add(botonPlay,botonPause,audio,video, botonPlayVideo,botonPauseVideo)


ft.app(main)
