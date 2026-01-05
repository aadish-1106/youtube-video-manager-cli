from storage import load_data
from manager import (
    list_videos,
    add_video,
    update_video,
    delete_video
)

def main():
    videos = load_data()

    while True:
        print("\nYouTube Video Manager")
        print("1. List Videos")
        print("2. Add Video")
        print("3. Update Video")
        print("4. Delete Video")
        print("5. Exit")

        choice = input("Choose an option: ")

        match choice:
            case "1":
                list_videos(videos)
            case "2":
                add_video(videos)
            case "3":
                update_video(videos)
            case "4":
                delete_video(videos)
            case "5":
                print("Goodbye!")
                break
            case _:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
