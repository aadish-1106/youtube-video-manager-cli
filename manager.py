from storage import save_data

def list_videos(videos):
    if not videos:
        print("No videos available.")
        return

    print("\nYour Videos:")
    for index, video in enumerate(videos, start=1):
        print(f"{index}. {video['name']} ({video['duration']})")


def add_video(videos):
    name = input("Enter video name: ")
    duration = input("Enter video duration: ")

    videos.append({
        "name": name,
        "duration": duration
    })

    save_data(videos)
    print("Video added successfully.")


def update_video(videos):
    list_videos(videos)

    try:
        choice = int(input("Enter video number to update: ")) - 1
        if 0 <= choice < len(videos):
            name = input("Enter new video name: ")
            duration = input("Enter new duration: ")

            videos[choice]["name"] = name
            videos[choice]["duration"] = duration

            save_data(videos)
            print("Video updated successfully.")
        else:
            print("Invalid selection.")
    except ValueError:
        print("Please enter a valid number.")


def delete_video(videos):
    list_videos(videos)

    try:
        choice = int(input("Enter video number to delete: ")) - 1
        if 0 <= choice < len(videos):
            deleted = videos.pop(choice)
            save_data(videos)
            print(f"Deleted video: {deleted['name']}")
        else:
            print("Invalid selection.")
    except ValueError:
        print("Please enter a valid number.")
