import aspose.slides
import sys


if __name__ == '__main__':
	if len(sys.argv) != 2:
		print('Please provide me with a .pptm file to analyze', file=sys.stderr)
		exit(1)
	# Load a presentation
	with aspose.slides.Presentation(sys.argv[1]) as presentation:
		# Check if presentation contains VBA Project
		if presentation.vba_project is not None:

			# Print each module
			for module in presentation.vba_project.modules:
				print(module.name)
				print(module.source_code)
