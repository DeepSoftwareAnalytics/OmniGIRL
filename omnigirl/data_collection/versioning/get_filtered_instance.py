import os
import json
def filter_instances(input_file_path, output_file_path, version_dict):
    """Filter instances based on version information and save results.
    
    Args:
        input_file_path: Path to input JSON file containing instances
        output_file_path: Path to save filtered instances
        version_dict: Dictionary mapping repos to pull request versions
    """
    with open(input_file_path, 'r') as file:
        data = json.load(file)
    
    print(f"Total instances: {len(data)}")
    filtered_data = []
    
    for instance in data:
        # Get version mapping for current repo if exists
        pull2version = version_dict.get(instance['repo'])
        pull_idx = str(instance['pull_number'])
        
        # Skip if no version information
        if not instance.get('version'):
            continue
            
        # Handle special cases
        if instance['version'] == '.':
            continue
            
        if instance['version'] != 'get_version':
            # Apply version corrections
            if instance['version'] == '4.25' and pull_idx in ['601', '603']:
                instance['version'] = '4.251'
            if instance['version'] == '0.13' and '7597' <= pull_idx <= '8244':
                instance['version'] = '0.13dev'
                
            # Initialize test result lists
            instance['PASS_TO_PASS'] = []
            instance['FAIL_TO_PASS'] = []
            filtered_data.append(instance)
            
        elif pull2version and pull_idx in pull2version:
            # Use version from version_dict if available
            instance['version'] = pull2version[pull_idx]
            instance['PASS_TO_PASS'] = []
            instance['FAIL_TO_PASS'] = []
            filtered_data.append(instance)
    
    print(f"Filtered instances: {len(filtered_data)}")
    
    with open(output_file_path, 'w') as file:
        json.dump(filtered_data, file, indent=4)

def main():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--base_dir', type=str, required=True, help='Base directory containing data files')
    parser.add_argument('--input_filename', type=str, default='final_task_instance_versions.json', 
                       help='Input filename to process')
    parser.add_argument('--output_filename', type=str, default='filtered_final_task_instance_versions.json',
                       help='Output filename to save filtered results')
    parser.add_argument('--version_dict_path', type=str, required=True,
                       help='Path to version dictionary JSON file')
    
    args = parser.parse_args()
    
    with open(args.version_dict_path, 'r') as f:
        version_dict = json.load(f)
    
    for root, dirs, files in os.walk(args.base_dir):
        if args.input_filename in files:
            input_file_path = os.path.join(root, args.input_filename)
            output_file_path = os.path.join(root, args.output_filename)
            print(f"Processing file: {input_file_path}")
            filter_instances(input_file_path, output_file_path, version_dict)

if __name__ == "__main__":
    main()
