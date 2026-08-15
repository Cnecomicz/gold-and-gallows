TEX_DIR   := tex
BUILD_DIR := build
PDF_DIR   := pdf

RULES_PDF := $(PDF_DIR)/Gold & Gallows Rules Booklet.pdf
REF_PDF   := $(PDF_DIR)/Gold & Gallows Referee Guidebook.pdf
MOD_PDF   := $(PDF_DIR)/Gold & Gallows Modular Rules.pdf

.PHONY: all rules-booklet referee-guidebook modular-rules clean

all: rules-booklet referee-guidebook modular-rules

rules-booklet:
	@mkdir -p "$(BUILD_DIR)" "$(PDF_DIR)"
	@echo "Building Gold & Gallows Rules Booklet..."
	cd "$(TEX_DIR)" && latexmk \
		-xelatex \
		-interaction=nonstopmode \
		-halt-on-error \
		-outdir="../$(BUILD_DIR)" \
		"rules_booklet.tex"
	@if [ ! -f "$(RULES_PDF)" ] || [ "$(BUILD_DIR)/rules_booklet.pdf" -nt "$(RULES_PDF)" ]; then \
		cp "$(BUILD_DIR)/rules_booklet.pdf" "$(RULES_PDF)"; \
		echo "Created: $(RULES_PDF)"; \
		open -a Skim "$(RULES_PDF)"; \
	else \
		echo "Rules Booklet is already up-to-date."; \
	fi

referee-guidebook:
	@mkdir -p "$(BUILD_DIR)" "$(PDF_DIR)"
	@echo "Building Gold & Gallows Referee Guidebook..."
	cd "$(TEX_DIR)" && latexmk \
		-xelatex \
		-interaction=nonstopmode \
		-halt-on-error \
		-outdir="../$(BUILD_DIR)" \
		"referee_guidebook.tex"
	@if [ ! -f "$(REF_PDF)" ] || [ "$(BUILD_DIR)/referee_guidebook.pdf" -nt "$(REF_PDF)" ]; then \
		cp "$(BUILD_DIR)/referee_guidebook.pdf" "$(REF_PDF)"; \
		echo "Created: $(REF_PDF)"; \
		open -a Skim "$(REF_PDF)"; \
	else \
		echo "Referee Guidebook is already up-to-date."; \
	fi

modular-rules:
	@mkdir -p "$(BUILD_DIR)" "$(PDF_DIR)"
	@echo "Building Gold & Gallows Modular Rules..."
	cd "$(TEX_DIR)" && latexmk \
		-xelatex \
		-interaction=nonstopmode \
		-halt-on-error \
		-outdir="../$(BUILD_DIR)" \
		"modular_rules.tex"
	@if [ ! -f "$(MOD_PDF)" ] || [ "$(BUILD_DIR)/modular_rules.pdf" -nt "$(MOD_PDF)" ]; then \
		cp "$(BUILD_DIR)/modular_rules.pdf" "$(MOD_PDF)"; \
		echo "Created: $(MOD_PDF)"; \
		open -a Skim "$(MOD_PDF)"; \
	else \
		echo "Modular Rules is already up-to-date."; \
	fi

clean:
	@echo "Cleaning build files..."
	rm -rf "$(BUILD_DIR)"
	@echo "Done."