# Makefile for building main blog and all sub-blogs

RED=\033[0;31m
GREEN=\033[0;32m
CYAN=\033[0;36m
YELLOW=\033[0;33m
NO_COLOR=\033[0m

.PHONY: all
all: build

.PHONY: build
build: main subblogs
	@echo "$(GREEN)======== Build Complete ==========$(NO_COLOR)"

.PHONY: main
main:
	@echo "$(CYAN)======== Building Main Blog ==========$(NO_COLOR)"
	bundle install
	bundle exec jekyll build
	@echo "$(CYAN)======================================$(NO_COLOR)"

.PHONY: subblogs
subblogs:
	@echo "$(CYAN)======== Building Sub-Blogs ==========$(NO_COLOR)"
	@home_dir=$$(pwd); \
	for d in blogs/*/ ; do \
	  echo "$(YELLOW)=> Building Blog: '$$d' $(NO_COLOR)"; \
	  cd $$home_dir/$$d; \
	  bundle install; \
	  bundle exec jekyll build --destination $$home_dir/_site/$${PWD##*/}; \
	done
	@echo "$(CYAN)======================================$(NO_COLOR)"

# Dependency management targets
.PHONY: update-deps
update-deps:
	@echo "$(CYAN)======== Updating Shared Dependencies ==========$(NO_COLOR)"
	bundle update
	@echo "$(CYAN)======== Updating Sub-Blog Dependencies ==========$(NO_COLOR)"
	@home_dir=$$(pwd); \
	for d in blogs/*/ ; do \
	  echo "$(YELLOW)=> Updating dependencies for: '$$d' $(NO_COLOR)"; \
	  cd $$home_dir/$$d; \
	  bundle update; \
	done
	@echo "$(GREEN)======== Dependencies Updated ==========$(NO_COLOR)"

.PHONY: clean
clean:
	@echo "$(CYAN)======== Cleaning Build Artifacts ==========$(NO_COLOR)"
	rm -rf _site/
	@echo "$(GREEN)======== Clean Complete ==========$(NO_COLOR)"

.PHONY: import-doltremare-blogspot
import-doltremare-blogspot:
	@echo "$(CYAN)======== Importing Blogspot Posts for Doltremare ==========$(NO_COLOR)"
	pushd blogs/doltremare/import; \
	python3 blogspot_import.py; \
	popd; \
	echo "$(GREEN)======== Blogspot Posts Imported for Doltremare ==========$(NO_COLOR)"