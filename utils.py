import numpy as np
import pickle

def load_data(split="train"):
    """
    A function to load the data.

    Parameters:
    - split: str, "train" or "test"

    Returns:
    - masked_images: np.ndarray, shape (n_images, channels, height, width), the images with random masks applied
    - masks: np.ndarray, shape (n_images, 4), the boundaries of the masks (left, bottom, right, top)
    - parametric: np.ndarray, shape (n_images, 3), the parametric representation of the images
    - description: list, the description of the images
    - images: np.ndarray, shape (n_images, channels, height, width), the original images
    """
    masked_images = []
    if split == "train":
        for i in range(10):
            masked_im_slice = np.load(f"data/masked_train_{i}.npy")
            masked_images.append(masked_im_slice)
        masked_images = np.concatenate(masked_images, axis=0)

        images = []
        for i in range(10):
            im_slice = np.load(f"data/images_train_{i}.npy")
            images.append(im_slice)
        images = np.concatenate(images, axis=0)
    else:
        masked_images = np.load(f"data/masked_test.npy")
        images = np.load(f"data/images_test.npy")

    description = pickle.load(open(f"data/desc_{split}.pkl", "rb"))

    parametric = np.load(f"data/param_{split}.npy")

    masks = np.load(f"data/mask_{split}.npy")


    return masked_images, masks, parametric, description, images


def apply_random_mask(images, minimum_proportion=0.4, maximum_proportion=0.8):
    """
    Apply a random rectangular mask to a batch of images and return the coordinates of the masked area.

    Parameters:
    - images: np.ndarray, shape (batch_size, channels, height, width)
    - minimum_proportion: float, minimum proportion of image dimensions for mask size
    - maximum_proportion: float, maximum proportion of image dimensions for mask size

    Returns:
    - masked_images: np.ndarray, images with applied random masks
    - mask_coordinates: np.ndarray, shape (batch_size, 4), coordinates (left, bottom, right, top) of masked area for each image
    """
    batch_size, channels, height, width = images.shape
    masked_images = images.copy()  # Copy images to avoid modifying the original array
    mask_coordinates = np.zeros((batch_size, 4), dtype=int)  # Array to store coordinates for each mask
    
    # Random mask sizes within the specified proportions
    mask_heights = np.random.randint(int(height * minimum_proportion), int(height * maximum_proportion), batch_size)
    mask_widths = np.random.randint(int(width * minimum_proportion), int(width * maximum_proportion), batch_size)
    
    # Random positions for the mask (ensuring mask fits within image boundaries)
    top_positions = np.random.randint(0, height - mask_heights + 1, batch_size)
    left_positions = np.random.randint(0, width - mask_widths + 1, batch_size)
    
    # Apply the masks and record coordinates
    for i in range(batch_size):
        top = top_positions[i]
        left = left_positions[i]
        mask_height = mask_heights[i]
        mask_width = mask_widths[i]
        
        # Define the coordinates
        bottom = top + mask_height
        right = left + mask_width
        
        # Set the mask area to -1 across all channels for the i-th image
        masked_images[i, :, top:bottom, left:right] = 255
        
        # Store the coordinates as (left, bottom, right, top)
        mask_coordinates[i] = [left, bottom, right, top]
    
    return masked_images, mask_coordinates

def mask_array_with_nan(arr, fraction=0.7):
    """
    Randomly mask a fraction of values in an array with NaN.

    Parameters:
    - arr: np.ndarray, the array to be masked
    - fraction: float, the fraction of values to be masked with NaN

    Returns:
    - masked_arr: np.ndarray, a copy of the array with NaN values injected
    """
    masked_arr = arr.copy()  # Create a copy to avoid modifying the original array
    total_values = arr.size  # Total number of elements in the array
    n_mask = int(total_values * fraction)  # Number of values to mask

    # Randomly choose indices to set as NaN
    flat_indices = np.random.choice(total_values, n_mask, replace=False)
    
    # Set chosen indices to NaN in the flattened array
    masked_arr.flat[flat_indices] = np.nan
    
    return masked_arr