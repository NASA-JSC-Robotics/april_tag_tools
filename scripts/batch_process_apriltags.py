import os
import cv2


def batch_upscale_images(input_dir, output_dir):
    """
    Reads all images from the input directory, scales them up,
    and saves them to the output directory.
    """
    # Supported image extensions for OpenCV
    valid_extensions = (".jpg", ".jpeg", ".png", ".bmp", ".tiff", ".webp")

    # Create output directory if it does not exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        print(f"Created output directory: {output_dir}")

    # List all files in the input directory
    files = os.listdir(input_dir)
    processed_count = 0

    for file_name in files:
        # Check if file has an eligible image extension
        if file_name.lower().endswith(valid_extensions):
            input_path = os.path.join(input_dir, file_name)
            output_path = os.path.join(output_dir, file_name)

            # Read image
            img = cv2.imread(input_path)
            if img is None:
                print(f"Skipping corrupt or unreadable image: {file_name}")
                continue

            # Execute the resolution resize configuration
            resized_img = cv2.resize(img, (128, 128), interpolation=cv2.INTER_NEAREST)

            # Save the enlarged image
            cv2.imwrite(output_path, resized_img)
            print(f"Processed: {file_name} -> 128x128")
            processed_count += 1

    print(f"\nSuccessfully batch processed {processed_count} images.")


if __name__ == "__main__":
    # Define folder locations
    INPUT_FOLDER = "<path-to-repo>/apriltag-imgs/tag36h11/"
    OUTPUT_FOLDER = "<path-to-destination>/36h11/"

    batch_upscale_images(INPUT_FOLDER, OUTPUT_FOLDER)
