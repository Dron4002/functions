def make_album(singer_name, album_name):
    album = f"{singer_name}, {album_name}"
    return album.title()
while True:
    print("\nПожалуйста, введите имя исполнителя и название альбома.")
    print("(Введите 'q' чтобы в любой момент выйти из цикла)")
    s_name = input("Имя исполнителя: ")
    if s_name == 'q':
        break
    a_name = input("Название альбома: ")
    if a_name == 'q':
        break
    album = make_album(s_name, a_name)
    print(f"\n{album}")
