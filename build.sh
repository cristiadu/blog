#!/usr/bin/env bash

echo "======== Building Main blog =========="
bundle install
bundle exec jekyll build
echo "======================================"
echo "======== Building Sub-Blogs =========="
home_dir=$(pwd)
for d in blogs/*/ ; do
    # For each subdirectory of `<repository>/blogs` do the following:
    echo "=> Building Blog: '$d'"
    cd $home_dir/$d
    bundle install
    # Basically, build subblogs individually so themes and custom layouts are applied
    # And set the build destination to <repository>/_site for gh-pages deployment.
    bundle exec jekyll build --destination $home_dir/_site/${PWD##*/}
done
