import sys, weasyprint, logging
logging.getLogger('weasyprint').setLevel(logging.ERROR)
src, dst = sys.argv[1], sys.argv[2]
weasyprint.HTML(src).write_pdf(dst)
print("wrote", dst)
