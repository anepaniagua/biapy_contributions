#!/bin/bash

best_execution=$1
dir_name=$2
new_dir=$3

# Define base directory (edit this)
base_dir="/data2/apaniagua/exp_results/"

dir_path="$base_dir/$dir_name"
mkdir -p "$new_dir"

# Copy checkpoint(s)
cp "$dir_path"/checkpoints/"${dir_name}_${best_execution}"* "$new_dir"

# Copy config file
cp "$dir_path"/config_files/"${dir_name}.yaml" "$new_dir"

echo "✅ Files copied successfully to $new_dir"
