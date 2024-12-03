# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'learningNotes'
copyright = '2024, fengyang'
author = 'fengyang'
release = '1.0.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
	 'sphinx_design',
	 'sphinx_copybutton',
	 "sphinx.ext.imgconverter", 
]

# 可选配置：自定义按钮样式
copybutton_prompt_text = "$ "  # 定义要去除的命令提示符
copybutton_prompt_is_regexp = True  # 告诉扩展这是一个正则表达式

templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

#html_theme = 'sphinx_rtd_theme'
html_theme = 'furo'

html_static_path = ['_static']

