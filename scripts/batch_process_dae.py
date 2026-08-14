import os
import xml.etree.ElementTree as ET

def batch_copy_dae(source_mesh_path, input_dir, output_dir):
    """
    Reads all images from the input directory, scales them up, 
    and saves them to the output directory.
    """
    # Supported image extensions for OpenCV
    valid_extensions = ('.jpg', '.jpeg', '.png', '.bmp', '.tiff', '.webp')
    
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
            output_path = os.path.join(output_dir, file_name[:-3] + "dae")
            
            try:
                # Register the default COLLADA namespace globally to avoid nasty 'ns0:' prefixes on save
                # .dae files almost universally use the 2005/11/COLLADASchema namespace
                ns = 'http://collada.org'
                ET.register_namespace('', ns)
                
                # Parse the XML structure
                tree = ET.parse(source_mesh_path)
                root = tree.getroot()

                # 2. Dynamically extract the namespace URL from the root tag
                if root.tag.startswith("{"):
                    actual_namespace = root.tag.split("}")[0].strip("{")
                    # Register it to keep the output file clean (no ns0:)
                    ET.register_namespace('', actual_namespace)
                else:
                    actual_namespace = ""

                # 3. Create a namespace dictionary for the search query
                # This maps a temporary prefix shortcut ('dae') to your file's real URL
                ns_map = {'dae': actual_namespace} if actual_namespace else {}

                # 4. Target the SPECIFIC init_from inside library_images -> image
                # This skips any unrelated init_from tags hidden elsewhere in the file
                search_query = ".//dae:library_images/dae:image/dae:init_from" if actual_namespace else ".//library_images/image/init_from"
                target_element = root.find(search_query, ns_map)

                # 5. Modify the element if found
                if target_element is not None:
                    print(f"Found texture tag! Current value: '{target_element.text}'")
                    target_element.text = file_name
                    print("Texture updated successfully.")
                else:
                    print("Error: Could not find the '<init_from>' tag using the namespace map.")
                    
                    # Debugging fallback: print out what tags actually exist in your file
                    print("\nListing all tags found in the file for debugging:")
                    for elem in root.iter():
                        if "init_from" in elem.tag:
                            print(f"-> Found tag name variant: {elem.tag}")


                # Write out the modified data to the new copy destination
                tree.write(output_path, encoding='utf-8', xml_declaration=True)
                print(f"\nSuccessfully created updated file copy at: '{output_path}'")
                print(f"Created: {file_name} -> meshfile")
                processed_count += 1

            except ET.ParseError:
                print(f"Error: The file '{source_mesh_path}' is not valid XML.")
                return False
            except Exception as e:
                print(f"An unexpected error occurred: {e}")
                return False

    print(f"\nSuccessfully batch processed {processed_count} images.")

if __name__ == "__main__":
    # Define folder locations
    SOURCE_MESH = "<path-to-source-mesh>/apriltag_model.dae"
    INPUT_FOLDER = "<path-to-128x128-textures>/36h11/"
    OUTPUT_FOLDER = "<path-to-destination>/36h11/"
    
    batch_copy_dae(SOURCE_MESH, INPUT_FOLDER, OUTPUT_FOLDER)