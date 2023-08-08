#!/usr/bin/env bash

echo "======== Building Main blog =========="
bundle install
bundle exec jekyll build
echo "======================================"
echo "======== Building Sub-Blogs =========="
home_dir=$(pwd)
for d in blogs/*/ ; do
    echo "=> Building Blog: '$d'"
    pushd $home_dir/$d
    bundle install
    bundle exec jekyll build --destination $home_dir/_site/${PWD##*/}
done

